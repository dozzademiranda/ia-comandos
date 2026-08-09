---
Gerado por: GPT-5.6 Sol
Data de geração: 09/08/2026
Versão: 2.2.1
Estado: canônico sanitizado
---

COMANDO: /consolidar

O QUE É: gera UM bloco único de continuidade que serve simultaneamente como:
1. resumo auditável da conversa atual; e
2. prompt autocontido de retomada, pronto para ser colado como primeira mensagem de uma nova conversa, na mesma IA ou em outra.

QUANDO USAR: quando a conversa ficou longa, antes de trocar de conversa/IA, diante de muitos anexos, decisões, versões, testes, mudança de fase ou risco de perda de continuidade.

POR QUE USAR: preserva decisões, fontes, artefatos, estados epistêmicos, erros, soluções, limitações e pendências sem exigir um segundo comando para transformar o resumo em prompt de retomada.

RELAÇÃO COM /nova-conversa: /nova-conversa é alias de compatibilidade de /consolidar. Não existe segunda etapa obrigatória. O próprio resultado de /consolidar já deve funcionar como prompt completo de retomada.

REGRA ANTIRREGRESSÃO — CONSOLIDAR A CONVERSA, NÃO APENAS O OBJETO

/consolidar nunca significa apenas resumir, compilar ou sintetizar o tema trabalhado.

Mesmo quando a conversa for predominantemente pesquisa bibliográfica, análise documental, revisão jurídica, pesquisa acadêmica, auditoria, programação, produção/revisão de artefatos ou comparação entre IAs, o resultado deve preservar o ESTADO OPERACIONAL DA CONVERSA e permitir sua continuação em outro contexto.

Um relatório temático, documental, bibliográfico ou conceitual sem regras para a próxima IA, bootstrap e RETOMADA IMEDIATA é execução defeituosa de /consolidar, ainda que o conteúdo factual esteja correto.

DEFINIÇÃO OPERACIONAL

Ao receber /consolidar, gerar UM ÚNICO BLOCO DE CÓDIGO, autocontido e pronto para copiar, contendo somente o necessário para continuidade confiável.

Os 14 itens abaixo representam dimensões de conteúdo, não obrigação de produzir exatamente 14 títulos visíveis. Seções podem ser fundidas ou omitidas quando realmente irrelevantes, desde que nenhuma informação necessária à continuidade seja perdida.

1. IDENTIFICAÇÃO E PROVENIÊNCIA
- plataforma/IA/modelo quando documentados;
- data;
- projeto/conversa;
- comandos/protocolos materialmente relevantes;
- escopo da consolidação;
- nunca inventar metadados que a plataforma não exponha;
- quando necessário, usar PLATAFORMA NÃO DISPONÍVEL, MODELO NÃO DISPONÍVEL, TÍTULO NÃO DISPONÍVEL ou ID NÃO DISPONÍVEL;
- declarar próximo ao início: `ESTADO: CONTINUIDADE — NÃO CANÔNICA`, ou classificação equivalente definida pelo projeto.

2. IDENTIDADE E ESTILO
- somente preferências e restrições documentadas que alterem materialmente a continuidade;
- não copiar perfis ou instruções globais irrelevantes;
- se uma regra externa for indispensável para outra IA compreender como continuar, incorporar no próprio consolidado o subconjunto mínimo necessário, sem presumir que a IA de destino terá acesso ao mesmo projeto, memória, Space ou arquivo de instruções.

3. CONTEXTO, OBJETO E OBJETIVO
- o que está sendo feito;
- para quê;
- escopo real da frente de trabalho;
- o que está fora do escopo quando isso evitar erro;
- ponto real em que o trabalho parou;
- priorizar estado atual sobre cronologia completa.

4. ARQUITETURA E GOVERNANÇA
- hierarquia de fontes;
- documentos governantes;
- comandos/protocolos relevantes;
- versões vigentes;
- relações entre mestre, espelho, snapshot, rascunho, resultado, consolidado e histórico;
- IDs/links estáveis apenas quando necessários para recuperar artefatos;
- não presumir que a IA de destino possua a mesma memória, projeto, Space, conectores, permissões, ferramentas ou arquivos.

