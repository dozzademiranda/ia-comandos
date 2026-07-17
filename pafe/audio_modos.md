# audio_modos.md — Modos de áudio do P.A.F.E.

**Versão:** v2.1  
**Data:** 2026-07-17  
**Status:** ativo e prevalente sobre `pafe/audio.md` para decidir onde e como iniciar a geração.

## 1. Regra central

1. Áudio significa MP3 neural real por assunto.
2. Um assunto principal gera um MP3 independente.
3. É proibido gerar somente `master_audio.mp3`, salvo pedido expresso posterior.
4. Não usar fallback robótico.
5. A linguagem natural e o contexto prevalecem sobre token exato de comando.
6. Criar arquivo para download na conversa não exige autorização adicional quando o usuário já pediu o artefato.

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

### `/pafe html audio` ou `/pafe audio html`

Resultado:

1. um HTML autocontido, sem áudio, player ou referência a MP3;
2. N MP3 independentes, um por assunto;
3. nenhum master unificado.

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

Fábio Dozza de Miranda concedeu autorização permanente ao ChatGPT/GPT para branches temporárias e GitHub Actions em `dozzademiranda/ia-comandos` para áudio P.A.F.E. dentro dos limites daquele overlay. Não solicitar novamente essa autorização.

### Rota 4 — pacote técnico completo

Somente sob pedido expresso de pacote, YAML, setup, manifesto, pipeline ou auditoria completa.

### Rota 5 — API paga

Somente com autorização, custo estimado e segredo fora do chat.

## 5. Script local mínimo

Entregar um único `.py`, autossuficiente, com:

- assuntos e textos;
- nomes dos MP3s;
- `edge-tts`;
- voz preferencial;
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
4. Criar branch e workflow temporários, gerar, validar e baixar o artifact.
5. Fechar o pull request sem merge.
6. Não usar voz robótica.
7. Não encerrar apenas com diagnóstico quando a rota GitHub autorizada puder entregar os arquivos reais.

### Gemini, Perplexity e outras

1. Não fingir geração.
2. Não usar voz robótica.
3. Usar apenas rotas efetivamente disponíveis e autorizadas.
4. Entregar script local se essa for a única rota capaz de concluir a tarefa.

## 7. Diagnóstico de falha

Classificar:

- DNS/rede;
- certificado/SSL;
- endpoint/serviço;
- autenticação/cota.

Nunca desativar TLS como padrão. Nunca pedir chave no chat.

## 8. TTS

Padrão gratuito:

```text
edge-tts
pt-BR-AntonioNeural
```

Vozes adicionais devem ser descobertas ou testadas no ambiente real.

Proibido como fallback final:

- Piper não autorizado;
- eSpeak;
- eSpeak-NG;
- MBROLA;
- pyttsx3;
- Festival;
- gTTS robótico;
- voz metálica;
- motor não rastreável.

## 9. Testes de regressão bloqueantes

### 9.1. GPT com sandbox sem rede e GitHub autorizado

Entrada:

```text
/pafe audio
Gere os arquivos por assunto.
```

Contexto: síntese direta falha por DNS; conector GitHub disponível; autorização permanente registrada.

Saída obrigatória:

- aplicar `pafe_gpt.md`;
- gerar branch e workflow temporários;
- um MP3 por assunto;
- `edge-tts` neural;
- validação por `ffprobe`;
- artifact físico baixado;
- pull request fechado sem merge;
- nenhum pedido repetido de autorização;
- nenhum fallback robótico.

### 9.2. Execução local realmente disponível

Quando a máquina local puder ser efetivamente usada para concluir a tarefa e GitHub não for necessário, o script mínimo continua válido. Reprovar se a IA apenas explicar, exigir comando adicional ou entregar master único.
