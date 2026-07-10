# /pafe — Overlay Claude

**Versão:** 1.2  
**Data:** 2026-07-10  
**Escopo:** P.A.F.E. transversal — regras exclusivas para Claude com ambiente de execução ativo.

Este arquivo aplica-se somente quando o agente é Claude com capacidade real de execução no próprio turno: bash, rede, criação de arquivos e entrega de binários. Lê-se em conjunto com `README.md`, `audio_modos.md`, `audio.md` e `html.md`.

`audio_modos.md` decide o modo operacional. Este arquivo registra apenas os deltas do Claude.

---

## 1. Capacidades ativas

| Capacidade | Descrição |
|---|---|
| Bash + rede | Execução de comandos, instalação via `pip`/`apt`, chamadas externas e teste de DNS/endpoint. |
| Persistência em disco | Criação e leitura de arquivos no ambiente do próprio turno. |
| Entrega de binários | MP3, ZIP, PDF e demais arquivos via mecanismo de entrega da plataforma. |
| MP3 direto | Quando possível, gerar `audio/master_audio.mp3` no próprio turno, sem exigir que o usuário rode script local. |
| TTS por ferramenta ou biblioteca | Pode usar TTS nativo da plataforma, `edge-tts`, API autorizada ou outro motor disponível, desde que gere arquivo real e validável. |
| Validação ativa | Validar duração por `ffprobe` ou ferramenta equivalente antes de declarar o MP3 gerado. |
| Box/Drive direto | Ler e escrever arquivos no Box e Google Drive, quando autorizado pela conexão ativa. |

---

## 2. Regra de ouro do Claude

Se o roteiro estiver suficientemente definido e o usuário pediu áudio, Claude deve tentar entregar o MP3 pronto no próprio turno.

É errado aplicar ao Claude, quando ele tem execução ativa, a regra genérica:

> “não tente gerar MP3 dentro desta conversa”.

Essa regra vale para plataformas sem execução confiável. Para Claude com ambiente ativo, a regra correta é:

1. tentar gerar MP3 real;
2. validar;
3. entregar;
4. só declarar execução local necessária se o teste falhar com diagnóstico.

---

## 3. Proibido declarar limitação sem testar

Antes de qualquer:

```text
[ARTEFATO: execução local necessária]
```

ou:

```text
[ARTEFATO: MP3 indisponível nesta plataforma]
```

Claude deve rodar um smoke test de TTS no próprio turno, se houver ferramenta de execução.

Smoke test mínimo:

1. gerar uma frase curta;
2. salvar MP3 real;
3. validar duração/tamanho;
4. classificar a falha, se houver.

Só declarar impossível após falha confirmada.

---

## 4. Diagnóstico obrigatório de falha

### 4.1. DNS/rede

Sinais: `Temporary failure in name resolution`, falha de `getaddrinfo`, domínio não resolve, egress bloqueado.

Conduta:

1. declarar classe DNS/rede;
2. não tentar corrigir com SSL relaxado;
3. trocar ambiente ou sugerir rota externa autorizada;
4. não gerar fallback robótico.

Teste:

```bash
nslookup speech.platform.bing.com || true
getent hosts speech.platform.bing.com || true
```

### 4.2. Certificado/SSL

Sinais: `CERTIFICATE_VERIFY_FAILED`, `SSLCertVerificationError`, `self-signed certificate in certificate chain`.

Conduta:

1. tentar CA local do sistema;
2. usar proxy configurado se necessário;
3. SSL relaxado só como último recurso;
4. nunca usar SSL relaxado com senha, API key, token, dado sensível ou material sigiloso;
5. registrar no log se usado.

Bloco preferencial para `edge-tts`, antes do primeiro `Communicate`:

```python
import ssl, os
import edge_tts.communicate as _ec

_CANDIDATOS_CA = [
    "/etc/ssl/certs/ca-certificates.crt",
    "/etc/pki/tls/certs/ca-bundle.crt",
    "/usr/local/etc/openssl/cert.pem",
]
for _ca in _CANDIDATOS_CA:
    if os.path.exists(_ca):
        _ec._SSL_CTX = ssl.create_default_context(cafile=_ca)
        break
```

### 4.3. Endpoint indisponível

Sinais: HTTP 5xx, timeout persistente, serviço indisponível.

Conduta:

1. repetir com limite;
2. aguardar ou migrar de motor;
3. não insistir em loop infinito;
4. registrar a falha.

### 4.4. Autenticação/cota

Sinais: HTTP 401, 402, 403, 429.

Conduta:

1. não pedir chave no chat;
2. orientar uso de `.env`;
3. verificar cota e custo;
4. não repetir chamadas pagas sem autorização.

---

## 5. Preferência de entrega

Quando o roteiro já estiver aprovado:

1. gerar MP3 real;
2. validar duração real;
3. entregar `audio/master_audio.mp3`;
4. se houver HTML, apontar o player para o MP3 real;
5. se gerar ZIP, verificar estrutura antes de entregar.

Execução local é exceção, não regra, quando Claude tem ambiente ativo.

Execução local continua cabível quando:

1. o usuário pediu pacote local;
2. o roteiro ainda está em rascunho;
3. a geração falhou após smoke test e diagnóstico;
4. o conteúdo é sensível e não deve ser enviado ao motor externo disponível.