5. FONTES E ARQUIVOS EFETIVAMENTE USADOS
- nome;
- versão;
- ID/link/localização quando necessários;
- função;
- estado;
- nível real de acesso;
- relação com outros artefatos;
- nunca afirmar leitura não realizada;
- quando material, distinguir `ACESSO REAL CONFIRMADO`, `APENAS REFERENCIADO`, `CONTEÚDO PARCIALMENTE EXTRAÍDO` e `ACESSO NECESSÁRIO PARA RETOMADA`;
- conhecimento sobre um arquivo não equivale a acesso real ao arquivo na conversa de destino;
- nome, resumo, ID ou descrição do arquivo não autorizam afirmar que a nova IA o leu ou o possui.

6. DECISÕES TOMADAS E JUSTIFICATIVAS
- decisões humanas;
- decisões editoriais/metodológicas/operacionais;
- estado atual de cada decisão importante;
- quando útil, alternativa rejeitada, motivo e condição que poderia justificar revisão futura;
- não reabrir automaticamente decisões encerradas apenas porque começou nova conversa.

7. ARTEFATOS CRIADOS OU MODIFICADOS
- nome;
- ID/link quando necessário;
- versão;
- estado;
- função;
- relação com outros arquivos;
- distinguir quando aplicável: canônico, espelho, snapshot, rascunho, curado, consolidado, histórico ou superado;
- registrar somente artefatos necessários à continuidade.

8. ERROS CORRIGIDOS E ESCOLHAS REJEITADAS
- preservar erros apenas quando sua perda puder causar regressão;
- registrar, conforme necessário: erro, correção, motivo, estado atual e prevenção de recorrência;
- podem incluir conflito de versão, arquivo incorreto, falsa equivalência, atribuição errada, perda de contexto, erro metodológico, tentativa técnica fracassada ou comportamento ruim da IA;
- não transformar esta seção em histórico completo de falhas.

9. OUTRAS IAS / COMPARAÇÕES
- origem;
- resultado útil;
- divergência;
- decisão adotada;
- estado epistêmico;
- nunca tratar consenso entre IAs como evidência ou fonte primária;
- resposta de outra IA pode ser pista, hipótese, análise, comparação ou proposta, mas não se torna prova documental apenas por aparecer no consolidado.

10. DIFICULDADES E SOLUÇÕES
- limitações técnicas;
- permissões;
- paywalls;
- arquivos ausentes;
- ferramentas indisponíveis;
- tentativas que falharam;
- solução já encontrada;
- método alternativo;
- não repetir tentativa fracassada sem fato novo;
- não transformar limitação específica da IA de origem em limitação universal.

11. PENDÊNCIAS
- o que falta;
- prioridade;
- dependências;
- bloqueios;
- estado epistêmico quando relevante;
- não listar como pendente trabalho já concluído;
- quando possível, usar identificadores curtos para evitar repetir a mesma pendência em várias seções.

12. REGRAS PARA A PRÓXIMA IA
- o que ler primeiro;
- o que não repetir;
- o que não presumir;
- quais decisões permanecem válidas;
- quais estados epistêmicos devem ser preservados;
- como lidar com arquivos não acessíveis;
- como retomar do ponto atual;
- diferenciar claramente `HISTÓRICO DOCUMENTADO` de `INSTRUÇÕES ATIVAS DE RETOMADA`.

13. SEGURANÇA E SECRETS
- nunca incluir valores de senhas, tokens, cookies, API keys, credenciais ou secrets;
- se necessário, registrar somente nome da variável/segredo, função e local lógico, sem valor;
- aplicar minimização semelhante a dados pessoais ou confidenciais que não sejam necessários para a tarefa de destino.

