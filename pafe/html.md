
COMANDO: /pafe html
ARQUIVO: pafe/html.md
PARENTE: pafe/README.md

O QUE É: política técnica e estética do HTML de estudo gerado pelo P.A.F.E.

QUANDO USAR: só é acionado quando o usuário pedir HTML, índice de revisão, pacote de estudo ou usar /pafe html.

1. REQUISITOS DE ARQUIVO
1.1. um único index.html, offline, autossuficiente.
1.2. CSS e JS internos; sem CDN; sem fonte ou biblioteca externa obrigatória; sem link externo obrigatório.
1.3. tag completa de <!doctype html> a </html>.
1.4. responsivo e leve.

2. PLAYER DE ÁUDIO MASTER (quando aplicável)
2.1. um único player, fixo no topo (sticky), z-index alto.
2.2. atributo loop nativo; badge textual "loop" visível.
2.3. tag de referência: <audio controls loop preload="metadata" src="audio/master_audio.mp3" style="width:100%;"></audio>
2.4. o loop é responsabilidade do HTML; jamais multiplicar o MP3 no Python.

3. ACESSIBILIDADE COGNITIVA (perfil TDAH e autismo nível 1)
3.1. fonte sans-serif no corpo.
3.2. texto alinhado à esquerda; nunca justificar.
3.3. line-height mínimo de 1.5.
3.4. contraste confortável; evitar preto puro sobre branco puro.
3.5. cor nunca é o único sinal: importância sempre acompanhada de badge textual [ALTO], [MÉDIO], [BAIXO] ou [PEGADINHA].
3.6. atributos ARIA quando houver controles interativos.

4. HIERARQUIA VISUAL
4.1. diferenciação entre blocos, escolas e módulos por matiz e luminosidade distintas.
4.2. separadores visíveis entre seções.
4.3. callouts em quatro variantes — crit (vermelho), warn (amarelo), good (verde), info (azul) — com border-left espesso e fundo tonal.
4.4. mapas e visões gerais em story cards (grid responsivo); nunca tabela plana para isso.

5. NAVEGAÇÃO E ESTUDO
5.1. menu lateral ou sumário interno quando o conteúdo tiver mais de quatro seções.
5.2. busca textual interna, opcional.
5.3. flashcards e quiz com feedback imediato, quando úteis.
5.4. modo claro e escuro, quando útil.
5.5. persistência em localStorage opcional, apenas para HTML executado na máquina local.

6. DIFERENÇA ENTRE HTML DE ESTUDO E HTML DE E-MAIL
6.1. as regras 1 a 5 valem para HTML de estudo (executado no navegador, local ou em pasta de disciplina).
6.2. HTML de e-mail tem escopo separado e só é gerado a pedido expresso.
6.3. nunca misturar regras de e-mail com regras de estudo.

7. HTML DE E-MAIL (escopo separado, só a pedido expresso)
7.1. CSS inline.
7.2. compatibilidade com Gmail e Outlook.
7.3. tabelas estruturais com role="presentation" quando usadas para layout.
7.4. atenção ao limite de tamanho do Gmail.
7.5. evitar CSS moderno incompatível com clientes de e-mail.

8. PROIBIÇÕES
8.1. CDN ou dependência externa obrigatória.
8.2. design plano sem hierarquia tonal.
8.3. cor como único veículo de significado.
8.4. justificar texto.
8.5. múltiplos players para simular loop.

9. VALIDAÇÃO ANTES DE AFIRMAR QUE O ARQUIVO FOI GERADO
9.1. não afirmar que o arquivo foi gerado sem que exista no caminho indicado.
9.2. quando a plataforma permitir gerar arquivo, devolver o caminho efetivo e marcar [ARTEFATO: código gerado].
9.3. quando a plataforma não permitir gerar arquivo, declarar [ARTEFATO: indisponível nesta plataforma] e entregar o conteúdo em bloco único para o usuário salvar.
9.4. quando o pacote final depender de execução pelo usuário (montagem da pasta com audio/), declarar [ARTEFATO: execução local necessária].
