# audio.md — Módulo P.A.F.E. de Áudio para Disciplinas de Direito

**Versão:** audio.md v6.0 MASTER  
**Data:** 2026-07-08  
**Escopo:** geração, auditoria e governança de áudio jurídico-didático no P.A.F.E.  
**Regra central:** não existe áudio gerado sem arquivo físico real, duração validada e cadeia mínima de rastreabilidade.

---

## 1. Finalidade

Este arquivo define o padrão operacional para geração de áudios de estudo no ecossistema P.A.F.E. para qualquer disciplina de Direito.

O objetivo é produzir áudio jurídico-didático, validável, reutilizável e compatível com estudo de prova, revisão de véspera, treino de questões, memorização de artigos, doutrina, jurisprudência e pegadinhas.

O áudio P.A.F.E. não é mero TTS. O roteiro deve ensinar, revisar, testar, fixar e reduzir fricção cognitiva.

---

## 2. Princípios obrigatórios

### 2.1. Não simular áudio

É proibido:

1. afirmar que um MP3 foi gerado sem existir arquivo físico real;
2. simular duração por loop;
3. duplicar áudio para fingir maior duração;
4. inserir silêncio artificial para atingir tempo mínimo;
5. inflar duração com repetições vazias;
6. declarar “áudio de 2 horas” sem validação real por ferramenta técnica;
7. substituir conteúdo jurídico por narração genérica.

Se o ambiente não puder gerar MP3 real, declarar:

> [ARTEFATO: execução local necessária] — O MP3 ainda não foi gerado nesta plataforma. O arquivo `master_audio.mp3` só existirá após execução local bem-sucedida do script de geração.

Quando o agente for Claude com ambiente de execução ativo, antes de declarar execução local necessária é obrigatório rodar um smoke test de TTS no próprio turno, conforme `pafe_claude.md` §2.1. Só declarar impossível após falha confirmada com diagnóstico.

### 2.2. Segurança de chaves e provedores externos

É proibido:

1. pedir que o usuário cole API key no chat;
2. gravar chave em memória;
3. embutir chave em script, HTML, JavaScript, Markdown, prompt, log ou manifesto;
4. versionar `.env`;
5. imprimir chave no terminal;
6. enviar texto jurídico sensível a API externa sem consentimento.

Regra segura:

1. usar `.env` ou variável de ambiente;
2. criar `.env.example` sem segredo real;
3. incluir `.gitignore` com `.env`;
4. estimar custo/caracteres antes de API paga;
5. declarar qual provedor externo receberá texto;
6. permitir fallback gratuito/local quando possível.

### 2.3. Áudio deve ser juridicamente útil

O áudio deve conter, conforme o material disponível:

1. explicação conceitual;
2. base legal;
3. doutrina indicada ou disponível;
4. jurisprudência indicada ou validada;
5. divergências relevantes;
6. pegadinhas de prova;
7. questões comentadas;
8. revisão progressiva;
9. revisão de véspera;
10. revisão relâmpago.

Não basta ler um resumo. O áudio deve transformar o material em estudo oral operacional.

### 2.4. Hierarquia documental

Ao gerar áudio jurídico, aplicar esta ordem de prevalência:

1. plano de ensino, ementa, cronograma oficial e conteúdo efetivamente ministrado;
2. PDFs, slides, cadernos, anotações e materiais do professor;
3. questões de prova, QConcursos, provas anteriores e simulados anexados;
4. legislação seca vigente, quando validada;
5. jurisprudência oficial, quando validada;
6. bibliografia oficial da disciplina;
7. materiais de revisão de IA, tratados como objeto de análise, não como prova;
8. conhecimento jurídico interno, apenas para organizar e explicar;
9. web somente se autorizada ou indispensável para atualização normativa/jurisprudencial.

Se a fonte não estiver acessível, escrever:

> não documentado no material disponível.

Se artigo, súmula, precedente ou dado não tiver sido validado, escrever:

> precisa validar antes de usar.

---

## 3. Arquitetura CODE vs DATA

É proibido injetar roteiros massivos acima de 2.000 palavras diretamente dentro do script Python, seja em listas, dicionários, strings triplas ou JSON embutido.

O script Python deve atuar como MOTOR de geração, lendo arquivos externos:

```text
audio/roteiro_audio.txt
audio/audio.yaml
audio/dicionario_fonetico.yaml
audio/suspeitos_foneticos.csv
```

O roteiro jurídico deve ficar em arquivo de dados. O código deve conter apenas lógica de leitura, validação, chunking, sanitização, fonética, síntese, retry, normalização, concatenação, validação, log e manifesto.

Exceção: smoke test, exemplo mínimo de documentação ou demonstração com menos de 2.000 palavras.

---

## 4. Saídas obrigatórias