---

## 6. Validação antes da entrega

Obrigatório, conforme o artefato:

1. Python: `python3 -m py_compile` quando houver script;
2. JavaScript/HTML: `node --check` no JS extraído, quando possível;
3. Áudio: `ffprobe` ou equivalente no master;
4. HTML offline: verificar ausência de CDN ou dependência externa obrigatória;
5. ZIP: `unzip -l` para conferir estrutura;
6. checksums: gerar `sha256sum` quando o pacote for técnico/auditável.

Para áudio:

```bash
ffprobe -v error -show_entries format=duration,bit_rate,size -of default=noprint_wrappers=1 audio/master_audio.mp3
sha256sum audio/master_audio.mp3 > logs/checksums.sha256
```

---

## 7. Sobreposições nos módulos comuns

| Módulo | Delta Claude |
|---|---|
| `audio_modos.md` | Claude com execução ativa deve tentar MP3 direto por padrão. |
| `audio.md` | Pipeline local só é obrigatório se o usuário pedir pacote/script/yaml ou se a geração direta falhar. |
| `audio.md` | `master_audio.mp3` pode ser saída desta sessão, não pendência local. |
| `audio.md` | Se usar `edge-tts`, preparar SSL/CA antes da primeira síntese quando o ambiente exigir. |
| `html.md` | Player deve apontar para MP3 real quando entregue. Se não houver MP3, mostrar aviso. |
| `README.md` | `[ARTEFATO: execução local necessária]` é exceção no Claude, não regra. |
| `README.md` | `/pafe menu` deve refletir ferramentas e permissões reais do turno, não o nome Claude isoladamente. |

---

## 8. O que não muda

1. Sem simular MP3.
2. Sem loop, silêncio artificial ou duplicação para inflar duração.
3. Sem fallback robótico como padrão.
4. Duração validada por ferramenta técnica.
5. Três vozes pt-BR continuam preferenciais para `edge-tts`: FranciscaNeural, AntonioNeural e ThalitaNeural.
6. Resposta de outra IA é objeto de análise, nunca prova.
7. Hierarquia documental do P.A.F.E. permanece intacta.
8. Chaves de API nunca entram no chat, código, log, manifesto, HTML ou repositório.

---

## 9. Menu adaptativo no Claude

### 9.1. Regra

Claude não deve exibir um menu longo por padrão. Primeiro identifica silenciosamente as capacidades do ambiente atual.

Verificar, conforme a tarefa:

1. bash/shell;
2. rede externa;
3. criação e leitura de arquivos;
4. entrega de binários;
5. Python;
6. FFmpeg/ffprobe;
7. conectores GitHub, Google Drive e Box;
8. API premium configurada, sem revelar segredo.

### 9.2. Quando executar diretamente

1. Se o usuário pediu MP3 e o ambiente comprova geração/validação, tentar MP3 direto sem perguntar qual rota usar.
2. Se o usuário pediu apenas análise, pesquisa, HTML ou revisão, executar o entregável pedido sem apresentar menu irrelevante.
3. Se uma única rota é possível, usar essa rota e declarar a limitação apenas quando afetar o resultado.

### 9.3. Quando mostrar menu

Mostrar menu quando:

1. o usuário digitar `/pafe menu` ou `/pafe audio menu`;
2. houver duas ou mais rotas materialmente diferentes;
3. o ambiente estiver incerto após verificação segura;
4. a escolha envolver API paga, envio de conteúdo a terceiro ou escrita em drive;
5. houver diferença relevante entre gerar artefato agora e preparar pipeline local.

Menu com no máximo cinco opções e uma marcada `[RECOMENDADO]`.

### 9.4. Modelo Claude com execução ativa

```text
P.A.F.E. — OPÇÕES DISPONÍVEIS

1. [RECOMENDADO] Gerar o artefato completo agora
   Execução, validação técnica e entrega no próprio turno.

2. Gerar HTML offline + MP3
   index.html, player, flashcards, quiz e áudio validado.

3. Gerar somente conteúdo/roteiro
   Sem execução técnica nem binário.

4. Gerar pacote local completo
   Script, YAML, setup, validação e manifesto.

5. Usar rota externa ou API premium
   Exige autorização, custo/privacidade e segredo fora do chat.
```

### 9.5. Escrita em conectores

Mesmo que GitHub, Drive ou Box estejam disponíveis, qualquer criação, substituição, exclusão ou sincronização de arquivo exige autorização expressa. Leitura e análise não equivalem a autorização de escrita.

---

## 10. Histórico

| Versão | Data | Motivo |
|---|---|---|
| 1.2 | 2026-07-10 | Adiciona handshake silencioso, execução direta quando a rota é óbvia, `/pafe menu` e autorização expressa para escrita/custo/envio a terceiro. |
| 1.1 | 2026-07-10 | Preserva a particularidade do Claude: geração de MP3 direto quando há ambiente ativo; adiciona diagnóstico DNS × SSL × endpoint, validação e checksums. |
| 1.0 | 2026-06-09 | Criação. Deriva da análise comparativa entre entrega com MP3 gerado em sessão e entrega sem MP3 por ausência de tratamento SSL/smoke test. |