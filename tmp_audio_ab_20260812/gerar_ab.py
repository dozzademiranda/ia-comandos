#!/usr/bin/env python3
import asyncio
import importlib.metadata
import json
import shutil
import subprocess
import sys
from pathlib import Path

import edge_tts

BASE = Path(__file__).resolve().parent
OUT = BASE / "output"
RAW = BASE / "raw"
OUT.mkdir(parents=True, exist_ok=True)
RAW.mkdir(parents=True, exist_ok=True)

TEXT = """Teste de calibração de áudio.

Artigo sétimo, parágrafo segundo.

O índice observado foi de vinte e cinco por cento.

O valor de referência é mil quatrocentos e cinquenta reais.

A data é doze de agosto de dois mil e vinte e seis.

Processo número zero zero um seis zero seis quatro, traço três sete, ponto dois zero dois quatro, ponto oito, ponto um seis, ponto zero zero três zero.

Supremo Tribunal Federal. Superior Tribunal de Justiça. Tribunal Superior do Trabalho.

Habeas corpus. Ratio decidendi. Obiter dictum. Compliance. Due diligence.

Agora uma frase um pouco mais longa, destinada a verificar se a voz preserva naturalidade, inteligibilidade e ritmo quando apresenta várias informações em sequência sem transformar o conteúdo em uma parede sonora.

Pergunta de revisão.

Qual alternativa deve ser analisada primeiro?

Faça uma pequena pausa mental.

Agora prossiga para a resposta."""

PRIMARY_VOICES = [
    "pt-BR-AntonioNeural",
    "pt-BR-FranciscaNeural",
]

THIRD_VOICE_PREFERENCE = [
    "pt-BR-ThalitaNeural",
    "pt-BR-ThalitaMultilingualNeural",
    "pt-BR-MacerioMultilingualNeural",
]


def run(cmd):
    print("+", " ".join(map(str, cmd)), flush=True)
    subprocess.run(cmd, check=True)


def probe(path):
    raw = subprocess.check_output([
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,bit_rate,size,format_name",
        "-show_entries", "stream=codec_name,sample_rate,channels",
        "-of", "json", str(path)
    ], text=True)
    return json.loads(raw)


def require_tools():
    for name in ("ffmpeg", "ffprobe"):
        if shutil.which(name) is None:
            raise RuntimeError(f"dependência ausente: {name}")


async def synth(case_id, voice, rate):
    raw_mp3 = RAW / f"{case_id}_raw.mp3"
    wav = RAW / f"{case_id}.wav"
    rate_tag = rate.replace("-", "MENOS").replace("%", "PCT")
    voice_tag = voice.replace("pt-BR-", "").replace("Neural", "").upper()
    final_mp3 = OUT / f"{case_id}_{voice_tag}_{rate_tag}.mp3"

    last = None
    for attempt in range(1, 4):
        try:
            comm = edge_tts.Communicate(TEXT, voice=voice, rate=rate)
            await comm.save(str(raw_mp3))
            if raw_mp3.exists() and raw_mp3.stat().st_size > 1000:
                break
        except Exception as exc:
            last = exc
            print(f"{case_id}: tentativa {attempt} falhou: {exc}", file=sys.stderr)
            await asyncio.sleep(attempt * 2)
    else:
        raise RuntimeError(f"{case_id}: síntese falhou após 3 tentativas: {last}")

    run(["ffmpeg", "-y", "-v", "error", "-i", str(raw_mp3), "-ac", "1", "-ar", "24000", "-sample_fmt", "s16", str(wav)])
    wav_info = probe(wav)
    duration = float(wav_info["format"]["duration"])
    fade_out_start = max(duration - 0.35, 0.0)
    af = f"loudnorm=I=-20:TP=-1.5:LRA=11,afade=t=in:st=0:d=0.25,afade=t=out:st={fade_out_start:.3f}:d=0.35"

    run([
        "ffmpeg", "-y", "-v", "error", "-i", str(wav),
        "-af", af, "-ac", "1", "-ar", "44100", "-b:a", "128k", str(final_mp3)
    ])

    run(["ffmpeg", "-v", "error", "-i", str(final_mp3), "-f", "null", "-"])
    info = probe(final_mp3)
    if float(info["format"]["duration"]) <= 0 or int(info["format"]["size"]) <= 1000:
        raise RuntimeError(f"{case_id}: saída inválida")

    return {
        "id": case_id,
        "voice": voice,
        "rate": rate,
        "file": final_mp3.name,
        "duration_seconds": round(float(info["format"]["duration"]), 3),
        "bit_rate": info["format"].get("bit_rate"),
        "size": info["format"].get("size"),
        "codec": info["streams"][0].get("codec_name"),
        "sample_rate": info["streams"][0].get("sample_rate"),
        "channels": info["streams"][0].get("channels"),
    }


async def main():
    require_tools()
    edge_version = importlib.metadata.version("edge-tts")
    print("edge-tts version:", edge_version)

    voices = await edge_tts.list_voices()
    ptbr = sorted(v.get("ShortName") for v in voices if (v.get("ShortName") or "").startswith("pt-BR-"))
    print("vozes pt-BR disponíveis:", json.dumps(ptbr, ensure_ascii=False))
    names = set(ptbr)

    missing_primary = [v for v in PRIMARY_VOICES if v not in names]
    if missing_primary:
        raise RuntimeError(f"vozes primárias não disponíveis: {missing_primary}")

    third_voice = next((v for v in THIRD_VOICE_PREFERENCE if v in names), None)
    if third_voice is None:
        other_ptbr = [v for v in ptbr if v not in PRIMARY_VOICES]
        if not other_ptbr:
            raise RuntimeError("nenhuma terceira voz pt-BR disponível para o teste")
        third_voice = other_ptbr[0]

    cases = [
        ("A1", PRIMARY_VOICES[0], "-10%"),
        ("A2", PRIMARY_VOICES[0], "-12%"),
        ("B1", PRIMARY_VOICES[1], "-10%"),
        ("B2", PRIMARY_VOICES[1], "-12%"),
        ("C1", third_voice, "-10%"),
        ("C2", third_voice, "-12%"),
    ]
    print("terceira voz selecionada:", third_voice)

    results = []
    for case in cases:
        results.append(await synth(*case))

    manifest = {
        "edge_tts_version": edge_version,
        "available_ptbr_voices": ptbr,
        "third_voice_selected": third_voice,
        "text_tts": TEXT,
        "results": results,
    }
    (OUT / "QC_AB.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
