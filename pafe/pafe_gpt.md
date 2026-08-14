# /pafe — Overlay GPT

**Versão:** 1.2  
**Data:** 2026-08-14  
**Escopo:** ChatGPT/GPT com ferramentas de execução, conectores de arquivos e acesso autorizado ao GitHub.  
**Estado:** canônico sanitizado

## 1. Regra de ouro

GPT não deve confundir bloqueio de rede do sandbox da conversa com impossibilidade absoluta de gerar MP3 neural.

Quando a síntese direta falhar por DNS, rede ou egress bloqueado, verificar e executar a próxima rota realmente disponível e autorizada antes de declarar indisponibilidade.

É proibido substituir MP3 neural por Piper não autorizado, eSpeak, pyttsx3, Festival, gTTS robótico, voz metálica, `speechSynthesis`, voz nativa do navegador ou HTML com audiobook simulado.

## 2. Rota GitHub Actions

Quando a rota estiver disponível e autorizada:

1. ler `README.md`, `audio_modos.md`, `audio.md`, `pafe_governanca_overlays.md` e este overlay;
2. testar a síntese direta no ambiente atual quando houver execução;
3. classificar a falha como DNS/rede/egress, SSL, endpoint ou autenticação/cota;
4. criar branch temporária a partir de `main`;
5. adicionar somente workflow, script e textos estritamente necessários em diretório temporário;
6. abrir pull request temporário apenas quando necessário para disparar o workflow;
7. nunca mesclar o pull request temporário;
8. usar runner `ubuntu-latest`, Python, FFmpeg, FFprobe e motor neural compatível com a rota;
9. descobrir/listar vozes pt-BR realmente disponíveis no runner antes da seleção;
10. gerar um MP3 independente por assunto, usando uma única voz por arquivo;
11. validar cada MP3 com `ffprobe` e as regras de `audio.md`;
12. publicar os MP3s como artifact do GitHub Actions;
13. confirmar a conclusão real do workflow;
14. baixar o artifact para a conversa quando a plataforma permitir;
15. descompactar e disponibilizar MP3s individuais quando a superfície permitir;
16. conferir quantidade de arquivos, duração e integridade;
17. fechar o pull request sem merge;
18. excluir a branch temporária quando a ferramenta disponível permitir.

## 3. Autorização

1. GitHub Actions, branches, commits e pull requests são escrita externa.
2. Usar essa rota somente quando houver autorização na instrução atual ou em fonte privada governante efetivamente acessível.
3. Se existir autorização persistente documentada, reutilizá-la apenas dentro dos limites registrados; não republicar sua redação, identidade ou detalhes privados no GitHub público.
4. Na ausência de autorização documentada, seguir a regra geral de `pafe_governanca_overlays.md`.
5. Autorização para uma rota não implica autorização para merge em `main`, force push, alteração permanente não relacionada, exclusão destrutiva, API paga, exposição de segredo ou publicação de conteúdo sensível.
6. Conteúdo sensível não deve ser processado em repositório público apenas por conveniência operacional.

## 4. Configuração técnica mínima

1. Motor gratuito preferencial: `edge-tts`, quando disponível na rota.
2. Runner: `ubuntu-latest`.
3. Python: versão estável compatível, preferencialmente 3.12.
4. FFmpeg e FFprobe: obrigatórios.
5. Ritmo recomendado: entre `-10%` e `-12%`, salvo preferência diferente do usuário.
6. Saída: MP3, preferencialmente 128 kbps e mono após normalização.
7. Um arquivo por assunto.
8. Uma única voz por arquivo.
9. Nenhum `master_audio.mp3` por padrão.
10. Nenhum loop, silêncio artificial ou duplicação para inflar duração.
11. O HTML, quando também solicitado, permanece separado e sem player, `<audio>`, `speechSynthesis` ou referência a `.mp3`.

## 5. Vozes

Antes de gerar, listar/testar as vozes pt-BR disponíveis no ambiente real do runner.

Estados: `PREFERRED`, `APPROVED`, `AVAILABLE`, `CANDIDATE`, `REJECTED_TEMP`, `LAST_RESORT`.

Selecionar de `APPROVED ∩ AVAILABLE`, excluindo `LAST_RESORT`. Se ainda não houver voz aprovada disponível, testar candidatas reais e registrar o resultado sem inventar disponibilidade.

Regras atuais:
- `pt-BR-AntonioNeural` = `LAST_RESORT`;
- `pt-BR-FranciscaNeural` = `LAST_RESORT`;
- `pt-BR-LeticiaNeural` ou nome equivalente retornado pelo serviço pode ser `CANDIDATE`;
- outras vozes pt-BR devem ser descobertas/testadas no runner.

Entre assuntos, rotação pode ocorrer somente entre vozes elegíveis. Não ressintetizar MP3 já válido apenas para cumprir rotação. Não inventar nome de voz nem declarar voz utilizada sem verificar a execução/arquivo.

## 6. Validação bloqueante

Para cada MP3, verificar:
- existência física;
- tamanho maior que zero;
- codec;
- duração;
- bitrate;
- frequência;
- canais;
- voz neural selecionada conforme política;
- início e final sem truncamento;
- ausência de loop e silêncio artificial;
- correspondência entre assunto, nome e conteúdo.

A execução só pode ser declarada concluída quando o caminho utilizado tiver terminado com sucesso, os arquivos físicos existirem e a quantidade de MP3s corresponder à quantidade de assuntos.

## 7. Entrega

1. MP3s individuais são a entrega primária quando a superfície suportar múltiplos arquivos.
2. ZIP pode ser oferecido adicionalmente como conveniência.
3. Quando GitHub Actions transportar o artifact como ZIP, isso é mecanismo de transporte, não obrigação de produto final.
4. Se a plataforma permitir, baixar/descompactar e expor cada MP3 individualmente.

## 8. Precedente técnico

A rota GitHub Actions já demonstrou viabilidade operacional em execução anterior validada. Esse precedente comprova apenas viabilidade técnica; não substitui preflight atual nem autorização aplicável.

Detalhes históricos ou privados de execuções anteriores não pertencem ao repositório público corrente.

## 9. Falha fechada

Se nenhuma rota neural disponível e autorizada puder concluir a tarefa:

`BLOQUEADO — requisito obrigatório não pôde ser validado; nenhum fallback inferior foi utilizado.`

Não entregar voz robótica, `speechSynthesis` ou HTML narrador como substituto. Não declarar MP3 gerado sem arquivo físico validado.

## 10. Precedência

- `html.md` governa o HTML;
- `audio_modos.md` governa a escolha da rota;
- `audio.md` governa síntese e validação;
- `pafe_governanca_overlays.md` governa autorização e sincronização;
- este arquivo amplia a capacidade operacional do GPT sem armazenar autorização privada.