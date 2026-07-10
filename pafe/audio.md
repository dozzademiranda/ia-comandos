# audio.md — Módulo P.A.F.E. de Áudio para Disciplinas de Direito

**Versão:** audio.md v6.2 MASTER  
**Data:** 2026-07-10  
**Escopo:** pipeline local/remoto, governança de motores TTS, auditoria e segurança de áudio jurídico-didático.  
**Regra central:** não existe áudio gerado sem arquivo físico real, duração validada e cadeia mínima de rastreabilidade.

> Para interpretar `/pafe audio`, `/pafe html audio` e `/pafe completo`, ler primeiro `pafe/audio_modos.md`. Este arquivo regula **como gerar** tecnicamente: pacote local, preflight, segurança, TTS, validação, manifesto e auditoria.

---

## 1. Finalidade

Este arquivo define o padrão operacional para geração de áudios de estudo no P.A.F.E. para disciplinas de Direito.

O áudio P.A.F.E. não é mero TTS. Deve ensinar, revisar, testar, fixar e reduzir fricção cognitiva.

---

## 2. Modos de áudio

A decisão do modo fica em `audio_modos.md`.

Resumo:

1. MP3 direto: padrão quando a plataforma consegue gerar arquivo real.
2. Roteiro textual: somente se pedido ou autorizado como fallback.
3. Pacote local: somente se o usuário pedir `pacote`, `local`, `script`, `yaml` ou equivalente.
4. Rota remota: GitHub Actions, Codespaces ou API premium autorizada.
5. Claude com execução ativa: aplicar também `pafe_claude.md`; ele pode gerar MP3 direto no próprio turno.

---

## 3. Proibições absolutas

É proibido:

1. afirmar que MP3 foi gerado sem arquivo físico;
2. simular duração por loop;
3. duplicar áudio para fingir duração;
4. inserir silêncio artificial para atingir tempo mínimo;
5. usar fallback robótico como padrão;
6. declarar duração sem validação técnica;
7. embutir API key em chat, código, HTML, Markdown, log ou manifesto;
8. versionar `.env`;
9. usar SSL relaxado como padrão;
10. usar SSL relaxado com senha, token, API key, dados sensíveis, peça jurídica sigilosa ou documento de cliente.

---

## 4. Segurança de chaves e APIs externas

APIs externas como OpenAI TTS, Gemini TTS, ElevenLabs, Hume AI, Narakeet ou equivalentes só podem ser usadas com autorização expressa.

Regras:

1. chave sempre em `.env`, variável de ambiente ou GitHub Secrets;
2. criar `.env.example` sem segredo real;
3. incluir `.env` no `.gitignore`;
4. estimar custo/caracteres antes de API paga;
5. declarar qual provedor externo receberá texto;
6. nunca repetir chave no log;
7. nunca colar chave no chat;
8. IA que pedir chave no chat está errada — recusar e orientar `.env`/Secrets.

---

## 5. Hierarquia documental do conteúdo

Ao criar roteiro jurídico de áudio, aplicar:

1. plano de ensino, ementa, cronograma, programa oficial;
2. PDFs, slides, cadernos, anotações e materiais do professor;
3. provas anteriores, listas, simulados e questões;
4. legislação vigente validada;
5. jurisprudência oficial validada;
6. bibliografia indicada;
7. respostas de IA como objeto de análise, nunca como prova;
8. web somente quando autorizada ou necessária para atualização.

Se algo não estiver na base:

```text
não documentado no material disponível
```

Se depender de validação:

```text
precisa validar antes de usar
```

---

## 6. Arquitetura CODE vs DATA

É proibido injetar roteiros massivos acima de 2.000 palavras diretamente no script Python.

O script deve ler arquivos externos:

```text
audio/roteiro_audio.txt
audio/audio.yaml
audio/dicionario_fonetico.yaml
audio/suspeitos_foneticos.csv
```

O código deve conter apenas lógica de leitura, validação, sanitização, fonética, chunking, síntese, retry, normalização, concatenação, validação, log e manifesto.

---

## 7. Estrutura de pacote local

Quando o usuário pedir pacote local, entregar:

```text
pafe_audio_[disciplina]/
├── README_AUDIO.md
├── requirements_audio.txt
├── setup_audio.sh
├── gerar_audio_v2.py
├── validar_audio.sh
├── flashcards_audio.csv
├── .env.example
├── .gitignore
└── audio/
    ├── roteiro_audio.txt
    ├── audio.yaml
    ├── dicionario_fonetico.yaml
    ├── suspeitos_foneticos.csv
    ├── dicionario_fonetico_runtime.yaml
    ├── dicionario_fonetico_revisado.yaml
    ├── chapters.json
    ├── manifest_audio.json
    ├── log_geracao_audio.txt
    ├── parts/
    └── master_audio.mp3
```

