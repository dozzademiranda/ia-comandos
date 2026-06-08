# audio.md — Módulo P.A.F.E. de Áudio para Disciplinas de Direito

## 1. Finalidade

Este arquivo define o padrão operacional para geração de áudios de estudo no ecossistema P.A.F.E. para qualquer disciplina de Direito.

O objetivo é produzir áudio jurídico-didático, validável, reutilizável e compatível com estudo de prova, revisão de véspera, treino de questões, memorização de artigos, doutrina, jurisprudência e pegadinhas.

Este módulo serve para disciplinas como Direito Civil, Processo Civil, Penal, Processo Penal, Constitucional, Administrativo, Tributário, Trabalho, Processo do Trabalho, Internacional, Criminologia, Empresarial, Consumidor, Ambiental e outras disciplinas jurídicas.

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

---

### 2.2. Áudio deve ser juridicamente útil

O áudio deve conter:

1. explicação conceitual;
2. base legal;
3. doutrina quando indicada ou disponível;
4. jurisprudência quando indicada ou disponível;
5. divergências relevantes;
6. pegadinhas de prova;
7. questões comentadas;
8. revisão progressiva;
9. revisão de véspera;
10. revisão relâmpago.

Não basta ler um resumo. O áudio deve ensinar, revisar, testar e fixar.

---

### 2.3. Hierarquia documental

Ao gerar áudio jurídico, aplicar esta ordem de prevalência:

1. plano de ensino, ementa, cronograma oficial e conteúdo efetivamente ministrado;
2. PDFs, slides, cadernos, anotações e materiais do professor;
3. questões de prova, QConcursos, provas anteriores e simulados anexados;
4. legislação seca vigente, quando validada em fonte confiável;
5. jurisprudência oficial, quando validada;
6. bibliografia oficial da disciplina;
7. materiais de revisão de IA, tratados como objeto de análise, não como prova;
8. conhecimento jurídico interno, apenas para organizar e explicar;
9. web somente se autorizada ou indispensável para atualização normativa/jurisprudencial.

Se a fonte não estiver acessível:

> não documentado no material disponível.

Se o artigo, súmula, precedente ou dado não tiver sido validado:

> precisa validar antes de usar.

---

## 3. Comando padrão

### 3.1. Forma curta

```text
/mpe /pafe audio
Gere áudio de revisão para [DISCIPLINA], com base nos anexos, duração mínima de [TEMPO], foco em [PROVA/TEMA/BIMESTRE].
```

### 3.2. Forma completa

```text
/mpe /pafe audio

DISCIPLINA:
[Nome da disciplina]

ESCOPO:
[1º bimestre / prova final / OAB / concurso / revisão geral / tema específico]

DURAÇÃO MÍNIMA:
[30 min / 1h / 2h / outro]

BASE OBRIGATÓRIA:
[arquivos anexados, plano de ensino, questões, caderno, legislação, jurisprudência]

OBJETIVO:
Gerar roteiro, audio.yaml, scripts e instruções para áudio jurídico-didático validável.

REGRAS:
- não inventar fonte, artigo, precedente, doutrina, dado ou jurisprudência;
- não afirmar MP3 real sem arquivo físico;
- validar duração por ffprobe;
- não usar loop, silêncio ou duplicação artificial;
- priorizar clareza para estudo com TDAH;
- gerar arquivos completos, não patches.
```

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
└── audio/
    ├── roteiro_audio.txt
    ├── audio.yaml
    ├── dicionario_fonetico.yaml
    ├── chapters.json
    ├── manifest_audio.json
    ├── log_geracao_audio.txt
    ├── parts/
    │   ├── 001_bloco_001.mp3
    │   ├── 002_bloco_002.mp3
    │   └── ...
    └── master_audio.mp3
