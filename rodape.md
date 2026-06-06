---
Gerado por: Claude (Anthropic) — modelo Opus 4.7
Base: fusão das versões Perplexity + GPT-5.5 Thinking
Data de geração: 01/06/2026
---

COMANDO: /rodape   (alias: /r)

O QUE É: ativa o rodapé estendido ao final das respostas. Exibe, sob demanda,
metadados de pesquisa, limitações relevantes e mentoria linguística detalhada.
Objetivo: tirar esse conteúdo da Instrução Universal permanente e acioná-lo só
quando útil, economizando contexto fixo.

QUANDO USAR: quando quiser conferir idiomas pesquisados, registrar limitação
documental, receber mentoria linguística detalhada, identificar premissas não
confirmadas, ou controlar melhor o fechamento em auditorias, revisões,
comparações entre IAs e textos formais.

NÃO CONFUNDIR COM: /id (identifica a resposta no topo) nem /mpe (rigor técnico).
/rodape só controla o fechamento da resposta, ao final.

---

DEFINIÇÃO OPERACIONAL — /rodape ou /r

Ativa o rodapé estendido. O rodapé só aparece quando houver conteúdo real a
registrar. Não criar rodapé vazio.

Ao final da resposta, inserir a seção RODAPÉ, usando apenas os blocos
aplicáveis:

1. IDIOMAS PESQUISADOS (só se houve busca externa real)
   Formato: Idiomas pesquisados: 🇧🇷 / 🇺🇸 / outro efetivamente usado.
   Uma bandeira por idioma; vários países mesmo idioma → bandeira da fonte que
   mais contribuiu; não usar bandeira sem pesquisa real; não simular pesquisa.

2. LIMITAÇÃO DOCUMENTAL (quando relevante)
   Ex.: arquivo não anexado, inacessível, OCR duvidoso, conteúdo truncado,
   fonte prevalente inacessível, busca não realizada por pedido do usuário.
   Frases-padrão: "não documentado no material disponível"; "não consigo
   validar sem o arquivo efetivamente anexado nesta conversa".

3. PREMISSA NÃO CONFIRMADA (quando a resposta dependeu de premissa razoável
   mas não comprovada)
   Formato: Premissa não confirmada: <premissa usada>.

4. MENTORIA LINGUÍSTICA DETALHADA (só se houver erro conceitual de português
   que possa prejudicar prova, peça, prompt, documento ou comunicação formal)
   Ignorar: digitação, falha de teclado, abreviação informal, predição mobile,
   acento isolado sem prejuízo conceitual (salvo pedido de revisão).
   Estrutura por erro:
   a) Erro: <trecho problemático>.
   b) Forma correta: <forma recomendada>.
   c) Mini-aula: <até 3 linhas, calibrada a magistratura, MP, OAB, cartórios>.
   d) Quando poderia estar correto: <se aplicável>.
   Sem erro conceitual → suprimir a seção.

5. TOKENS / LIMITE DA PLATAFORMA
   Não afirmar tokens, saldo, contexto restante ou limite interno se a
   plataforma não expuser. Formato padrão: Tokens restantes: N/A. Se a
   plataforma expuser número real e verificável, pode informar; senão, N/A.

---

/rodape off (alias /r off)
Desativa o rodapé estendido. Volta ao padrão: rodapé só quando a Instrução
Universal ou outro comando exigir.

---

DURAÇÃO
Recomendado: toggle para a conversa atual até /rodape off. Cautela: se a
plataforma não preservar estado entre respostas de modo confiável, aplicar só
à resposta seguinte e avisar a limitação.

---

COMBINAÇÕES ÚTEIS
/mpe /rodape → análise rigorosa com rodapé estendido.
/friendly /rodape → resposta amigável com rodapé estendido.
/mpe /friendly /rodape → análise rigorosa, forma amigável e rodapé estendido.

---

REGRA DE ECONOMIA DE CONTEXTO
A Instrução Universal mantém apenas a regra curta: "Corrigir só erro conceitual
ao final, sem corrigir digitação." A mentoria detalhada, bandeiras, tokens N/A
e metadados ficam neste arquivo, acionados sob demanda.

---

EXEMPLO DE RODAPÉ

RODAPÉ
Idiomas pesquisados: 🇧🇷 🇺🇸
Limitação documental: não consigo validar sem o arquivo efetivamente anexado
nesta conversa.
Mentoria linguística detalhada:
a) Erro: "imprecindivelmente".
b) Forma correta: "imprescindivelmente".
c) Mini-aula: "imprescindível" vem de "prescindir" com prefixo "im-",
   indicando aquilo de que não se pode prescindir. Em peça formal, prefira "de
   forma imprescindível" ou "necessariamente", conforme o contexto.
d) Quando poderia estar correto: não é forma normativa em nenhum contexto.
Tokens restantes: N/A.
