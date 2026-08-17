# /help — AJUDA CANÔNICA DE COMANDOS

Gerado por: GPT-5.6 Sol
Data: 17/08/2026
Versão: 1.0.0
Estado: candidato sanitizado

## 1. Objetivo

Fornecer ajuda operacional atualizada sobre comandos canônicos sem executar o comando consultado e sem inventar parâmetros, flags, aliases ou semântica ausentes das fontes vigentes.

## 2. Sintaxe

- `/help` → exibe ajuda curta sobre como consultar comandos e aponta para `/comandos` quando o objetivo for apenas listar o catálogo.
- `/help <comando>` → resolve a definição canônica vigente do comando e mostra sua sintaxe, variantes, modificadores documentados, defaults, comportamento de execução e exemplos úteis.
- `/<comando>?` → alias curto de `/help <comando>` quando a forma for inequívoca; exemplos: `/mpe?`, `/prompt?`, `/bootstrap?`.
- `/help <comando> completo` → inclui também fonte canônica, versão interna, arquivo especializado aplicável, regras de fallback e observações de compatibilidade relevantes.

O nome em `<comando>` pode ser informado com ou sem `/`. Para famílias, aceitar a forma-base quando inequívoca; por exemplo, `mpe` cobre `/mpe`, `/mpe+` e `/mpe-`.

## 3. Regra de resolução

1. Consultar `comandos.md` primeiro quando acessível.
2. Se o comando apontar para definição especializada ativa, consultar também o arquivo indicado, como `consolidar.md`, `bootstrap.md`, `pafe/README.md` ou `prompts/README.md`.
3. Aplicar as regras vigentes de resolução resiliente, versão interna, estado, conteúdo, fallback e `NÃO LOCALIZADO NESTA IA ≠ INEXISTENTE`.
4. Não promover arquivo histórico, redirecionador legado ou snapshot antigo a fonte vigente.
5. Se duas fontes declararem a mesma versão e divergirem materialmente, informar `NÃO SINCRONIZADO` e não escolher silenciosamente uma delas.

## 4. Saída mínima

Para `/help <comando>`, responder de forma curta e operacional com:

- `COMANDO`;
- `FUNÇÃO`;
- `SINTAXE`;
- `VARIANTES / MODIFICADORES DOCUMENTADOS`;
- `DEFAULTS E COMPORTAMENTO DE EXECUÇÃO`;
- `EXEMPLOS`;
- `FONTE / VERSÃO` quando confirmáveis.

Se o usuário perguntar por “parâmetros”, distinguir explicitamente:
- comandos/aliases;
- variantes sintáticas;
- modificadores documentados;
- instruções livres que podem acompanhar o comando;
- parâmetros inexistentes ou não documentados.

## 5. Segurança epistêmica

1. Não inventar flags no estilo CLI (`--deep`, `--web`, `--execute`, etc.) se não estiverem documentadas.
2. Não inferir que uma instrução livre é parâmetro formal do comando.
3. Não executar o comando-alvo apenas porque ele foi consultado via `/help` ou `?`.
4. Se a definição não puder ser recuperada integralmente, declarar recuperação parcial ou indisponibilidade conforme as regras canônicas, em vez de completar por memória.
5. Se o usuário fornecer definição mais recente diretamente na conversa, ela prevalece para aquela execução, subordinada às regras superiores aplicáveis.

## 6. Exemplos

### `/help mpe`
Mostrar `/mpe`, `/mpe+`, `/mpe-`, ordens como `não execute`/`apenas o prompt`, `/id off`, idiomas de pesquisa documentados, defaults e comportamento de execução.

### `/mpe?`
Equivale a `/help mpe` e não executa `/mpe`.

### `/help bootstrap completo`
Mostrar `/bootstrap`, `/boot`, `/bootstrap <destino>`, `/bootstrap completo`, formas de recuperação documentadas e a versão do `bootstrap.md` efetivamente confirmada.

### `/help prompt`
Mostrar catálogo/semântica de `/prompt`, incluindo carregar, executar, `não execute` e `promover`, sem executar nenhum alias da biblioteca.

## 7. Relação com `/comandos`

- `/comandos` responde “quais comandos existem?” com catálogo curto.
- `/help <comando>` responde “como este comando funciona e quais formas documentadas posso usar?”.

## 8. Ativação

Este arquivo só se torna definição operacional ativa após ser referenciado pelo `comandos.md` canônico vigente. Até lá, seu estado é CANDIDATO, não comando ativo.