```

Se o MP3 não puder ser gerado na plataforma, entregar todos os arquivos exceto `master_audio.mp3`, com instrução clara para geração local.

---

## 5. Duração mínima e palavras estimadas

### 5.1. Parâmetro de cálculo

Usar como estimativa média:

```text
145 a 165 palavras por minuto em português do Brasil.
```

Para áudio jurídico, preferir cálculo conservador de 150 palavras por minuto.

### 5.2. Tabela de referência

| Duração-alvo | Palavras mínimas recomendadas | Observação |
|---:|---:|---|
| 15 min | 2.300 a 2.700 | revisão curta |
| 30 min | 4.500 a 5.200 | revisão de aula |
| 45 min | 6.800 a 7.800 | revisão de tema grande |
| 60 min | 9.000 a 10.500 | revisão de bimestre |
| 90 min | 13.500 a 15.800 | revisão intensiva |
| 120 min | 18.000 a 22.000 | revisão completa |
| 180 min | 27.000 a 33.000 | maratona |

Se o roteiro tiver menos palavras do que o mínimo estimado, expandir antes de tentar gerar o áudio.

---

## 6. Estrutura didática do roteiro

### 6.1. Estrutura mínima

Todo roteiro jurídico de áudio deve seguir esta estrutura:

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

### 6.2. Modelo de blocos para áudio longo

Para áudios de 2 horas:

```text
BLOCO 1 — Estratégia de prova — 5 a 8 min
BLOCO 2 — Fundamentos e princípios — 10 a 20 min
BLOCO 3 — Tema central 1 — 15 a 25 min
BLOCO 4 — Tema central 2 — 15 a 25 min
BLOCO 5 — Tema central 3 — 15 a 25 min
BLOCO 6 — Comparações e tabelas narradas — 10 a 15 min
BLOCO 7 — Jurisprudência e divergências — 10 a 20 min
BLOCO 8 — Questões objetivas comentadas — 15 a 30 min
BLOCO 9 — Questões discursivas ou peças, se cabível — 10 a 20 min
BLOCO 10 — Pegadinhas e revisão de véspera — 10 a 15 min
BLOCO 11 — Revisão relâmpago final — 5 a 10 min
```

Adaptar conforme disciplina e tempo disponível.

---

## 7. Regras para acessibilidade cognitiva

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

## 8. Padrão jurídico de conteúdo

### 8.1. Direito material

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

### 8.2. Direito processual

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

### 8.3. Disciplinas dogmáticas com jurisprudência

Quando houver STF/STJ/TST/TSE/TRE/TRF/TJ:

1. separar tese firmada, precedente isolado e tendência;
2. não transformar precedente isolado em regra geral;
3. indicar divergência quando houver;
4. em divergência STF × STJ, expor ambas antes da conclusão;
5. declarar “não documentado” quando a fonte não estiver disponível;
6. não inventar número de RE, REsp, AREsp, Tema, súmula ou informativo.

---

## 9. Padrão de questões comentadas em áudio

### 9.1. Estrutura de cada questão

Cada questão deve ser narrada assim:

```text
Questão [número].
[Enunciado claro e resumido, se necessário.]

Pausa mental: pense na resposta antes de ouvir o gabarito.

Gabarito: letra [x] / certo / errado.

Por quê?
[Explicação da correta.]

Por que as demais estão erradas?
[Explicação curta das incorretas.]

Pegadinha:
[Termo, exceção ou raciocínio que a banca tentou explorar.]
```

### 9.2. Questões com alternativas longas

Se a questão tiver alternativas muito longas:

1. resumir o enunciado;
2. narrar apenas as alternativas necessárias;
3. explicar a estrutura lógica da banca;
4. preservar a informação jurídica relevante;
5. não mutilar a questão a ponto de alterar o sentido.

---

## 10. Dicionário fonético

### 10.1. Finalidade

O dicionário fonético serve para melhorar pronúncia em TTS.

Ele não substitui o texto jurídico limpo. Deve ser aplicado apenas na versão de áudio.

### 10.2. Arquivo

Criar:

```text
audio/dicionario_fonetico.yaml
```

### 10.3. Exemplo genérico para Direito

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
  "ADI": "ação direta de inconstitucionalidade"
  "ADC": "ação declaratória de constitucionalidade"
  "ADPF": "arguição de descumprimento de preceito fundamental"
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
```

