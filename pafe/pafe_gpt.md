# /pafe — Overlay GPT

**Versão:** 1.4  
**Data:** 2026-08-19  
**Escopo:** ChatGPT/GPT com ferramentas de execução, conectores de arquivos e acesso autorizado ao GitHub.  
**Estado:** canônico sanitizado

## 1. Regra de ouro

GPT não deve confundir bloqueio de rede do sandbox da conversa com impossibilidade absoluta de gerar MP3 neural.

Quando a síntese direta falhar por DNS, rede ou egress bloqueado, verificar e executar a próxima rota realmente disponível e autorizada antes de declarar indisponibilidade.

Também é proibido confundir Secret configurado com provedor operacional. Para APIs pagas, consultar `audio_api_paga.md` e aplicar os gates de autenticação, endpoint, saldo/cota, smoke test e voz elegível.

É proibido substituir MP3 neural por Piper não autorizado, eSpeak, pyttsx3, Festival, gTTS robótico, voz metálica, `speechSynthesis`, voz nativa do navegador ou HTML com audiobook simulado.

## 2. Fontes obrigatórias para áudio

Antes de uma rota de áudio material, ler:

```text
pafe/README.md
pafe/audio_modos.md
pafe/audio.md
pafe/audio_api_paga.md
pafe/audio_capacidades_plataformas.md
pafe/VOICE_REGISTRY.json
pafe/audio_perfil_fabio.md
pafe/pafe_governanca_overlays.md
pafe/pafe_gpt.md
```

Se houver override temporário vigente, lê-lo também.

Não depender de memória para saber se ElevenLabs, Hume, Fish ou outro provedor está configurado.

## 3. Rota GitHub Actions

Quando a rota estiver disponível e autorizada:

1. resolver o provedor e o pool de vozes a partir das fontes vigentes;
2. testar a síntese direta no ambiente atual quando houver execução e isso for útil;
3. classificar a falha como DNS/rede/egress, SSL, endpoint, autenticação, cota/rate limit, saldo/crédito, payload/contrato ou voz/modelo;
4. preferir workflow persistente já governado quando ele existir e estiver correto;
5. usar branch/workflow temporários apenas para experimento, diagnóstico ou quando não existir rota persistente adequada;
6. nunca tornar repositório público apenas para obter execução ou Secret;
7. usar runner compatível, FFmpeg e FFprobe quando necessário;
8. descobrir/listar vozes realmente disponíveis no provedor quando o catálogo for dinâmico;
9. gerar um MP3 independente por assunto, com uma ou várias vozes elegíveis conforme papéis/segmentos e a política de diversidade de `audio.md`;
10. validar cada MP3 com `ffprobe` e as regras de `audio.md`;
11. quando houver múltiplas vozes, preservar mapeamento auditável entre segmento/papel e voz usada;
12. publicar os MP3s como artifact do GitHub Actions quando essa for a superfície de transporte;
13. confirmar a conclusão real do workflow;
14. baixar o artifact para a conversa quando a plataforma permitir;
15. descompactar e disponibilizar MP3s individuais quando a superfície permitir;
16. conferir quantidade de arquivos, duração e integridade;
17. fechar PR temporário sem merge e excluir branch temporária quando a ferramenta disponível permitir e isso não causar perda de evidência necessária.

## 4. Autorização

1. GitHub Actions, branches, commits e pull requests são escrita externa.
2. Usar essa rota somente quando houver autorização na instrução atual ou em fonte privada governante efetivamente acessível.
3. Se existir autorização persistente documentada, reutilizá-la apenas dentro dos limites registrados; não republicar sua redação, identidade ou detalhes privados no GitHub público.
4. Na ausência de autorização documentada, seguir a regra geral de `pafe_governanca_overlays.md`.
5. Autorização para uma rota não implica autorização para force push, exclusão destrutiva, exposição de segredo ou publicação de conteúdo sensível.
6. Conteúdo sensível não deve ser processado em repositório público apenas por conveniência operacional.
7. Não pedir novamente API key em chat quando o registry operacional indicar Secret configurado e a rota privada puder testá-lo sem revelar valor.

## 5. Configuração técnica mínima

