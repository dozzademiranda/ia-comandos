# audio_modos.md — Modos de áudio do P.A.F.E.

STATUS: ativo e prevalente sobre `pafe/audio.md` para a interpretação dos comandos `/pafe audio`, `/pafe html audio` e `/pafe completo`.

Este arquivo existe para separar três coisas que antes ficavam misturadas:

1. gerar um MP3 real;
2. gerar apenas roteiro textual;
3. gerar pacote local com `audio.yaml`, script Python e pipeline.

## 1. Regra central

Por padrão, áudio significa **MP3 real**, não pacote local.

Se o usuário digitar apenas:

```text
/pafe audio
```

ou:

```text
/pafe html audio
```

a IA deve tentar gerar arquivo MP3 real diretamente na plataforma, se a plataforma permitir.

## 2. Modo MP3 direto — padrão

Invocações:

```text
/pafe audio
/pafe audio mp3
/pafe html audio
/pafe html audio mp3
/pafe completo
```

Resultado esperado:

1. gerar `audio/master_audio.mp3`, se a plataforma permitir;
2. quando houver HTML, gerar `index.html` offline;
3. quando houver HTML, incluir flashcards clicáveis embutidos;
4. quando houver HTML, incluir quiz interativo embutido;
5. quando houver HTML, incluir player apontando para `audio/master_audio.mp3`, se o MP3 existir;
6. não gerar pacote local por padrão.

Neste modo é proibido gerar, salvo pedido expresso do usuário:

1. `audio.yaml`;
2. qualquer arquivo `.yaml` de áudio;
3. `roteiro_audio.txt`;
4. qualquer arquivo `.txt` de roteiro de áudio;
5. `gerar_audio.py`;
6. `gerar_audio_v2.py`;
7. `setup_audio.sh`;
8. `validar_audio.sh`;
9. `requirements_audio.txt`;
10. `manifest_audio.json`;
11. `chapters.json`;
12. pipeline local de áudio;
13. pacote local de geração de áudio.

## 3. Modo roteiro — somente se pedido

Invocação expressa:

```text
/pafe audio roteiro
```

Resultado esperado:

1. gerar roteiro falável em texto;
2. não declarar MP3 gerado;
3. não gerar pacote local;
4. não gerar `audio.yaml`;
5. não gerar script Python.

Fallback:

Se o usuário pediu MP3 real e a plataforma não conseguir gerar MP3, só entregar roteiro se o usuário tiver autorizado fallback textual ou se o prompt específico permitir roteiro em caso de falha.

Se o usuário disser “quero áudio, não roteiro”, não entregar roteiro como substituto, salvo se ele autorizar fallback.

## 4. Modo pacote local — desativado por padrão

STATUS: DESATIVADO POR PADRÃO.

Este modo preserva o comportamento antigo do `pafe/audio.md`, mas só pode ser acionado por pedido expresso.

Invocações que ativam este modo:

```text
/pafe audio pacote
/pafe audio local
/pafe audio pipeline
/pafe audio script
/pafe audio yaml
```

Também ativa se o usuário pedir expressamente qualquer um destes itens:

1. `audio.yaml`;
2. script Python;
3. `gerar_audio_v2.py`;
4. pipeline local;
5. geração local;
6. pacote local;
7. `setup_audio.sh`;
8. `validar_audio.sh`;
9. `requirements_audio.txt`.

Neste modo, aplicar `pafe/audio.md`.

## 5. Como reativar o modo antigo em urgência

Para reativar o modo antigo, usar:

```text
/pafe audio pacote
```

ou:

```text
/pafe audio local
```

Isso permite gerar `audio.yaml`, script Python, arquivos `.sh`, manifesto, capítulos e demais peças do pipeline local.

## 6. Pesquisa profunda

`/pafe html audio` é modo de artefato, não modo de pesquisa.

Não fazer pesquisa profunda, nem navegar na web, salvo se o usuário pedir expressamente pesquisa, atualização, jurisprudência nova, fontes recentes ou validação externa.

A pesquisa profunda pertence a comandos como:

```text
/pafe
/pafe completo
/pafe pesquisa
/pafe aprofundado
```

ou a pedidos expressos de busca externa.

## 7. Revisões emergencial e relâmpago

Não gerar revisão emergencial, revisão de 2 horas, revisão relâmpago ou checklist de véspera por padrão dentro de `/pafe html audio`.

Gerar essas revisões apenas quando:

1. o usuário pedir expressamente;
2. o material anexado já exigir isso;
3. o comando usado for `/pafe completo` e o objetivo for estudo integral.

## 8. Declaração de artefato

Nunca afirmar que MP3 foi gerado sem arquivo físico real.

Declarações permitidas:

```text
[ARTEFATO: MP3 gerado]
```

somente se `audio/master_audio.mp3` existir.

```text
[ARTEFATO: MP3 indisponível nesta plataforma]
```

quando a plataforma não puder gerar MP3 real.

```text
[ARTEFATO: execução local necessária]
```

somente se o usuário tiver pedido ou autorizado pacote local ou fallback de geração local.

## 9. HTML com áudio

Quando o comando for:

```text
/pafe html audio
```

gerar:

1. `index.html` offline e autossuficiente;
2. flashcards clicáveis dentro do HTML;
3. quiz interativo dentro do HTML;
4. `audio/master_audio.mp3`, se possível;
5. player no HTML apontando para `audio/master_audio.mp3`, se o MP3 existir.

O HTML é adendo de estudo. O áudio MP3 é o artefato principal quando o usuário pedir áudio.

## 10. Rodapé operacional

Versão: audio_modos.md v1.0  
Data: 06/07/2026  
Regra central: `/pafe audio` e `/pafe html audio` tentam MP3 direto por padrão; pacote local fica desativado até pedido expresso.
