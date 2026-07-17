# /pafe — Overlay GPT

**Versão:** 1.0  
**Data:** 2026-07-17  
**Escopo:** ChatGPT/GPT com ferramentas de execução, conectores de arquivos e acesso autorizado ao GitHub.

## 1. Regra de ouro

GPT não deve confundir bloqueio de rede do sandbox da conversa com impossibilidade absoluta de gerar MP3 neural.

Quando a síntese direta com `edge-tts` falhar por DNS, rede ou egress bloqueado, e houver conector GitHub com permissão de escrita, aplicar a rota GitHub Actions descrita neste overlay antes de declarar indisponibilidade.

É proibido substituir a voz neural por Piper, eSpeak, pyttsx3, Festival, gTTS robótico ou outro fallback metálico.

## 2. Rota GPT validada — GitHub Actions

A sequência operacional é:

1. ler `README.md`, `audio_modos.md`, `audio.md`, `pafe_governanca_overlays.md` e este overlay;
2. testar a síntese direta no ambiente atual;
3. classificar a falha como DNS/rede, SSL, endpoint ou autenticação/cota;
4. se a síntese direta falhar e a rota GitHub estiver disponível, criar branch temporária a partir de `main`;
5. adicionar somente workflow, script e textos estritamente necessários em diretório temporário;
6. abrir pull request temporário apenas para disparar workflow por `pull_request`;
7. nunca mesclar o pull request temporário;
8. usar runner `ubuntu-latest`, Python, FFmpeg, FFprobe e `edge-tts`;
9. gerar um MP3 independente por assunto;
10. validar cada MP3 com `ffprobe`;
11. publicar os MP3 como artifact do GitHub Actions;
12. aguardar conclusão real do workflow;
13. baixar o artifact para a conversa;
14. conferir quantidade de arquivos, duração total, integridade e manifesto;
15. fechar o pull request sem merge;
16. excluir a branch temporária quando a ferramenta disponível permitir.

## 3. Autorização permanente de Fábio

Fábio Dozza de Miranda autorizou permanentemente o ChatGPT/GPT a usar GitHub Actions e branches temporárias no repositório `dozzademiranda/ia-comandos` para gerar áudios P.A.F.E., sem solicitar nova autorização em cada execução.

Essa autorização cobre:

- criação de branch temporária;
- criação de workflow temporário;
- commits temporários na branch;
- abertura de pull request apenas para disparar o workflow;
- execução do GitHub Actions;
- download do artifact;
- fechamento do pull request sem merge.

A autorização não cobre:

- merge no ramo `main`;
- force push;
- exclusão de arquivos permanentes;
- alteração de conteúdo não relacionado ao P.A.F.E.;
- uso de API paga;
- uso, exposição ou solicitação de chaves e segredos;
- publicação de material sigiloso, dados pessoais sensíveis ou documentos jurídicos protegidos em repositório público;
- alteração destrutiva fora da branch temporária.

Se o conteúdo for sensível e não houver repositório privado autorizado, a rota pública deve ser bloqueada.

## 4. Configuração técnica mínima

1. Motor: `edge-tts`.
2. Runner: `ubuntu-latest`.
3. Python: versão estável compatível, preferencialmente 3.12.
4. FFmpeg e FFprobe: obrigatórios.
5. Ritmo recomendado: entre `-10%` e `-12%`.
6. Saída: MP3, preferencialmente 128 kbps e mono após normalização.
7. Um arquivo por assunto.
8. Nenhum `master_audio.mp3` por padrão.
9. Nenhum loop, silêncio artificial ou duplicação para inflar duração.
10. O HTML, quando também solicitado, permanece separado e sem player, `<audio>` ou referência a `.mp3`.

## 5. Vozes

Antes de gerar, listar ou testar as vozes pt-BR disponíveis no ambiente real do runner.

Priorizar, quando efetivamente disponíveis:

- `pt-BR-AntonioNeural`;
- `pt-BR-FranciscaNeural`;
- `pt-BR-ThalitaNeural` ou o nome exato equivalente retornado pelo serviço.

Não inventar nome de voz. Não declarar múltiplas vozes sem verificar os arquivos realmente gerados.

## 6. Validação bloqueante

Para cada MP3, verificar:

- existência física;
- tamanho maior que zero;
- codec;
- duração;
- bitrate;
- frequência;
- canais;
- início e final sem truncamento;
- ausência de loop e silêncio artificial;
- correspondência entre assunto, nome e conteúdo.

A execução só pode ser declarada concluída quando:

1. o workflow terminar com `success`;
2. o artifact existir;
3. o artifact for baixado;
4. a quantidade de MP3s corresponder à quantidade de assuntos;
5. a validação técnica estiver registrada.

## 7. Precedente técnico validado

Em 17/07/2026, o GPT-5.6 Thinking executou com sucesso esta rota no repositório `dozzademiranda/ia-comandos`:

- branch temporária: `pafe-criminologia-p2-audios-20260717`;
- workflow: `PAFE Criminologia P2 - Gerar 20 MP3`;
- run: `29565980504`;
- resultado: `success`;
- artifact: `CHATGPT_GPT56_CRIMINOLOGIA_P2_20_AUDIOS_v1.0_20260717`;
- quantidade: 20 MP3;
- duração total validada: 84 minutos e 6 segundos;
- vozes neurais: Antonio, Francisca e Thalita;
- fallback robótico: não utilizado;
- pull request: fechado sem merge;
- ramo principal: não alterado.

Esse precedente comprova a viabilidade da rota. Não dispensa novo preflight em cada execução.

## 8. Falha fechada

Se a síntese direta falhar e GitHub Actions não estiver disponível ou for inadequado ao conteúdo:

`BLOQUEADO — requisito obrigatório não pôde ser validado; nenhum fallback inferior foi utilizado.`

Não entregar Piper ou voz robótica. Não declarar MP3 gerado sem artifact físico baixado.

## 9. Precedência

- `html.md` governa o HTML;
- `audio_modos.md` governa a escolha da rota;
- `audio.md` governa síntese e validação;
- `pafe_governanca_overlays.md` governa autorização e sincronização;
- este arquivo amplia a capacidade operacional do GPT e registra a autorização permanente para GitHub Actions.