Sempre que o usuário pedir geração completa de áudio, entregar:

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
    │   ├── 001_bloco_001.mp3
    │   ├── 002_bloco_002.mp3
    │   └── ...
    └── master_audio.mp3
```

Se o MP3 não puder ser gerado na plataforma, entregar todos os arquivos possíveis, exceto `master_audio.mp3`, com instrução clara para geração local.

---

## 5. Duração mínima e palavras estimadas

Usar como estimativa média:

```text
145 a 165 palavras por minuto em português do Brasil.
```

Para áudio jurídico, preferir cálculo conservador de 150 palavras por minuto.

| Duração-alvo | Palavras mínimas recomendadas | Uso típico |
|---:|---:|---|
| 15 min | 2.300 a 2.700 | revisão curta |
| 30 min | 4.500 a 5.200 | revisão de aula |
| 45 min | 6.800 a 7.800 | revisão de tema grande |
| 60 min | 9.000 a 10.500 | revisão de bimestre |
| 90 min | 13.500 a 15.800 | revisão intensiva |
| 120 min | 18.000 a 22.000 | revisão completa |
| 180 min | 27.000 a 33.000 | maratona |

Se o roteiro tiver menos palavras do que o mínimo estimado, expandir o roteiro antes de tentar gerar o áudio. É proibido inflar duração com silêncio, loop, duplicação ou conteúdo vazio.

---

## 6. Estrutura didática do roteiro

### 6.1. Estrutura mínima

Todo roteiro jurídico de áudio deve conter, conforme o escopo:

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
11. resumo final;
12. checklist de véspera;
13. revisão relâmpago.

### 6.2. Direito material

Quando a disciplina for de Direito material, organizar por:

1. conceito;
2. natureza jurídica;
3. fundamento legal;
4. requisitos;
5. efeitos;
6. exceções;
7. jurisprudência;
8. comparação com instituto próximo;
9. exemplo prático;
10. pegadinha de prova.

### 6.3. Direito processual

Quando a disciplina for processual, organizar por:

1. cabimento;
2. competência;
3. legitimidade;
4. prazo;
5. procedimento;
6. efeitos;
7. recursos;
8. nulidades;
9. preclusões;
10. pegadinhas de prova.

### 6.4. Matriz D.S.C.P.E.

Para conteúdos processuais, recursais, peças, decisões, nulidades e fluxos de prova, usar preferencialmente:

```text
D — Decisão: qual ato, problema ou decisão existe?
S — Sistema: qual ramo, rito, competência ou regime jurídico rege?
C — Cabimento: o que cabe, quando cabe e por qual fundamento?
P — Prazo: qual prazo, termo inicial e forma de contagem?
E — Efeitos: o que muda no processo, no direito material e na estratégia?
```

A matriz D.S.C.P.E. não é obrigatória para todo Direito. Em conteúdos dogmáticos materiais, usar matriz conceito → fundamento → requisitos → efeitos → exceções → pegadinhas.

### 6.5. Jurisprudência

Quando houver STF/STJ/TST/TSE/TRE/TRF/TJ:

1. separar tese firmada, precedente isolado e tendência;
2. não transformar precedente isolado em regra geral;
3. indicar divergência quando houver;
4. em divergência STF × STJ, expor ambas antes da conclusão;
5. declarar “não documentado” quando a fonte não estiver disponível;
6. não inventar número de RE, REsp, AREsp, Tema, súmula ou informativo.

---

## 7. Acessibilidade cognitiva

O áudio deve respeitar estudo com TDAH, TEA nível 1, ansiedade, burnout e fadiga cognitiva.

### 7.1. Obrigatório

1. frases curtas e claras;
2. avisos de transição;
3. repetição pedagógica moderada;
4. exemplos práticos;
5. “se aparecer X, pense em Y”;
6. pausas entre blocos;
7. retomadas periódicas;
8. evitar blocos homogêneos muito longos;
9. explicar antes de aprofundar;
10. separar regra, exceção e pegadinha.

### 7.2. Evitar

1. parede sonora sem pausas;
2. longas listas sem organização;
3. leitura mecânica de tabelas;
4. excesso de latim sem tradução;
5. excesso de siglas;
6. tom motivacional vazio;
7. linguagem épica ou teatral;
8. excesso de “atenção” sem critério;
9. blocos de mais de 12 minutos sem transição;
10. alternância desnecessária de vozes.

---

## 8. Sanitização pré-TTS

Antes da síntese, aplicar função conceitual obrigatória:

```text
sanitize_for_tts(texto)
```

Finalidade: transformar texto escrito em texto falável, sem alterar o sentido jurídico.

A função deve:

1. remover Markdown pesado que não deva ser narrado;
2. converter `#`, `##`, `**`, `*`, pipes de tabela e marcadores em fala natural;
3. converter `art.` em “artigo” e `arts.` em “artigos”;
4. converter `§` em “parágrafo”;
5. converter `inc.` em “inciso”, quando aplicável;
6. converter algarismos romanos de norma em “inciso primeiro”, “inciso segundo”, conforme o contexto;
7. transformar tabelas em narrativa contínua;
8. evitar leitura literal de URLs longas;
9. preservar citações legais, números de artigos, súmulas, temas e precedentes;
10. nunca mudar o conteúdo jurídico-base.

