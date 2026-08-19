# audio.md — Padrão técnico de áudio P.A.F.E.

**Versão:** v7.3 MASTER  
**Data:** 2026-08-19  
**Escopo:** técnica de síntese, processamento, validação e publicação.  
**Roteamento:** decidido por `audio_modos.md`.

## 1. Regra técnica central

1. Cada assunto principal produz um MP3 independente.
2. Um MP3 pode usar uma ou várias vozes neurais elegíveis. Não existe limite geral de uma voz por arquivo.
3. A finalidade da rotação é evitar que a mesma voz domine todos os áudios/arquivos e aproveitar diversidade real de vozes, inclusive dentro de um mesmo MP3 quando isso tiver função semântica ou pedagógica.
4. Dentro de um arquivo, múltiplas vozes são permitidas para personagens, papéis, perguntas/respostas, contrapontos, blocos conceituais ou transições semanticamente distintas. Evitar troca aleatória a cada frase apenas para criar variedade.
5. Em um lote de áudios, distribuir as vozes elegíveis de modo a reduzir repetição desnecessária antes de reutilizar a mesma voz, sem sacrificar adequação ao papel, inteligibilidade, qualidade ou preferência do usuário.
6. Vozes com janela de disponibilidade temporária devem ser aproveitadas preferencialmente em novas gerações ou em regenerações já necessárias enquanto estiverem runtime-eligible e aprovadas; disponibilidade temporária nunca supera bans, preflight, qualidade ou segurança.
7. Quando houver personagem ou função cognitiva recorrente, manter identidade vocal estável enquanto isso ajudar reconhecimento e aprendizagem; trocar apenas por decisão pedagógica, indisponibilidade, qualidade ou instrução aplicável.
8. MP3 já válido não deve ser ressintetizado apenas para cumprir variedade, rotação ou aproveitar uma voz nova/temporária; aplicar a política de diversidade prioritariamente a conteúdo novo ou a regeneração já necessária.
9. Não concatenar assuntos diferentes em `master_audio.mp3`.
10. Chunks são temporários internos de um assunto, não capítulos de um master.
11. Falha em um assunto não invalida os arquivos já aprovados.
12. Arquivo existente não equivale a arquivo conforme.
13. HTML, TTS do navegador e `speechSynthesis` não substituem MP3 real solicitado.
14. Estado de provedor pago pertence a `audio_api_paga.md`; perfil/ranking/bans pertencem aos registries estruturados. Não duplicar nem inferir disponibilidade a partir de memória.

## 2. Nomes

Padrão:

```text
01_INTRODUCAO_E_MAPA.mp3
02_PRIMEIRO_ASSUNTO.mp3
...
NN_REVISAO_FINAL.mp3
```

Sem acentos, caracteres problemáticos ou nomes genéricos.

## 3. Motor, provedor e voz

A rota é decidida por `audio_modos.md`. Quando houver API paga, consultar `audio_api_paga.md`; quando houver decisão de voz, consultar `VOICE_REGISTRY.json`, `audio_perfil_fabio.md` e eventual override temporário vigente.

Rota gratuita compatível quando selecionada:

```text
edge-tts
```

A voz não é fixa. Antes da síntese, descobrir/testar o catálogo realmente disponível na rota atual.

Estados operacionais:

```text
PREFERRED
APPROVED
AVAILABLE
CANDIDATE
REJECTED_TEMP
LAST_RESORT
BANNED_BY_USER
```

Elegibilidade:

```text
eligible = PREFERRED/APPROVED ∩ AVAILABLE \ LAST_RESORT \ BANNED_BY_USER
```

O `VOICE_REGISTRY.json` é a fonte estruturada do ranking permanente e bans. `VOICE_PRIORITY_OVERRIDE_2026-08.json`, enquanto vigente, pode alterar prioridade temporariamente, mas não converte provedor indisponível em disponível.

Quando houver várias vozes elegíveis, a seleção pode distribuir vozes entre assuntos e também dentro do mesmo assunto por segmentos/papéis semanticamente distintos. Em um conjunto de arquivos, evitar usar sempre a mesma voz quando houver alternativas elegíveis adequadas. Vozes temporariamente disponíveis podem receber prioridade de uso enquanto a janela estiver aberta, sem ultrapassar bans, qualidade ou preflight. Cache/hash de MP3 já válido prevalece sobre ressintetização apenas para cumprir rotação.

Proibido: eSpeak, eSpeak-NG, MBROLA, pyttsx3, Festival, gTTS robótico, voz metálica, motor não rastreável e `speechSynthesis` como substituto de MP3.

## 4. Preflight de provedor

Antes de síntese longa, validar conforme a rota:

```text
Secret ou ausência de Secret conforme esperado
→ autenticação
→ endpoint
→ saldo/cota
→ catálogo/voice ID/modelo
→ smoke test curto
→ ffprobe
→ produção
```

Falha deve ser classificada pela causa observada: rede/egress, TLS, autenticação, cota/rate limit, saldo/crédito, payload/contrato de API, voz/modelo ou processamento local.

Não transformar erro de payload, crédito ou cota em alegação de chave ausente/inválida.

## 5. Pipeline por assunto

