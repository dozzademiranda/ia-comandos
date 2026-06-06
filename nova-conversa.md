---
Gerado por: Claude (Anthropic) — modelo Opus 4.7
Data de geração: 01/06/2026
---

COMANDO: /nova-conversa

O QUE É: gera o prompt de inicialização da próxima conversa, estruturado para
ser colado como primeira mensagem de uma nova conversa (mesma IA ou outra).

QUANDO USAR: depois de /consolidar, ou ao iniciar uma nova conversa que
precise herdar o contexto da anterior.

POR QUE USAR: arranca a nova conversa já com identidade, arquitetura, decisões
e pendências, sem refazer explicação.

NÃO CONFUNDIR COM: /consolidar. /consolidar resume o que passou; /nova-conversa
prepara o que vem.

---

DEFINIÇÃO OPERACIONAL

Ao receber /nova-conversa, gerar UM bloco único com as seções:
1. IDENTIDADE E ESTILO;
2. ARQUITETURA;
3. SECRETS (apenas nomes de variáveis/credenciais necessárias, nunca valores);
4. DECISÕES;
5. DIFICULDADES E SOLUÇÕES;
6. PENDÊNCIAS;
7. REGRAS PARA A PRÓXIMA IA;
8. SEGURANÇA.

Não inventar. Onde algo for incerto: "não documentado no histórico disponível".