Exemplo:

```text
Entrada: art. 927, parágrafo único, CC.
Saída falada: artigo 927, parágrafo único, do Código Civil.
```

---

## 9. Pausas, cadência e anti-fadiga

### 9.1. Cadência

Áudio P.A.F.E. é material de estudo denso, não narração expressa.

Padrão para `edge-tts` em revisão longa:

```text
rate: -10% a -12%
```

O motor deve permitir ajuste por bloco, mas a configuração-base deve ser lenta o suficiente para processamento cognitivo.

### 9.2. Matriz tripla de pausas

| Tipo de pausa | Duração recomendada | Uso |
|---|---:|---|
| Micro-pausa | 300 a 500 ms | listas, incisos, enumerações, separação de alternativas |
| Pausa pedagógica | 3000 a 3500 ms | fim de bloco, assimilação, respiração cognitiva |
| Pausa de capítulo | 4000 a 6000 ms | mudança forte de assunto, módulo ou tema |

As pausas são para aprendizagem. Continuam proibidas pausas vazias usadas apenas para simular duração.

### 9.3. Tratamento anti-fadiga

A concatenação bruta de chunks MP3 pode gerar estalos, pops, clicks e fadiga auditiva.

Obrigatório:

1. aplicar `fade_in(50)` e `fade_out(50)` em cada chunk;
2. aplicar fade inicial/final no master entre 800 ms e 1200 ms;
3. evitar cortes abruptos entre blocos;
4. validar silêncios longos acidentais com `silencedetect`, quando possível.

---

## 10. Normalização e loudness

### 10.1. Padrão

Normalização obrigatória quando possível:

```text
FFmpeg loudnorm
I=-20 LUFS
TP=-1.5 dBTP
LRA=11
```

Correção terminológica:

1. LUFS, LRA e true peak pertencem à medição de loudness;
2. `-20 dBFS` por Pydub é fallback de amplitude/RMS, não EBU R128 completo;
3. quando se falar em EBU R128, usar LUFS, LRA e true peak.

### 10.2. Perfis adaptativos

| Perfil | Alvo | Uso |
|---|---:|---|
| `study_long` | -20 LUFS | estudo longo, fone, baixa fadiga |
| `podcast` | -16 LUFS | audição casual, caixa de som |
| `mobile_noisy` | -14 LUFS | rua, ônibus, ambiente ruidoso |

Padrão P.A.F.E.:

```text
normalization_profile: study_long
```

`mobile_noisy` é opcional e pode gerar mais fadiga. Não usar como padrão para audiolivro jurídico longo.

---

## 11. Dicionário fonético e governança

### 11.1. Arquivos

Usar:

```text
audio/dicionario_fonetico.yaml
audio/suspeitos_foneticos.csv
audio/dicionario_fonetico_runtime.yaml
audio/dicionario_fonetico_revisado.yaml
```

### 11.2. Fluxo

1. O texto-base permanece intacto.
2. `sanitize_for_tts()` prepara a cópia falada.
3. O dicionário fonético aplica substituições apenas na cópia falada.
4. Termos duvidosos são lançados em `suspeitos_foneticos.csv`.
5. O usuário revisa os suspeitos.
6. Termos aprovados podem migrar para `dicionario_fonetico_revisado.yaml`.
7. O log registra substituições aplicadas.
8. O recurso pode ser desligado com `--no-phonetic`.

### 11.3. Exemplo de `dicionario_fonetico.yaml`

