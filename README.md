# ia-comandos — governança multi-IA

Revisão de governança: 1.7.0
Data: 07/08/2026

## Objetivo

Sistema portátil de instruções e comandos para uso em múltiplas IAs, com baixa fricção operacional, rastreabilidade e espelhos em Box, Google Drive e GitHub.

## Fontes ativas

- `instrucoes-universais.md` — comportamento global, segurança e continuidade de uma tecla.
- `comandos.md` — significado canônico dos comandos iniciados por `/`.
- `consolidar.md` — definição detalhada vigente de `/consolidar`.
- `nconversa.md` — alias/compatibilidade de `/nova-conversa`.
- `pafe/` — material especializado do P.A.F.E., quando aplicável.

`mpe.md` e `id.md` permanecem somente como redirecionadores de compatibilidade para links antigos. **Nunca prevalecem sobre `comandos.md`.**

## Prevalência operacional

1. definição explicitamente fornecida pelo usuário na conversa;
2. Box, quando acessível;
3. Google Drive, quando acessível;
4. GitHub Raw;
5. histórico consolidado.

Localização preferencial:
- Claude: Box → Recursos-IA → Comandos;
- Gemini/GPT: Google Drive → Documentos → I.A. → Comandos;
- Perplexity/sem conector: GitHub Raw.

Se espelhos divergirem, comparar versão interna e conteúdo antes de executar.

## Duas regras que não podem regredir

1. `/mpe`, `/mpe+` e `/mpe-` geram cabeçalho automaticamente; `/id` não é necessário. `/id` serve para cabeçalho fora da família MPE, e `/id off` o desativa quando solicitado.
2. Toda resposta substantiva deve oferecer, quando houver continuidade útil, um menu de até três opções acionáveis por **uma única tecla**. Um `1`, `2` ou `3` isolado executa a opção correspondente do menu mais recente.

## Privacidade

O GitHub público contém apenas material global sanitizado. Conteúdo privado ou específico de projeto permanece em armazenamento privado ou sob a governança do próprio projeto.
