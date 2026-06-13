# pafe_prompt_outras_ias.md
**Versão:** 1.0 | **Data:** 2026-06-09 | **Escopo:** PAFE — uso com GPT, Gemini e Perplexity

Este arquivo é um **prompt-mestre pronto para colar** em GPT, Gemini ou Perplexity
(versões PRO/pagas). Objetivo: fazer essas IAs produzirem **apenas conteúdo de texto**
no formato exato que o script `gerar_audio_v2.py` (Claude/Box/GitHub) consome, **sem**
tentarem gerar áudio — porque elas só produzem voz robótica (pyttsx3/gTTS) ou nada.

Fluxo: elas geram texto → você roda `python3 gerar_audio_v2.py` na sua máquina → o MP3
sai com as vozes neurais (Francisca, Antonio, Thalita).

O `pafe_claude.md` NÃO entra aqui: é exclusivo do Claude e induziria essas IAs a fingir
execução. Não anexe esse arquivo a elas.

---

## 1. Como usar (passo a passo)

1.1 Abra a IA (GPT, Gemini ou Perplexity) na versão paga.

1.2 Anexe o material da disciplina: plano de ensino, cronograma, provas anteriores,
PDFs do professor, caderno. (Sem material, a IA inventa — proibido.)

1.3 Anexe também, se a IA aceitar, os módulos `README.md`, `audio.md` e `html.md` do PAFE.
Nunca anexe o `pafe_claude.md`.

1.4 Cole o **Prompt A** (seção 3), preenchendo os campos entre colchetes.

1.5 Receba o roteiro e o `audio.yaml`. Se quiser flashcards e questões, use o **Prompt B** (seção 4).

1.6 Salve os arquivos e rode na sua máquina:

```bash
bash setup_audio.sh
python3 gerar_audio_v2.py --preflight
python3 gerar_audio_v2.py
bash validar_audio.sh
```

1.7 Traga o resultado (ou o roteiro) ao Claude e peça: "valida e fecha". O Claude corrige
erros de jurisprudência/data e monta o pacote final.

---

## 2. Divisão de trabalho (para economizar tokens do Claude)

| Tarefa | Quem faz | Por quê |
|---|---|---|
| Pesquisa bruta, varredura de doutrina/julgados | GPT / Gemini / Perplexity | volume; Perplexity cita fonte |
| Rascunho longo do roteiro (8k–20k palavras) | GPT / Gemini | volume caro em token |
| Rascunho de `audio.yaml`, flashcards, questões | GPT / Gemini | estrutura repetitiva |
| Transcrição/resumo de PDF ou aula longa | Gemini (contexto grande) / GPT | volume |
| Brainstorm e variações (mnemônicos, aberturas) | qualquer uma | volume |
| Validação jurisprudencial e correção de erros | Claude | juízo crítico |
| Montagem do pacote final + geração do MP3 | Claude | execução real |
| Versionamento no Box/Drive | Claude | acesso direto |

Regra de bolso: **rascunho e pesquisa vêm delas; o "ok final" e a execução vêm do Claude.**

---

## 3. PROMPT A — Roteiro + audio.yaml (colar na IA)