```yaml
substituicoes:
  "art.": "artigo"
  "arts.": "artigos"
  "CC": "Código Civil"
  "CPC": "Código de Processo Civil"
  "CPP": "Código de Processo Penal"
  "CP": "Código Penal"
  "CF": "Constituição Federal"
  "CLT": "Consolidação das Leis do Trabalho"
  "CDC": "Código de Defesa do Consumidor"
  "ECA": "Estatuto da Criança e do Adolescente"
  "STF": "Supremo Tribunal Federal"
  "STJ": "Superior Tribunal de Justiça"
  "TST": "Tribunal Superior do Trabalho"
  "TSE": "Tribunal Superior Eleitoral"
  "RE": "recurso extraordinário"
  "REsp": "recurso especial"
  "AREsp": "agravo em recurso especial"
  "HC": "habeas corpus"
  "MS": "mandado de segurança"
  "ex tunc": "com efeitos retroativos"
  "ex nunc": "com efeitos a partir de agora"
  "fumus boni iuris": "fúmus bóni iúris"
  "periculum in mora": "perículum in móra"
  "ratio decidendi": "rácio decidêndi"
  "obiter dictum": "óbiter díctum"
  "Exequatur": "Éks-e-quá-tur"
  "Kompetenz-Kompetenz": "Kômpetentz Kômpetentz"
  "jure imperii": "júri impéri"
  "jure gestionis": "júri géstionis"
  "ad hoc": "ad róc"
  "Las Leñas": "Lás Lê-nhas"
```

Nunca aplicar substituição que altere sentido jurídico.

---

## 12. Padrão do `audio.yaml`

### 12.1. Estrutura mínima

```yaml
metadata:
  projeto: "P.A.F.E."
  audio_md_version: "v6.0 MASTER"
  disciplina: "Nome da disciplina"
  escopo: "1º bimestre / prova final / revisão"
  idioma: "pt-BR"
  duracao_minima_minutos: 120
  palavras_minimas: 18000
  proibido_simular_duracao: true
  validacao_obrigatoria: "ffprobe"
  observacao: "Não afirmar MP3 gerado sem arquivo físico real."

config:
  motor_padrao: "edge-tts"
  formato_saida: "mp3"
  pasta_partes: "audio/parts"
  arquivo_final: "audio/master_audio.mp3"
  roteiro: "audio/roteiro_audio.txt"
  dicionario_fonetico: "audio/dicionario_fonetico.yaml"
  suspeitos_foneticos: "audio/suspeitos_foneticos.csv"
  chunk_words_padrao: 600
  min_duration_seconds: 7200
  normalization_profile: "study_long"
  loudnorm:
    I: -20
    TP: -1.5
    LRA: 11
  pausas:
    micro_ms: 400
    pedagogica_ms: 3500
    capitulo_ms: 5000
  sanitizacao:
    habilitada: true
  fonetica:
    habilitada: true

vozes:
  conceito: "pt-BR-FranciscaNeural"
  fundamento: "pt-BR-AntonioNeural"
  revisao: "pt-BR-ThalitaNeural"

blocos:
  - id: "bloco_001"
    ordem: 1
    titulo: "Abertura e estratégia"
    chapter_title: "Estratégia"
    voz: "pt-BR-FranciscaNeural"
    rate: "-10%"
    pitch: "+0Hz"
    pause_after_ms: 3500
    pausa_tipo: "pedagogica"
    palavras_estimadas: 900
    tipo: "abertura"
    base: ["plano de ensino", "anexos"]
    tags: ["estrategia", "prova"]
    texto: |
      Texto do bloco aqui.
```

### 12.2. Campos obrigatórios por bloco

1. `id`;
2. `ordem`;
3. `titulo`;
4. `chapter_title`;
5. `voz`;
6. `texto`;
7. `palavras_estimadas`;
8. `pause_after_ms`.

### 12.3. Campos opcionais por bloco

1. `rate`;
2. `pitch`;
3. `volume`;
4. `tipo`;
5. `base`;
6. `tags`;
7. `questoes_referenciadas`;
8. `pausa_tipo`;
9. `audio_tags`;
10. `normalization_profile`.

---

## 13. Vozes, motores e rotas de síntese

### 13.1. Motor padrão

O motor padrão gratuito/local continua sendo:

```text
edge-tts
```

Vozes preferenciais:

```text
pt-BR-FranciscaNeural — conceitos, sínteses e revisão geral
pt-BR-AntonioNeural — fundamentação legal, artigos, jurisprudência
pt-BR-ThalitaNeural — pegadinhas, revisão de véspera, alertas
```

Se alguma voz não estiver disponível, o script deve listar vozes `pt-BR` disponíveis e solicitar ou aplicar fallback seguro.

### 13.2. APIs externas opcionais

APIs externas só devem ser usadas se o usuário pedir ou autorizar expressamente.

Provedores possíveis:

1. OpenAI TTS;
2. Gemini TTS;
3. ElevenLabs;
4. Hume AI;
5. outro provedor expressamente indicado.

Regras:

1. chave sempre por `.env`;
2. nunca colar chave no prompt;
3. nunca registrar chave em log;
4. estimar custo;
5. declarar envio de texto a serviço externo;
6. preservar fallback Edge-TTS.

### 13.3. OpenAI CLI

Pode ser documentada como rota opcional para quem prefere terminal e não quer escrever script Python.

Condições:

1. usar variável de ambiente;
2. não inserir chave no comando;
3. salvar saída em MP3 real;
4. validar por `ffprobe`;
5. registrar no manifesto como `tts_engine: openai_cli`.

### 13.4. Gemini TTS e tags de áudio

Gemini TTS pode ser rota opcional avançada quando houver suporte a controle por linguagem natural e tags expressivas.

Regras para estudo jurídico:

1. usar tags com moderação;
2. preferir `[serious]`, `[slowly]`, `[calm]`;
3. usar `[whispers]` apenas para pegadinhas ou alertas pontuais;
4. evitar teatralização;
5. registrar tags no `audio.yaml`;
6. manter roteiro limpo sem tags quando for necessário gerar por outro motor.

### 13.5. ElevenLabs

ElevenLabs é opcional e útil para vozes de alta naturalidade.

Regras:

1. usar `ELEVENLABS_API_KEY` no `.env`;
2. usar voice IDs em configuração externa;
3. não inserir chave em código;
4. estimar caracteres;
5. validar MP3 final por `ffprobe`;
6. registrar provedor e voz no manifesto.

### 13.6. Hume AI

Hume AI é opcional e deve usar script próprio, separado do script ElevenLabs.

Regras:

1. usar `HUME_API_KEY` no `.env`;
2. não confundir API key com voice ID;
3. não tentar usar chave Hume no script ElevenLabs;
4. registrar provedor e voz no manifesto.

### 13.7. NotebookLM / Gemini Audio Overview

NotebookLM ou Gemini Audio Overview podem ser usados como rota auxiliar rápida para gerar visão oral conversacional.

Limitações:

1. não substitui pipeline P.A.F.E. auditável;
2. pode resumir demais;
3. não garante chunking, capítulos, LUFS, hash, log e manifesto;
4. não deve ser tratado como master canônico de prova.

Uso recomendado:

```text
rota auxiliar rápida, não substituta do pacote P.A.F.E.
```

### 13.8. Make/n8n

Make e n8n podem ser documentados como arquitetura opcional no-code:

```text
Google Drive / pasta de texto
→ Make ou n8n
→ API TTS
→ salvar MP3
→ salvar log/manifesto
→ validar quando possível
```

Não prometer fluxo pronto sem credenciais, módulos disponíveis e teste real.

### 13.9. Rotas não canônicas

Não usar como padrão:

1. extensão de navegador de terceiro para baixar NotebookLM;
2. renomear `.mp4` para `.m4a` como solução principal;
3. gravação do Microsoft Edge Read Aloud como pipeline oficial;
4. colar API key no chat para a IA “gerar internamente”.

Fallback emergencial permitido:

```text
Edge Read Aloud + gravação local
```

Mas deve ser rotulado como fallback manual não auditável.

Para converter contêiner ou áudio, preferir FFmpeg:

```bash
ffmpeg -i entrada.mp4 -vn -c:a copy saida.m4a
ffmpeg -i entrada.mp4 -vn -codec:a libmp3lame -b:a 128k saida.mp3
```

---

## 14. Script `gerar_audio_v2.py`

### 14.1. Funções obrigatórias

O script deve:

1. ler `audio/audio.yaml`;
2. validar schema;
3. ler `audio/roteiro_audio.txt`;
4. aplicar `sanitize_for_tts()`;
5. ler `audio/dicionario_fonetico.yaml`, se existir;
6. gerar `audio/suspeitos_foneticos.csv`, se detectar termos duvidosos;
7. aplicar substituições fonéticas apenas no texto falado;
8. dividir blocos longos em sub-blocos;
9. gerar partes em `audio/parts`;
10. aplicar retry em falhas;
11. permitir retomar geração;
12. aplicar micro-pausas, pausas pedagógicas e pausas de capítulo;
13. aplicar fade por chunk;
14. concatenar em `audio/master_audio.mp3`;
15. normalizar por perfil;
16. gerar `audio/chapters.json`;
17. gerar `audio/manifest_audio.json`;
18. gerar `audio/log_geracao_audio.txt`;
19. validar duração final por `ffprobe`;
20. falhar se o áudio tiver menos que a duração mínima;
21. não instalar dependências automaticamente;
22. aplicar tratamento de SSL/CA do sistema antes da primeira síntese, quando aplicável;
23. embutir capítulos ID3 com falha graciosa;
24. preservar partes individuais, salvo `--clean-parts`.

### 14.2. SSL/CA

Função obrigatória em ambiente Claude com proxy/CA autoassinado:

```text
preparar_ssl()
```

Em máquina doméstica, deve ser inofensiva.

A função deve procurar certificados locais do sistema e configurar contexto SSL antes da primeira síntese. Se falhar, registrar diagnóstico no log.

### 14.3. Argumentos obrigatórios

