# audio_perfil_fabio.md — Perfil operacional de voz P.A.F.E.

**Versão:** v1.1.0  
**Data:** 2026-08-19  
**Status:** ativo  
**Escopo:** critérios de seleção de voz e ponteiros para ranking/bans.

## 1. Fonte de verdade

Este arquivo é um perfil resumido. **Não duplica o ranking completo.**

Para a ordem atual, IDs, estados e níveis de velocidade, ler:

```text
pafe/VOICE_REGISTRY.json
```

Para prioridade temporária Fish em agosto de 2026, quando ainda vigente, ler também:

```text
pafe/VOICE_PRIORITY_OVERRIDE_2026-08.json
```

Se houver divergência, os registries estruturados prevalecem sobre exemplos deste arquivo.

## 2. Perfil-alvo

Preferência predominante para estudo longo:

```text
voz masculina madura/idosa
professoral
calorosa e bonachona
natural
clara
paciente
ligeiramente entusiasmada
confortável para conteúdo acadêmico longo
```

Evitar:

```text
monotonia
som robótico
grave excessivamente ameaçador
caricatura
locução publicitária
```

## 3. Regras de seleção

1. Preferência não substitui disponibilidade: a voz deve passar o preflight real do provedor.
2. Não usar voz banida nem como fallback.
3. Não ressintetizar arquivo válido apenas para cumprir rotação ou preferência de variedade.
4. Um MP3 pode usar uma ou várias vozes elegíveis; não existe regra geral de uma única voz por arquivo.
5. Em um conjunto de áudios, evitar repetir a mesma voz em todos os arquivos quando houver alternativas elegíveis adequadas. A diversidade entre arquivos é objetivo explícito.
6. Dentro do mesmo MP3, múltiplas vozes podem ser usadas por papel, personagem, pergunta/resposta, contraponto, bloco conceitual ou transição semântica. Evitar alternância aleatória apenas para aumentar variedade.
7. Quando houver personagem ou função cognitiva recorrente, manter voz estável quando isso ajudar reconhecimento; troca de voz exige motivo pedagógico, qualidade, indisponibilidade ou instrução aplicável.
8. Vozes aprovadas com janela de acesso temporária devem ser aproveitadas preferencialmente em conteúdo novo ou em regeneração já necessária enquanto estiverem disponíveis, sem superar bans, qualidade ou preflight.
9. Ajustes de velocidade são graduais e pertencem ao `VOICE_REGISTRY.json`; não inventar alteração de cadência sem feedback do usuário.
10. Distinguir vozes de mesmo nome em provedores diferentes; identidade nominal não implica equivalência.
11. Uma voz pode permanecer `APPROVED` enquanto o provedor está temporariamente indisponível. Nesse caso, a voz não é `AVAILABLE` naquela execução.

## 4. Bans permanentes atualmente registrados

Consultar a lista estruturada completa em `VOICE_REGISTRY.json`. Entre os bans já persistidos estão:

```text
Antonio
Francisca
Brian Multilingual (Edge)
Emma Multilingual (Edge)
```

O override Fish também contém um ban próprio persistente para `Friendly Mature`.

## 5. Fish temporário

Durante a vigência do override de agosto, as vozes Fish podem preceder o ranking permanente **somente se o provedor passar os gates de autenticação, crédito/cota e TTS smoke test**.

`Capitão Nascimento` foi aprovado para uso com rank comparativo ainda pendente, mas o último preflight de provedor registrado em 2026-08-17 retornou HTTP 402 por crédito de API. Portanto, aprovação da voz não equivale a disponibilidade atual do provedor.

## 6. Precedência

```text
VOICE_REGISTRY.json
→ ranking permanente, bans, perfil e velocidade

VOICE_PRIORITY_OVERRIDE_2026-08.json
→ override temporário vigente

audio_api_paga.md
→ disponibilidade real do provedor/Secret/endpoint

este arquivo
→ resumo legível do perfil
```