Se o MP3 não for gerado, não incluir `master_audio.mp3` e declarar execução local necessária.

---

## 8. Duração e palavras

Usar cálculo conservador:

```text
150 palavras por minuto
```

| Duração | Palavras úteis recomendadas |
|---:|---:|
| 15 min | 2.300 a 2.700 |
| 30 min | 4.500 a 5.200 |
| 45 min | 6.800 a 7.800 |
| 60 min | 9.000 a 10.500 |
| 90 min | 13.500 a 15.800 |
| 120 min | 18.000 a 22.000 |
| 180 min | 27.000 a 33.000 |

É proibido inflar duração com silêncio, loop ou repetição vazia.

---

## 9. Estrutura didática do roteiro

O roteiro deve conter, conforme o escopo:

1. abertura objetiva;
2. mapa mental da prova;
3. conceitos centrais;
4. artigos mais prováveis;
5. doutrina essencial;
6. jurisprudência essencial, se aplicável;
7. comparação entre institutos;
8. pegadinhas;
9. questões comentadas;
10. revisão espaçada;
11. checklist de véspera;
12. revisão relâmpago.

Para Direito material: conceito, natureza, fundamento, requisitos, efeitos, exceções, jurisprudência, comparação, exemplo e pegadinha.

Para Direito processual: cabimento, competência, legitimidade, prazo, procedimento, efeitos, recursos, nulidades, preclusões e pegadinhas.

---

## 10. Acessibilidade cognitiva

Obrigatório:

1. frases curtas;
2. avisos de transição;
3. repetição pedagógica moderada;
4. exemplos práticos;
5. “se aparecer X, pense em Y”;
6. pausas entre blocos;
7. retomadas periódicas;
8. separação entre regra, exceção e pegadinha.

Evitar parede sonora, leitura mecânica de tabelas, latim sem tradução, excesso de siglas e tom motivacional vazio.

---

## 11. Sanitização pré-TTS

Antes da síntese, aplicar:

```text
sanitize_for_tts(texto)
```

A função deve remover Markdown pesado, expandir abreviações jurídicas, narrar tabelas como texto contínuo, evitar leitura literal de URLs longas, preservar conteúdo jurídico e nunca alterar sentido.

---

## 12. Pausas, ritmo e anti-fadiga

Padrão para revisão jurídica longa em `edge-tts`:

```text
rate: -10% a -12%
```

Matriz de pausas:

| Tipo | Duração | Uso |
|---|---:|---|
| Micro-pausa | 300 a 500 ms | listas, incisos, enumerações |
| Pausa pedagógica | 3000 a 3500 ms | fim de bloco |
| Pausa de capítulo | 4000 a 6000 ms | mudança forte de tema |

Tratamento anti-fadiga: fade curto por chunk, fade inicial/final no master, evitar cortes abruptos e detectar silêncios longos acidentais quando possível.

---

## 13. Normalização e loudness

Padrão:

```text
FFmpeg loudnorm
I=-20 LUFS
TP=-1.5 dBTP
LRA=11
```

Perfis:

| Perfil | Alvo | Uso |
|---|---:|---|
| `study_long` | -20 LUFS | estudo longo, fone, baixa fadiga |
| `podcast` | -16 LUFS | audição casual |
| `mobile_noisy` | -14 LUFS | rua, ônibus, ambiente ruidoso |

Padrão P.A.F.E.:

```text
normalization_profile: study_long
```

---

## 14. Preflight de áudio

O preflight opera em três camadas independentes; cada camada tem correção própria. Nunca pular etapas nem trocar de motor sem terminar o diagnóstico.

### 14.1. Camada 1 — rede/DNS

Testar:

```bash
nslookup speech.platform.bing.com
getent hosts speech.platform.bing.com
```

Correção: verificar conexão, DNS do sistema, proxy ou trocar ambiente.

### 14.2. Camada 2 — SSL/certificado

Sinais: `CERTIFICATE_VERIFY_FAILED`, `SSLCertVerificationError`, `self-signed certificate in certificate chain`.

Correção padrão:

1. tentar CA do sistema;
2. tentar proxy configurado;
3. no Claude, ver `pafe_claude.md` §2.2 para o código de referência;
4. SSL relaxado somente como diagnóstico de última instância;
5. SSL relaxado é proibido com credenciais, API keys, senhas, tokens, dados sensíveis ou material sigiloso.

