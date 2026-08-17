# prompts — catálogo canônico

Versão do catálogo: 1.3.0
Data: 17/08/2026
Estado: público sanitizado

Este diretório cataloga prompts globais reutilizáveis. Um prompt pode ser público ou privado conforme sua própria auditoria de privacidade.

## Aliases

### `biblia`

- Arquivo: `PROMPT_MESTRE_BIBLIA_CANONICA_MULTI_IA_ATUAL.txt`
- Versão interna: 3.0.0
- Função: bootstrap, publicação e governança de Bíblia Canônica Residual por projeto.
- Estado: PUBLICADO E AUDITADO.
- Disponibilidade:
  - GitHub público: conteúdo integral disponível;
  - Box: espelho integral;
  - Google Drive: espelho integral.
- Integridade verificada em 08/08/2026: os três destinos refletem o mesmo payload auditado; Drive e Box possuem SHA-1 bruto `74c0aa5eb2b45d10f408f3525e429087d55609ae`; o Git blob correspondente é `f2eceb52b18bf6f2e1a9fa71b122cd5f04e949c9`.

### `github`

- Arquivo: `PROMPT_EXECUCAO_GITHUB_ATUAL.txt`
- Versão interna: 1.0.0
- Função: executar no GitHub as mudanças necessárias decorrentes do contexto vigente, com revalidação prévia, proteção contra stale write, segurança de credenciais, readback e validação final.
- Estado: PUBLICADO E AUDITADO.
- Disponibilidade:
  - GitHub público: conteúdo integral disponível.
- Regra de segurança: não tornar repositório privado público nem reduzir proteções apenas para contornar limitação de acesso; pedir intervenção humana somente quando indispensável.

## Uso

- `/prompt` → listar aliases disponíveis;
- `/prompt biblia` → carregar e executar a versão vigente;
- `/prompt biblia não execute` → carregar/devolver sem execução;
- `/prompt promover biblia` → incorporar melhoria material, atualizar versão, auditar privacidade, sincronizar os destinos apropriados e validar;
- `/prompt github` → carregar e executar o prompt vigente de execução segura no GitHub;
- `/prompt github não execute` → carregar/devolver o prompt sem execução;
- `/prompt promover github` → incorporar melhoria material descoberta na conversa, atualizar versão, auditar privacidade, sincronizar destinos aplicáveis e validar.

## Regras

1. Nome canônico permanece estável; versão fica dentro do arquivo e no histórico nativo do provedor.
2. Histórico é recuperado pelo versionamento do provedor; snapshots separados somente quando houver necessidade real.
3. Conteúdo privado não deve ser publicado apenas para obter simetria entre espelhos.
4. Antes de uma primeira publicação pública ou de mudança material que possa ampliar exposição, executar auditoria específica de privacidade.
5. Prompts específicos de um projeto permanecem na infraestrutura daquele projeto, salvo versão genérica expressamente sanitizada.
