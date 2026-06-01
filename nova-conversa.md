---
Gerado por: Claude (Anthropic) — modelo Opus 4.8
Data de geração: 30/05/2026
---

COMANDO: /nova-conversa

O QUE É: gera o prompt de inicialização para colar como primeira
mensagem de uma nova conversa, já contextualizada com tudo o que foi
decidido na conversa anterior.

QUANDO USAR: depois que /consolidar gerou o resumo e você escolheu
"sim, gere o prompt de inicialização". Também isoladamente, quando
você já tem o material e quer apenas a formatação.

POR QUE USAR: a nova IA (ou nova conversa) lê um bloco único e já
trabalha no mesmo nível de contexto, sem refazer o caminho.

NÃO CONFUNDIR COM: /consolidar. /consolidar RESUME a conversa
encerrada. /nova-conversa transforma esse resumo num PROMPT pronto
para iniciar a próxima.

---

DEFINIÇÃO OPERACIONAL

Gerar um único bloco de código contendo, em ordem:

IDENTIDADE E ESTILO
Quem é o usuário, perfil, postura esperada, idioma, formato de resposta.

ARQUITETURA
Estrutura técnica/conceitual do trabalho em curso. Onde as coisas moram,
como se conectam.

SECRETS
Só o NOME das credenciais ou variáveis necessárias. Nunca o valor.

DECISÕES
O que já foi decidido e não se rediscute, salvo pedido explícito.

DIFICULDADES E SOLUÇÕES
O que travou, como resolveu. Evita a próxima IA repetir o erro.

PENDÊNCIAS
O que falta fazer, em ordem de prioridade.

REGRAS PARA A PRÓXIMA IA
O que ela deve e não deve fazer. Incluir: "antes de gastar tokens em
geração longa, validar a premissa com o usuário".

SEGURANÇA
O que não publicar, o que não executar sem confirmação, o que tratar
como confidencial.

Não inventar. Onde algo for incerto: "não documentado no histórico
disponível".
