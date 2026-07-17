# /pafe — Overlay Claude

**Versão:** 1.3
**Data:** 2026-07-17
**Escopo:** Claude com ambiente de execução ativo.

## 1. Regra de ouro

Quando houver bash, rede, arquivos e entrega de binários, Claude deve fazer smoke test e tentar gerar MP3 neural direto.

## 2. Saída

1. Gerar um MP3 independente por assunto.
2. Não gerar `master_audio.mp3` por padrão.
3. Validar cada MP3 individualmente.
4. Falha em um assunto não invalida os demais.
5. Se o usuário pedir HTML junto, o HTML permanece sem áudio, player ou referência a MP3.

## 3. Falha

Antes de declarar impossibilidade, classificar DNS/rede, SSL, endpoint ou autenticação/cota.

É proibido:

- fallback robótico;
- eSpeak;
- MBROLA;
- pyttsx3;
- Festival;
- gTTS robótico;
- alegar “zero tokens proibidos” sem verificar o próprio HTML.

## 4. Contingência

Se a geração direta falhar:

1. se o ambiente Linux local conhecido for compatível, entregar automaticamente o script local mínimo;
2. não pedir autorização adicional;
3. não exigir outro comando;
4. não apresentar GitHub como única rota;
5. GitHub/Drive/Box exigem autorização de escrita externa.

## 5. Validação

Para cada MP3: `ffprobe`, tamanho, duração, codec, voz, início/final e ausência de truncamento.

Para HTML: aplicar integralmente `html.md`; áudio não afasta proibição de `<audio>`, `.mp3`, player ou impressão.

## 6. Precedência por artefato

- `html.md` governa o HTML;
- `audio_modos.md` governa a rota;
- `audio.md` governa a técnica;
- este overlay apenas amplia a capacidade do Claude.
