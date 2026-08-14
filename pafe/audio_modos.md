# audio_modos.md — Modos de áudio do P.A.F.E.

**Versão:** v2.3.0  
**Data:** 2026-08-14  
**Status:** ativo e prevalente sobre `pafe/audio.md` para decidir onde e como iniciar a geração.

## 1. Regra central

1. Áudio significa MP3 neural real por assunto.
2. Um assunto principal gera um MP3 independente e usa uma única voz naquele arquivo.
3. Não alternar vozes dentro do mesmo assunto apenas para variedade.
4. É proibido gerar somente `master_audio.mp3`, salvo pedido expresso posterior.
5. Não usar fallback robótico.
6. HTML, `speechSynthesis` ou voz nativa do navegador não substituem `/pafe audio`.
7. A linguagem natural e o contexto prevalecem sobre token exato de comando.
8. Criar arquivo para download na conversa não exige autorização adicional quando o usuário já pediu o artefato.

## 2. Saída por comando

### `/pafe audio`

Resultado:

```text
01_<ASSUNTO>.mp3
02_<ASSUNTO>.mp3
...
NN_<ASSUNTO>.mp3
```

Sem HTML por padrão.

Quando a plataforma suportar arquivos individuais, entregar os MP3s individualmente. ZIP pode ser oferecido como conveniência adicional ou usado como transporte obrigatório de um provedor, mas não substitui conceitualmente os MP3s individuais.

### `/pafe html audio` ou `/pafe audio html`

Resultado:

1. um HTML autocontido, sem áudio, player, `speechSynthesis` ou referência a MP3;
2. N MP3 independentes, um por assunto;
3. nenhum master unificado;
4. ZIP apenas como conveniência adicional ou transporte técnico quando necessário.

### `/pafe audio local` ou `/pafe audio script`

Força um script local mínimo.

### `/pafe audio pacote`

Força pacote técnico completo.

## 3. Definição de assunto

1. Usar títulos, módulos e unidades conceituais reais.
2. Não dividir apenas por caracteres.
3. Não fundir assuntos independentes.
4. Se um assunto ultrapassar limite técnico, usar `PARTE_01`, `PARTE_02`.
5. A quantidade de MP3s deve corresponder à lista de assuntos.

## 4. Hierarquia obrigatória de rotas

### Rota 1 — MP3 neural direto

Usar quando a plataforma consegue sintetizar, validar e entregar os arquivos.

Falha de DNS/rede/egress no sandbox é falha da rota direta, não prova de impossibilidade global.

### Rota 2 — script local mínimo automático

Usar quando:
- a rota direta falhar;
- a máquina local do usuário puder ser efetivamente usada para concluir a geração;
- não houver rota remota já autorizada que entregue diretamente os MP3 solicitados.

Não pedir nova autorização para gerar o script quando o usuário já pediu áudio e a execução local for a única rota prática.

### Rota 3 — GitHub Actions ou Codespaces

Usar quando:
- a execução direta falhar;
- a conversa não puder executar na máquina local do usuário;
- houver conector GitHub com permissão;
- a rota estiver autorizada;
- o conteúdo puder ser processado com segurança no repositório escolhido.

Para ChatGPT/GPT, aplicar `pafe_gpt.md`.

Se existir autorização persistente para rota remota documentada em fonte privada governante ou no contexto atual, reutilizá-la estritamente dentro dos limites registrados. Não republicar identidade, redação ou detalhes privados dessa autorização. Na ausência de autorização documentada, seguir `pafe_governanca_overlays.md`.

### Rota 4 — pacote técnico completo

Somente sob pedido expresso de pacote, YAML, setup, manifesto, pipeline ou auditoria completa.

### Rota 5 — API paga

Somente com autorização, custo estimado e segredo fora do chat.

## 5. Script local mínimo

Entregar um único `.py`, autossuficiente, com:
- assuntos e textos;
- nomes dos MP3s;
- motor neural;
- descoberta/seleção de voz;
- retries;
- pausas reais;
- PCM uniforme;
- normalização;
- validação individual;
- publicação segura;
- `--list`;
- `--only`;
- `--force`.

Não gerar README, YAML, TXT, JSON, manifesto, requirements, setup, ZIP ou hash por padrão.

## 6. Capacidade por plataforma

### Claude com execução ativa