### 14.3. Camada 3 — endpoint/serviço

Fazer síntese real de 1 frase com `pt-BR-FranciscaNeural` e validar por `ffprobe`.

```bash
edge-tts --voice pt-BR-FranciscaNeural --text "Teste PAFE." --write-media teste_pafe.mp3
ffprobe -v error -show_entries format=duration,bit_rate,size -of default=noprint_wrappers=1 teste_pafe.mp3
```

Se DNS e SSL passarem, mas o teste real falhar, classificar como endpoint/serviço, autenticação, cota, dependência local ou indisponibilidade temporária.

---

## 15. Dicionário fonético

Arquivos:

```text
audio/dicionario_fonetico.yaml
audio/suspeitos_foneticos.csv
audio/dicionario_fonetico_runtime.yaml
audio/dicionario_fonetico_revisado.yaml
```

Fluxo:

1. texto-base permanece intacto;
2. `sanitize_for_tts()` cria cópia falável;
3. dicionário atua só na cópia falável;
4. termos duvidosos vão para `suspeitos_foneticos.csv`;
5. termos aprovados migram para YAML revisado;
6. log registra substituições;
7. `--no-phonetic` desativa.

Exemplos: `art.` → artigo; `CC` → Código Civil; `STJ` → Superior Tribunal de Justiça; `REsp` → recurso especial; `ex tunc` → com efeitos retroativos.

---

## 16. Motores TTS

### 16.1. Padrão gratuito

```text
edge-tts
```

Vozes preferenciais:

```text
pt-BR-FranciscaNeural — conceitos e sínteses
pt-BR-AntonioNeural — fundamento legal e jurisprudência
pt-BR-ThalitaNeural — pegadinhas e revisão
```

### 16.2. Motores premium via API

Motores premium (ElevenLabs, OpenAI TTS, Hume, Gemini TTS, Narakeet ou equivalente) são opcionais. Só usar se o usuário pedir expressamente. `edge-tts` permanece como motor gratuito preferencial.

Segurança transversal:

1. nunca colar API key, senha ou token em prompt de nenhuma IA;
2. chaves vivem em `.env` local, variável de ambiente ou GitHub Secrets;
3. IA que pedir chave no chat está errada — recusar;
4. não versionar `.env`;
5. incluir `.env.example`.

Custo e privacidade:

1. estimar custo por caractere antes de gerar;
2. avisar que o texto é enviado a terceiro;
3. permitir manter `edge-tts` como fallback gratuito;
4. registrar no log a rota efetivamente usada.

### 16.3. ElevenReader

ElevenReader é modo manual de escuta/revisão, não API. Gerar roteiro textual limpo, sem Markdown pesado, tabela, YAML, JSON ou código. Não presumir MP3 exportável nem créditos de ElevenLabs API.

### 16.4. Piper offline

Plano B offline, sem chave. Qualidade inferior à neural online deve ser declarada; vozes pt-BR devem ser validadas na primeira execução local antes de virar padrão.

### 16.5. Fallbacks proibidos

Não usar como padrão: `espeak`, `espeak-ng`, `pyttsx3`, Festival, voz metálica local ou gTTS robótico.

---

## 17. Rotas remotas de contingência

A decisão de rota pertence a `audio_modos.md`. Este arquivo só fixa requisitos mínimos das rotas técnicas.

### 17.1. GitHub Actions

Usar quando ambiente local/chat não tem rede confiável ou quando se quer execução automatizada.

Registrar:

1. workflow usado;
2. `ffprobe` do teste curto;
3. `ffprobe` do master;
4. `sha256sum` do MP3;
5. log stdout/stderr;
6. artifact digest quando disponível.

Estado: documentado; exige primeira execução assistida antes de virar padrão.

### 17.2. Codespaces

Usar como terminal remoto manual para testar dependências, rede, vozes e geração.

Estado: documentado; exige primeira execução assistida antes de virar padrão.

---

## 18. Script `gerar_audio_v2.py`

Quando houver pacote local, o script deve:

1. ler `audio/audio.yaml`;
2. validar schema;
3. ler `audio/roteiro_audio.txt`;
4. aplicar `sanitize_for_tts()`;
5. aplicar dicionário fonético;
6. dividir blocos longos;
7. gerar partes;
8. aplicar retry;
9. permitir `--resume`;
10. concatenar;
11. normalizar;
12. gerar `chapters.json`;
13. gerar `manifest_audio.json`;
14. gerar `log_geracao_audio.txt`;
15. validar com `ffprobe`;
16. calcular `sha256_master` do `audio/master_audio.mp3` quando houver MP3;
17. falhar se abaixo do mínimo;
18. preservar partes, salvo `--clean-parts`.

