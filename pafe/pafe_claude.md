# /pafe — Overlay Claude
**Versão:** 1.0 | **Data:** 2026-06-09 | **Escopo:** PAFE transversal

Aplica-se **somente quando o agente é Claude com ambiente de execução ativo**
(bash + rede + criação de arquivos + `present_files`). Lê-se **em conjunto** com
`README.md`, `audio.md` e `html.md`, que permanecem a fonte primária. Este
arquivo lista apenas os **deltas** — o que ativa, o que substitui e o que
adiciona quando o agente for Claude.

---

## 1. Capacidades ativas

| Capacidade | Descrição |
|---|---|
| Bash + rede | Execução de comandos, instalação via `pip`/`apt`, chamadas de rede externas. |
| Persistência em disco | Criação e leitura de arquivos no ambiente de execução do próprio turno. |
| Entrega de binários | MP3, ZIP, PDF entregues via `present_files` — prontos para baixar. |
| TTS nativo | Rodar `edge-tts` + `ffmpeg` dentro do próprio turno e gerar `master_audio.mp3`. |
| Validação ativa | Verificar sintaxe (`py_compile`, `node --check`) e duração (`ffprobe`) antes de entregar. |
| Box/Drive direto | Ler e escrever arquivos no Box e no Google Drive sem intermediação do usuário. |

---

## 2. Regras de execução

### 2.1 Proibido declarar limitação sem testar
Antes de qualquer `[ARTEFATO: execução local necessária]` envolvendo TTS ou qualquer
outra capacidade de rede/execução, rodar um *smoke test* no próprio turno (1 frase,
1 chamada). Só declarar impossível após falha **confirmada** com diagnóstico.

### 2.2 Tratamento de SSL obrigatório para edge-tts
O ambiente Claude usa proxy com CA auto-assinado. O modo padrão do `edge-tts` falha
com `SSLCertVerificationError`. Aplicar **antes** do primeiro `Communicate`:

```python
import ssl, os
import edge_tts.communicate as _ec

_CANDIDATOS_CA = [
    "/etc/ssl/certs/ca-certificates.crt",   # Debian/Ubuntu/Termux
    "/etc/pki/tls/certs/ca-bundle.crt",     # Fedora/RHEL
    "/usr/local/etc/openssl/cert.pem",      # macOS Homebrew
]
for _ca in _CANDIDATOS_CA:
    if os.path.exists(_ca):
        _ec._SSL_CTX = ssl.create_default_context(cafile=_ca)
        break
```

Sem este bloco, a geração **sempre falha** neste ambiente, mesmo com rede ativa e
DNS resolvendo corretamente.

### 2.3 Preferência de entrega
Quando o roteiro já estiver aprovado, **gerar e entregar o MP3 pronto** via
`present_files` — não deixar como execução local. Execução local é exceção
(roteiro ainda em rascunho, usuário pediu explicitamente, ou geração falhou após
diagnóstico).

### 2.4 Validação antes da entrega
- Scripts Python: `python3 -m py_compile`.
- JavaScript / HTML: `node --check` no bloco JS extraído.
- Áudio: `ffprobe_duration()` no master; falhar se abaixo do mínimo definido em `audio.yaml`.
- HTML offline: `grep -Eic "https?://|cdn"` para confirmar ausência de recursos externos.
- ZIP: `unzip -l` para confirmar estrutura antes de entregar.

---

## 3. Sobreposições pontuais nos módulos comuns

| Módulo | Seção | Delta Claude |
|---|---|---|
| `audio.md` | §4 estrutura de saída | `master_audio.mp3` é saída **desta sessão** (não pendente de execução local). |
| `audio.md` | §13 script de geração | `gerar_audio_v2.py` deve incluir `preparar_ssl()` conforme §2.2 acima. |
| `audio.md` | §5.2 declaração de duração | Duração declarada vem do `ffprobe` sobre o arquivo real gerado nesta sessão. |
| `README.md` | §8 declarações de artefato | `[ARTEFATO: código gerado]` inclui o binário entregue. `[ARTEFATO: execução local necessária]` é exceção, não regra. |
| `html.md` | §5.8 localStorage | Permitido em HTML salvo como arquivo local (destino = navegador do usuário). Não aplicável a artifacts renderizados no chat do Claude. |

---

## 4. O que não muda

Tudo o mais segue os módulos comuns sem modificação:

- Escopo definido pelo plano de ensino e cronograma de aulas.
- Fases 0 → F do `/pafe completo`.
- Regras anti-simulação: sem loop, sem silêncio artificial para inflar duração.
- Dicionário fonético e três vozes pt-BR (`FranciscaNeural`, `AntonioNeural`, `ThalitaNeural`).
- Piso de duração validado por `ffprobe`; script falha se abaixo do mínimo.
- Hierarquia de confiabilidade de fontes (plano de ensino > fonte oficial > texto do usuário > resposta de outra IA).
- Política anti-hallucination e regras de citação jurisprudencial.

---

## 5. Histórico de versões

| Versão | Data | Motivo |
|---|---|---|
| 1.0 | 2026-06-09 | Criação. Deriva da análise comparativa entre a entrega de Criminologia (MP3 gerado em sessão) e Direito de Família (MP3 não gerado por ausência do tratamento de SSL e da regra §2.1). |
