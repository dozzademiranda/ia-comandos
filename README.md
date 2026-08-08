# ia-comandos — governança multi-IA

Versão da arquitetura: 1.8.0
Data: 07/08/2026
Estado: canônico sanitizado

## 1. Objetivo

Manter um conjunto pequeno de fontes governantes que possa ser consultado por diferentes IAs sem duplicar regras, exigir memorização do usuário ou permitir que arquivos históricos vençam versões ativas.

## 2. Localizações equivalentes

- GitHub público: `dozzademiranda/ia-comandos`, branch `main`;
- Google Drive: `Meu Drive → Documentos → I.A. → Comandos`;
- Box: `Recursos-IA → Comandos`.

A localização preferencial depende da plataforma e serve para descoberta. Autoridade é determinada por instrução atual do usuário, versão interna, estado e conteúdo, conforme `comandos.md`.

## 3. Árvore lógica ativa

```text
Comandos/
├── README.md
├── instrucoes-universais.md
├── comandos.md
├── consolidar.md
├── pafe/
└── prompts/
```

### Função

- `instrucoes-universais.md` — comportamento global, reconciliação de espelhos, privacidade e continuidade por uma tecla;
- `comandos.md` — significado e execução dos comandos iniciados por `/`;
- `consolidar.md` — definição integral de `/consolidar`;
- `pafe/` — módulos especializados do P.A.F.E.;
- `prompts/` — biblioteca de prompts reutilizáveis; `prompts/README.md` é o catálogo.

## 4. Compatibilidade

Os seguintes caminhos podem permanecer para preservar links antigos, mas são apenas redirecionadores e nunca fontes autônomas:

- `mpe.md`;
- `id.md`;
- `friendly.md`;
- `rodape.md`;
- `nconversa.md`;
- configurações provider-specific marcadas como legadas, como `instrucoes-universais-GEMINI.md` e `instrucoes-personalizadas-gpt.md`.

Se um redirecionador divergir de uma fonte ativa, a fonte ativa prevalece.

## 5. Histórico e limpeza

- `archive/`, `old/`, `*.old*`, `(OLD)` e `intermediario_*` são históricos;
- não entram no bootstrap;
- não são consultados por padrão;
- só devem ser lidos para auditoria, recuperação ou comparação de versões;
- GitHub normalmente usa o próprio histórico de commits em vez de manter snapshots ativos.

## 6. Privacidade

GitHub público contém somente núcleo global sanitizado.

Drive e Box podem conter extensões privadas, inclusive autorizações operacionais ou materiais específicos, quando isso for necessário. Essas extensões não devem ser copiadas ao GitHub apenas para obter identidade byte a byte.

O critério entre espelhos é equivalência semântica do núcleo público e preservação deliberada das extensões privadas.

## 7. Biblioteca de prompts

- `/prompt` abre o catálogo;
- `/prompt <alias>` carrega e executa o prompt vigente;
- `/prompt <alias> não execute` apenas carrega/devolve;
- `/prompt promover <alias>` incorpora melhoria material, atualiza versão interna e catálogo e sincroniza somente os destinos apropriados.

Nome de prompt canônico é estável; número de versão não entra no nome do arquivo.

## 8. Regra operacional

1. carregar a fonte ativa adequada;
2. ignorar histórico salvo pedido específico;
3. executar ações já autorizadas;
4. não publicar informação privada em espelho público;
5. reler e validar após alteração;
6. quando houver continuação útil, oferecer opções executáveis por uma tecla.
