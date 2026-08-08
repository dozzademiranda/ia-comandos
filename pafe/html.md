# html.md — P.A.F.E. HTML público

**Versão:** 2026-08-07.6  
**Estado:** núcleo público sanitizado  
**Escopo:** geração de HTML de estudo pelo P.A.F.E.

## 1. Regra central

`/pafe html` gera exatamente **um arquivo HTML completo**, autocontido, offline, responsivo e acessível, sem áudio, sem impressão e sem arquivos auxiliares por padrão.

Este núcleo público define o comportamento obrigatório. Espelhos privados em Box/Google Drive podem conter extensão de acessibilidade e preferências de apresentação mais detalhada, desde que não contrariem este arquivo.

## 2. Artefato único

1. Gerar somente um `.html`, salvo pedido expresso em contrário.
2. Incorporar CSS, JavaScript e dados textuais no próprio arquivo.
3. Não depender de CDN, biblioteca remota, fonte externa, API, analytics ou banco remoto.
4. O HTML deve funcionar offline e, quando tecnicamente possível, por `file://`.
5. Não criar por padrão ZIP, README, TXT, JSON, YAML, manifesto, hash, CSS separado, JS separado ou pasta auxiliar.
6. `localStorage` é permitido para progresso, preferências e retomada.

## 3. Proibição absoluta de áudio

É proibido inserir, controlar, reproduzir, sincronizar, referenciar ou simular áudio no HTML.

Bloquear, entre outros:
- `<audio>`;
- `<video>`;
- `<source>`;
- `new Audio()`;
- `.play()`;
- `.pause()`;
- `currentTime`;
- `playbackRate`;
- `AudioContext`;
- `speechSynthesis`;
- referências `.mp3`, `.wav`, `.ogg`, `.flac` ou `.m4a`;
- player, controles, timestamps ou espaço reservado para mídia futura.

A existência de áudio em outra etapa do P.A.F.E. não autoriza integração ao HTML.

## 4. Proibição de impressão

Não inserir por padrão:
- botão Imprimir;
- Imprimir/PDF;
- `window.print()`;
- `onclick="print()"`;
- `@media print`.

Impressão só entra mediante pedido expresso específico.

## 5. Conteúdo visível

Cada bloco visível deve ajudar a compreender, diferenciar, memorizar, resolver questões, revisar erros ou executar estratégia de estudo.

Não exibir no fluxo principal:
- nomes de IAs, modelos ou plataformas;
- comparação entre IAs;
- erros de outras IAs;
- inventário de anexos;
- histórico de elaboração;
- ferramentas, scripts, hashes ou caminhos internos;
- justificativas técnicas do processo de geração.

Quando realmente necessário, concentrar fontes e funcionamento em seção discreta ao final, fechada por padrão.

## 6. Tela inicial e navegação

1. Abrir diretamente no estudo, sem tela técnica intermediária.
2. Cabeçalho compacto com tema/disciplina, objetivo, progresso, **Retomar**, **Buscar** e **Opções**.
3. Ferramentas secundárias permanecem recolhidas.
4. Não usar sidebar permanentemente aberta como padrão.
5. No celular, conteúdo principal vem antes de menus e filtros.
6. No desktop, cabeçalho e conteúdo principal compartilham largura útil e alinhamento.

## 7. Opções e busca

### Opções
Pode agrupar:
- modo automático/celular/desktop;
- escala de texto;
- espaçamento;
- tema;
- modo foco;
- baixa estimulação;
- flashcards;
- revisar erros;
- notas;
- glossário;
- limpar progresso com confirmação;
- navegação entre módulos.

Não incluir impressão nem exportação/importação de progresso sem pedido expresso.

### Busca
1. Abrir somente após acionamento.
2. Funcionar offline.
3. Pesquisar tema, conceito, referência e questão.
4. Permitir limpar filtro e informar ausência de resultados.

## 8. Progresso e retomada

Quando útil, persistir em `localStorage`:
- última seção significativa;
- módulos concluídos;
- questão atual;
- respostas e erros;
- flashcards revisados;
- notas;
- modo de visualização;
- tema, escala e espaçamento;
- baixa estimulação.

**Retomar** deve levar ao último ponto significativo, não apenas à posição bruta de rolagem.

## 9. Responsividade e tipografia

1. Suportar celular e desktop sem overflow horizontal geral.
2. Texto de estudo alinhado à esquerda, nunca justificado.
3. Fonte sans-serif do sistema.
4. Corpo preferencial próximo de 16 px, evitando redução excessiva em telas estreitas.
5. `line-height` confortável, aproximadamente 1,55–1,70.
6. Largura principal de leitura preferencial em torno de 68–80ch.
7. Parágrafos curtos e negrito seletivo.
8. Suportar zoom de 200% sem perda de conteúdo ou função.

## 10. Controles e toque

1. Controles podem ser visualmente compactos.
2. Em telas de toque, preservar área clicável efetiva confortável, preferencialmente ao menos 48 × 48 CSS px.
3. Ícone pode ser menor que a área clicável.
4. Separar ações destrutivas de ações principais.
5. Rótulos devem ser claros e não depender só de ícone.

## 11. Hierarquia visual

