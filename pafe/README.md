COMANDO: /pafe

ARQUIVO: pafe/README.md
VERSÃO: 2026-08-14.1
STATUS: canônico sanitizado

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

`/pafe html` gera exatamente um HTML autocontido, offline, acessível, responsivo, sem áudio, sem player, sem `speechSynthesis`, sem impressão e sem arquivos auxiliares.

HTML ou TTS nativo do navegador nunca substituem MP3 real quando áudio foi solicitado.

REGRA DE ÁUDIO

1. Áudio significa MP3 neural real por assunto.
2. Um assunto principal gera um MP3 independente.
3. Cada MP3 usa uma única voz; não alternar vozes dentro do mesmo assunto apenas por variedade.
4. `master_audio.mp3` é proibido por padrão.
5. Se um assunto exceder limite técnico, usar partes numeradas.
6. Falha em um assunto não invalida os demais.
7. A exclusão de um MP3 estudado é comportamento normal.
8. Regeneração seletiva deve existir por `--only` quando houver script local.
9. A voz deve ser descoberta/testada na rota real; Antonio e Francisca são `LAST_RESORT`, não padrão.
10. Cache/hash de MP3 válido prevalece sobre ressintetização apenas para cumprir rotação.

COMANDO COMBINADO

`/pafe html audio` e `/pafe audio html` geram:

1. um HTML independente, sem áudio, player, `speechSynthesis` ou referência a MP3;
2. N MP3 independentes, um por assunto;
3. nenhum master unificado;
4. MP3s individuais como entrega primária quando a superfície suportar;
5. ZIP opcional como conveniência adicional ou transporte técnico obrigatório de um provedor.

ROTEAMENTO

Ordem geral:

1. MP3 neural direto;
2. script local mínimo automático quando a máquina local puder efetivamente executar;
3. GitHub Actions/Codespaces quando a execução direta ou local não puder ser concluída pela conversa e houver autorização aplicável;
4. pacote local completo, somente sob pedido;
5. API paga, somente com autorização.

Falha de DNS/rede/egress no sandbox encerra somente a rota direta. Não declarar impossibilidade global enquanto houver rota neural autorizada capaz de concluir.

Para Claude com execução ativa, aplicar `pafe_claude.md`.

Para ChatGPT/GPT com acesso ao GitHub, aplicar `pafe_gpt.md`. Se o sandbox direto falhar e uma rota remota autorizada estiver disponível, não encerrar apenas com diagnóstico: aplicar a rota governada e entregar o artefato validado.

OVERLAYS DE PLATAFORMA

1. `pafe_claude.md` — Claude com bash, rede, arquivos e entrega de binários.
2. `pafe_gpt.md` — ChatGPT/GPT com conectores e rota GitHub Actions.
3. Overlays ampliam capacidades, mas não afastam `html.md`, `audio_modos.md`, `audio.md` ou `pafe_governanca_overlays.md`.
4. `pafe_prompt_outras_ias.md` — instrução mínima para outras plataformas.

AUTORIZAÇÃO

1. O pedido para gerar artefatos já autoriza criar arquivos para download dentro da conversa.
2. Escrita externa e rotas remotas são governadas por `pafe_governanca_overlays.md` e pela instrução atual do usuário.
3. Se existir autorização persistente documentada em fonte privada governante ou no contexto atual, reutilizá-la estritamente dentro de seus limites; não copiá-la para repositório público.
4. Na ausência de autorização documentada, não presumir permissão para escrita externa.
5. Merge em ramo principal, API paga, envio de conteúdo sensível a terceiro e alteração destrutiva não são presumidos como autorizados.

ENTREGA

1. Quando possível, disponibilizar MP3s individualmente.
2. ZIP pode ser oferecido adicionalmente como conveniência.
3. Artifact ZIP de GitHub Actions é transporte técnico; quando a superfície permitir, descompactar e disponibilizar os MP3s individuais.
4. Não substituir MP3 solicitado por HTML narrador, `speechSynthesis` ou voz do navegador.

ARQUIVAMENTO

Arquivos dentro de `archive/` são históricos e nunca prevalecem sobre os arquivos ativos deste diretório.

CONFIABILIDADE

1. Não fingir MP3.
2. Não usar eSpeak, eSpeak-NG, MBROLA, pyttsx3, Festival, Piper não autorizado, gTTS robótico ou TTS de navegador como substituto.
3. Não declarar conformidade sem validação.
4. Existência do arquivo não equivale a conformidade.
5. Em falha bloqueante: `BLOQUEADO — requisito obrigatório não pôde ser validado; nenhum fallback inferior foi utilizado.`