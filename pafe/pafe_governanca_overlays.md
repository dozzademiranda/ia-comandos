# pafe_governanca_overlays.md — Governança P.A.F.E.

**Versão:** 1.4  
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
- `pafe_claude.md` amplia capacidade do Claude;
- `pafe_gpt.md` amplia capacidade do ChatGPT/GPT e documenta a rota GitHub Actions;
- nenhum overlay afasta `html.md`.

Nenhum roteador de áudio pode inserir player no HTML.

## 3. Autorização

Não confundir criação de arquivo para download dentro da conversa com escrita em conta externa.

O pedido para gerar artefato já autoriza a criação dentro da conversa.

Regra geral: escrita externa, API paga, envio sensível a terceiro e ação destrutiva exigem consentimento expresso.

Exceção delimitada: Fábio Dozza de Miranda autorizou o ChatGPT/GPT, inclusive em execuções futuras, a usar branches temporárias e GitHub Actions no repositório `dozzademiranda/ia-comandos` para geração de áudio P.A.F.E., nos limites de `pafe_gpt.md`. Não solicitar novamente essa autorização.

A exceção não autoriza merge em `main`, force push, alteração permanente não relacionada, exclusão destrutiva, API paga, uso de segredos ou exposição de conteúdo sigiloso em repositório público.

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

Reprovar se a IA pedir novamente a autorização prevista em `pafe_gpt.md`, usar voz robótica, gerar apenas um master, inserir áudio no HTML, declarar MP3 antes de baixar artifact físico, mesclar pull request temporário em `main` ou encerrar com diagnóstico quando uma rota autorizada puder entregar o artefato.

## 7. Sincronização

Box, Google Drive e GitHub devem manter conteúdo, versão e data idênticos. Divergência significa `NÃO SINCRONIZADO`.

Arquivos obrigatórios:

- `README.md`;
- `audio_modos.md`;
- `audio.md`;
- `html.md`;
- `pafe_claude.md`;
- `pafe_gpt.md`;
- `pafe_governanca_overlays.md`.
