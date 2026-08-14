# audio.md — Padrão técnico de áudio P.A.F.E.

**Versão:** v7.1 MASTER  
**Data:** 2026-08-14  
**Escopo:** técnica de síntese, processamento, validação e publicação.  
**Roteamento:** decidido por `audio_modos.md`.

## 1. Regra técnica central

1. Cada assunto principal produz um MP3 independente.
2. Cada MP3 usa uma única voz; não alternar vozes dentro do mesmo assunto apenas por variedade.
3. Não concatenar assuntos diferentes em `master_audio.mp3`.
4. Chunks são temporários internos de um assunto, não capítulos de um master.
5. Falha em um assunto não invalida os arquivos já aprovados.
6. Arquivo existente não equivale a arquivo conforme.
7. HTML, TTS do navegador e `speechSynthesis` não substituem MP3 real solicitado.

## 2. Nomes

Padrão:

```text
01_INTRODUCAO_E_MAPA.mp3
02_PRIMEIRO_ASSUNTO.mp3
...
NN_REVISAO_FINAL.mp3
```

Sem acentos, caracteres problemáticos ou nomes genéricos.

## 3. Motor e voz

Motor gratuito preferencial quando a rota escolhida o suportar:

```text
edge-tts
rate: -10% a -12%
```

A voz não é fixa. Antes da síntese, descobrir ou testar o catálogo realmente disponível na rota atual.

Estados operacionais:

```text
PREFERRED
APPROVED
AVAILABLE
CANDIDATE
REJECTED_TEMP
LAST_RESORT
```

Elegibilidade:

```text
eligible = APPROVED ∩ AVAILABLE \ LAST_RESORT
```

`pt-BR-AntonioNeural` e `pt-BR-FranciscaNeural` são `LAST_RESORT`, não padrão. `pt-BR-LeticiaNeural` ou nome equivalente retornado pelo serviço pode ser `CANDIDATE`. Não inventar nomes nem disponibilidade.

Quando houver várias vozes elegíveis, pode haver rotação entre assuntos conforme prioridade do usuário e uso recente. Cache/hash de MP3 já válido prevalece sobre ressintetização apenas para cumprir rotação.

Proibido: eSpeak, eSpeak-NG, MBROLA, pyttsx3, Festival, gTTS robótico, voz metálica, motor não rastreável e `speechSynthesis` como substituto de MP3.

## 4. Pipeline por assunto

```text
texto original
→ cópia falável
→ sanitização
→ correções fonéticas
→ divisão semântica
→ síntese neural
→ validação dos chunks
→ PCM WAV uniforme
→ pausas reais
→ concatenação apenas daquele assunto
→ loudnorm
→ fade
→ codificação MP3 única
→ ffprobe
→ publicação segura
```

Padrão intermediário: PCM 24 kHz, mono, 16-bit.

Loudness de estudo longo:

```text
I=-20 LUFS
TP=-1.5 dBTP
LRA=11
```

## 5. Script local mínimo

O script padrão de contingência deve ser um único `.py` autossuficiente.

CLI obrigatória:

```bash
python3 gerar_audio.py --list
python3 gerar_audio.py
python3 gerar_audio.py --only 2 5
python3 gerar_audio.py --only 2 --force
```

Comportamento:

- sem argumento: gera somente arquivos ausentes;
- `--list`: lista assuntos e destinos;
- `--only`: gera apenas os números indicados;
- `--force`: permite sobrescrita intencional;
- arquivo válido existente é preservado por padrão;
- não usar `sudo`.

## 6. Pacote técnico completo

Somente sob pedido expresso. Pode conter YAML, roteiro externo, dicionário fonético, manifesto, logs, validação e partes.

O pacote também deve gerar N MP3s por assunto; nunca master único por padrão.

ZIP não é pacote obrigatório. Pode ser oferecido adicionalmente como conveniência ou ser usado como transporte técnico de um artifact remoto.

## 7. Retry e retomada

1. Dividir sem cortar frases.
2. Tentar cada chunk até três vezes.
3. Usar espera progressiva.
4. Preservar chunks válidos.
5. Não reiniciar todos os assuntos por falha isolada.
6. Não ocultar `stderr`.
7. Verificar `returncode`.

## 8. Publicação segura

1. gerar em temporário;
2. validar;
3. copiar para `.part` no diretório final;
4. `flush` e `fsync`;
5. `os.replace()` apenas no mesmo sistema de arquivos;
6. remover `.part` em falha;
7. nunca apagar outros MP3s válidos.

Entrega ao usuário:
- quando a superfície suportar, disponibilizar os MP3s individualmente;
- ZIP pode ser oferecido como conveniência adicional;
- quando o provedor remoto entregar somente artifact ZIP, baixar/descompactar e expor os MP3s individualmente quando tecnicamente possível.

## 9. Validação individual

Para cada MP3:

- existência;
- tamanho maior que zero;
- duração positiva;
- codec válido;
- voz neural autorizada e efetivamente usada;
- início e final audíveis;
- ausência de truncamento;
- ausência de loop;
- ausência de silêncio para inflar duração;
- loudness;
- nome correto;
- correspondência entre assunto, texto e arquivo.

Validação global:

- quantidade de MP3s = quantidade de assuntos;
- `master_audio.mp3` ausente, salvo pedido expresso;
- duração informada por arquivo;
- exclusão de um arquivo não quebra os demais;
- ausência de substituição por `speechSynthesis`/TTS do navegador.

## 10. Duração

Usar aproximadamente 150 palavras úteis por minuto como estimativa. Não inflar com repetição ou silêncio. A duração varia conforme o assunto; não impor duração idêntica a todos.

## 11. Segurança

- não registrar segredos;
- chave apenas em `.env`, variável de ambiente ou Secret;
- API paga somente com autorização;
- não desativar TLS;
- não expor conteúdo sensível desnecessariamente;
- não publicar conteúdo sensível em repositório público apenas para obter execução remota.

## 12. Estado final

Aprovado:

```text
CONFORME — todos os arquivos passaram nas validações.
```

Falha:

```text
BLOQUEADO — requisito obrigatório não pôde ser validado; nenhum fallback inferior foi utilizado.
```