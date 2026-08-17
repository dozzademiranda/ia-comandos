# audio_api_paga.md — Registro operacional de provedores TTS

**Versão:** v1.0.1  
**Data:** 2026-08-17  
**Status:** ativo  
**Escopo:** disponibilidade operacional de provedores TTS e localização lógica de Secrets.  
**Não contém valores de credenciais.**

## 1. Regra central

Este arquivo responde: **quais provedores existem, qual Secret lógico usam, onde a execução autorizada está preparada e qual é o último estado operacional conhecido**.

Ele NÃO decide sozinho qual voz usar. Preferências, ranking e bans pertencem a `VOICE_REGISTRY.json` e, quando vigente, a `VOICE_PRIORITY_OVERRIDE_2026-08.json`.

Ele NÃO substitui preflight. Estado persistido pode envelhecer; disponibilidade atual exige validação do runtime antes de consumir texto longo ou crédito relevante.

## 2. Segurança

1. Nunca registrar valor de API key, token, Secret ou credencial neste repositório.
2. Nunca pedir ao usuário para colar chave no chat quando já existir rota por Secret.
3. Secrets operacionais conhecidos nesta arquitetura residem como GitHub Actions Secrets no repositório privado `dozzademiranda/ias-state`.
4. Um Secret existir não prova que autenticação, cota, saldo, endpoint ou TTS estejam operacionais.
5. Não tornar repositório público para obter acesso a Secret ou para processar conteúdo sensível.

## 3. Matriz operacional

| Provedor | Secret lógico | Execução preparada | Estado atual confirmado | Uso |
|---|---|---|---|---|
| Microsoft Edge / `edge-tts` | nenhum | rotas locais/GitHub compatíveis | `AVAILABLE_TESTED` conforme `VOICE_REGISTRY.json`; catálogo deve ser redescoberto no runtime | gratuito/fallback neural |
| ElevenLabs | `ELEVENLABS_API_KEY` | `dozzademiranda/ias-state` → `.github/workflows/elevenlabs-dispatch.yml` | `AUTHENTICATED_AND_TTS_VALIDATED` no histórico operacional de 2026-08-17 preservado em `VOICE_REGISTRY.json` | premium elegível quando voz/conta passarem preflight |
| Hume AI / Octave | `HUME_API_KEY`; `HUME_SECRET_KEY` apenas para token OAuth quando necessário | worker persistente existe, mas precisa reconciliação | `AUTH_AND_VOICE_LISTING_PASS__TTS_BLOCKED_PAYLOAD_PARSE`: API key listou 160 vozes HUME_AI; filtro masculino retornou 97; CUSTOM_VOICE retornou 0; OAuth token retornou HTTP 200; TTS `/v0/tts/file` e `/v0/tts` retornaram HTTP 400 `E0101 payload_parse` nos testes de 2026-08-17 | não elegível para produção até novo TTS E2E HTTP 200 |
| Fish Audio | `FISH_AUDIO_API_KEY` | worker persistente existe, mas usa contrato legado e precisa reconciliação | `CONFIGURED_BUT_API_CREDIT_BLOCKED`: houve TTS PT-BR anterior bem-sucedido em 2026-08-17 com Capitão Nascimento; preflight posterior pelo contrato atual retornou HTTP 402 `Insufficient API credit` | não elegível enquanto o preflight continuar 402 |
| Azure AI Speech / Microsoft Speech API | credencial própria se configurada | não confirmada nesta rodada | `HISTORICAL_REFERENCE__CURRENT_SECRET_NOT_VERIFIED_THIS_RUN` | capacidade distinta de `edge-tts`; não presumir disponibilidade |

## 4. Fish Audio — regra atual

O contrato HTTP atual da rota é:

```text
POST https://api.fish.audio/v1/tts
Authorization: Bearer <FISH_AUDIO_API_KEY>
header model: s2-pro
body reference_id: <voice/model id>
```

`voice_id` no corpo e campo `language` não são tratados como equivalentes ao contrato atual da rota. O identificador de voz/modelo deve ser enviado como `reference_id`.

