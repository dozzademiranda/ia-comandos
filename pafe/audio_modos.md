# audio_modos.md — Modos de áudio do P.A.F.E.

**Versão:** audio_modos.md v1.1  
**Data:** 2026-07-10  
**Status:** ativo e prevalente sobre `pafe/audio.md` para interpretar `/pafe audio`, `/pafe html audio` e `/pafe completo`.

Este arquivo separa quatro coisas que não podem ser confundidas:

1. gerar MP3 real direto na plataforma;
2. gerar roteiro textual falável;
3. gerar pacote local com `audio.yaml`, script Python e pipeline;
4. acionar rota remota/externa, como GitHub Actions, Codespaces ou API premium.

---

## 1. Regra central

Por padrão, quando o usuário pede áudio, a IA deve buscar **MP3 real**, não apenas roteiro.

A forma de gerar depende da capacidade real da plataforma:

1. se a plataforma consegue criar arquivo MP3 real no próprio turno, deve tentar gerar e validar;
2. se a plataforma não consegue gerar MP3 real, deve declarar a limitação e só entregar roteiro se o usuário autorizou fallback textual;
3. se o usuário pedir pacote local, aplicar `pafe/audio.md`;
4. se o agente for Claude com ambiente de execução ativo, aplicar também `pafe/pafe_claude.md`.

Nunca afirmar MP3 gerado sem arquivo físico real.

---

## 2. Modo MP3 direto — padrão

Invocações:

```text
/pafe audio
/pafe audio mp3
/pafe html audio
/pafe html audio mp3
/pafe completo
```

Resultado esperado:

1. gerar `audio/master_audio.mp3`, se a plataforma permitir;
2. validar duração real com ferramenta técnica quando disponível;
3. quando houver HTML, gerar `index.html` offline;
4. incluir flashcards clicáveis e quiz embutido quando o comando exigir HTML;
5. incluir player apontando para `audio/master_audio.mp3`, se o MP3 existir;
6. não gerar pacote local por padrão.

Neste modo é proibido gerar, salvo pedido expresso:

1. `audio.yaml`;
2. `roteiro_audio.txt`;
3. `gerar_audio.py` ou `gerar_audio_v2.py`;
4. `setup_audio.sh`;
5. `validar_audio.sh`;
6. `requirements_audio.txt`;
7. `manifest_audio.json`;
8. `chapters.json`;
9. pipeline local completo.

---

## 3. Roteamento por capacidade da plataforma

### 3.1. Claude com execução ativa

Se Claude tiver bash, rede, criação de arquivos e entrega de binários, ele deve:

1. tentar gerar MP3 real no próprio turno;
2. fazer smoke test antes de declarar impossibilidade;
3. aplicar `pafe/pafe_claude.md`;
4. validar com `ffprobe` quando disponível;
5. entregar o MP3 pronto.

Neste caso, é errado impor a regra genérica “não tente gerar MP3 dentro da conversa”. Essa regra vale para plataformas sem execução confiável, não para Claude quando há capacidade real.

### 3.2. GPT, Gemini, Perplexity e outras IAs sem geração confiável de arquivo

Se a plataforma não provar capacidade de gerar MP3 real:

1. não fingir geração;
2. não usar voz robótica local como substituto;
3. entregar roteiro limpo somente se o usuário aceitar fallback textual;
4. encaminhar para geração local, GitHub Actions, Codespaces ou API externa autorizada.

### 3.3. Ambiente incerto

Se a IA não sabe se consegue gerar MP3:

1. realizar teste curto quando houver ferramenta de execução;
2. se não houver ferramenta de execução, declarar `[ARTEFATO: MP3 indisponível nesta plataforma]`;
3. não prometer entrega futura.

---

## 4. Modo roteiro — somente se pedido ou autorizado

Invocação expressa:

```text
/pafe audio roteiro
```

Resultado esperado:

1. gerar roteiro falável em texto;
2. não declarar MP3 gerado;
3. não gerar pacote local;
4. não gerar `audio.yaml`;
5. não gerar script Python.

Fallback:

1. se o usuário pediu MP3 real e a plataforma não conseguir, só entregar roteiro se houver autorização para fallback textual;
2. se o usuário disser “quero áudio, não roteiro”, não substituir por roteiro sem autorização.

---

## 5. Modo pacote local — desativado por padrão

STATUS: desativado por padrão.

Este modo preserva o pipeline técnico de `pafe/audio.md`, mas só é acionado por pedido expresso.

