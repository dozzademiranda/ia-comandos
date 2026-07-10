# pafe_governanca_overlays.md — Governança de overlays, deltas e capacidades por IA

**Versão:** 1.1  
**Data:** 2026-07-10  
**Escopo:** P.A.F.E. transversal — preservação de regras específicas por plataforma/IA  
**Status:** ativo e canônico para impedir apagamento indevido de deltas úteis.

---

## 1. Regra central

Nenhuma IA pode remover, simplificar ou neutralizar uma regra específica de outra IA apenas porque ela própria não consegue executar aquela capacidade.

A incapacidade operacional de uma plataforma é **limite da plataforma**, não prova de que a regra é inútil, falsa ou obsoleta.

Quando uma regra não se aplica ao ambiente atual, a IA deve classificá-la como:

```text
ESCOPO_DE_PLATAFORMA: não aplicável aqui; preservar no overlay correspondente.
```

Nunca converter “não consigo executar” em “deve ser apagado”.

---

## 2. Camadas canônicas

O P.A.F.E. deve ser lido em camadas:

1. `README.md` — núcleo transversal do comando `/pafe`;
2. `audio_modos.md` — roteamento entre MP3 direto, roteiro textual, pacote local e rotas externas;
3. `audio.md` — governança técnica de áudio, validação, manifesto, TTS, segurança e auditoria;
4. `html.md` — governança do HTML offline;
5. `pafe_claude.md` — overlay exclusivo do Claude quando houver ambiente de execução ativo;
6. `pafe_prompt_outras_ias.md` — prompt/launcher para GPT, Gemini, Perplexity e outras IAs sem overlay Claude;
7. `pafe_governanca_overlays.md` — regra de preservação de deltas por IA, origem e escopo.

Em conflito aparente, aplicar a regra mais específica sem apagar a regra geral.

---

## 3. Princípio “capacidade não é verdade”

Distinguir sempre:

1. **verdade técnica/documental** — o que é correto sobre ferramenta, fluxo, arquivo, lei ou fonte;
2. **capacidade local da IA** — o que a plataforma atual consegue executar;
3. **política operacional do projeto** — o que o P.A.F.E. decide fazer por segurança, rastreabilidade e qualidade.

Exemplo:

```text
Claude com ambiente de execução pode gerar MP3 real no próprio turno.
GPT/Gemini/Perplexity podem não conseguir gerar MP3 real com qualidade auditável.
As duas afirmações podem ser verdadeiras ao mesmo tempo.
```

Logo, é errado transformar uma regra genérica como “não tente gerar MP3 nesta conversa” em regra universal contra Claude, quando `pafe_claude.md` disser o contrário.

---

## 4. Regra anti-apagamento

Ao revisar arquivos P.A.F.E., a IA deve seguir este procedimento:

1. identificar se a regra é universal ou específica de plataforma;
2. se for específica, preservar no overlay próprio;
3. se parecer incompatível, registrar como conflito aparente;
4. propor nota de escopo, não exclusão;
5. só remover regra se houver autorização expressa do usuário e justificativa documentada;
6. registrar a remoção no histórico/changelog.

Nunca apagar silenciosamente:

1. regras Claude de `present_files`, bash, rede, `ffprobe`, `edge-tts`, `preparar_ssl()` ou geração direta de MP3;
2. regras GPT/Gemini/Perplexity de roteiro textual, HTML, YAML ou pesquisa;
3. regras de segurança de API key;
4. regras de diagnóstico DNS × SSL × endpoint;
5. regras de auditoria por `ffprobe`, hash, checksum, manifesto ou artifact digest.

---

## 5. Cláusula anti-apagamento de overlay alheio

1. Nenhuma IA remove regra específica de outra plataforma alegando que “não consegue executar aquela regra”.
2. Incapacidade de executar não equivale a invalidade da regra.
3. IA que não é titular do overlay pode sinalizar dúvida ou propor nota de escopo.
4. IA que não é titular do overlay não pode apagar, simplificar ou consolidar a regra para dentro dos próprios limites.
5. Toda alteração em overlay alheio exige autorização expressa do Fábio no turno.
6. Exemplo concreto: GPT/Gemini/Perplexity não removem `pafe_claude.md`, nem suas remissões nos módulos comuns, por não terem execução em sessão.

---

## 6. Matriz de plataformas

| Ambiente | Pode gerar MP3 direto? | Conduta P.A.F.E. |
|---|---:|---|
| Claude com execução ativa, bash, rede e entrega de arquivo | Sim, se smoke test passar | Tentar MP3 real; validar por `ffprobe`; entregar arquivo; não cair direto em execução local. |
| GPT/ChatGPT sem ferramenta de geração de arquivo MP3 real | Não de forma garantida | Gerar roteiro, YAML, HTML ou script; não afirmar MP3 gerado. |
| Gemini/Perplexity sem execução confiável de binário | Não de forma garantida | Gerar texto, pesquisa, roteiro, YAML e checklist; execução fica local ou em outro ambiente. |
| Máquina local do usuário | Sim | Rota preferencial para execução robusta com `edge-tts`, `ffmpeg`, `ffprobe`, logs e hashes. |
| GitHub Actions | Sim, se rede e dependências passarem | Contingência automatizada; publicar artifact com checksum/digest. |
| Codespaces | Sim, se rede e dependências passarem | Contingência manual/remota para debug. |

