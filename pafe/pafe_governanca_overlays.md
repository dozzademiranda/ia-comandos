# pafe_governanca_overlays.md — Governança P.A.F.E.

**Versão:** 1.3
**Data:** 2026-07-17
**Status:** canônico

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
- `pafe_claude.md` amplia capacidade do Claude, sem afastar `html.md`.

Nenhum roteador de áudio pode inserir player no HTML.

## 3. Autorização

Não confundir:

- criação de arquivo para download dentro da conversa;
- escrita em conta externa.

O pedido para gerar artefato já autoriza a primeira.

Exigem consentimento expresso:

- GitHub, Drive ou Box;
- branch, commit, workflow;
- API paga;
- envio sensível a terceiro;
- exclusão ou substituição externa.

## 4. Modularidade obrigatória

1. um MP3 por assunto;
2. nenhum master único por padrão;
3. exclusão progressiva permitida;
4. regeneração seletiva por `--only`;
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

- pedir autorização para script local já solicitado;
- exigir outro comando quando a intenção está clara;
- apresentar GitHub como única rota;
- usar voz robótica;
- gerar apenas um master;
- inserir áudio no HTML;
- encerrar com diagnóstico sem artefato corretivo.

## 7. Sincronização

Box, Google Drive e GitHub devem manter conteúdo, versão e data idênticos. Divergência significa `NÃO SINCRONIZADO`.