Invocações que ativam este modo:

```text
/pafe audio pacote
/pafe audio local
/pafe audio pipeline
/pafe audio script
/pafe audio yaml
```

Também ativa se o usuário pedir expressamente:

1. `audio.yaml`;
2. script Python;
3. `gerar_audio_v2.py`;
4. pipeline local;
5. geração local;
6. pacote local;
7. `setup_audio.sh`;
8. `validar_audio.sh`;
9. `requirements_audio.txt`.

Neste modo, aplicar `pafe/audio.md`.

---

## 6. Diagnóstico obrigatório de falha TTS

Se `edge-tts` ou motor equivalente falhar, diagnosticar a classe antes de qualquer contorno.

### 6.1. DNS/rede

Sinais: `Temporary failure in name resolution`, falha de `getaddrinfo`, domínio não resolve, egress bloqueado.

Interpretação:

1. ambiente sem rede externa real ou DNS bloqueado;
2. típico de sandbox de IA;
3. não é corrigível por SSL relaxado;
4. trocar ambiente: máquina local, Claude com rede real, GitHub Actions ou Codespaces.

Teste sugerido:

```bash
nslookup speech.platform.bing.com
getent hosts speech.platform.bing.com
```

### 6.2. Certificado/SSL

Sinais: `CERTIFICATE_VERIFY_FAILED`, `SSLCertVerificationError`, `self-signed certificate in certificate chain`.

Regra:

1. tentar CA do sistema ou proxy configurado antes de relaxar SSL;
2. SSL relaxado é último recurso;
3. nunca usar SSL relaxado com senha, token, API key, dados sensíveis ou material sigiloso;
4. nunca tratar SSL relaxado como padrão;
5. registrar no log quando usado.

### 6.3. Endpoint indisponível

Sinais: HTTP 5xx, serviço indisponível, timeout persistente no provedor.

Conduta:

1. aguardar e repetir com limite;
2. migrar para motor alternativo autorizado;
3. não insistir em loop infinito.

### 6.4. Autenticação, cota e custo

Sinais: HTTP 401, 402, 403, 429.

Conduta:

1. não pedir chave no chat;
2. orientar `.env` ou variável de ambiente;
3. verificar cota/créditos localmente;
4. não repetir chamadas pagas em loop.

---

## 7. Rotas de execução

Ordem preferencial:

1. MP3 direto na plataforma, se houver capacidade real;
2. Claude com execução ativa, quando disponível;
3. máquina local do usuário com `edge-tts`;
4. GitHub Actions para execução remota automatizada;
5. Codespaces para shell remoto manual;
6. API premium autorizada: OpenAI TTS, ElevenLabs, Gemini TTS, Hume AI, Narakeet ou equivalente;
7. Piper offline como plano B, declarando qualidade inferior;
8. roteiro textual, apenas como fallback autorizado.

Proibido fallback robótico como padrão: `espeak`, `espeak-ng`, `pyttsx3`, Festival ou voz metálica local.

---

## 8. Declarações de artefato

Permitidas:

```text
[ARTEFATO: MP3 gerado]
```

Somente se `audio/master_audio.mp3` existir.

```text
[ARTEFATO: MP3 indisponível nesta plataforma]
```

Quando não houver capacidade de gerar MP3 real.

```text
[ARTEFATO: execução local necessária]
```

Somente se o usuário pediu ou autorizou pacote local/fallback técnico.

```text
[ARTEFATO: roteiro falável gerado]
```

Somente quando o entregável real for texto para posterior síntese.

---

## 9. HTML com áudio

Quando o comando for:

```text
/pafe html audio
```

gerar:

1. `index.html` offline e autossuficiente;
2. flashcards clicáveis dentro do HTML;
3. quiz interativo dentro do HTML;
4. `audio/master_audio.mp3`, se possível;
5. player no HTML apontando para `audio/master_audio.mp3`, se o MP3 existir;
6. aviso claro se o MP3 não existir.

O HTML é adendo de estudo. O áudio MP3 é artefato principal quando o usuário pede áudio.

---

## 10. Rodapé operacional

Versão: audio_modos.md v1.1  
Data: 2026-07-10  
Regra central: `/pafe audio` tenta MP3 real por padrão. Claude com execução ativa deve gerar MP3 direto; pacote local fica desativado até pedido expresso. Falhas TTS exigem diagnóstico DNS × SSL × endpoint antes de contorno.