```text
texto original
→ cópia falável
→ sanitização
→ correções fonéticas
→ divisão semântica
→ definição de papéis/segmentos
→ mapeamento de voz(es) elegível(is)
→ síntese neural por segmento
→ validação dos chunks
→ PCM WAV uniforme
→ pausas reais
→ concatenação apenas daquele assunto
→ loudnorm
→ fade
→ codificação MP3 única
→ ffprobe
→ publicação segura
```

Padrão intermediário: PCM 24 kHz, mono, 16-bit.

Loudness de estudo longo:

```text
I=-20 LUFS
TP=-1.5 dBTP
LRA=11
```

Quando houver múltiplas vozes no mesmo MP3, normalizar os segmentos para evitar saltos de loudness e preservar transições audíveis sem cortes abruptos.

## 6. Script local mínimo

O script padrão de contingência deve ser um único `.py` autossuficiente.

CLI obrigatória:

```bash
python3 gerar_audio.py --list
python3 gerar_audio.py
python3 gerar_audio.py --only 2 5
python3 gerar_audio.py --only 2 --force
```

Comportamento:

- sem argumento: gera somente arquivos ausentes;
- `--list`: lista assuntos e destinos;
- `--only`: gera apenas os números indicados;
- `--force`: permite sobrescrita intencional;
- arquivo válido existente é preservado por padrão;
- quando houver múltiplas vozes, o script deve preservar mapeamento determinístico entre papel/segmento e voz para permitir reprodução e auditoria;
- não usar `sudo`.

## 7. Pacote técnico completo

Somente sob pedido expresso. Pode conter YAML, roteiro externo, dicionário fonético, manifesto, logs, validação e partes.

O pacote também deve gerar N MP3s por assunto; nunca master único por padrão.

ZIP não é pacote obrigatório. Pode ser oferecido adicionalmente como conveniência ou ser usado como transporte técnico de um artifact remoto.

## 8. Retry e retomada

1. Dividir sem cortar frases.
2. Tentar cada chunk até três vezes quando a falha for retriável.
3. Usar espera progressiva para erros transitórios/rate limit.
4. Preservar chunks válidos.
5. Não reiniciar todos os assuntos por falha isolada.
6. Não ocultar `stderr`.
7. Verificar `returncode`/HTTP status.
8. Não repetir automaticamente erro não retriável de crédito, autorização ou payload sem alterar a condição causadora.

## 9. Publicação segura

1. gerar em temporário;
2. validar;
3. copiar para `.part` no diretório final;
4. `flush` e `fsync`;
5. `os.replace()` apenas no mesmo sistema de arquivos;
6. remover `.part` em falha;
7. nunca apagar outros MP3s válidos.

Entrega ao usuário:
- quando a superfície suportar, disponibilizar os MP3s individualmente;
- ZIP pode ser oferecido como conveniência adicional;
- quando o provedor remoto entregar somente artifact ZIP, baixar/descompactar e expor os MP3s individualmente quando tecnicamente possível.

## 10. Validação individual

Para cada MP3:

- existência;
- tamanho maior que zero;
- duração positiva;
- codec válido;
- voz ou vozes neurais autorizadas e efetivamente usadas;
- provedor(es) efetivamente usado(s) e runtime-eligible;
- quando multivoz, correspondência entre segmento/papel e voz planejada;
- quando multivoz, transições sem cortes abruptos ou desequilíbrio de loudness;
- início e final audíveis;
- ausência de truncamento;
- ausência de loop;
- ausência de silêncio para inflar duração;
- loudness;
- nome correto;
- correspondência entre assunto, texto e arquivo.

Validação global:

- quantidade de MP3s = quantidade de assuntos;
- `master_audio.mp3` ausente, salvo pedido expresso;
- duração informada por arquivo;
- quando houver várias vozes elegíveis adequadas, ausência de repetição desnecessária da mesma voz em todos os arquivos;
- uso oportuno de vozes temporariamente disponíveis em conteúdo novo quando isso não reduzir qualidade;
- exclusão de um arquivo não quebra os demais;
- ausência de substituição por `speechSynthesis`/TTS do navegador.

## 11. Duração

Usar aproximadamente 150 palavras úteis por minuto como estimativa. Não inflar com repetição ou silêncio. A duração varia conforme o assunto; não impor duração idêntica a todos.

## 12. Segurança

- não registrar segredos;
- chave apenas em `.env`, variável de ambiente ou Secret;
- não copiar valor de Secret para documentação, logs, prompts, registries ou continuidade;
- API paga somente com autorização aplicável;
- não desativar TLS;
- não expor conteúdo sensível desnecessariamente;
- não publicar conteúdo sensível em repositório público apenas para obter execução remota;
- existência de Secret pode ser documentada por nome lógico/localização, nunca por valor.

## 13. Fontes relacionadas

```text
pafe/audio_modos.md
pafe/audio_api_paga.md
pafe/audio_perfil_fabio.md
pafe/audio_capacidades_plataformas.md
pafe/VOICE_REGISTRY.json
pafe/VOICE_PRIORITY_OVERRIDE_2026-08.json
pafe/pafe_gpt.md
pafe/pafe_governanca_overlays.md
```

## 14. Estado final

Aprovado:

```text
CONFORME — todos os arquivos passaram nas validações.
```

Falha:

```text
BLOQUEADO — requisito obrigatório não pôde ser validado; nenhum fallback inferior foi utilizado.
```