---

## 7. Regra específica de áudio

O fluxo de áudio deve preservar simultaneamente estas verdades:

1. `edge-tts` é motor gratuito útil, mas depende de serviço online.
2. DNS, SSL/certificado e endpoint indisponível são classes diferentes de erro.
3. SSL relaxado só é último recurso para erro de certificado, nunca padrão.
4. SSL relaxado é proibido com senha, token, API key ou dado sensível.
5. Se o ambiente for Claude e tiver execução real, deve fazer smoke test antes de declarar impossibilidade.
6. Se a IA não puder gerar MP3 real, deve entregar roteiro/YAML/script/HTML sem afirmar que o MP3 existe.
7. Fallback robótico ou degradado não deve ser usado para “cumprir tarefa”.
8. Piper TTS pode ser plano B offline, com qualidade declaradamente inferior à `edge-tts`.

---

## 8. Metadados obrigatórios para dica de IA

Toda dica preciosa trazida de outra IA deve ser preservada com estes campos, quando disponíveis:

```text
ORIGEM_IA:
MODELO:
DATA:
PROJETO/CONTEXTO:
TRECHO ÚTIL:
ESCOPO:
STATUS: incorporar | preservar como overlay | verificar | rejeitar
MOTIVO:
RISCO SE APAGAR:
ARQUIVOS AFETADOS:
```

Se faltar modelo/data, registrar “não informado”.

---

## 9. Cabeçalho padrão de origem da dica

Toda regra portada de uma conversa/IA para um arquivo do P.A.F.E. registra, em comentário próximo à regra:

```text
Origem: [IA + modelo, ex.: Claude Opus 4.8]
Data: [AAAA-MM-DD]
Contexto/projeto: [ex.: PAFE | consolidacao-prompt-launcher | FDM-039]
Risco se apagado: [1 linha]
```

Finalidade: permitir auditar por que a regra existe, quando surgiu e o que se perde ao removê-la. Uma futura revisão que não entenda o motivo deve consultar esse cabeçalho antes de propor exclusão.

---

## 10. Como pedir nova rodada à IA de origem

Quando uma dica veio de modelo antigo, a próxima consulta à mesma IA deve perguntar:

```text
Reavalie esta orientação à luz do seu modelo atual e das ferramentas atuais.
Não apague regras específicas de outra plataforma por incapacidade sua.
Classifique cada item como: manter, atualizar, mover para overlay, depreciar ou remover.
Explique o motivo técnico e indique o arquivo P.A.F.E. afetado.
```

---

## 11. Histórico de origem incorporado

### 11.1. Claude Opus 4.8 Extra — 2026-05-29

Origem identificada em prompt anexado:

```text
[PAFE | projeto: consolidacao-prompt-launcher | modelo: Claude Opus 4.8 Extra | data: 2026-05-29 | FDM-039]
```

Deltas preciosos:

1. diagnóstico DNS × SSL × endpoint;
2. regra de não gerar áudio degradado;
3. plano B Piper offline;
4. launcher enxuto para plataforma com Bloco A instalado;
5. launcher autossuficiente para plataforma sem instrução persistente.

### 11.2. IA GPT — relatório comparativo posterior

Origem identificada no mesmo anexo como “IA GPT”.

Deltas preciosos:

1. recomendação de usar a proposta Claude com ajustes;
2. separação entre conteúdo/roteiro e execução técnica do áudio;
3. preflight técnico obrigatório;
4. logs, `ffprobe`, checksums e artifact digest;
5. versão enxuta de arranque P.A.F.E. v11.4.1.

### 11.3. Claude Opus 4.7 alto — análise de consolidação — 2026-07-10

Origem informada pelo usuário: resposta da IA Claude com modelo Opus 4.7 alto.

Deltas preciosos:

1. reconhecer que `audio_modos.md` é roteador de modo e `audio.md` define técnica;
2. corrigir a linha de versionamento para `audio.md v6.x MASTER`;
3. propor `audio.md v6.2 MASTER`, `audio_modos.md v1.2`, `pafe_prompt_outras_ias.md v1.2` e `pafe_governanca_overlays.md v1.1`;
4. separar v11.4.2 de v11.4.3: agora atualiza arquivos canônicos; depois implementar `sha256_master` no script e testar rotas Actions/Codespaces;
5. reforçar que Fable/novo modelo pode atuar como auditor posterior, não como condição para avançar.

---

## 12. Rodapé operacional

Versão: `pafe_governanca_overlays.md v1.1`  
Data: 2026-07-10  
Regra central: preservar deltas específicos por IA; incapacidade local não autoriza apagar regra canônica ou overlay de outra plataforma.  
Arquivos relacionados: `README.md`, `audio_modos.md`, `audio.md`, `html.md`, `pafe_claude.md`, `pafe_prompt_outras_ias.md`.

Histórico:

| Versão | Data | Motivo |
|---|---|---|
| v1.1 | 2026-07-10 | Adiciona cláusula antiapagamento de overlay alheio, cabeçalho padrão de origem da dica e origem Claude Opus 4.7 alto. |
| v1.0 | 2026-07-10 | Criação do controle de governança de overlays e deltas úteis. |