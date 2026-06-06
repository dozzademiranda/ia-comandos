---
Gerado por: Claude (Anthropic) — modelo Opus 4.7
Data de geração: 01/06/2026
---

COMANDO: /consolidar

O QUE É: gera um resumo de continuidade da conversa atual, em bloco único,
para retomar o trabalho noutra conversa ou noutra IA sem perder contexto.

QUANDO USAR: quando a conversa ficou longa, ou antes de trocar de IA/conversa,
para não repetir trabalho já feito.

POR QUE USAR: preserva decisões, pendências e o caminho percorrido, evitando
reabrir o que já foi resolvido.

NÃO CONFUNDIR COM: /nova-conversa. /consolidar diagnostica e resume a conversa
encerrada; /nova-conversa produz o prompt de inicialização da próxima.

---

DEFINIÇÃO OPERACIONAL

Ao receber /consolidar, gerar UM bloco único contendo, quando pertinente:
1. identificação da origem (IA, modelo, data);
2. contexto e objetivo;
3. protocolo/comandos ativos;
4. decisões tomadas e justificativas;
5. erros corrigidos;
6. escolhas rejeitadas (e por quê);
7. respostas de outras IAs analisadas e conclusão comparativa;
8. pendências;
9. próximos passos;
10. instruções para a próxima IA não repetir trabalho.

Não inventar decisões. Onde algo for incerto: "não documentado no histórico
disponível".

Ao final, oferecer (sem executar) gerar o /nova-conversa.
