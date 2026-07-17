COMANDO: /pafe html
ARQUIVO: pafe/html.md
PARENTE: pafe/README.md
VERSÃO CANÔNICA: 2026-07-17.5

O QUE É

Política técnica, visual e funcional para geração de HTML de estudo pelo P.A.F.E.

REGRA CENTRAL

/pafe html gera exatamente um arquivo HTML de estudo, autocontido, offline, responsivo, acessível, sem qualquer execução de áudio e sem arquivos auxiliares por padrão.

NOVIDADES DA VERSÃO 2026-07-17.5

1. Botões visualmente compactos, preservando área de toque efetiva mínima de 48 × 48 CSS px em telas de toque (§11).
2. Caixa flutuante obrigatória para artigos de lei, com texto integral embutido e link oficial de conferência (§19).
3. Identidade visual de módulos e motivação para TDAH: fronteiras demarcadas, extensão visível, feedback de conclusão e gamificação leve (§20), com ícones estáticos embutidos permitidos (§16).
4. Explicações visuais didáticas: mapa geral sintético e mini-mapas por módulo, com texto HTML pesquisável, responsividade e baixa carga cognitiva (§21).

1. ESCOPO E PRECEDÊNCIA

1.1. Este arquivo regula HTML de estudo executado em navegador, localmente ou em pasta de disciplina.

1.2. HTML de e-mail possui escopo separado e só deve ser produzido mediante pedido expresso.

1.3. A ordem atual do usuário prevalece sobre instruções antigas, anexos, relatórios e respostas de outras IAs.

1.4. Esta versão substitui integralmente as versões anteriores de pafe/html.md.

1.5. Em dúvida, aplicar a interpretação mais restritiva:

/pafe html = um único HTML completo, offline, acessível, responsivo, sem áudio, sem impressão e sem arquivos auxiliares.

2. PROIBIÇÃO ABSOLUTA DE ÁUDIO

2.1. É proibido inserir, controlar, reproduzir, sincronizar, referenciar ou simular áudio no HTML.

2.2. É proibido inserir:

- <audio>;
- <video>;
- <source>;
- player;
- MP3, WAV, OGG, FLAC, M4A ou outra mídia;
- botões de reprodução, pausa, volume ou velocidade;
- new Audio();
- .play();
- .pause();
- currentTime;
- playbackRate;
- Media Session API;
- MediaMetadata;
- AudioContext;
- Web Audio API;
- speechSynthesis;
- síntese de voz;
- capítulos por timestamp;
- transcrição sincronizada;
- notas ou bookmarks temporais;
- referência a arquivo de áudio ausente;
- espaço reservado para futuro player.

2.3. /pafe html não gera como consequência:

- MP3;
- roteiro de áudio;
- texto TTS;
- TXT;
- script de geração de áudio;
- manifesto de áudio;
- pacote com áudio;
- pasta de mídia.

2.4. A existência de áudio em outra conversa, pasta ou etapa não autoriza sua integração ao HTML.

3. PROIBIÇÃO DE IMPRESSÃO

3.1. Não inserir botão Imprimir.

3.2. Não inserir opção Imprimir/PDF.

3.3. Não usar window.print(), onclick="print()" ou chamadas equivalentes.

3.4. Não criar folha @media print por padrão.

3.5. Impressão só poderá ser acrescentada mediante pedido expresso posterior do usuário, específico para aquele HTML.

4. ARTEFATO ÚNICO

4.1. Gerar por padrão somente um arquivo .html completo.

4.2. CSS, JavaScript e dados textuais devem ficar incorporados no próprio HTML.

4.3. Não usar CDN, fonte externa obrigatória, biblioteca externa obrigatória, API remota, analytics, banco remoto ou recurso remoto necessário ao funcionamento. Links de conferência a fontes oficiais (§19) são permitidos, desde que o HTML funcione integralmente sem eles.

4.4. O HTML deve funcionar sem internet e, quando tecnicamente possível, diretamente por file://.

4.5. Não criar por padrão:

- ZIP;
- README;
- TXT;
- JSON separado;
- manifesto;
- YAML;
- hash;
- pasta auxiliar;
- relatório técnico;
- script separado;
- CSS separado;
- JavaScript separado.

4.6. Não incluir exportação ou importação de progresso por arquivo, JSON ou download, salvo pedido expresso.

4.7. Persistência local por localStorage é permitida quando útil, sem gerar arquivo externo.

5. FILTRO DE RELEVÂNCIA VISÍVEL

