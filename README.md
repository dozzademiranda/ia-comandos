# ia-comandos — Sistema de comandos multi-IA (Fábio)

## Objetivo
Conjunto de arquivos .md que definem um sistema de comandos portável, usado
em várias IAs (Claude, GPT, Gemini, Perplexity). Padroniza perfil, postura,
estrutura de resposta e comandos, para reduzir retrabalho e sobrecarga
cognitiva no fluxo multi-IA.

## Arquivos principais
- instrucoes-universais.md — núcleo permanente para colar no Perfil da IA.
- comandos.md — índice operacional dos comandos ativos.
- friendly.md — comando adaptativo de acessibilidade cognitiva (/friendly).
- rodape.md — comando de rodapé estendido sob demanda (/rodape).
- consolidar.md — definição do /consolidar.
- nconversa.md — definição do /nconversa.
- id.md — definição do /id (identificação e proveniência).
- mpe.md
- pafe.md

## Como usar
Cada comando tem um arquivo .md próprio. Quando a IA tiver acesso ao arquivo,
deve ler a definição completa antes de executar o comando.

## Localização canônica por IA
- Claude → Box → Recursos-IA → Comandos → <nome-do-comando>.md
- Gemini / GPT → Google Drive → Meu Drive → Documentos → I.A. → comandos → <nome-do-comando>.md
- Perplexity → GitHub Raw → https://raw.githubusercontent.com/dozzademiranda/ia-comandos/main/<nome-do-comando>.md

## Regra de prevalência
1. Se a IA tiver acesso ao Box, prevalece a versão do Box.
2. Se não, usar a fonte acessível na plataforma atual.
3. Se eu anexar/colar uma versão mais recente na conversa, essa versão
   prevalece para a tarefa atual.

## Privacidade no GitHub
1. Não presumir que GitHub público é seguro.
2. Este repositório só pode conter instruções sanitizadas: sem dados
   pessoais sensíveis, sem chaves, sem detalhes de casos jurídicos, sem
   estratégias confidenciais.
3. Conteúdo sensível vai apenas para Box, Google Drive, GitHub privado ou
   arquivo anexado direto na conversa.