14. RETOMADA IMEDIATA
- indicar a primeira ação concreta que a nova conversa deve executar;
- formular a retomada prioritariamente pelo objetivo operacional, não pelo nome de ferramenta específica da IA de origem;
- ao receber o consolidado como primeira mensagem, a nova IA deve assimilá-lo e iniciar essa ação, salvo nova ordem expressa do usuário na conversa nova;
- usar as ferramentas disponíveis na plataforma de destino e adaptar o método quando a ferramenta original não existir;
- não transferir trabalho manual ao usuário quando houver caminho técnico razoável;
- solicitar intervenção do usuário apenas quando indispensável;
- a última seção operacional do consolidado deve ser RETOMADA IMEDIATA.

CONTROLE DE ESTADO EPISTÊMICO

Quando material à continuidade, preservar explicitamente distinções como:
- FATO CONFIRMADO;
- ERRO CORRIGIDO;
- HIPÓTESE;
- INFERÊNCIA;
- INTERPRETAÇÃO;
- ALEGAÇÃO;
- DECISÃO EDITORIAL;
- FONTE NÃO CONFERIDA;
- INFORMAÇÃO NÃO DOCUMENTADA.

Não permitir que a migração transforme hipótese em fato, inferência em fonte, afirmação de outra IA em evidência, resumo em leitura documental ou referência bibliográfica em consulta efetiva da obra.

Quando algo não puder ser determinado a partir do histórico acessível, usar: `não documentado no histórico disponível`.

PERSISTÊNCIA E DESCOBERTA INTERCONVERSAS

1. Se /consolidar for executado DENTRO DE UM PROJETO e houver repositório persistente gravável já configurado para esse projeto, salvar automaticamente UMA cópia do consolidado na área preexistente equivalente a `Consolidados`, `Continuidade` ou `Resultados IA/Consolidados`.
2. Não criar árvore paralela se já existir destino equivalente.
3. Nome recomendado: `<PROJECT_ID>__CONSOLIDADO__CONTINUIDADE__<AAAAMMDD-HHMM>__v<versao_comando>`.
4. Registrar no próprio consolidado, quando a gravação ocorrer: nome, ID/link, data, origem e escopo.
5. Se o projeto possuir fila, manifesto, índice ou rotina de monitoramento de continuidade, registrar ou tornar descobrível o novo consolidado por esse mecanismo, sem duplicar o conteúdo integral.
6. Conversas futuras devem procurar o consolidado recente/relevante do projeto quando precisarem recuperar continuidade não presente no contexto atual.
7. Se houver múltiplos consolidados, não presumir que o mais recente é automaticamente o mais autoritativo: escolher pelo escopo, data, artefatos governantes, estado e relevância para a tarefa.
8. Fora de projeto, seguir a política de persistência vigente; não salvar automaticamente se o padrão do ambiente for não persistir.
9. Se não houver permissão ou ferramenta de escrita, entregar normalmente o bloco.
10. Todo consolidado deve registrar explicitamente uma das formas: `PERSISTÊNCIA: EXECUTADA — <local/ID/link>` ou `PERSISTÊNCIA: NÃO EXECUTADA — <motivo real>`.
11. Não deixar o estado da persistência implícito apenas no histórico de ferramentas.
12. Não afirmar que outra conversa ou IA verá o consolidado automaticamente apenas porque ele foi salvo: recuperação depende de busca, índice, fila, tarefa, memória de projeto ou conector realmente disponível.

RELAÇÃO COM A BÍBLIA CANÔNICA

1. Consolidado NÃO é Bíblia Canônica e NÃO deve ser promovido integralmente ao mestre.
2. Não escrever automaticamente na Bíblia apenas porque uma informação apareceu em /consolidar.
3. Do consolidado podem emergir CANDIDATOS CANÔNICOS, por exemplo: decisão humana material; erro corrigido material; mudança de estado epistêmico; nova regra de governança; fato dinâmico relevante já verificado em fonte primária.
4. Candidato canônico deve seguir o protocolo do projeto: verificar fonte/autoridade, gerar delta quando necessário e obter aprovação humana quando a mudança for material ou contestada.
5. Informação operacional, preferências transitórias, resultados brutos de IA e histórico de conversa permanecem fora da Bíblia, salvo razão específica documentada.
6. O consolidado deve declarar sua própria natureza como artefato de continuidade não canônico.