5.1. Cada bloco visível deve ajudar a:

1. entender o conteúdo;
2. diferenciar conceitos;
3. memorizar;
4. resolver questões;
5. revisar erros; ou
6. executar estratégia de estudo pedida.

5.2. Se não cumprir nenhuma função acima, remover.

5.3. Não exibir no fluxo principal:

- nomes de IAs, modelos ou plataformas;
- comparação entre IAs;
- erros de outras IAs;
- inventário de anexos;
- histórico de elaboração;
- decisões internas de layout;
- ferramentas utilizadas;
- detalhes de validação;
- Python, FFmpeg, TTS, bibliotecas ou scripts;
- hashes;
- caminhos internos;
- justificativas sobre o processo de geração.

5.4. Quando fontes ou funcionamento forem realmente necessários, colocar tudo em seção discreta denominada "Fontes e funcionamento", fechada por padrão e situada ao final.

6. TELA INICIAL E CABEÇALHO

6.1. A tela inicial deve abrir diretamente no estudo, sem página técnica intermediária.

6.2. O cabeçalho visível deve ser compacto e conter somente:

- disciplina ou tema;
- avaliação ou objetivo;
- resumo curto do escopo, quando necessário;
- progresso atual;
- Retomar;
- Buscar;
- Opções.

6.3. Não exibir diretamente na barra principal:

- Tema;
- A−;
- A+;
- Foco;
- filtros;
- navegação extensa;
- limpar progresso;
- notas;
- glossário;
- configurações;
- informações técnicas.

6.4. Todos os controles secundários devem ficar em submenus, painéis, drawers, popovers ou <details> fechados por padrão.

6.5. Não usar barra lateral permanentemente aberta como padrão.

6.6. No celular, navegação, filtros e configurações devem permanecer ocultos até ação do usuário; nunca devem aparecer antes do conteúdo principal.

6.7. No desktop, o conteúdo visível do cabeçalho e o conteúdo principal devem usar o mesmo contêiner, a mesma largura máxima e o mesmo alinhamento horizontal.

6.8. O fundo, a borda ou a área sticky do cabeçalho podem ocupar toda a largura da janela; títulos, progresso e botões devem ficar em contêiner interno centralizado e alinhado ao conteúdo principal.

6.9. Não combinar cabeçalho com conteúdo espalhado por toda a tela e corpo principal em coluna estreita centralizada, salvo pedido expresso.

7. MENU OPÇÕES

7.1. O botão Opções deve abrir painel fechado por padrão e agrupar apenas ferramentas úteis.

7.2. Grupo Visualização:

- Automático;
- Celular;
- Desktop;
- tamanho do texto;
- espaçamento;
- tema;
- modo foco;
- baixa estimulação.

7.3. Grupo Estudo:

- flashcards;
- revisar erros;
- notas;
- glossário;
- limpar progresso, mediante confirmação.

7.4. Grupo Navegação:

- módulos;
- pegadinhas;
- questões;
- flashcards;
- quiz;
- revisão final.

7.5. Não incluir Imprimir/PDF.

7.6. Não incluir exportar ou importar progresso, salvo pedido expresso.

7.7. O menu deve:

- fechar por clique fora;
- fechar por Esc;
- devolver o foco ao botão de origem;
- permanecer navegável por teclado;
- permitir rolagem interna em telas estreitas;
- não causar overflow horizontal geral.

8. BUSCA

8.1. Buscar deve abrir campo ou painel somente após acionamento.

8.2. A busca deve funcionar offline e pesquisar por palavra, tema, conceito, referência e questão.

8.3. Deve permitir limpar o filtro, informar ausência de resultados e preservar navegação por teclado.

8.4. O campo de busca não deve ocupar permanentemente a tela inicial.

9. RETOMADA E PROGRESSO

9.1. O HTML deve facilitar retomada após distração.

9.2. Salvar em localStorage, quando aplicável:

- última seção significativa;
- módulos concluídos;
- questão atual;
- respostas dadas;
- erros;
- flashcards revisados;
- dificuldade;
- notas;
- modo de visualização;
- tema;
- escala;
- espaçamento;
- baixa estimulação.

9.3. Usar namespace por conteúdo e versão.

9.4. Não salvar qualquer campo relacionado a áudio, mídia ou impressão.

9.5. O botão Retomar deve levar ao último ponto significativo, não apenas à última posição bruta de rolagem.

9.6. Limpar progresso deve ficar dentro de Opções e exigir confirmação clara.