Adaptar por disciplina.

### 10.4. Regras

1. Não aplicar substituição no texto-base de estudo;
2. aplicar apenas na cópia falada;
3. registrar substituições no log;
4. permitir desativar com `--no-phonetic`;
5. nunca alterar sentido jurídico.

---

## 11. Padrão do audio.yaml

### 11.1. Estrutura mínima

```yaml
metadata:
  projeto: "P.A.F.E."
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
  dicionario_fonetico: "audio/dicionario_fonetico.yaml"
  pausa_padrao_ms: 900
  chunk_words_padrao: 900
  min_duration_seconds: 7200

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
    rate: "+0%"
    pitch: "+0Hz"
    pause_after_ms: 1200
    palavras_estimadas: 900
    texto: |
      Texto do bloco aqui.
```

### 11.2. Campos obrigatórios por bloco

1. `id`;
2. `ordem`;
3. `titulo`;
4. `chapter_title`;
5. `voz`;
6. `texto`;
7. `palavras_estimadas`;
8. `pause_after_ms`.

### 11.3. Campos opcionais por bloco

1. `rate`;
2. `pitch`;
3. `volume`;
4. `tipo`;
5. `base`;
6. `tags`;
7. `questoes_referenciadas`.

---

## 12. Vozes e ritmo

### 12.1. Vozes padrão Edge-TTS

Usar preferencialmente:

```text
pt-BR-FranciscaNeural — conceitos, sínteses e revisão geral
pt-BR-AntonioNeural — fundamentação legal, artigos, jurisprudência
pt-BR-ThalitaNeural — pegadinhas, revisão de véspera, alertas
```

Se alguma voz não estiver disponível, o script deve listar as vozes `pt-BR` disponíveis e pedir substituição.

### 12.2. Velocidade sugerida

| Tipo de conteúdo | Rate sugerido |
|---|---:|
| conceito difícil | `-5%` |
| regra geral | `+0%` |
| artigo de lei | `-5%` |
| jurisprudência | `-5%` |
| questões comentadas | `+0%` |
| revisão de véspera | `+5%` |
| revisão relâmpago | `+8%` |

O script deve aceitar `rate`, mas não deve quebrar se o motor TTS ignorar esse parâmetro.

---

## 13. Script gerar_audio_v2.py

### 13.1. Funções obrigatórias

O script deve:

1. ler `audio/audio.yaml`;
2. validar schema;
3. ler `audio/dicionario_fonetico.yaml`, se existir;
4. aplicar substituições fonéticas apenas no texto falado;
5. dividir blocos longos em sub-blocos;
6. gerar partes em `audio/parts`;
7. aplicar retry em falhas;
8. permitir retomar geração;
9. concatenar em `audio/master_audio.mp3`;
10. gerar `audio/chapters.json`;
11. gerar `audio/manifest_audio.json`;
12. gerar `audio/log_geracao_audio.txt`;
13. validar duração final por `ffprobe`;
14. falhar se o áudio tiver menos que a duração mínima;
15. não instalar dependências automaticamente.

### 13.2. Argumentos obrigatórios

```text
--preflight
--resume
--force
--validate-only
--min-minutes
--chunk-words
--no-phonetic
--clean-parts
```

### 13.3. Comportamento dos argumentos

#### `--preflight`

Executar:

1. versão do Python;
2. existência de `ffmpeg`;
3. existência de `ffprobe`;
4. import de `edge_tts`;
5. import de `pydub`;
6. import de `yaml`;
7. import de `mutagen`;
8. DNS de `speech.platform.bing.com`;
9. teste curto com voz `pt-BR-FranciscaNeural`;
10. validação do teste por `ffprobe`;
11. checagem de permissão de escrita;
12. checagem de espaço em disco.

#### `--resume`

Reaproveitar partes já geradas, desde que:

1. arquivo exista;
2. tamanho seja maior que 1 KB;
3. duração seja superior a 10 segundos;
4. `ffprobe` consiga ler o arquivo.

#### `--force`

Apagar:

1. `audio/master_audio.mp3`;
2. `audio/manifest_audio.json`;
3. `audio/chapters.json`;
4. partes anteriores, se confirmado pelo script.

#### `--validate-only`

Validar:

1. existência de `audio/master_audio.mp3`;
2. duração real;
3. tamanho;
4. bitrate;
5. duração mínima.

#### `--min-minutes`

Permitir alterar duração mínima. Padrão:

```text
120
```

#### `--chunk-words`

Tamanho máximo de cada sub-bloco. Padrão:

```text
900
```

#### `--no-phonetic`

Desativa dicionário fonético.

#### `--clean-parts`

Apaga partes após gerar master. Não usar como padrão.

---

## 14. Preflight local

### 14.1. Comandos manuais

```bash
python3 --version
ffmpeg -version
ffprobe -version
python3 -c "import edge_tts, pydub, yaml, mutagen; print('imports ok')"
nslookup speech.platform.bing.com
edge-tts --list-voices | grep pt-BR
```

### 14.2. Teste curto

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

## 15. setup_audio.sh

O pacote deve incluir um script:

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "== PAFE AUDIO: setup =="

python3 -m venv .venv
source .venv/bin/activate

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements_audio.txt

if command -v apt >/dev/null 2>&1; then
  sudo apt update
  sudo apt install -y ffmpeg dnsutils
fi

python3 gerar_audio_v2.py --preflight

echo "Setup concluído."
```

---

## 16. validar_audio.sh

O pacote deve incluir:

```bash
#!/usr/bin/env bash
set -euo pipefail

ARQUIVO="${1:-audio/master_audio.mp3}"
MIN_SEGUNDOS="${2:-7200}"

if [ ! -f "$ARQUIVO" ]; then
  echo "Arquivo não encontrado: $ARQUIVO"
  exit 1
fi

DURACAO=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$ARQUIVO")

echo "Duração em segundos: $DURACAO"
echo "Arquivo:"
ls -lh "$ARQUIVO"

python3 - <<PY
duracao = float("$DURACAO")
minimo = float("$MIN_SEGUNDOS")
if duracao < minimo:
    raise SystemExit(f"ERRO: áudio menor que o mínimo. Duração={duracao:.2f}s; mínimo={minimo:.2f}s")