Argumentos esperados: `--preflight`, `--resume`, `--force`, `--validate-only`, `--min-minutes`, `--chunk-words`, `--no-phonetic`, `--clean-parts`, `--normalization-profile`, `--engine`, `--dry-run`.

---

## 19. `audio.yaml`

Campos mínimos:

```yaml
metadata:
  projeto: "P.A.F.E."
  audio_md_version: "v6.2 MASTER"
  disciplina: "Nome da disciplina"
  escopo: "prova / bimestre / revisão"
  idioma: "pt-BR"
  duracao_minima_minutos: 60
  proibido_simular_duracao: true
  validacao_obrigatoria: "ffprobe"

config:
  motor_padrao: "edge-tts"
  formato_saida: "mp3"
  roteiro: "audio/roteiro_audio.txt"
  arquivo_final: "audio/master_audio.mp3"
  pasta_partes: "audio/parts"
  normalization_profile: "study_long"
  chunk_words_padrao: 600
  pausas:
    micro_ms: 400
    pedagogica_ms: 3500
    capitulo_ms: 5000

vozes:
  conceito: "pt-BR-FranciscaNeural"
  fundamento: "pt-BR-AntonioNeural"
  revisao: "pt-BR-ThalitaNeural"
```

Cada bloco deve ter: `id`, `ordem`, `titulo`, `chapter_title`, `voz`, `texto`, `palavras_estimadas`, `pause_after_ms`.

---

## 20. Manifesto e logs

`manifest_audio.json` deve registrar:

1. `audio_md_version`;
2. `tts_engine`;
3. `normalization_profile`;
4. `source_hash`;
5. `content_hash`;
6. `audio_yaml_hash`;
7. `script_hash`;
8. duração real;
9. palavras totais;
10. blocos/chunks;
11. retries/falhas;
12. LUFS/LRA/true peak quando disponível;
13. `ffprobe`;
14. `sha256sum`;
15. `sha256_master` — hash SHA-256 do arquivo `audio/master_audio.mp3`;
16. artifact digest quando houver GitHub Actions;
17. status final.

Finalidade do `sha256_master`: conferir integridade após transferência/download; independe do `ffprobe`.

Nunca registrar segredo.

---

## 21. HTML com áudio

Quando houver HTML:

1. player deve apontar para `audio/master_audio.mp3`;
2. se o MP3 não existir, mostrar aviso;
3. não usar CDN obrigatória;
4. manter offline;
5. não embutir API key.

Tag base:

```html
<audio controls loop preload="metadata" src="audio/master_audio.mp3" style="width:100%;"></audio>
```

---

## 22. Critérios de aprovação

Aprovado somente se:

1. roteiro existe;
2. fonte incerta está marcada;
3. não há invenção jurídica;
4. se há MP3, arquivo físico existe;
5. duração foi validada;
6. não há loop/silêncio/duplicação artificial;
7. não há segredo exposto;
8. manifesto/log existem quando pacote técnico;
9. falhas foram classificadas;
10. fallback foi autorizado.

---

## 23. Remissão ao roteador de modo

Este arquivo define **como** gerar o áudio. Onde/quem gera é decisão do roteador em `audio_modos.md`: rota local, Claude em sessão, GitHub Actions, Codespaces, Piper offline e API premium. Consultar `audio_modos.md` antes de decidir a rota.

---

## 24. Histórico

| Versão | Data | Motivo |
|---|---|---|
| v6.2 MASTER | 2026-07-10 | Renomeia preflight para “preflight de áudio”, consolida 3 camadas DNS/SSL/endpoint, generaliza motores premium, inclui `sha256_master` e remete rotas para `audio_modos.md`. |
| v6.1 MASTER | 2026-07-10 | Incorpora deltas do prompt anexado: Claude pode gerar MP3 direto; separa DNS × SSL × endpoint; adiciona GitHub Actions/Codespaces, artifact digest, checksums, launchers e fallback Piper; corrige regra local-only absoluta. |
| v6.0 MASTER | 2026-07-08 | Sanitização pré-TTS, pausas, LUFS, governança fonética, manifesto avançado, rotas OpenAI/Gemini/ElevenLabs/Hume/NotebookLM/Make/n8n. |
| v5.0 MASTER | 2026-07-06 | CODE vs DATA, roteiro externo, cadência didática, pausas pedagógicas, fade, loudness, retry, dicionário fonético e validação. |
| v2.1 | 2026-06-09 | Smoke test Claude, duração-alvo, preparar_ssl, gap, fade e capítulos ID3. |