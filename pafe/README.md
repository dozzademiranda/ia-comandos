COMANDO: /pafe

ARQUIVO: pafe/README.md
VERSÃO: 2026-07-17.3
STATUS: canônico

O QUE É

Fluxo de estudo com artefatos opcionais e roteamento por capacidade real.

INVOCAÇÕES

1. `/pafe` — estudo sem artefatos por padrão.
2. `/pafe completo` — inclui artefatos quando pedidos e possíveis.
3. `/pafe html` — aplicar `html.md`.
4. `/pafe audio` — aplicar primeiro `audio_modos.md`.
5. `/pafe html audio` e `/pafe audio html` — equivalentes.
6. `/pafe audio local` ou `/pafe audio script` — script local mínimo.
7. `/pafe audio pacote` — pacote técnico completo.
8. `/pafe menu` — menu apenas quando houver múltiplas rotas reais, custo, escrita externa ou incerteza relevante.

REGRA DE HTML

`/pafe html` gera exatamente um HTML autocontido, offline, acessível, responsivo, sem áudio, sem player, sem impressão e sem arquivos auxiliares.

REGRA DE ÁUDIO

1. Áudio significa MP3 real por assunto.
2. Um assunto principal gera um MP3 independente.
3. `master_audio.mp3` é proibido por padrão.
4. Se um assunto exceder limite técnico, usar partes numeradas.
5. Falha em um assunto não invalida os demais.
6. A exclusão de um MP3 estudado é comportamento normal.
7. Regeneração seletiva deve existir por `--only`.

COMANDO COMBINADO

`/pafe html audio` e `/pafe audio html` geram:

1. um HTML independente, sem qualquer áudio, player ou referência a MP3;
2. N MP3 independentes, um por assunto;
3. nenhum master unificado;
4. nenhum ZIP, YAML, manifesto, TXT ou pacote técnico por padrão.

ROTEAMENTO

Ordem obrigatória:

1. MP3 neural direto;
2. script local mínimo automático;
3. pacote local completo, somente sob pedido;
4. GitHub Actions/Codespaces, somente se local indisponível ou pedido;
5. API paga, somente com autorização.

Quando a síntese direta falhar e o ambiente Linux local conhecido for compatível, gerar imediatamente o script local mínimo. Não pedir nova autorização, não exigir outro comando e não apresentar GitHub como única rota.

AUTORIZAÇÃO

O pedido para “gerar os arquivos” já autoriza criar artefatos para download nesta conversa.

Autorização adicional só é necessária para escrita externa, API paga, envio sensível a terceiro ou ação destrutiva.

CONFIABILIDADE

1. Não fingir MP3.
2. Não usar eSpeak, eSpeak-NG, MBROLA, pyttsx3, Festival ou gTTS robótico.
3. Não declarar conformidade sem validação.
4. Existência do arquivo não equivale a conformidade.
5. Em falha bloqueante: `BLOQUEADO — requisito obrigatório não pôde ser validado; nenhum fallback inferior foi utilizado.`
