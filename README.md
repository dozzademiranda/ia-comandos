# ia-comandos

Repositório canônico de comandos e instruções para uso em múltiplas IAs.

## Objetivo

Centralizar, versionar e distribuir os arquivos `.md` do sistema de comandos
de forma legível por humanos e reutilizável por diferentes IAs.

## Arquivos principais

- `instrucoes-universais.md`
- `comandos.md`
- `friendly.md`
- `consolidar.md`
- `nova-conversa.md`
- `id.md`

## Arquivos históricos

Os arquivos abaixo podem ser mantidos por histórico, mas não são mais
comandos principais do sistema:

- `friendly-tdah.md`
- `friendly-autista.md`
- `friendly-burnout.md`

## Como usar

1. Cada comando possui um arquivo `.md` próprio.
2. Quando a IA tiver acesso ao arquivo correspondente, deve ler a definição
   completa antes de executar o comando.
3. `README.md` explica o repositório e as regras de acesso.
4. `comandos.md` é o índice operacional da lista ativa.
5. `friendly.md` define o novo `/friendly` adaptativo.

## Localização canônica por IA

- IA CLAUDE = Box → Recursos-IA → Comandos → `<nome-do-comando>.md`
- IA GEMINI / GPT = Google Drive → Meu Drive → Documentos → `I.A.` → comandos → `<nome-do-comando>.md`
- IA PERPLEXITY = GitHub Raw → `https://raw.githubusercontent.com/dozzademiranda/ia-comandos/main/<nome-do-comando>.md`

## Links principais

- Repositório humano:
  `https://github.com/dozzademiranda/ia-comandos`

- Leitura automatizada preferencial por IA:
  `https://raw.githubusercontent.com/dozzademiranda/ia-comandos/main/<nome-do-comando>.md`

## Regra de prevalência

1. Se houver arquivo anexado ou colado na conversa atual, essa versão prevalece
   para a tarefa atual.
2. Se a IA tiver acesso ao Box, prevalece Box.
3. Se a IA não tiver acesso ao Box, usar a fonte acessível na plataforma atual.
4. Se a IA não tiver acesso à fonte principal, usar GitHub Raw como fallback.
5. Se houver divergência entre versões e a IA não conseguir acessar a fonte
   prevalente, deve declarar a limitação.

## Regra de integridade

- Não inventar comando, fonte, caminho, URL ou arquivo.
- Se algo não estiver documentado no material disponível, escrever:
  `não documentado no material disponível`.
- Se depender de arquivo não acessível na conversa, escrever:
  `não consigo validar sem o arquivo efetivamente anexado nesta conversa`.

## Observação de segurança

Este repositório deve conter apenas arquivos de comandos e instruções sem dados
sensíveis, credenciais, informações pessoais privadas ou conteúdo que dependa
de sigilo.
