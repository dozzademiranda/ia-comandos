---
Gerado por: Claude (Anthropic) — modelo Opus 4.8
Data de geração: 30/05/2026
---

COMANDO: /consolidar

O QUE É: instrução que gera um resumo de continuidade completo de uma
conversa, em bloco único, para você retomar o trabalho noutra conversa
ou noutra IA sem perder contexto.

QUANDO USAR: ao fim de uma conversa longa, antes de ela travar por
limite, ou quando você quiser migrar o trabalho para outra plataforma.

POR QUE USAR: preserva decisões, justificativas e pendências num formato
que a próxima IA lê e continua de onde paramos, sem refazer o caminho.

NÃO CONFUNDIR COM: /nova-conversa. /consolidar RESUME o que já foi feito.
/nova-conversa INICIA uma conversa nova já contextualizada. Primeiro
consolida-se; depois, se você quiser, gera-se o prompt de inicialização.

---

DEFINIÇÃO OPERACIONAL

Ao receber /consolidar, gerar um resumo de continuidade em um único
bloco de código, contendo, quando pertinente:

- identificação da origem (plataforma, modelo, data);
- contexto;
- objetivo;
- protocolo ativo;
- decisões tomadas;
- justificativas;
- erros corrigidos;
- escolhas rejeitadas;
- respostas de IAs analisadas;
- ranking ou conclusão comparativa, se houver;
- pendências;
- próximos passos;
- instruções para a próxima IA não repetir trabalho;
- prompt inicial, se útil.

Não inventar decisões. Onde algo for incerto, escrever exatamente:
"não documentado no histórico disponível".

Ao final do bloco, SEMPRE oferecer explicitamente, SEM EXECUTAR até o
usuário confirmar:

"Posso transformar isto num prompt de inicialização pronto para colar
como primeira mensagem de uma nova conversa, no formato de bloco único
com as seções IDENTIDADE E ESTILO, ARQUITETURA, SECRETS (só nomes),
DECISÕES, DIFICULDADES E SOLUÇÕES, PENDÊNCIAS, REGRAS PARA A PRÓXIMA IA
e SEGURANÇA. Quer que eu gere?"

Só gerar esse prompt de inicialização se o usuário responder "sim". Se
não quiser, não gastar tokens gerando o resultado não desejado.