**Atenção:** o arquivo persistente `dozzademiranda/ias-state/.github/workflows/scripts/fish_synth.js` ainda estava usando o contrato legado `voice_id`/`language` na auditoria de 2026-08-17. A tentativa de substituição direta desse worker a partir desta execução foi bloqueada pela camada de segurança da ferramenta por o arquivo operacional referenciar Secrets. O delta pendente foi registrado em `dozzademiranda/ias-state` issue `#1`; não declarar o worker persistente como corrigido até readback de commit posterior.

A política temporária `FISH_FIRST` só se aplica quando o provedor estiver **runtime-available**. Erro de crédito/cota/autenticação retira Fish da elegibilidade daquela execução e o roteamento continua para a próxima rota autorizada.

### Capitão Nascimento

Referência comunitária usada no teste:

```text
reference_id: 102bccca7dc64b6b8f8494c199c5d153
```

Estado:

```text
VOICE: APPROVED_FOR_USE_RANK_PENDING
HISTORICAL_PTBR_TTS: PASS — 2026-08-17 — ~9.3 s
CURRENT_PROVIDER_RUNTIME: BLOCKED — HTTP 402 API CREDIT
```

O nome identifica um modelo comunitário da Fish; não representa afirmação de licença oficial, identidade do ator ou endosso do personagem.

## 5. Hume AI — regra atual

Autenticação confirmada:

```text
X-Hume-Api-Key: <HUME_API_KEY>
```

Token OAuth também foi confirmado sem expor credenciais:

```text
POST /oauth2-cc/token
Basic HUME_API_KEY:HUME_SECRET_KEY
→ HTTP 200 em 2026-08-17
```

Descoberta confirmada em 2026-08-17:

```text
HUME_AI total: 160
HUME_AI com tag GENDER:Male: 97
CUSTOM_VOICE: 0
```

Entretanto, o TTS REST não passou no E2E desta rodada:

```text
POST /v0/tts/file
→ HTTP 400
→ code E0101 / payload_parse

POST /v0/tts
version: "2"
voice id explícita
instant_mode: false
→ HTTP 400
→ code E0101 / payload_parse
```

O erro persistiu com payloads alinhados à documentação oficial. Classificar como **TTS_BLOCKED_PENDING_REVALIDATION**, não como chave ausente ou inválida.

**Atenção:** os workers persistentes `hume_synth_simple.js`, `hume_synth_token.js` e a orquestração de `hume-synth.yml` também precisam reconciliação. O workflow atual reutiliza uma camada de fallback multi-provider que pode transportar um mesmo `VOICE_ID` entre provedores incompatíveis. O delta está registrado na issue `dozzademiranda/ias-state#1`.

Artefatos de auditoria preservados no GitHub Actions:

```text
run 32011571653 / artifact 9281954656 — catálogo Hume e diagnósticos
run 32029850349 / artifact 9288464910 — TTS mínimo Hume file, HTTP 400
run 32030363531 / artifact 9288648083 — TTS JSON Octave 2 com voice explícita, HTTP 400
```

## 6. Regra de elegibilidade do provedor

Antes de texto longo:

```text
provider_eligible = SECRET/NO_SECRET_OK
                    ∩ AUTH_OK
                    ∩ ENDPOINT_OK
                    ∩ QUOTA_OR_CREDIT_OK
                    ∩ TTS_SMOKE_TEST_OK
                    ∩ VOICE_ELIGIBLE
```

Falhar em qualquer gate significa `REJECTED_TEMP` para aquela rota/execução, sem apagar evidência histórica de testes anteriores.

## 7. Precedência

- `audio_modos.md` decide a rota;
- este arquivo informa estado/capacidade dos provedores pagos;
- `audio.md` governa síntese, processamento e validação;
- `VOICE_REGISTRY.json` governa ranking/perfil/bans permanentes;
- `VOICE_PRIORITY_OVERRIDE_2026-08.json` governa a prioridade temporária Fish enquanto estiver vigente, sempre condicionada ao preflight;
- `audio_capacidades_plataformas.md` descreve onde cada rota pode ser executada;
- `pafe_governanca_overlays.md` governa autorização para escrita/execução externa.
