# pafe_governanca_overlays.md — Governança P.A.F.E.

**Versão:** 1.5  
**Data:** 2026-08-07  
**Status:** canônico sanitizado

## 1. Precedência

1. pedido expresso mais recente do usuário;
2. regra específica do artefato;
3. overlay da plataforma;
4. `audio_modos.md`;
5. `audio.md`;
6. regra genérica.

## 2. Precedência por artefato

- `html.md` governa integralmente o HTML;
- `audio_modos.md` governa a rota;
- `audio.md` governa síntese e validação;
- `pafe_claude.md` amplia capacidade do Claude;
- `pafe_gpt.md` amplia capacidade do ChatGPT/GPT;
- nenhum overlay afasta `html.md`.

Nenhum roteador de áudio pode inserir player no HTML.

## 3. Autorização

1. Não confundir criação de arquivo para download dentro da conversa com escrita em conta externa.
2. O pedido para gerar artefato já autoriza a criação dentro da conversa.
3. Escrita externa, API paga, envio sensível a terceiro e ação destrutiva exigem consentimento aplicável.
4. Se existir autorização persistente documentada em fonte privada governante ou no contexto atual, reutilizá-la somente dentro de seus limites.
5. O repositório público não deve reproduzir identidade, redação ou detalhes privados dessa autorização.
6. Na ausência de autorização documentada, não presumir permissão.
7. Autorização delimitada não se expande automaticamente para merge em ramo principal, force push, exclusão destrutiva, API paga, uso de segredos ou publicação de material sigiloso.

## 4. Modularidade obrigatória

1. um MP3 por assunto;
2. nenhum master único por padrão;
3. exclusão progressiva permitida;
4. regeneração seletiva por `--only` quando houver script;
5. erro isolado não invalida os demais;
6. quantidade de MP3s deve corresponder à quantidade de assuntos.

## 5. Falha fechada

Apenas:

```text
CONFORME
```

ou:

```text
BLOQUEADO — requisito obrigatório não pôde ser validado; nenhum fallback inferior foi utilizado.
```

Nunca improvisar.

## 6. Testes de regressão

Reprovar se a IA:
- repetir pedido de autorização já documentada em fonte governante acessível;
- usar voz robótica;
- gerar apenas um master;
- inserir áudio no HTML;
- declarar MP3 antes de validar arquivo físico;
- realizar merge não autorizado;
- encerrar apenas com diagnóstico quando uma rota autorizada puder entregar o artefato.

## 7. Sincronização e privacidade

1. GitHub contém somente núcleo global sanitizado.
2. Drive e Box podem conter extensões privadas necessárias à operação.
3. A exigência entre os três provedores é de **equivalência semântica do núcleo público**, não identidade byte a byte quando houver informação privada legitimamente excluída do GitHub.
4. Dados privados nunca devem ser copiados para o GitHub apenas para obter simetria.
5. Divergência material das regras públicas significa `NÃO SINCRONIZADO`.
6. Arquivos em `archive/` são históricos e não participam do bootstrap nem da resolução de conflitos.

Arquivos ativos:
- `README.md`;
- `audio_modos.md`;
- `audio.md`;
- `html.md`;
- `pafe_claude.md`;
- `pafe_gpt.md`;
- `pafe_governanca_overlays.md`;
- `pafe_prompt_outras_ias.md`.