1. Usar paleta curta, baixa saturação, contraste verificável e consistência.
2. Cor nunca é o único veículo de significado.
3. Estados correto/concluído, atenção e erro devem ter também rótulo ou símbolo compreensível.
4. Módulos podem receber acentos visuais próprios, discretos e consistentes no corpo, navegação e progresso.
5. Evitar animação contínua, piscar, excesso de sombras e estímulos concorrentes.
6. Respeitar `prefers-reduced-motion`.

## 12. Baixa carga cognitiva

Priorizar:
- previsibilidade;
- divulgação progressiva;
- respostas inicialmente ocultas;
- aprofundamentos recolhidos;
- questões uma por vez;
- ferramentas secundárias fechadas por padrão;
- modo foco quando útil;
- modo de baixa estimulação;
- feedback discreto de progresso;
- início e fim inequívocos dos módulos.

Esses princípios são requisitos de design gerais deste sistema e não devem ser apresentados como diagnóstico ou perfil pessoal do usuário.

## 13. Questões, flashcards e revisão

1. Apresentar questões uma por vez.
2. Não antecipar gabarito.
3. Após resposta, mostrar em blocos curtos: resposta correta, fundamento, pegadinha e como reconhecer na prova.
4. Permitir revisar erros e refazer questões quando isso fizer parte do pedido.
5. Flashcards permanecem fechados até ação do usuário.

## 14. Acessibilidade, segurança e privacidade

Obrigatório:
- HTML semântico;
- hierarquia correta de títulos;
- link “Ir para o conteúdo”;
- foco visível;
- navegação por teclado;
- contraste suficiente;
- conteúdo compreensível sem depender de cor;
- mensagens de estado acessíveis;
- zoom do navegador não bloqueado.

Segurança:
- não usar analytics por padrão;
- não enviar conteúdo sensível a serviço externo sem autorização;
- evitar `innerHTML` com dados não confiáveis;
- preferir `textContent`, `createElement` e atributos controlados;
- proibir `eval()` e `new Function()`;
- não registrar conteúdo sensível no console.

## 15. Imagens, ícones e diagramas

1. Fotos e ilustrações complexas somente quando pedidas ou materialmente úteis.
2. Ícones leves podem ser SVG inline curto ou caractere estático e devem ser redundantes ao texto.
3. Não transformar conteúdo textual principal em imagem.
4. Para conteúdo abstrato, comparativo, sequencial ou classificatório, usar quando útil:
   - mapa conceitual;
   - fluxo;
   - linha do tempo;
   - árvore de classificação;
   - quadro comparativo;
   - causa e efeito;
   - sequência passo a passo.
5. O texto dos mapas deve permanecer pesquisável e selecionável.
6. No celular, transformar mapas horizontais em fluxo vertical ou cards empilhados.
7. Relações essenciais também devem existir em texto acessível.

## 16. Dispositivos legais — conferência dupla

Quando houver referência jurídica relevante:
1. permitir abrir caixa acessível com identificação do dispositivo;
2. embutir texto literal apenas quando efetivamente conferido em fonte oficial;
3. se não conferido, marcar claramente como síntese e fornecer referência oficial para conferência;
4. nunca fabricar texto legal literal;
5. o conteúdo essencial deve continuar funcionando offline;
6. link oficial pode depender de internet, mas não o funcionamento do estudo.

## 17. Validação bloqueante

Antes da entrega, verificar:

### Conteúdo
- nenhum nome de IA no fluxo principal;
- nenhuma auditoria ou histórico técnico visível;
- nenhum dado pessoal usado como decoração ou metadado de interface;
- somente conteúdo útil ao estudo.

### Ausência de áudio
Buscar e bloquear:
```text
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
```

### Ausência de impressão
Buscar e bloquear:
```text
window.print
onclick="print()
>Imprimir<
Imprimir/PDF
@media print
```

### Estrutura
- IDs únicos;
- links internos válidos;
- títulos em ordem;
- busca funcional;
- progresso e retomada funcionais;
- controles acessíveis;
- sem overflow horizontal geral;
- responsividade em celular e desktop;
- zoom de 200%;
- teclado e foco;
- modo claro/escuro quando implementado;
- redução de movimento.

### JavaScript
- validar sintaxe quando houver ambiente de execução;
- proibir `eval` e `new Function`;
- evitar `innerHTML` inseguro;
- não declarar testes que não foram realmente executados.

## 18. Entrega

1. Entregar o HTML inteiro e completo.
2. Nunca entregar patch, diff ou “insira aqui”.
3. Em correção de HTML existente, carregar o original integral antes de editar.
4. Gerar exatamente um `.html`, salvo pedido expresso em contrário.
5. Não gerar áudio, impressão, JSON, manifesto, ZIP, README, TXT, script, hash ou pasta auxiliar por padrão.
6. Só afirmar que o arquivo foi criado depois de confirmar sua existência e disponibilização real.

## 19. Precedência

1. Pedido expresso atual do usuário.
2. Este `html.md` para requisitos públicos obrigatórios.
3. Extensão privada correspondente em Box/Drive, quando acessível e não conflitante.
4. `pafe/README.md` e governança geral.

Nenhum overlay de áudio ou de plataforma pode afastar as proibições centrais deste arquivo.
