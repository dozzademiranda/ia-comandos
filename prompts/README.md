# prompts — catálogo canônico

Versão do catálogo: 1.1.0
Data: 07/08/2026
Estado: público sanitizado

Este diretório cataloga prompts reutilizáveis. O catálogo pode apontar para prompts privados sem publicar seu conteúdo.

## Aliases

### `biblia`

- Arquivo: `PROMPT_MESTRE_BIBLIA_CANONICA_MULTI_IA_ATUAL.txt`
- Versão interna conhecida: 3.0.0
- Função: bootstrap, publicação e governança de Bíblia Canônica Residual por projeto.
- Disponibilidade:
  - Box: conteúdo disponível em espelho privado;
  - Google Drive: conteúdo disponível em espelho privado;
  - GitHub público: **catálogo somente**; o conteúdo integral não é publicado até auditoria específica de privacidade.

## Uso

- `/prompt` → listar aliases disponíveis;
- `/prompt biblia` → carregar e executar o prompt se uma fonte com o conteúdo estiver acessível;
- `/prompt biblia não execute` → carregar/devolver sem execução;
- `/prompt promover biblia` → incorporar melhoria material, atualizar versão e validar/sincronizar apenas os destinos apropriados.

## Regras

1. Nome de arquivo canônico permanece estável; versão fica dentro do arquivo e no histórico nativo do provedor.
2. Histórico é recuperado pelo versionamento do provedor; snapshots separados somente quando houver necessidade real.
3. Prompt privado não deve ser publicado no GitHub apenas para obter simetria entre espelhos.
4. Se a plataforma só tiver acesso ao GitHub e o conteúdo do alias for privado, declarar a indisponibilidade real; nunca reconstruir ou inventar o prompt por memória.
5. Prompts específicos de um projeto permanecem na infraestrutura privada daquele projeto, salvo versão genérica expressamente sanitizada.