10. RESPONSIVIDADE E TIPOGRAFIA

10.1. Implementar modos Automático, Celular e Desktop, persistidos em localStorage quando úteis.

10.2. Celular:

- uma coluna;
- margens reduzidas;
- cabeçalho compacto;
- textos longos recolhíveis;
- rolagem horizontal somente dentro de tabelas ou menus;
- nenhum overflow horizontal da página;
- nenhum painel secundário aberto por padrão.

10.3. Desktop:

- largura máxima controlada;
- cards em duas ou três colunas somente quando melhorarem leitura;
- conteúdo principal centralizado;
- cabeçalho e conteúdo principal com a mesma largura útil e alinhamento horizontal;
- usar contêiner interno no cabeçalho quando o fundo sticky ocupar toda a janela;
- nenhuma barra lateral obrigatória.

10.4. Tipografia padrão:

html { font-size: 16px; }
body { line-height: 1.6; }

10.5. Em telas estreitas, não reduzir normalmente abaixo de 15,5 px.

10.6. Regras obrigatórias:

- fonte sans-serif do sistema;
- texto alinhado à esquerda;
- texto de estudo nunca justificado;
- largura principal preferencial de 72ch, dentro do intervalo de 68ch a 80ch;
- line-height entre 1,55 e 1,70;
- parágrafos curtos;
- negrito seletivo;
- evitar caixa alta em blocos longos;
- suportar zoom de 200% sem perda de conteúdo ou função.

11. BOTÕES E ÁREAS DE TOQUE (COMPACTOS POR PADRÃO)

11.1. Botões e controles devem ser visualmente compactos: altura visível padrão entre 34 e 40 px no desktop, fonte entre 0,85 rem e 0,95 rem e padding horizontal proporcional.

11.2. Em telas de toque, a área clicável efetiva deve permanecer de no mínimo 48 × 48 CSS px, obtida por padding, margem clicável, pseudo-elemento ou área estendida invisível, ainda que o desenho visível seja menor. O piso de 24 × 24 CSS px é apenas limite absoluto de conformidade e não é o alvo do projeto.

11.3. Ícone visual pode ser menor que a área clicável total.

11.4. Ações destrutivas, opostas ou irreversíveis devem ter separação adequada; Cancelar, excluir, reiniciar e apagar progresso não devem ficar colados à ação principal.

11.5. Botões devem ter rótulos claros e aparência hierárquica distinta:

- ação principal;
- ação secundária;
- navegação;
- confirmação;
- destrutiva.

11.6. Evitar muitos botões com aparência equivalente; botões compactos não podem virar alvos minúsculos ou aglomerados.

12. CORES E HIERARQUIA VISUAL

12.1. Não existe paleta universal comprovada para TDAH.

12.2. Priorizar poucos estímulos concorrentes, paleta curta, baixa saturação, contraste verificável, consistência e personalização.

12.3. Usar:

- uma cor estrutural discreta para navegação e ação principal;
- verde para correto, concluído ou seguro;
- âmbar para atenção, exceção ou pegadinha;
- vermelho para erro material, resposta incorreta ou ação destrutiva;
- superfícies neutras para o conteúdo comum.

12.4. Diferenciar módulos sem transformar cada um em cor intensa distinta.

12.5. A diferenciação pode usar variações discretas de matiz e luminosidade em:

- borda superior;
- faixa lateral;
- cabeçalho da seção;
- badge textual;
- fundo suave.

12.6. Cor nunca deve ser o único veículo de significado.

12.7. Evitar que todas as seções e todos os botões pareçam visualmente idênticos.

12.8. Base cromática recomendada: superfícies neutras de baixa saturação com acentos calmos (azuis e verdes dessaturados); tons quentes e vibrantes reservados a atenção, pegadinha e erro. Evitar fundos brancos puros de alto brilho no tema claro.

12.9. O conjunto de cores dos módulos forma um mapa cromático fixo do documento: a mesma cor identifica o mesmo módulo no corpo, na navegação, no progresso e nas questões vinculadas.

13. BAIXA ESTIMULAÇÃO E DIVULGAÇÃO PROGRESSIVA

13.1. Priorizar legibilidade para adulto com TDAH, autismo nível 1, burnout e ansiedade moderada.

13.2. Implementar modo de baixa estimulação que reduza sombras, bordas decorativas, cores não essenciais, elementos periféricos, animações e informações simultâneas.

13.3. Implementar modo foco quando útil, mostrando apenas o bloco atual e controles essenciais.