```text
--preflight
--resume
--force
--validate-only
--min-minutes
--chunk-words
--no-phonetic
--clean-parts
--normalization-profile
--engine
--dry-run
```

### 14.4. `--preflight`

Executar:

1. versão do Python;
2. existência de `ffmpeg`;
3. existência de `ffprobe`;
4. import de dependências;
5. DNS do serviço TTS escolhido;
6. teste curto de TTS;
7. validação do teste por `ffprobe`;
8. permissão de escrita;
9. espaço em disco;
10. existência de `.env` quando API externa for selecionada.

### 14.5. `--resume`

Reaproveitar partes já geradas, desde que:

1. arquivo exista;
2. tamanho seja maior que 1 KB;
3. duração seja superior a 10 segundos;
4. `ffprobe` consiga ler o arquivo;
5. hash do texto do bloco não tenha mudado, quando disponível.

### 14.6. `--validate-only`

Validar:

1. existência de `audio/master_audio.mp3`;
2. duração real;
3. tamanho;
4. bitrate;
5. LUFS/LRA/TP quando possível;
6. duração mínima;
7. silêncios acidentais longos;
8. consistência com `manifest_audio.json`.

---

## 15. Preflight local

### 15.1. Comandos manuais

```bash
python3 --version
ffmpeg -version
ffprobe -version
python3 -c "import edge_tts, pydub, yaml, mutagen; print('imports ok')"
nslookup speech.platform.bing.com
edge-tts --list-voices | grep pt-BR
```

### 15.2. Teste curto Edge-TTS

```bash
mkdir -p audio/testes

edge-tts \
  --voice pt-BR-FranciscaNeural \
  --text "Teste de áudio PAFE para disciplina de Direito." \
  --write-media audio/testes/teste_pafe.mp3

ffprobe -v error \
  -show_entries format=duration,bit_rate,size \
  -of default=noprint_wrappers=1 \
  audio/testes/teste_pafe.mp3
```

---

## 16. `requirements_audio.txt`

Base obrigatória:

```text
edge-tts
pydub
mutagen
PyYAML
python-dotenv
```

Recomendadas quando houver validação avançada:

```text
ffmpeg-normalize
pyloudnorm
soundfile
```

Dependências externas devem ser justificadas. Não inflar ambiente com pacote desnecessário.

---

## 17. `.env.example` e `.gitignore`

### 17.1. `.env.example`

```env
# Escolha apenas as chaves dos provedores que você realmente usa.
OPENAI_API_KEY=coloque_sua_chave_aqui
GEMINI_API_KEY=coloque_sua_chave_aqui
ELEVENLABS_API_KEY=coloque_sua_chave_aqui
HUME_API_KEY=coloque_sua_chave_aqui

# IDs de voz, quando aplicável.
ELEVENLABS_VOICE_ID=coloque_o_id_da_voz_aqui
HUME_VOICE_ID=coloque_o_id_da_voz_aqui
```

### 17.2. `.gitignore`

```gitignore
.env
*.key
*.pem
audio/parts/
audio/master_audio.mp3
```

---

## 18. `manifest_audio.json`

O manifesto deve servir como prova técnica mínima da geração.

Exemplo recomendado:

```json
{
  "projeto": "P.A.F.E.",
  "audio_md_version": "v6.0 MASTER",
  "disciplina": "Direito Civil IV",
  "escopo": "1º bimestre",
  "roteiro_arquivo": "audio/roteiro_audio.txt",
  "audio_yaml": "audio/audio.yaml",
  "arquivo_final": "audio/master_audio.mp3",
  "tts_engine": "edge-tts",
  "normalization_profile": "study_long",
  "generated_at": "2026-07-08T00:00:00-03:00",
  "source_hash": "sha256:...",
  "content_hash": "sha256:...",
  "audio_yaml_hash": "sha256:...",
  "script_hash": "sha256:...",
  "duracao_segundos": 7320.5,
  "duracao_minutos": 122.0,
  "palavras_totais": 19244,
  "blocos": 13,
  "sub_blocos": 31,
  "chunks": 31,
  "retries": 0,
  "falhas": 0,
  "bitrate": "128k",
  "loudness_integrated_lufs": -20.1,
  "loudness_range_lra": 11.0,
  "true_peak_dbtp": -1.5,
  "validado_por": ["ffprobe", "ffmpeg loudnorm"],
  "minimo_segundos": 7200,
  "voice_map": {
    "conceito": "pt-BR-FranciscaNeural",
    "fundamento": "pt-BR-AntonioNeural",
    "revisao": "pt-BR-ThalitaNeural"
  },
  "status": "aprovado"
}
```

Não registrar segredo, chave, token ou URL privada no manifesto.

---

## 19. `log_geracao_audio.txt`

O log deve registrar:

1. data e hora;
2. sistema operacional;
3. versão Python;
4. motor TTS;
5. vozes;
6. arquivo YAML;
7. total de blocos;
8. total de sub-blocos;
9. palavras totais;
10. duração por parte;
11. pausas aplicadas;
12. substituições fonéticas;
13. termos suspeitos;
14. erros;
15. retries;
16. duração final;
17. loudness quando disponível;
18. validação final.

Nunca registrar chaves de API.

---

## 20. Capítulos

### 20.1. `chapters.json`

Gerar:

```json
[
  {
    "id": "bloco_001",
    "titulo": "Estratégia de prova",
    "inicio_segundos": 0,
    "fim_segundos": 420
  }
]
```

### 20.2. Capítulos embutidos no MP3

Pode tentar embutir capítulos ID3 `CHAP` e `CTOC` com `mutagen`.

Regra:

1. capítulos embutidos são recurso adicional;
2. não prometer compatibilidade universal;
3. manter sempre `chapters.json`;
4. manter partes individuais em `audio/parts`.

---

## 21. HTML e player

Quando houver HTML P.A.F.E. junto com áudio:

1. incluir player para `audio/master_audio.mp3`;
2. mostrar aviso se o arquivo não existir;
3. listar capítulos;
4. listar partes individuais;
5. permitir baixar roteiro;
6. permitir abrir checklist;
7. não usar dependência online obrigatória;
8. manter HTML offline;
9. não embutir API keys no HTML.

---

## 22. Critérios de aprovação

Um pacote de áudio P.A.F.E. só pode ser considerado aprovado se:

1. roteiro existir;
2. `audio.yaml` existir e for válido;
3. `dicionario_fonetico.yaml` existir ou ausência estiver justificada;
4. `suspeitos_foneticos.csv` existir ou ausência estiver justificada;
5. `gerar_audio_v2.py` existir;
6. `setup_audio.sh` existir;
7. `validar_audio.sh` existir;
8. `requirements_audio.txt` existir;
9. `.env.example` existir quando houver API externa;
10. `audio/master_audio.mp3` existir ou houver declaração expressa de execução local necessária;
11. se o MP3 existir, duração tiver sido validada por `ffprobe`;
12. duração mínima tiver sido cumprida;
13. não houver loop, silêncio ou duplicação artificial;
14. conteúdo estiver alinhado à disciplina e aos anexos;
15. fontes incertas estiverem marcadas;
16. não houver invenção de artigo, precedente, súmula, tese ou dado;
17. não houver segredo exposto;
18. manifesto e log existirem;
19. hash e métricas forem registrados quando possível.

---

## 23. Prompt padrão para gerar pacote de áudio

```text
/mpe /pafe audio

Atue como especialista em Direito, metodologia de estudo jurídico, acessibilidade cognitiva e engenharia de áudio educacional.

Gere um pacote de áudio P.A.F.E. para a disciplina [DISCIPLINA], com base nos anexos efetivamente acessíveis.

ESCOPO:
[descrever tema, bimestre ou prova]

DURAÇÃO MÍNIMA:
[tempo em minutos]

BASE:
[plano de ensino, cronograma, PDFs, questões, caderno, bibliografia]

ENTREGAR:
1. README_AUDIO.md;
2. roteiro_audio.txt;
3. audio/audio.yaml;
4. audio/dicionario_fonetico.yaml;
5. audio/suspeitos_foneticos.csv;
6. gerar_audio_v2.py;
7. setup_audio.sh;
8. validar_audio.sh;
9. requirements_audio.txt;
10. .env.example;
11. .gitignore;
12. flashcards_audio.csv;
13. audio/chapters.json;
14. audio/manifest_audio.json;
15. audio/log_geracao_audio.txt;
16. audio/master_audio.mp3, somente se o MP3 real puder ser gerado e validado.

REGRAS:
- Não inventar lei, artigo, precedente, súmula, doutrina, dado ou fonte.
- Se não houver validação, escrever “precisa validar antes de usar”.
- Não afirmar MP3 gerado sem arquivo físico.
- Não simular duração por loop, silêncio ou duplicação.
- Validar duração real por ffprobe.
- Usar linguagem clara, técnica e adequada a estudante de Direito.
- Adaptar para TDAH: blocos, pausas, retomadas, exemplos e pegadinhas.
- Separar regra, exceção e pegadinha.
- Tratar respostas de IA anexadas como material auxiliar, não como prova.
- Usar os anexos como base prevalente.
- Não expor chaves de API.
- Usar .env para provedores externos.
```

---

## 24. Prompt padrão para corrigir áudio curto

