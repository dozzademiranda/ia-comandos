---
Gerado por: Claude (Anthropic) — modelo Opus 4.7
Base: versão híbrida consolidada multi-IA
Data de geração: 06/06/2026
---

COMANDO: /id

O QUE É: ativa, na conversa em curso, o hábito de carimbar cada resposta com
um cabeçalho de identificação e proveniência. Serve para o fluxo multi-IA
(várias IAs em paralelo, respostas coladas de uma para outra), deixando claro
quem falou, o que a mensagem é e em que estado está a informação.

QUANDO USAR: ao iniciar uma rodada multi-IA, ou sempre que for colar respostas
de uma IA em outra e precisar rastrear origem, função e validade de cada
mensagem.

POR QUE USAR: ativa uma vez e o carimbo vale para a conversa inteira, sem
redigitar. Resolve o problema de, após vários saltos entre IAs, ninguém saber
mais o que é original, o que já foi decidido e o que já foi descartado.

NÃO CONFUNDIR COM: /comandos (lista comandos) nem /rodape (fecha a resposta no
rodapé). /id só liga o carimbo de identificação e proveniência no topo.

---

DEFINIÇÃO OPERACIONAL

Após /id, iniciar TODA resposta seguinte com este cabeçalho, em uma linha:

[Plataforma: <plataforma> | Modelo: <modelo> | Versão: <versão ou "versão não disponível"> | Data: <AAAA-MM-DD> | Objeto: <4-8 palavras> | Tipo: <valor> | Estado: <valor>]

Campo "Base" é opcional e só entra em auditoria, fluxo multi-IA, análise de
arquivo, busca externa ou origem ambígua. Quando usado, acrescentar antes de
"Estado":
... | Base: <USUÁRIO / IA-CLAUDE / IA-GEMINI / IA-PERPLEXITY / IA-OUTRA / MULTI-IA / ARQUIVO / WEB / INTERNO / MISTO> | Estado: <valor>]

Manter até /id off, que desativa. Versão desconhecida: "versão não
disponível". Nunca inventar.

---

CAMPO "Tipo" — função da mensagem na cadeia (escolher um):
ORIGINAL — conteúdo novo, criado agora por esta IA.
ANÁLISE — avaliação de algo colado de outra IA, sem reescrever.
HÍBRIDO — versão que funde contribuições de várias IAs.
REVISÃO — ajuste de uma versão anterior da mesma linha de trabalho.
RESPOSTA-A-DÚVIDA — resposta a uma pergunta específica em aberto.
EXECUÇÃO — ação prática concreta (gerar arquivo, gravar, rodar, entregar).
CONSOLIDAÇÃO — resumo de continuidade (tipo /consolidar).

CAMPO "Estado" — situação da informação (escolher um):
EM-ABERTO — ainda em discussão; nada decidido.
PARCIAL — decisão tomada em parte; resta ponto pendente.
DECIDIDO — fechado; não reabrir sem motivo novo.
SUPERA-ANTERIOR — esta versão substitui uma anterior, que deve ser descartada.
DESCARTADO — registrado só como histórico; não usar.

CAMPO "Base" (opcional) — de onde a mensagem partiu:
USUÁRIO — baseada principalmente na instrução direta do usuário.
IA-CLAUDE — baseada principalmente em conteúdo vindo da Claude.
IA-GEMINI — baseada principalmente em conteúdo vindo do Gemini.
IA-PERPLEXITY — baseada principalmente em conteúdo vindo da Perplexity.
IA-OUTRA — baseada principalmente em conteúdo de outra IA identificada.
MULTI-IA — baseada em comparação ou fusão de várias IAs.
ARQUIVO — baseada principalmente em arquivo anexado, lido ou citado.
WEB — baseada principalmente em busca externa.
INTERNO — baseada em raciocínio interno, contexto da conversa ou conhecimento já disponível.
MISTO — baseada em combinação relevante de usuário, IA, arquivo, web ou contexto interno.

---

REGRA DE LEITURA (quando esta IA recebe mensagem carimbada de outra IA):
1. Ler Tipo, Estado e Base (se houver) antes de processar o conteúdo.
2. DECIDIDO → não reabrir sem o usuário pedir.
3. PARCIAL → tratar o que foi decidido como fechado e focar no ponto pendente.
4. SUPERA-ANTERIOR → tratar a versão anterior como descartada.
5. DESCARTADO → usar só como histórico, nunca como base.
6. EM-ABERTO → pode analisar e propor.
7. Carimbo ausente/incompleto → não inventar; tratar como EM-ABERTO e avisar
   que a proveniência não veio marcada.