13.4. Usar divulgação progressiva:

- respostas inicialmente ocultas;
- aprofundamentos em <details>;
- notas recolhidas;
- questões uma por vez;
- flashcards inicialmente fechados;
- ferramentas secundárias ocultas por padrão;
- Fontes e funcionamento fechado por padrão.

13.5. Respeitar prefers-reduced-motion.

13.6. Proibir animação contínua, piscar, transições longas, rolagem forçada, foco inesperado e decoração obrigatória.

14. QUESTÕES, FLASHCARDS E REVISÃO

14.1. Questões devem ser apresentadas uma por vez.

14.2. Não antecipar gabarito.

14.3. Após a resposta, mostrar em blocos curtos:

- resposta correta;
- fundamento;
- pegadinha;
- como reconhecer na prova.

14.4. Permitir revisar somente erros e refazer questões quando isso fizer parte do pedido.

14.5. Flashcards devem permanecer fechados até ação, permitir marcar dificuldade e evitar abertura automática de todos.

15. ACESSIBILIDADE, SEGURANÇA E PRIVACIDADE

15.1. Obrigatório:

- HTML semântico;
- hierarquia correta de títulos;
- link "Ir para o conteúdo";
- foco visível;
- navegação por teclado;
- contraste suficiente;
- prefers-reduced-motion;
- conteúdo compreensível sem depender de cor;
- mensagens de estado acessíveis;
- modais ou painéis acessíveis quando usados;
- nenhuma restrição ao zoom do navegador.

15.2. Não usar ARIA para substituir semântica HTML nativa disponível.

15.3. Não enviar conteúdo jurídico a serviço externo sem autorização.

15.4. Não usar analytics por padrão.

15.5. Evitar innerHTML com dados não confiáveis.

15.6. Preferir textContent, createElement e atributos explicitamente controlados.

15.7. Proibir eval() e new Function().

15.8. Não registrar conteúdo sensível no console.

16. IMAGENS, ÍCONES, SVG E DIAGRAMAS

16.1. Fotos, ilustrações complexas e imagens externas: somente mediante pedido expresso; nunca como decoração; nunca por arquivo externo ou base64 volumoso que comprometa o artefato único.

16.2. Ícones e pictogramas leves são permitidos e recomendados, desde que: embutidos no próprio HTML (SVG inline curto ou caractere unicode estático); estáticos; discretos; redundantes ao texto (nunca substituem o rótulo); usados com função fixa — identidade do módulo, estado de conclusão, atenção/pegadinha e ação principal. Máximo de um ícone por função por bloco.

16.3. Se o usuário pedir exclusão de imagem ou ícone, remover img, picture, figure, svg, legendas e textos derivados, sem substituir silenciosamente por outro elemento visual.

17. VALIDAÇÃO BLOQUEANTE

17.1. Conteúdo visível:

- nenhum nome de IA no fluxo principal;
- nenhuma auditoria visível;
- nenhum histórico de criação;
- nenhuma informação técnica irrelevante;
- somente conteúdo útil ao estudo;
- Fontes e funcionamento fechado por padrão.

17.2. Ausência de áudio:

Buscar e bloquear:

<audio
<video
<source
new Audio
.play(
.pause(
currentTime
playbackRate
mediaSession
MediaMetadata
AudioContext
speechSynthesis
.mp3
.wav
.ogg
.flac
.m4a

17.3. Ausência de impressão:

Buscar e bloquear:

window.print
onclick="print()
>Imprimir<
Imprimir/PDF
@media print

17.4. Ausência de arquivos auxiliares e exportação não solicitada:

- nenhum JSON separado;
- nenhum manifesto;
- nenhum download automático;
- nenhuma função exportar/importar progresso sem pedido expresso;
- nenhum ZIP por padrão.

17.5. Estrutura:

- IDs únicos;
- links internos válidos;
- títulos em ordem;
- cabeçalho compacto;
- apenas Retomar, Buscar e Opções como ferramentas principais;
- no desktop, contêiner visível do cabeçalho e conteúdo principal com a mesma largura e alinhamento;
- fundo sticky em largura total permitido somente com contêiner interno alinhado ao main;
- navegação secundária recolhida;
- nenhum sidebar permanente por padrão;
- no celular, nenhum painel secundário antes do conteúdo;
- busca funcional;
- progresso funcional;
- localStorage funcional;
- botões compactos conforme §11, com área de toque efetiva de 48 × 48 CSS px em telas de toque;
- caixa flutuante de artigos de lei funcional offline (§19), sem texto legal fabricado;
- identidade visual e marcadores de extensão dos módulos presentes (§20);
- explicações visuais proporcionais ao conteúdo, com mapa geral e mini-mapas quando úteis (§21);
- texto dos mapas pesquisável e selecionável, sem transformar toda a explicação em imagem;
- mapas adaptados a fluxo vertical ou cards empilhados no celular, sem overflow horizontal geral;
- nenhuma foto ou ilustração não solicitada; ícones apenas conforme §16.2;
- nenhum overflow horizontal geral.

17.6. JavaScript:

- extrair e executar node --check em cada bloco JavaScript;
- console sem erros não tratados;
- ausência de eval, new Function e innerHTML inseguro.

17.7. Responsividade:

Testar celular, tablet quando possível, desktop, modo claro, modo escuro, zoom de 200%, teclado, foco, redução de movimento e texto ampliado.

17.8. Persistência:

Testar salvar, recarregar, retomar, reiniciar com confirmação e mudança de versão.

17.9. Não declarar teste em Android físico, TalkBack ou leitor de tela humano se ele não ocorreu.

18. ENTREGA

18.1. Entregar sempre o HTML inteiro e completo.

18.2. Nunca entregar patch, diff, trecho solto ou instrução do tipo "insira aqui".

18.3. Em correção de HTML existente, carregar o original integral antes de editar.

18.4. Gerar exatamente um arquivo .html, salvo pedido expresso em contrário.

18.5. Não gerar áudio, impressão, JSON, manifesto, ZIP, README, TXT, script, hash ou pasta auxiliar por padrão.

18.6. Nome recomendado:

<IA>_<MODELO>_<MATERIA>_HTML_ESTUDO_<CONVERSA>_<DATA>_vN.html

18.7. O nome do arquivo pode conter proveniência; o corpo visível não deve exibir IA, modelo ou processo de geração.

18.8. Só afirmar que o arquivo foi criado depois de confirmar sua existência e fornecer o artefato.

19. CAIXA FLUTUANTE DE ARTIGOS DE LEI (CONFERÊNCIA DUPLA)

19.1. Toda referência a dispositivo legal no corpo do estudo — "art. N" da CF, CC, CP, CPC, CPP, CDC, CLT, leis e resoluções — deve ser um elemento acionável (botão inline ou equivalente acessível), visualmente identificável como interativo sem poluir o texto.

19.2. Ao acionar, abrir caixa flutuante contendo, nesta ordem: identificação completa do dispositivo (diploma, artigo, parágrafo/inciso quando citado); o texto legal; e link de conferência para a fonte oficial, com prioridade Planalto (planalto.gov.br) e, alternativamente, Câmara dos Deputados, Senado Federal ou STF, abrindo em nova aba com rel="noopener".

19.3. Funcionamento offline obrigatório: o texto exibido na caixa fica embutido no próprio HTML. O link oficial é o único elemento dependente de internet e nunca pode ser essencial ao uso.

19.4. Anti-invenção: é proibido fabricar, completar de memória ou parafrasear texto legal apresentado como literal. O texto integral só entra na caixa se tiver sido conferido na fonte oficial durante a geração. Caso contrário, a caixa exibe a identificação do dispositivo, a síntese assumida no material com a marca "síntese — texto não conferido na fonte oficial nesta geração" e o link oficial para conferência.

19.5. A caixa vale inclusive quando o texto integral já consta no corpo do material: sua função é conferência dupla.

19.6. Acessibilidade da caixa: fechar por Esc e por clique fora; devolver o foco ao elemento de origem; navegável por teclado; rolagem interna própria; não travar a rolagem geral em telas pequenas; uma única caixa aberta por vez.

19.7. Proibido qualquer fetch, iframe ou incorporação remota do conteúdo legal; apenas href estático para a fonte oficial.

20. IDENTIDADE VISUAL DE MÓDULOS E MOTIVAÇÃO (TDAH)

20.1. Cada módulo deve ter fronteiras inequívocas de início e fim: borda superior ou faixa lateral na cor do módulo, badge "Módulo N de Y" e fecho visual claro, de modo que uma olhada rápida revele onde o módulo começa e onde termina.

20.2. Cada módulo deve exibir, junto ao título, um marcador de extensão que reduza a ansiedade de leitura: número de blocos ou tempo estimado de leitura (ex.: "5 blocos · ~4 min").

20.3. Cada módulo deve ter um ícone identificador estático (conforme §16.2) e cor própria do mapa cromático (§12.9), repetidos de forma consistente na navegação e no progresso.

20.4. Feedback de conclusão obrigatório: ao marcar o módulo como concluído, aplicar confirmação visual imediata e discreta — marca de conferido, mudança de cor para o verde de concluído e atualização do progresso global "X de Y módulos" — criando sensação de etapa vencida.

20.5. Gamificação leve permitida por padrão: contadores de módulos e questões, barra de progresso global e por bloco de questões, e sequência de acertos. Proibidos por padrão: sons, confetes, pontos/moedas, rankings, animações longas e qualquer elemento que dispute atenção com o conteúdo. Tudo deve respeitar o modo de baixa estimulação e prefers-reduced-motion.

20.6. Fundamento (resumo de pesquisa, sem exibir no HTML): codificação por cor por categoria acelera o reconhecimento e reduz carga cognitiva; feedback imediato de progresso (barras, marcas de conclusão, mini-vitórias) sustenta a motivação dopaminérgica no TDAH; início e fim claramente demarcados reduzem a sobrecarga; paletas de baixa saturação com acentos calmos evitam superestimulação; ícones e pictogramas apoiam o pensamento visual, desde que estáticos e redundantes ao texto.

21. EXPLICAÇÕES VISUAIS DIDÁTICAS

21.1. Conteúdos abstratos, comparativos, sequenciais, classificatórios ou relacionais devem, quando isso melhorar a compreensão, possuir representação visual didática no próprio HTML.

21.2. Priorizar:

- mapas conceituais;
- fluxos;
- linhas do tempo;
- árvores de classificação;
- quadros de comparação;
- relações de causa e efeito;
- sequências passo a passo;
- esquemas "conceito → distinção → pegadinha".

21.3. Não condensar toda a disciplina em uma única imagem ou mapa denso. Dividir preferencialmente em:

- um mapa geral sintético, com três a cinco ramos principais;
- mini-mapas por módulo ou assunto;
- aprofundamentos recolhidos.

21.4. Cada mapa deve conter preferencialmente:

- de três a cinco ramos principais;
- de cinco a nove nós inicialmente visíveis;
- uma ideia principal por nó;
- texto curto, normalmente de três a doze palavras por nó;
- no máximo um ícone estático por conceito ou função.

21.5. O texto dos mapas deve permanecer em elementos HTML semânticos, pesquisáveis, selecionáveis e ampliáveis. SVG inline curto pode ser usado para conectores, setas, formas e ícones, mas não deve converter todo o texto em imagem.

21.6. A explicação visual não substitui integralmente o conteúdo textual. Após o mapa, apresentar síntese curta, comparação, exemplo, pegadinha ou pergunta de recuperação ativa, conforme o assunto.

21.7. No celular, mapas horizontais devem transformar-se em fluxo vertical, linha do tempo vertical ou cards empilhados. Não exigir arraste horizontal da página para compreender o mapa.

21.8. Todo mapa deve continuar compreensível:

- sem depender de cor;
- com zoom de 200%;
- por teclado;
- no modo escuro;
- no modo de baixa estimulação;
- com prefers-reduced-motion;
- quando ícones não forem percebidos.

21.9. Cores, ícones, posição e setas não substituem rótulos textuais. Relações essenciais devem ser declaradas também em texto acessível.

21.10. Detalhes, exceções, fundamentos extensos e controvérsias devem ficar recolhidos, preservando uma visão inicial curta.

21.11. Informações jurídicas, legais e doutrinárias devem ser verificadas antes da representação visual. Simplificação visual não autoriza transformar classificação controvertida em regra uniforme. Divergência deve ser marcada expressamente.

21.12. A ordem pedagógica recomendada por módulo é:

1. título, badge e marcador de extensão;
2. mini-mapa visual;
3. regra central em uma frase;
4. comparação, sequência ou classificação;
5. exemplo;
6. pegadinha;
7. aprofundamento recolhido;
8. recuperação ativa;
9. conclusão do módulo.

21.13. Proibir:

- infográfico rasterizado grande como conteúdo principal;
- texto minúsculo;
- excesso de cruzamento de linhas;
- mais de três níveis de profundidade simultaneamente visíveis;
- animações ou movimento decorativo;
- elementos sem função didática;
- ícones ambíguos;
- repetição do mesmo mapa;
- mais de um mapa denso simultaneamente aberto;
- mapa cuja leitura dependa exclusivamente de cor, posição ou imagem.