```text
/mpe /pafe audio corrigir

O áudio gerado ficou curto demais.

PROBLEMA:
O arquivo anterior tem apenas [duração] e [tamanho]. Quero áudio real de pelo menos [tempo mínimo].

TAREFA:
Refazer o roteiro e o pipeline de geração para produzir áudio real, juridicamente útil e validável.

REGRAS:
1. Calcular palavras mínimas pela duração desejada.
2. Expandir o roteiro antes de gerar áudio.
3. Dividir o texto em blocos e sub-blocos.
4. Gerar partes individuais.
5. Concatenar em master_audio.mp3.
6. Validar por ffprobe.
7. Falhar se ficar abaixo do mínimo.
8. Não usar loop, silêncio ou duplicação artificial.
9. Gerar log e manifest_audio.json.
10. Declarar execução local necessária se o MP3 não puder ser gerado na plataforma.
```

---

## 25. Prompt padrão para auditar pacote de áudio

```text
/mpe /audit pafe audio

Audite o pacote de áudio P.A.F.E. anexado.

Verifique:
1. se o roteiro corresponde à disciplina;
2. se a duração prometida é compatível com palavras estimadas;
3. se audio.yaml é válido;
4. se há sanitize_for_tts();
5. se há dicionário fonético;
6. se há suspeitos_foneticos.csv;
7. se gerar_audio_v2.py possui preflight;
8. se há resume;
9. se há validate-only;
10. se há divisão em sub-blocos;
11. se há retry;
12. se há matriz de pausas;
13. se há fade por chunk;
14. se há normalização;
15. se ffprobe valida duração final;
16. se há risco de loop, silêncio ou duplicação artificial;
17. se há chapters.json;
18. se há manifest_audio.json;
19. se há log;
20. se os conteúdos jurídicos foram inventados;
21. se as fontes incertas estão marcadas;
22. se há chave de API exposta;
23. se o pacote é reutilizável para estudo.

Ao final, classifique:
- APROVADO;
- APROVADO COM AJUSTES;
- REPROVADO.

Se houver ajustes, indique ação objetiva.
```

---

## 26. Sincronização entre drives

Quando houver divergência entre Google Drive, GitHub e Box:

1. prevalece a versão com maior número de versão e histórico mais recente validado;
2. evitar manter versões diferentes com o mesmo nome;
3. sincronizar o conteúdo integral, não patches;
4. preservar histórico por versão do Drive, commit do GitHub ou versionamento do Box;
5. atualizar o rodapé operacional em todos os destinos.

---

## 27. Regras finais

1. Áudio P.A.F.E. não é mero TTS.
2. Áudio P.A.F.E. é material jurídico de estudo.
3. O roteiro deve ser melhor que o texto bruto.
4. A geração deve ser validável.
5. A duração deve ser real.
6. As fontes devem ser controladas.
7. As incertezas devem ser declaradas.
8. O usuário não deve ter que montar patches.
9. O pacote deve ser completo.
10. O script deve falhar quando não puder cumprir a promessa.
11. Nenhuma chave de API deve aparecer em chat, código, HTML, log, manifesto ou arquivo versionado.

---

## 28. Rodapé operacional

Versão: `audio.md v6.0 MASTER — governança multi-motor, sanitização TTS e rotas opcionais seguras`  
Uso: drives virtuais, comandos P.A.F.E., projetos jurídicos e pacotes de áudio  
Escopo: qualquer disciplina de Direito  
Regra central: não existe áudio gerado sem arquivo real, duração validada e cadeia mínima de rastreabilidade.  
Overlay Claude: quando o agente for Claude com ambiente de execução, ler também `pafe_claude.md` — smoke test obrigatório antes de declarar execução local e `preparar_ssl()` antes da primeira síntese quando aplicável.

Histórico:

- v6.0 MASTER (2026-07-08): preserva v5.0 e adiciona sanitização pré-TTS, matriz tripla de pausas, perfis adaptativos de loudness, governança fonética com suspeitos, manifesto avançado com hashes/métricas, rotas opcionais seguras para OpenAI, Gemini, ElevenLabs, Hume, NotebookLM e Make/n8n, e regra reforçada de segurança de API keys.
- v5.0 MASTER (2026-07-06): arquitetura CODE vs DATA; roteiro_audio.txt externo obrigatório para roteiros massivos; cadência didática lenta; pausas pedagógicas de 3000 a 3500 ms; fade_in(50)/fade_out(50) por chunk; normalização por loudness; retry mínimo de 3 tentativas; dicionário fonético pré-síntese configurável; validação acústica com ffprobe/FFmpeg.
- v2.1 (2026-06-09): smoke test obrigatório para Claude antes de declarar execução local; duração-alvo declarável na invocação; preparar_ssl, gap de transição, fade, capítulos ID3; referência ao pafe_claude.md.
- v2.0: padrão geral para disciplinas de Direito.