1. Fazer smoke test.
2. Gerar MP3 neural direto quando possível.
3. Gerar um MP3 por assunto.
4. Nunca gerar master único por padrão.
5. Se falhar, aplicar `pafe_claude.md` e a rota compatível.

### ChatGPT/GPT com conectores

1. Fazer smoke test do ambiente direto quando houver execução.
2. Não presumir incapacidade apenas porque o sandbox bloqueou DNS.
3. Se a síntese direta falhar e GitHub estiver acessível, aplicar `pafe_gpt.md`.
4. Só iniciar escrita externa se houver autorização aplicável documentada.
5. Quando a rota GitHub estiver autorizada, usar branch/workflow temporários, gerar, validar e baixar o artifact.
6. Fechar o pull request sem merge.
7. Não usar voz robótica.
8. Não encerrar apenas com diagnóstico quando uma rota autorizada puder entregar os arquivos reais.
9. Não substituir MP3 por `speechSynthesis` no HTML.

### Gemini, Perplexity e outras

1. Não fingir geração.
2. Não usar voz robótica.
3. Usar apenas rotas efetivamente disponíveis e autorizadas.
4. Entregar script local se essa for a única rota capaz de concluir a tarefa.
5. Não transformar HTML com TTS do navegador em equivalente de MP3 real.

## 7. Diagnóstico de falha

Classificar:
- DNS/rede/egress;
- certificado/SSL;
- endpoint/serviço;
- autenticação/cota.

Nunca desativar TLS como padrão. Nunca pedir chave no chat.

## 8. Motor e pool de vozes

Rota gratuita preferencial quando disponível:

```text
edge-tts
```

A voz NÃO é fixa. Antes da geração, descobrir/testar as vozes realmente disponíveis no ambiente da rota escolhida.

Estados de voz:

```text
PREFERRED
APPROVED
AVAILABLE
CANDIDATE
REJECTED_TEMP
LAST_RESORT
```

Regra de elegibilidade:

```text
eligible = APPROVED ∩ AVAILABLE \ LAST_RESORT
```

Se ainda não houver voz `APPROVED`, testar candidatas reais e não inventar disponibilidade. `pt-BR-AntonioNeural` e `pt-BR-FranciscaNeural` são `LAST_RESORT`, não preferência. `pt-BR-LeticiaNeural` ou nome equivalente retornado pelo serviço pode ser `CANDIDATE`. Outras vozes pt-BR devem ser descobertas/testadas no ambiente real.

Um arquivo usa uma só voz. Entre assuntos, rotação é permitida somente entre vozes elegíveis. Cache/hash de MP3 já válido prevalece sobre ressintetização apenas para cumprir rotação.

Proibido como fallback final:
- Piper não autorizado;
- eSpeak;
- eSpeak-NG;
- MBROLA;
- pyttsx3;
- Festival;
- gTTS robótico;
- voz metálica;
- motor não rastreável;
- `speechSynthesis` como substituto de MP3 solicitado.

## 9. Testes de regressão bloqueantes

### 9.1. GPT com sandbox sem rede e rota GitHub autorizada

Entrada:

```text
/pafe audio
Gere os arquivos por assunto.
```

Contexto: síntese direta falha por DNS; conector GitHub disponível; autorização aplicável documentada.

Saída obrigatória:
- aplicar `pafe_gpt.md`;
- usar branch e workflow temporários conforme autorização;
- um MP3 por assunto;
- voz neural descoberta/validada no runner;
- validação por `ffprobe`;
- artifact físico baixado quando suportado;
- pull request fechado sem merge;
- nenhum pedido repetido de autorização já documentada;
- nenhum fallback robótico;
- nenhum `speechSynthesis` apresentado como substituto.

### 9.2. Execução local realmente disponível

Quando a máquina local puder ser efetivamente usada para concluir a tarefa e GitHub não for necessário, o script mínimo continua válido. Reprovar se a IA apenas explicar, exigir comando adicional ou entregar master único.

### 9.3. Entrega individual + ZIP

Quando a plataforma permitir múltiplos downloads, reprovar se a única entrega ao usuário for ZIP. Aceitar ZIP adicional de conveniência. Se o provedor remoto só transportar artifact como ZIP, baixar/descompactar e expor os MP3s individualmente quando a superfície permitir.