1. A escolha do motor/provedor não é fixa; aplicar `audio_modos.md` + `audio_api_paga.md` + registries de voz.
2. `edge-tts` continua rota neural gratuita compatível quando selecionada e disponível.
3. Para provedores premium, usar os contratos atuais persistidos no worker privado e validar com smoke test antes de texto longo.
4. Runner GitHub: `ubuntu-latest` ou versão compatível.
5. FFmpeg e FFprobe: obrigatórios quando houver pós-processamento/validação.
6. Saída: MP3; processamento final conforme `audio.md`.
7. Um arquivo por assunto.
8. Um arquivo pode conter uma ou várias vozes elegíveis; diversidade é permitida dentro do arquivo quando estruturada por papel/segmento e desejada no conjunto de arquivos.
9. Nenhum `master_audio.mp3` por padrão.
10. Nenhum loop, silêncio artificial ou duplicação para inflar duração.
11. O HTML, quando também solicitado, permanece separado e sem player, `<audio>`, `speechSynthesis` ou referência a `.mp3`.

## 6. Provedores premium confirmados na arquitetura

O estado atual deve ser lido de `audio_api_paga.md`; este bloco é apenas um índice:

```text
ELEVENLABS → ELEVENLABS_API_KEY
HUME       → HUME_API_KEY [+ HUME_SECRET_KEY para token, quando necessário]
FISH       → FISH_AUDIO_API_KEY
```

Os valores nunca são lidos, escritos ou reproduzidos pela documentação.

Uma falha atual de Hume/Fish não autoriza apagá-los do catálogo nem reclassificá-los como “nunca configurados”. Preservar a causa exata observada e revalidar futuramente.

## 7. Vozes

Antes de gerar, aplicar:

```text
VOICE_REGISTRY.json
→ ranking permanente, bans, velocidade

VOICE_PRIORITY_OVERRIDE_2026-08.json
→ prioridade temporária, se vigente

audio_api_paga.md
→ disponibilidade do provedor
```

Estados: `PREFERRED`, `APPROVED`, `AVAILABLE`, `CANDIDATE`, `REJECTED_TEMP`, `LAST_RESORT`, `BANNED_BY_USER`.

Selecionar somente vozes elegíveis em provedores que passaram o preflight. Aprovação histórica da voz não torna o provedor disponível no presente.

A rotação pode ocorrer entre assuntos e dentro do mesmo assunto por personagem, papel ou segmento semanticamente distinto. Em um lote, evitar repetir a mesma voz em todos os arquivos quando houver alternativas elegíveis adequadas. Vozes temporariamente disponíveis podem ser priorizadas em conteúdo novo enquanto a janela estiver aberta, sem superar bans, qualidade ou preflight. Não ressintetizar MP3 já válido apenas para cumprir rotação ou aproveitar voz nova. Não inventar nome de voz nem declarar voz utilizada sem verificar a execução/arquivo.

## 8. Validação bloqueante

Para cada MP3, verificar:
- existência física;
- tamanho maior que zero;
- codec;
- duração;
- voz ou vozes neurais selecionadas conforme política;
- provedor(es) efetivamente usado(s) e aprovado(s) no smoke test;
- quando multivoz, correspondência entre papel/segmento e voz prevista;
- início e final sem truncamento;
- ausência de loop e silêncio artificial;
- correspondência entre assunto, nome e conteúdo.

A execução só pode ser declarada concluída quando o caminho utilizado tiver terminado com sucesso, os arquivos físicos existirem e a quantidade de MP3s corresponder à quantidade de assuntos.

## 9. Entrega

1. MP3s individuais são a entrega primária quando a superfície suportar múltiplos arquivos.
2. ZIP pode ser oferecido adicionalmente como conveniência.
3. Quando GitHub Actions transportar o artifact como ZIP, isso é mecanismo de transporte, não obrigação de produto final.
4. Se a plataforma permitir, baixar/descompactar e expor cada MP3 individualmente.

## 10. Falha fechada e continuação

Se um provedor falhar:

```text
registrar causa precisa
→ REJECTED_TEMP naquela execução
→ preservar evidência histórica anterior
→ tentar próxima rota autorizada e elegível
```

Se nenhuma rota neural disponível e autorizada puder concluir a tarefa:

`BLOQUEADO — requisito obrigatório não pôde ser validado; nenhum fallback inferior foi utilizado.`

Não entregar voz robótica, `speechSynthesis` ou HTML narrador como substituto. Não declarar MP3 gerado sem arquivo físico validado.

## 11. Precedência

- `html.md` governa o HTML;
- `audio_modos.md` governa a escolha da rota;
- `audio_api_paga.md` governa o registry operacional de provedores/Secrets lógicos;
- `audio.md` governa síntese e validação;
- `VOICE_REGISTRY.json` e override vigente governam seleção/preferência de voz;
- `audio_capacidades_plataformas.md` governa a matriz de execução por plataforma;
- `pafe_governanca_overlays.md` governa autorização e sincronização;
- este arquivo amplia a capacidade operacional do GPT sem armazenar autorização privada ou segredo.