print("OK: duração mínima atendida.")
PY
```

---

## 17. requirements_audio.txt

Usar:

```text
edge-tts
pydub
mutagen
PyYAML
python-dotenv
```

Não incluir dependências desnecessárias.

---

## 18. Integração opcional com ElevenLabs

### 18.1. Regra

ElevenLabs é opcional. Só usar se o usuário pedir expressamente.

### 18.2. Segurança

1. nunca pedir chave no chat;
2. nunca salvar chave em memória;
3. orientar uso de `.env`;
4. não imprimir chave no terminal;
5. não versionar `.env`;
6. incluir `.env.example`.

### 18.3. Arquivo .env.example

```env
ELEVENLABS_API_KEY=coloque_sua_chave_aqui
ELEVENLABS_VOICE_ID=coloque_o_id_da_voz_aqui
```

### 18.4. Aviso obrigatório

Antes de usar API paga:

1. estimar caracteres;
2. avisar que pode haver custo;
3. avisar que o envio do texto à API externa depende de consentimento;
4. permitir manter Edge-TTS gratuito.

---

## 19. HTML e player

Quando houver HTML PAFE junto com áudio:

1. incluir player para `audio/master_audio.mp3`;
2. mostrar aviso se o arquivo não existir;
3. listar capítulos;
4. listar partes individuais;
5. permitir baixar roteiro;
6. permitir abrir checklist;
7. não usar dependência online obrigatória;
8. manter HTML offline.

---

## 20. Logs e manifesto

### 20.1. log_geracao_audio.txt

O log deve registrar:

1. data e hora;
2. sistema operacional;
3. versão Python;
4. vozes;
5. arquivo YAML;
6. total de blocos;
7. total de sub-blocos;
8. palavras totais;
9. duração por parte;
10. erros;
11. retries;
12. duração final;
13. validação final.

### 20.2. manifest_audio.json

Exemplo:

```json
{
  "projeto": "P.A.F.E.",
  "disciplina": "Direito Civil IV",
  "escopo": "1º bimestre",
  "arquivo_final": "audio/master_audio.mp3",
  "duracao_segundos": 7320.5,
  "duracao_minutos": 122.0,
  "palavras_totais": 19244,
  "blocos": 13,
  "sub_blocos": 31,
  "validado_por": "ffprobe",
  "minimo_segundos": 7200,
  "status": "aprovado"
}
```

---

## 21. Capítulos

### 21.1. chapters.json

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

### 21.2. Capítulos embutidos no MP3

Pode tentar embutir capítulos ID3 `CHAP` e `CTOC` com `mutagen`.

Regra:

1. capítulos embutidos são recurso adicional;
2. não prometer compatibilidade universal;
3. manter sempre `chapters.json`;
4. manter partes individuais em `audio/parts`.

---

## 22. Critérios de aprovação

Um pacote de áudio PAFE só pode ser considerado aprovado se:

1. roteiro existir;
2. `audio.yaml` existir e for válido;
3. `dicionario_fonetico.yaml` existir ou sua ausência estiver justificada;
4. `gerar_audio_v2.py` existir;
5. `setup_audio.sh` existir;
6. `validar_audio.sh` existir;
7. `requirements_audio.txt` existir;
8. `audio/master_audio.mp3` existir ou houver declaração expressa de execução local necessária;
9. se o MP3 existir, duração tiver sido validada por `ffprobe`;
10. duração mínima tiver sido cumprida;
11. não houver loop, silêncio ou duplicação artificial;
12. conteúdo estiver alinhado à disciplina e aos anexos;
13. fontes incertas estiverem marcadas;
14. não houver invenção de artigo, precedente, súmula, tese ou dado.

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
5. gerar_audio_v2.py;
6. setup_audio.sh;
7. validar_audio.sh;
8. requirements_audio.txt;
9. flashcards_audio.csv;
10. audio/chapters.json;
11. audio/manifest_audio.json;
12. audio/log_geracao_audio.txt;
13. audio/master_audio.mp3, somente se o MP3 real puder ser gerado e validado.

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
4. se gerar_audio_v2.py possui preflight;
5. se há resume;
6. se há force;
7. se há validate-only;
8. se há divisão em sub-blocos;
9. se há retry;
10. se ffprobe valida duração final;
11. se há risco de loop, silêncio ou duplicação artificial;
12. se há dicionário fonético;
13. se há chapters.json;
14. se há manifest_audio.json;
15. se há log;
16. se os conteúdos jurídicos foram inventados;
17. se as fontes incertas estão marcadas;
18. se o pacote é reutilizável para estudo.

Ao final, classifique:
- APROVADO;
- APROVADO COM AJUSTES;
- REPROVADO.

Se houver ajustes, indique ação objetiva.
```

---

## 26. Regras finais

1. Áudio PAFE não é mero TTS.
2. Áudio PAFE é material jurídico de estudo.
3. O roteiro deve ser melhor que o texto bruto.
4. A geração deve ser validável.
5. A duração deve ser real.
6. As fontes devem ser controladas.
7. As incertezas devem ser declaradas.
8. O usuário não deve ter que montar patches.
9. O pacote deve ser completo.
10. O script deve falhar quando não puder cumprir a promessa.

---

## 27. Rodapé operacional

Versão: audio.md v2.0 — padrão geral para disciplinas de Direito  
Uso: drives virtuais, comandos PAFE, projetos jurídicos e pacotes de áudio  
Escopo: qualquer disciplina de Direito  
Regra central: não existe áudio gerado sem arquivo real e duração validada