```text
Você é especialista em Direito, metodologia de estudo jurídico, acessibilidade
cognitiva (TDAH e TEA nível 1) e engenharia de áudio educacional.

CONTEXTO
Faço parte de um fluxo multi-IA chamado P.A.F.E. Seu papel é gerar APENAS TEXTO:
o roteiro de áudio e o arquivo audio.yaml. NÃO gere áudio, não gere MP3, não use
pyttsx3, gTTS ou espeak. A geração de áudio será feita por mim, em python3, com
edge-tts e vozes neurais. Se você sugerir gerar áudio, estará errado.

DISCIPLINA: [nome da disciplina]
ESCOPO: [bimestre / prova / tema específico]
DURAÇÃO-ALVO: [ex.: 60 min]
BASE OBRIGATÓRIA: [arquivos que anexei: plano de ensino, cronograma, provas, PDFs]

REGRAS DE CONTEÚDO (inegociáveis)
1. Use como base prevalente, nesta ordem: plano de ensino e cronograma; material do
   professor; provas anteriores; legislação vigente; jurisprudência oficial; bibliografia.
2. NÃO invente lei, artigo, súmula, precedente, número de RE/REsp/Tema, doutrina,
   data ou dado. Se não tiver certeza, escreva: "precisa validar antes de usar".
3. Marque os pontos que dependem de confirmação com o sinal: [VERIFICAR].
4. Trate o escopo pelo que foi efetivamente dado em aula (cronograma), não pelo
   programa inteiro da disciplina.
5. Separe sempre regra, exceção e pegadinha.

REGRAS DE DURAÇÃO
6. Calcule as palavras pela duração-alvo, a 150 palavras por minuto. Ex.: 60 min ≈
   9.000 a 10.500 palavras.
7. NÃO infle o texto com repetição vazia para atingir a duração. Conteúdo real primeiro.

ACESSIBILIDADE (TDAH/TEA)
8. Frases curtas. Avisos de transição entre blocos. Exemplos práticos.
9. Use "se aparecer X, pense em Y". Explique antes de aprofundar.
10. Evite parede sonora, latim sem tradução e tom motivacional vazio.

ESTRUTURA DO ROTEIRO (blocos)
- Bloco 1: abertura e estratégia de prova.
- Blocos centrais: um por tema do cronograma (conceito, base legal, doutrina,
  jurisprudência se houver, comparação, exemplo, pegadinha).
- Bloco de tabelas comparativas narradas.
- Bloco de pegadinhas.
- Bloco de questões comentadas (enunciado, pausa mental, gabarito, porquê, pegadinha).
- Bloco de revisão final (véspera + relâmpago).

SAÍDA — entregue DOIS blocos de texto, nesta ordem:

(1) roteiro_audio.txt
   Texto corrido, dividido pelos blocos acima, com cabeçalhos no formato:
   ====== BLOCO N — TÍTULO ======
   Cada bloco é a fala completa, pronta para ser narrada.

(2) audio.yaml
   Siga EXATAMENTE este esquema (campos obrigatórios por bloco):
   - metadata: projeto, disciplina, escopo, idioma "pt-BR", duracao_alvo_minutos,
     proibido_simular_duracao: true, validacao_obrigatoria: "ffprobe".
   - config: motor_padrao "edge-tts", formato_saida "mp3", pasta_partes
     "audio/parts", arquivo_final "audio/master_audio.mp3", dicionario_fonetico
     "audio/dicionario_fonetico.yaml", chunk_words_padrao 900,
     min_duration_seconds [duração-alvo em segundos x 0,8].
   - vozes: conceito "pt-BR-FranciscaNeural", fundamento "pt-BR-AntonioNeural",
     revisao "pt-BR-ThalitaNeural".
   - blocos: lista; cada item com:
       id (bloco_001, bloco_002, ...)
       ordem (número)
       titulo
       chapter_title (curto, sem acento problemático)
       voz (use Francisca para conceito/síntese/revisão; Antonio para
            fundamentação legal e jurisprudência; Thalita para pegadinhas e questões)
       rate ("+0%" padrão; "-5%" para artigo/jurisprudência; "+5%" para revisão)
       pitch "+0Hz"
       pause_after_ms 1200
       palavras_estimadas (conte as palavras do texto do bloco)
       texto (use bloco literal YAML com "|", a fala completa do bloco)

NÃO faça mais nada além desses dois blocos de texto. Não comente o código, não
ofereça gerar áudio, não gere imagens.
```

---

## 4. PROMPT B — Flashcards + questões (opcional, colar depois)

```text
Mantendo a mesma disciplina e a mesma base anexada, gere agora DOIS blocos de texto:

(1) flashcards_audio.csv
   Formato CSV com cabeçalho exatamente: frente;verso;tags
   - separador ponto e vírgula;
   - cada linha entre aspas;
   - 30 a 40 cards cobrindo todo o escopo;
   - tags por tema (ex.: principios, casamento, regime-bens, PEGADINHA).
   - NÃO invente fonte; marque [VERIFICAR] no verso quando não tiver certeza.

(2) questoes.md
   - 10 a 15 questões objetivas (certo/errado ou múltipla escolha);
   - para cada uma: enunciado, gabarito, justificativa da correta,
     justificativa curta das erradas, e a pegadinha explorada;
   - baseadas no material anexado; nada inventado.

Não gere áudio nem código. Apenas os dois blocos de texto.
```

---

## 5. PROMPT C — Pesquisa dirigida (Perplexity de preferência)

```text
Pesquise e me traga, com FONTE para cada item (link ou citação oficial):

TEMA: [tema jurídico]
PERÍODO/ATUALIDADE: [ex.: entendimento vigente em 2026]

Quero:
1. a tese/regra atual e a base legal;
2. o número oficial de súmula, Tema, RE ou REsp, se houver;
3. data do julgamento ou da norma;
4. se há divergência STF × STJ ou mudança recente (overruling, revisão de súmula);
5. fonte de cada afirmação.

Não conclua sem fonte. Se não encontrar, diga "não encontrado". Vou levar este
material para validação final antes de usar.
```

---

## 6. Checklist antes de rodar o python3

1. Recebi `roteiro_audio.txt` e `audio.yaml` em texto.
2. Salvei nos caminhos certos (`audio/roteiro_audio.txt`, `audio/audio.yaml`).
3. O `audio.yaml` tem os campos obrigatórios por bloco (id, ordem, titulo,
   chapter_title, voz, texto, palavras_estimadas, pause_after_ms).
4. Marquei para validação tudo que veio com [VERIFICAR].
5. Tenho `gerar_audio_v2.py`, `setup_audio.sh`, `validar_audio.sh`,
   `requirements_audio.txt` e `dicionario_fonetico.yaml` na pasta.
6. Rodei: setup → preflight → geração → validação.
7. Levei o roteiro (ou o pacote) ao Claude para validação jurisprudencial e fechamento.

---

## 7. O que NUNCA pedir a essas IAs

1. Gerar o MP3 final (voz robótica — inaceitável).
2. Confirmar jurisprudência como verdade sem fonte (papel do Claude validar).
3. Usar pyttsx3, gTTS ou espeak.
4. Tratar a resposta de outra IA como prova — é objeto de análise.
5. Aplicar o `pafe_claude.md` (não serve para elas).
