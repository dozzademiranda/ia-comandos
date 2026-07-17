# audio_modos.md — Modos de áudio do P.A.F.E.

**Versão:** v2.0
**Data:** 2026-07-17
**Status:** ativo e prevalente sobre `pafe/audio.md` para decidir onde e como iniciar a geração.

## 1. Regra central

1. Áudio significa MP3 neural real por assunto.
2. Um assunto principal gera um MP3 independente.
3. É proibido gerar somente `master_audio.mp3`, salvo pedido expresso posterior.
4. Não usar fallback robótico.
5. A linguagem natural e o contexto prevalecem sobre token exato de comando.
6. Criar arquivo para download na conversa não exige autorização adicional quando o usuário já pediu o artefato.

## 2. Saída por comando

### `/pafe audio`

Resultado:

```text
01_<ASSUNTO>.mp3
02_<ASSUNTO>.mp3
...
NN_<ASSUNTO>.mp3
```

Sem HTML por padrão.

### `/pafe html audio` ou `/pafe audio html`

Resultado:

1. um HTML autocontido, sem áudio, player ou referência a MP3;
2. N MP3 independentes, um por assunto;
3. nenhum master unificado.

### `/pafe audio local` ou `/pafe audio script`

Força um script local mínimo.

### `/pafe audio pacote`

Força pacote técnico completo.

## 3. Definição de assunto

1. Usar títulos, módulos e unidades conceituais reais.
2. Não dividir apenas por caracteres.
3. Não fundir assuntos independentes.
4. Se um assunto ultrapassar limite técnico, usar `PARTE_01`, `PARTE_02`.
5. A quantidade de MP3s deve corresponder à lista de assuntos.

## 4. Hierarquia obrigatória de rotas

### Rota 1 — MP3 neural direto

Usar quando a plataforma consegue sintetizar, validar e entregar os arquivos.

### Rota 2 — script local mínimo automático

Usar automaticamente quando:

- a rota direta falhar;
- o ambiente Linux local conhecido for compatível;
- não houver custo, escrita externa ou envio sensível a terceiro.

Não pedir nova autorização. Não exigir `/pafe audio local`. Não encerrar apenas com explicação.

### Rota 3 — pacote técnico completo

Somente sob pedido expresso de pacote, YAML, setup, manifesto, pipeline ou auditoria completa.

### Rota 4 — GitHub Actions ou Codespaces

Somente quando a execução local estiver indisponível/inadequada ou quando o usuário pedir automação remota. Exige autorização para escrita externa.

### Rota 5 — API paga

Somente com autorização, custo estimado e segredo fora do chat.

## 5. Script local mínimo

Entregar um único `.py`, autossuficiente, com:

- assuntos e textos;
- nomes dos MP3s;
- `edge-tts`;
- voz preferencial;
- retries;
- pausas reais;
- PCM uniforme;
- normalização;
- validação individual;
- publicação segura;
- `--list`;
- `--only`;
- `--force`.

Não gerar README, YAML, TXT, JSON, manifesto, requirements, setup, ZIP ou hash por padrão.

## 6. Capacidade por plataforma

### Claude com execução ativa

1. Fazer smoke test.
2. Gerar MP3 neural direto quando possível.
3. Gerar um MP3 por assunto.
4. Nunca gerar master único por padrão.
5. Se falhar, aplicar a rota local mínima ou outra rota autorizada.

### GPT, Gemini, Perplexity e outras

1. Não fingir geração.
2. Não usar voz robótica.
3. Se o ambiente direto falhar e o Linux local for conhecido, gerar automaticamente o script local mínimo.
4. GitHub não é rota obrigatória nem preferencial sobre a máquina local.

## 7. Diagnóstico de falha

Classificar:

- DNS/rede;
- certificado/SSL;
- endpoint/serviço;
- autenticação/cota.

Nunca desativar TLS como padrão. Nunca pedir chave no chat.

## 8. TTS

Padrão gratuito:

```text
edge-tts
pt-BR-AntonioNeural
```

Fallback masculino pt-BR neural pode ser descoberto dinamicamente.

Proibido como fallback final:

- eSpeak;
- eSpeak-NG;
- MBROLA;
- pyttsx3;
- Festival;
- gTTS robótico;
- voz metálica;
- motor não rastreável.

## 9. Teste de regressão bloqueante

Entrada:

```text
/pafe audio
Conforme informação anterior, gere esses 28 arquivos.
```

Contexto conhecido: Linux, `edge-tts`, FFmpeg e FFprobe locais; geração direta falhou; um MP3 por assunto.

Saída obrigatória:

- um script Python físico;
- 28 MP3s independentes;
- `--list`;
- `--only`;
- sem GitHub;
- sem nova autorização;
- sem master único;
- sem voz robótica;
- um único comando real para executar.

Reprovar se a IA apenas explicar, pedir outro comando ou pedir autorização para o script local.