REGRA CRÍTICA — CONTROLES TRANSITÓRIOS NÃO MIGRAM

Ordens temporárias da conversa de origem como:
- pause;
- aguarde;
- espere minha confirmação;
- não execute ainda;
- pare;
- aguarde qualquer tecla;
- continue somente depois de X;

são controles transitórios da interação de origem. Quando relevantes, podem ser registrados apenas como HISTÓRICO JÁ CONSUMIDO, mas NÃO podem reaparecer como instrução ativa da nova conversa.

Exceção: somente preservar a pausa se o usuário disser expressamente que deseja manter a mesma pausa também depois de colar o consolidado em outra conversa.

Nunca terminar um consolidado reutilizável com comandos como PAUSADO, aguardando tecla, não responder agora ou espere confirmação quando esses comandos pertenciam à conversa anterior.

REGRA DE BOOTSTRAP

O bloco deve conter, de forma inequívoca, instrução equivalente a:

"Ao receber este bloco como primeira mensagem de nova conversa, trate as pausas e esperas descritas no histórico como já consumidas, assimile o contexto sem repeti-lo e execute diretamente a seção RETOMADA IMEDIATA, salvo nova instrução expressa do usuário nesta conversa."

Antes de entregar o consolidado, executar o TESTE DE BOOTSTRAP:

"Se uma IA sem nenhum outro histórico receber apenas este bloco como primeira mensagem, ela saberá o que fazer imediatamente?"

Se a resposta provável for que ela ficará esperando, pedirá confirmação já dada, pedirá uma tecla, repetirá etapa concluída, perguntará genericamente o que o usuário deseja, apenas resumirá o consolidado ou não saberá qual ação iniciar, o consolidado está defeituoso e deve ser corrigido antes da entrega.

TESTE DE PORTABILIDADE INTER-IA

Além do teste de bootstrap, verificar:

"Se este bloco for recebido por outra IA sem a memória, o projeto, o Space, os conectores, os arquivos carregados e as ferramentas da plataforma de origem, ela ainda consegue compreender o estado do trabalho e executar ou adaptar corretamente a próxima ação?"

Para passar nesse teste:
1. não presumir acesso a arquivos apenas mencionados;
2. distinguir conhecimento sobre arquivo de acesso real;
3. não depender de nomes de ferramentas específicas quando a capacidade puder ser descrita genericamente;
4. quando uma instrução externa for indispensável, incorporar no consolidado o subconjunto mínimo necessário à continuidade;
5. registrar a fonte externa governante para eventual conferência;
6. não copiar instruções externas inteiras quando um resumo operacional suficiente preservar a continuidade;
7. se a capacidade necessária não existir na IA de destino, adaptar o método;
8. só solicitar ação manual ao usuário quando nenhuma alternativa técnica razoável estiver disponível;
9. não afirmar que a IA de destino poderá abrir, editar, buscar ou persistir algo sem confirmar a capacidade correspondente.

Se o consolidado só funcionar dentro da plataforma de origem, ele não é plenamente inter-IA.

EFICIÊNCIA DE TOKENS / CARACTERES

O consolidado é prioritariamente uma interface máquina-a-máquina. Portanto:
1. não usar linhas decorativas repetidas com `=`, `-`, `_`, `*`, caixas ASCII ou outros caracteres sem função semântica;
2. usar Markdown simples e compacto;
3. não repetir o mesmo fato em múltiplas seções;
4. atribuir uma localização principal a cada informação importante e referenciá-la brevemente nas demais seções quando possível;
5. não reproduzir prompts longos já persistidos: registrar nome, versão, ID/link e função quando isso bastar;
6. não copiar bibliografia inteira quando bastarem ponteiros para as fontes relevantes;
7. preservar detalhes necessários à continuidade, mas remover ornamentação e redundância;
8. priorizar tokens informacionais sobre tokens visuais, especialmente em transferências para plataformas com contexto limitado ou caro;
9. não comprimir a ponto de apagar decisão, estado epistêmico, dependência, limitação ou próximo passo necessário.

