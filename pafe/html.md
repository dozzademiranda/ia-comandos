COMANDO: /pafe html
ARQUIVO: pafe/html.md
PARENTE: pafe/README.md

O QUE É: política técnica e visual do HTML de estudo gerado pelo P.A.F.E.

QUANDO USAR: acionar quando o usuário pedir HTML, index.html, pacote de estudo, interface de revisão, flashcards em HTML, quiz, SRS, ScrollSpy, página offline ou usar /pafe html.

1. ESCOPO

1.1. Este arquivo regula HTML de estudo, executado em navegador, localmente ou em pasta de disciplina.

1.2. HTML de e-mail tem escopo separado e só deve ser gerado a pedido expresso.

1.3. Não misturar regras de HTML de estudo com HTML de e-mail.

2. REQUISITOS DE ARQUIVO

2.1. Gerar um único arquivo index.html, offline e autossuficiente, salvo pedido expresso em contrário.

2.2. O arquivo deve conter HTML completo, de <!doctype html> a </html>.

2.3. CSS e JS devem ser internos.

2.4. Não usar CDN, fontes externas obrigatórias, bibliotecas externas obrigatórias, imagens externas obrigatórias ou links externos obrigatórios.

2.5. O HTML deve continuar funcional sem internet.

2.6. Recursos externos opcionais só podem ser usados se:
2.6.1. o usuário pedir expressamente;
2.6.2. houver fallback local;
2.6.3. a dependência externa for declarada.

3. ACESSIBILIDADE COGNITIVA

3.1. Priorizar legibilidade para adulto com TDAH, autismo nível 1, burnout e ansiedade moderada.

3.2. Usar fonte sans-serif no corpo.

3.3. Texto alinhado à esquerda; nunca justificar texto longo.

3.4. line-height mínimo de 1.5.

3.5. Usar contraste confortável; evitar preto puro sobre branco puro quando possível.

3.6. Evitar poluição visual, excesso de animação, piscadas, transições agressivas e elementos que desviem a atenção.

3.7. Cor nunca deve ser o único veículo de significado.

3.8. Importância deve ser indicada com texto, badge ou rótulo, como [ALTO], [MÉDIO], [BAIXO] ou [PEGADINHA].

3.9. Controles interativos devem ter rótulos claros e, quando cabível, atributos ARIA.

4. HIERARQUIA VISUAL

4.1. Usar hierarquia visual clara entre:
4.1.1. disciplina;
4.1.2. módulo;
4.1.3. tema;
4.1.4. subtópico;
4.1.5. pegadinha;
4.1.6. revisão.

4.2. Usar separadores visíveis entre seções.

4.3. Usar cards, callouts, tabelas comparativas e blocos de revisão quando melhorarem a compreensão.

4.4. Callouts recomendados:
4.4.1. crit — erro grave, prova, pegadinha forte;
4.4.2. warn — atenção, exceção, risco de confusão;
4.4.3. good — síntese correta, fórmula segura, chave de memória;
4.4.4. info — contexto, definição, explicação.

4.5. Mapas, panoramas e revisões gerais devem preferir cards ou grids responsivos, não tabelas extensas quando isso prejudicar leitura.

5. NAVEGAÇÃO E RECURSOS DE ESTUDO

5.1. Menu lateral, sumário interno ou navegação fixa são recomendados quando houver mais de quatro seções.

5.2. Busca textual interna pode ser incluída quando o conteúdo for extenso.

5.3. ScrollSpy pode ser incluído quando houver navegação lateral ou sumário fixo.

5.4. Flashcards clicáveis podem ser incluídos quando úteis para memorização.

5.5. Quiz com gabarito comentado pode ser incluído quando houver treino de prova.

5.6. SRS ou Leitner podem ser incluídos quando o usuário pedir revisão ativa ou persistência de estudo.

5.7. Modo claro/escuro pode ser incluído quando útil.

5.8. Persistência em localStorage pode ser incluída em HTML local, mas deve:
5.8.1. não depender de servidor;
5.8.2. não exigir login;
5.8.3. não armazenar dado sensível;
5.8.4. permitir reiniciar progresso quando possível.

5.9. Busca, ScrollSpy, flashcards, quiz, SRS e localStorage não são obrigatórios em todo HTML; devem ser proporcionais ao pedido e ao tamanho do conteúdo.

6. PLAYER DE ÁUDIO MASTER

6.1. Quando houver áudio master, usar um único player apontando para:
audio/master_audio.mp3

6.2. O player deve ficar visível e acessível, preferencialmente em posição sticky no topo ou em área claramente identificada.

6.3. Referência recomendada: <audio controls loop preload="metadata" src="audio/master_audio.mp3" style="width:100%;"></audio>

6.4. O loop é responsabilidade do HTML.

6.5. Jamais multiplicar o MP3 no Python apenas para simular loop.

6.6. Se o arquivo audio/master_audio.mp3 não existir, não afirmar que o player está funcional; declarar que depende da geração local do áudio.

7. HTML DE E-MAIL

7.1. HTML de e-mail só deve ser gerado sob pedido expresso.

7.2. Quando o pedido for HTML de e-mail:
7.2.1. usar CSS inline;
7.2.2. priorizar compatibilidade com Gmail e Outlook;
7.2.3. usar tabelas estruturais com role="presentation" quando necessário;
7.2.4. evitar CSS moderno incompatível;
7.2.5. observar limite de tamanho do Gmail.

7.3. Não aplicar automaticamente regras de HTML de e-mail ao HTML de estudo.

8. PROIBIÇÕES

8.1. Proibido usar CDN como dependência obrigatória.

8.2. Proibido usar fonte externa obrigatória.

8.3. Proibido usar imagem externa obrigatória.

8.4. Proibido usar biblioteca externa obrigatória.

8.5. Proibido justificar texto longo.

8.6. Proibido usar cor como único sinal de significado.

8.7. Proibido gerar design plano sem hierarquia visual quando o conteúdo for complexo.

8.8. Proibido misturar HTML de estudo e HTML de e-mail sem pedido expresso.

8.9. Proibido afirmar que o index.html foi gerado sem arquivo real ou sem entregar o conteúdo integral.

9. VALIDAÇÃO ANTES DE AFIRMAR QUE O ARQUIVO FOI GERADO

9.1. Se a plataforma permitir criar arquivo, só afirmar geração depois de confirmar o caminho efetivo do arquivo.

9.2. Se a plataforma não permitir criar arquivo, declarar:
[ARTEFATO: indisponível nesta plataforma]

9.3. Se entregar apenas o código para o usuário salvar, declarar:
[ARTEFATO: código gerado]

9.4. Se o funcionamento depender de pasta, áudio, imagens ou execução local, declarar:
[ARTEFATO: execução local necessária]

9.5. Quando houver pacote com HTML e áudio, explicar a estrutura esperada:
9.5.1. index.html;
9.5.2. audio/master_audio.mp3;
9.5.3. demais arquivos, se expressamente pedidos.

10. SAÍDA

10.1. Entregar o HTML inteiro, completo, sem truncamento.

10.2. Não entregar patch, trecho solto ou instrução do tipo "insira aqui".

10.3. Se o arquivo for longo demais para uma resposta segura, dividir por partes apenas após avisar e manter controle claro de continuidade.

10.4. Em pedido de correção de HTML existente, carregar o original integral antes de editar.
