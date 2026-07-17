# pafe_prompt_outras_ias.md

**Versão:** 1.6  
**Data:** 2026-07-17  
**Escopo:** GPT, Gemini, Perplexity e outras IAs, respeitados os overlays específicos de plataforma.

## 1. Regra de base

1. Verificar capacidade real da plataforma antes de escolher a rota.
2. Se houver síntese neural direta, gerar um MP3 por assunto.
3. Se existir overlay específico da plataforma, ele deve ser lido e aplicado.
4. Para ChatGPT/GPT, aplicar `pafe_gpt.md`.
5. Para Claude com execução ativa, aplicar `pafe_claude.md`.
6. Não usar voz robótica.
7. Não gerar master único por padrão.
8. Não declarar MP3 gerado sem arquivo físico validado.

## 2. Hierarquia geral de rotas

```text
MP3 neural direto
→ rota específica da plataforma efetivamente disponível
→ script local mínimo, quando a máquina local puder executar
→ pacote técnico completo, sob pedido
→ API paga, com autorização
```

A ordem pode ser ajustada pelo overlay específico quando houver capacidade já validada e autorização permanente.

## 3. Regra específica do ChatGPT/GPT

Quando o ChatGPT/GPT possuir conector GitHub com permissão e a síntese direta falhar por DNS, rede ou egress bloqueado:

1. ler `pafe_gpt.md`;
2. não tratar o bloqueio do sandbox como impossibilidade absoluta;
3. usar branch temporária e GitHub Actions no repositório autorizado;
4. gerar um MP3 neural por assunto com `edge-tts`;
5. validar cada arquivo com `ffprobe`;
6. publicar e baixar o artifact;
7. fechar o pull request sem merge;
8. não solicitar novamente a autorização permanente já registrada em `pafe_gpt.md`.

Essa rota é proibida para conteúdo sigiloso em repositório público.

## 4. Regra para Gemini, Perplexity e outras IAs

1. Não presumir ferramentas inexistentes.
2. Não fingir geração.
3. Usar somente rotas efetivamente disponíveis e autorizadas.
4. Se não houver síntese nem rota remota segura, entregar script local mínimo apenas quando ele puder realmente concluir a tarefa.
5. Não substituir áudio neural por Piper não autorizado, eSpeak, MBROLA, pyttsx3, Festival ou gTTS robótico.

## 5. Lançador enxuto — GPT

```text
/mpe
P.A.F.E. — INICIALIZAÇÃO GPT

DISCIPLINA: [nome]
OBJETIVO: [resultado]
ANEXOS: [listar]

1. Leia README.md, audio_modos.md, audio.md, pafe_governanca_overlays.md e pafe_gpt.md.
2. Leia os anexos acessíveis e não invente conteúdo.
3. Para áudio, gere um MP3 neural por assunto.
4. Faça smoke test direto.
5. Se o sandbox falhar por DNS/rede e o GitHub estiver disponível, aplique pafe_gpt.md e gere os arquivos via GitHub Actions.
6. Não peça novamente autorização para a rota GitHub já autorizada em pafe_gpt.md.
7. Valide cada MP3 e só declare conclusão após baixar o artifact físico.
8. Se houver HTML, aplique html.md: um HTML separado, sem áudio, player, referência a MP3 ou impressão.
```

## 6. Lançador genérico — outras IAs

```text
/mpe
P.A.F.E. — INICIALIZAÇÃO

DISCIPLINA: [nome]
OBJETIVO: [resultado]
ANEXOS: [listar]

1. Leia os anexos acessíveis.
2. Verifique as capacidades reais da plataforma.
3. Não invente nem finja geração de arquivo.
4. Para áudio, gere um MP3 neural por assunto.
5. Aplique o overlay específico da plataforma, se existir.
6. Não use fallback robótico.
7. Se houver HTML, gere um HTML separado, sem áudio, player ou impressão.
```

## 7. Testes bloqueantes

### 7.1. GPT com sandbox sem rede e GitHub autorizado

Entrada:

```text
/pafe audio
Gere os arquivos por assunto.
```

Saída esperada:

- leitura de `pafe_gpt.md`;
- branch e workflow temporários;
- MP3s neurais independentes;
- validação por `ffprobe`;
- artifact físico baixado;
- pull request fechado sem merge;
- nenhuma nova solicitação de autorização;
- nenhum fallback robótico.

### 7.2. Plataforma sem rota remota ou execução direta

Saída esperada:

- não fingir MP3;
- não usar voz robótica;
- declarar bloqueio ou entregar script local mínimo somente quando essa rota for realmente executável.