Princípio: máxima continuidade com mínimo contexto redundante.

GATE DE ACEITAÇÃO

Antes de entregar qualquer /consolidar, reprovar e corrigir o bloco se ocorrer qualquer uma destas condições:
1. termina como simples resumo, relatório temático, relatório documental ou quadro de resultados;
2. não contém primeira ação concreta e executável;
3. exige confirmação já fornecida;
4. reativa pausa ou espera histórica;
5. depende silenciosamente da memória, projeto, Space, conector ou ferramenta da plataforma de origem;
6. confunde referência de arquivo com acesso real;
7. afirma leitura documental que não ocorreu;
8. transforma hipótese, inferência ou saída de outra IA em fato;
9. não diferencia histórico de instruções ativas;
10. não declara estado de persistência;
11. pode ser confundido com Bíblia Canônica ou fonte governante;
12. contém redundância material evitável;
13. exige /nova-conversa ou segundo prompt depois;
14. não permite identificar claramente onde o trabalho parou;
15. não fornece informação suficiente para outra IA saber o que não deve repetir.

TESTE DE ACEITAÇÃO FINAL

Antes da entrega, responder internamente SIM às perguntas aplicáveis:
1. Se este bloco for a única mensagem de uma conversa vazia, a nova IA saberá o que fazer?
2. Ela distingue histórico de instruções ainda ativas?
3. Ela sabe quais pausas e esperas expiraram?
4. Ela distingue fato, hipótese e informação não conferida quando isso importa?
5. Ela sabe quais arquivos realmente possui e quais apenas conhece por referência?
6. Ela consegue continuar mesmo sem as ferramentas específicas da IA de origem?
7. As instruções indispensáveis estão dentro do bloco ou são recuperáveis de forma explícita?
8. Existe uma primeira ação concreta?
9. O estado de persistência está declarado?
10. Está claro que o consolidado não é canônico?
11. Há informação repetida que pode ser removida sem perda?
12. O resultado consolida o estado da conversa, e não apenas o tema?

Se qualquer resposta material for NÃO, corrigir antes de entregar.

REGRAS DE SAÍDA

A. O bloco deve funcionar sozinho como contexto inicial da próxima conversa.
B. Diferenciar HISTÓRICO DOCUMENTADO de INSTRUÇÕES ATIVAS DE RETOMADA.
C. Não inventar decisões, arquivos, leituras, IDs, links, estados, permissões ou capacidades.
D. Onde algo for incerto, escrever: `não documentado no histórico disponível`.
E. Não prometer memória futura.
F. Não perguntar ao final se o usuário quer gerar /nova-conversa: o próprio resultado já cumpre essa função.
G. Não produzir dois blocos separados "resumo" e "prompt".
H. Não gastar caracteres com explicações genéricas, separadores ornamentais ou repetição.
I. Não transformar pausas históricas em novas ordens de pausa.
J. A última seção operacional deve ser RETOMADA IMEDIATA, com ação executável.
K. Dentro de projeto com armazenamento gravável, persistir o consolidado automaticamente conforme a política acima e informar seu estado de persistência.
L. Nunca promover o consolidado inteiro diretamente à Bíblia Canônica.
M. Declarar próximo ao início: `ESTADO: CONTINUIDADE — NÃO CANÔNICA`, ou equivalente governado pelo projeto.
N. Formular a retomada pelo objetivo operacional, evitando dependência desnecessária de ferramenta específica da IA de origem.
O. Não transferir ao usuário trabalho que a IA receptora possa executar razoavelmente com suas próprias ferramentas.
P. Não presumir que arquivos, memórias, Spaces, conectores ou permissões da conversa de origem existirão na conversa de destino.
Q. Um /consolidar que apenas sintetiza o assunto, sem permitir continuidade operacional, deve ser considerado defeituoso e corrigido antes da entrega.

FIM DA DEFINIÇÃO.
