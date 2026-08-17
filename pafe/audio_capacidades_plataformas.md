# audio_capacidades_plataformas.md — Capacidades de execução de áudio

**Versão:** v1.0.0  
**Data:** 2026-08-17  
**Status:** ativo  
**Escopo:** onde o P.A.F.E. pode executar TTS e como interpretar falhas de ambiente.

## 1. Regra central

Capacidade é verificada por execução, não presumida pela marca da IA.

Uma falha local de DNS, egress, certificado, biblioteca ou sandbox encerra somente aquela rota. Ela não prova que o provedor ou o P.A.F.E. sejam globalmente incapazes de gerar MP3.

## 2. ChatGPT/GPT com GitHub autorizado

Quando o ambiente direto não puder concluir e a rota GitHub estiver autorizada:

```text
ChatGPT
→ repositório privado de execução
→ GitHub Actions Secret
→ runner
→ API/TTS
→ ffprobe/validação
→ artifact
→ entrega dos MP3s
```

Repositório privado operacional atualmente usado para integrações premium:

```text
dozzademiranda/ias-state
```

Workflows atualmente previstos:

```text
.github/workflows/elevenlabs-dispatch.yml
.github/workflows/hume-synth.yml
.github/workflows/fish-audio-synth.yml
```

O repositório não precisa ser público para essa rota. Não pedir mudança de visibilidade sem necessidade técnica demonstrada.

## 3. Provedores

### Edge / Microsoft neural via `edge-tts`

- não exige API key nesta arquitetura;
- bom fallback gratuito quando o runtime consegue acessar o serviço;
- catálogo deve ser redescoberto/testado;
- ranking e bans estão em `VOICE_REGISTRY.json`.

### ElevenLabs

- Secret lógico: `ELEVENLABS_API_KEY`;
- integração privada GitHub já possui histórico de autenticação/listagem/TTS bem-sucedidos;
- verificar cota e voz antes de síntese longa.

### Hume AI

- Secrets lógicos: `HUME_API_KEY`; `HUME_SECRET_KEY` somente quando estratégia de token for usada;
- listagem de vozes por API key e emissão de token OAuth passaram em 2026-08-17;
- TTS REST continua `REJECTED_TEMP` por HTTP 400 `E0101 payload_parse` no último E2E;
- não converter isso em alegação de chave inválida.

### Fish Audio

- Secret lógico: `FISH_AUDIO_API_KEY`;
- integração usa `reference_id` e header de modelo;
- houve teste PT-BR bem-sucedido com Capitão Nascimento em 2026-08-17;
- preflight posterior retornou HTTP 402 por crédito de API; tratar como indisponibilidade temporária do provedor, não como ausência de Secret.

### Azure AI Speech

- é distinto de `edge-tts`;
- exige configuração própria quando usado;
- nenhuma disponibilidade atual deve ser inferida apenas de referências históricas.

## 4. Gates antes de produção

Executar, na medida aplicável:

```text
1. Secret/credencial disponível sem revelar valor
2. autenticação
3. endpoint
4. saldo/cota
5. catálogo/voice ID
6. smoke test curto
7. ffprobe do resultado
8. somente então texto longo
```

Falha em um gate → `REJECTED_TEMP` daquela rota e tentativa da próxima rota autorizada.

## 5. Fontes relacionadas

```text
pafe/audio_modos.md
pafe/audio.md
pafe/audio_api_paga.md
pafe/audio_perfil_fabio.md
pafe/VOICE_REGISTRY.json
pafe/VOICE_PRIORITY_OVERRIDE_2026-08.json
pafe/pafe_gpt.md
pafe/pafe_governanca_overlays.md
```
