---
Gerado por: GPT-5.6 Sol
Data de geração: 21/08/2026
Versão: 2.5.0
Estado: CANÔNICO SANITIZADO
Base: consolidar.md v2.4.0 + handoff curto validado via Caixa Postal /tarefa + fallback integral
---

COMANDO: /consolidar

## O QUE É

Produz um ARTEFATO INTEGRAL DE CONTINUIDADE que registra o estado operacional da conversa e permite retomada confiável na mesma conversa, em conversa sucessora ou em outra IA.

O artefato integral sempre existe e é finalizado antes da persistência. A interface humana é adaptativa e possui três modos:
- TAREFA: o artefato fica persistido no repositório e uma TASK de handoff validada é criada; o chat mostra somente `/tarefa <TASK_ID>`;
- RECIBO: o artefato fica persistido e o chat mostra apenas metadados mínimos, quando não há necessidade de transporte imediato;
- INTEGRAL: o bloco completo é mostrado quando a persistência/handoff não puder ser validada ou quando o usuário pedir o conteúdo.

A linha `/tarefa <TASK_ID>` é apenas a chave de transporte; nunca substitui semanticamente o artefato integral persistido.

A operação possui três camadas:
A. ARTEFATO INTEGRAL DE CONTINUIDADE
- contém o estado necessário para continuidade;
- possui RUN_ID;
- não depende do resultado posterior da transação;
- não é reescrito apenas para inserir estados pós-gravação.

B. TRANSAÇÃO DE PERSISTÊNCIA
- resolve residência;
- grava CURRENT e SNAPSHOT quando aplicável;
- relê;
- compara;
- valida;
- testa recuperação direta.

C. HANDOFF / ENTREGA
- quando possível, cria TASK de continuidade na Caixa Postal Multi-IA existente;
- valida TASK_ID, TASK_REF, residência, conteúdo e referências ao consolidado;
- determina MODO DE ENTREGA;
- produz TAREFA, RECIBO ou FALLBACK INTEGRAL.

Estados pós-gravação pertencem à transação/handoff e não precisam ser inseridos novamente no artefato integral.

## QUANDO USAR

Quando a conversa ficou longa, antes de trocar de conversa/IA, diante de muitos anexos, decisões, versões, testes, mudança de fase, risco de perda de continuidade ou quando se deseja atualizar/inicializar uma conversa a partir do estado persistido.

## RELAÇÃO COM /nova-conversa

`/nova-conversa` continua alias de compatibilidade de `/consolidar` e sinaliza portabilidade imediata.

Quando a Caixa Postal `/tarefa` e o Google Drive aplicável estiverem acessíveis e todos os gates de handoff passarem, `/nova-conversa` e `/consolidar` devem preferir MODO DE ENTREGA: TAREFA, entregando somente uma linha `/tarefa <TASK_ID>`.

Se o handoff curto não puder ser comprovado, usar MODO DE ENTREGA: INTEGRAL. Não entregar ao usuário uma chave não validada.

## 1. REGRA ANTIRREGRESSÃO

`/consolidar` nunca significa apenas resumir, compilar ou sintetizar o tema. O artefato deve preservar o ESTADO OPERACIONAL DA CONVERSA e permitir continuação confiável em outro contexto.

Relatório temático sem regras para a próxima IA, sem estado material suficiente ou sem RETOMADA IMEDIATA executável é defeituoso.

A economia obtida pela linha curta `/tarefa` nunca autoriza reduzir o conteúdo persistido.

## 2. DEFINIÇÃO DO ARTEFATO INTEGRAL

Sempre gerar internamente UM ÚNICO BLOCO autocontido contendo, quando material:
1. IDENTIFICAÇÃO E PROVENIÊNCIA;
2. IDENTIDADE E ESTILO;
3. CONTEXTO, OBJETO E OBJETIVO;
4. ARQUITETURA E GOVERNANÇA;
5. FONTES E ARQUIVOS EFETIVAMENTE USADOS;
6. DECISÕES TOMADAS E JUSTIFICATIVAS;
7. ARTEFATOS CRIADOS OU MODIFICADOS;
8. ERROS CORRIGIDOS E ESCOLHAS REJEITADAS;
9. OUTRAS IAS / COMPARAÇÕES;
10. DIFICULDADES E SOLUÇÕES;
11. PENDÊNCIAS;
12. REGRAS PARA A PRÓXIMA IA;
13. SEGURANÇA E SECRETS;
14. RETOMADA IMEDIATA.

As dimensões podem ser fundidas para reduzir redundância sem perda de continuidade.

Próximo ao início declarar:
ESTADO: CONTINUIDADE — NÃO CANÔNICA
RUN_ID: <identificador único da execução>

Nunca inventar plataforma, modelo, título, IDs, arquivos, versões, leituras ou capacidades.

## 3. AUTOCONTENÇÃO E PONTEIROS

Autocontenção significa que uma IA receptora, recebendo o artefato integral, consegue compreender o estado e executar corretamente RETOMADA IMEDIATA.

Ponteiros como nome, ID, link, versão, hash, caminho, TASK_REF e CONTINUITY_REF podem substituir a reprodução integral de documentos externos quando seu corpo completo não for necessário.

Ponteiros NÃO podem substituir fatos materiais, decisões vigentes, restrições, resultados estabelecidos, erros corrigidos cuja perda cause regressão, estados epistêmicos, pendências, dependências, regras operacionais, instruções para a próxima IA ou conteúdo necessário à RETOMADA IMEDIATA.

Regra: PONTEIRO PODE SUBSTITUIR O OBJETO EXTERNO; NÃO PODE SUBSTITUIR O ESTADO NECESSÁRIO DA CONVERSA.

## 4. ESTADOS DE ACESSO

Quando material, distinguir:
- ACESSO REAL CONFIRMADO;
- APENAS REFERENCIADO;
- CONTEÚDO PARCIALMENTE EXTRAÍDO;
- ACESSO NECESSÁRIO PARA RETOMADA;
- REFERÊNCIA DOCUMENTADA — ACESSO NÃO CONFIRMADO NESTA IA;
- FONTE CANÔNICA: IDENTIFICADA — CONTEÚDO NÃO MATERIALIZADO.

Conhecimento sobre arquivo não equivale a acesso real. Metadados, SHA, tamanho, path ou confirmação de download não equivalem à leitura do corpo.

## 5. CONTROLE DE ESTADO EPISTÊMICO

Quando material, preservar: FATO CONFIRMADO; ERRO CORRIGIDO; HIPÓTESE; INFERÊNCIA; INTERPRETAÇÃO; ALEGAÇÃO; DECISÃO EDITORIAL; FONTE NÃO CONFERIDA; INFORMAÇÃO NÃO DOCUMENTADA.

Não transformar hipótese em fato, inferência em fonte, resposta de IA em evidência, referência em leitura ou perda de acesso em perda automática de confirmação documental anterior.

## 6. PESQUISA NEGATIVA NÃO PROVA INEXISTÊNCIA

1. NÃO LOCALIZADO NESTA IA não significa INEXISTENTE.
2. Ausência local não invalida referência documentada a arquivo, versão ou artefato posterior.
3. Usar REFERÊNCIA DOCUMENTADA — ACESSO NÃO CONFIRMADO NESTA IA quando adequado.
4. Snapshot mais antigo não invalida automaticamente versão posterior.
5. Inexistência exige evidência positiva suficiente.
6. Fontes da mesma versão materialmente divergentes devem ser classificadas NÃO SINCRONIZADO até reconciliação.

## 7. PAGINAÇÃO DOCUMENTAL

Quando transportar páginas, localizadores ou citações:
1. não converter índice técnico do PDF, posição física, P<n> de parser/OCR ou contador do visualizador em paginação bibliográfica sem conferir o número impresso;
2. quando relevante, separar PÁGINA IMPRESSA, ÍNDICE/PÁGINA TÉCNICA DO PDF e CITAÇÃO ACADÊMICA;
3. para referência bibliográfica, prevalece a paginação impressa da edição adotada, salvo norma específica;
4. se a página impressa não foi conferida, manter FONTE NÃO CONFERIDA/pendência adequada.

## 8. CONTROLES TRANSITÓRIOS NÃO MIGRAM

Ordens como pause, aguarde, espere confirmação, não execute ainda ou equivalentes da interação de origem não se tornam automaticamente instruções da sucessora. Podem ser preservadas como HISTÓRICO JÁ CONSUMIDO. Somente permanecem ativas por determinação expressa do usuário.

## 9. RETOMADA IMEDIATA

A última seção operacional do artefato integral deve ser RETOMADA IMEDIATA. Ela deve conter ação concreta e executável; adaptar-se às ferramentas disponíveis; não reabrir trabalho concluído; não pedir genericamente o próximo passo quando já determinável; minimizar trabalho manual.

Teste: uma IA sem o restante do histórico saberia o que fazer imediatamente depois de recuperar este artefato? Se não, corrigir.

## 10. PORTABILIDADE INTER-IA

O artefato integral deve funcionar mesmo quando a IA receptora não possui memória da origem, Project/Space, conectores, arquivos ou ferramentas equivalentes.

O MODO DE ENTREGA: TAREFA somente é apropriado quando a conversa receptora puder, pelas capacidades autorizadas disponíveis, resolver a Caixa Postal/TASK e materializar o artefato persistido. Se isso não puder ser estabelecido na origem, não fingir portabilidade: usar INTEGRAL.

## 11. RESIDÊNCIA POR PROJETO

Antes de persistir:
1. identificar PROJECT_ID/PROJECT_KEY ou residência documental suficientemente confirmada;
2. identificar PROJECT_ROOT_ID/REPOSITORY_ROOT_ID ou diretório governante equivalente;
3. resolver destino na ordem: destino explícito; destino canônico registrado; Bíblia/registro governante; descoberta restrita à árvore confirmada;
4. preferir ID estável de pasta a busca nominal;
5. restringir busca nominal à árvore do projeto;
6. validar ancestralidade real;
7. nome semelhante não prova equivalência;
8. nunca gravar em outro projeto só porque existe pasta chamada Consolidados, Continuidade ou equivalente;
9. diante de candidatos conflitantes, não adivinhar;
10. não criar árvore paralela quando destino válido já existe;
11. se residência não puder ser confirmada, não declarar persistência correta.

## 12. PERSISTÊNCIA — FASE DE ESCRITA

Depois que o artefato integral estiver finalizado:
1. atribuir RUN_ID;
2. resolver projeto e residência;
3. aplicar CURRENT + SNAPSHOT da seção 12.1;
4. obter FILE_ID/equivalente estável de cada objeto gravado;
5. não alterar o artefato integral apenas para inserir resultados posteriores.

Registrar na transação: RUN_ID, PROJECT_ID, provider, nomes, FILE_ID(s), path lógico, link(s), modo de persistência e versão de `/consolidar`.

A persistência não está conforme até passar pela validação.

### 12.1. POLÍTICA CURRENT + SNAPSHOT POR MARCO

1. CURRENT é o padrão. Em `/consolidar` comum, manter um único artefato estável por projeto, preferencialmente `<PROJECT_ID>__CONSOLIDADO__CONTINUIDADE__CURRENT`, atualizado em lugar quando possível.
2. Se CURRENT não existir, criá-lo uma vez na residência validada.
3. Histórico nativo do provedor cobre mudanças ordinárias; não criar timestamp a cada execução.
4. SNAPSHOT é adicional e excepcional quando houver:
   - `/nova-conversa` explícita;
   - fechamento/congelamento de fase;
   - mudança estrutural de alto risco;
   - marco material que exija referência histórica estável;
   - pedido expresso do usuário.
5. Com gatilho de SNAPSHOT, atualizar/validar CURRENT e também persistir snapshot do mesmo artefato, salvo impossibilidade documentada.
6. Nome recomendado: `<PROJECT_ID>__CONSOLIDADO__CONTINUIDADE__<AAAAMMDD-HHMM>__v<versao>`.
7. CURRENT e SNAPSHOT são continuidade não canônica, nunca Bíblia Canônica.
8. Se atualização em lugar não for suportada, registrar isso e usar o equivalente estável mais próximo sem criar múltiplos pseudo-CURRENT.
9. Ausência de snapshot não é falha sem gatilho; com gatilho, snapshot é requisito.
10. O usuário não precisa memorizar parâmetro novo.

### 12.2. TASK DE HANDOFF PARA NOVA/OUTRA CONVERSA

Quando houver Google Drive e a Caixa Postal Multi-IA existente acessíveis, `/consolidar` deve tentar criar uma TASK de handoff depois que o artefato de continuidade estiver persistido e validado.

NÃO criar nova Caixa Postal, banco, Sheet, Apps Script, worker, API ou protocolo paralelo. Usar o protocolo `/tarefa` vigente e sua residência existente.

A TASK de handoff deve conter, no mínimo:
- TASK_TYPE: CONTINUITY_HANDOFF;
- OBJECTIVE: assimilar o estado persistido e continuar da RETOMADA IMEDIATA;
- SOURCE_REFS: FILE_ID do CURRENT e, quando material, SNAPSHOT e CONTINUITY_REF;
- EXPECTED_RUN_ID do consolidado;
- instrução para recuperar o artefato diretamente pelo identificador estável;
- instrução para validar identidade/escopo antes de assimilar;
- instrução para não reabrir trabalho concluído;
- instrução para não pedir ao usuário o prompt integral quando a recuperação funcionar;
- instrução para executar a RETOMADA IMEDIATA ou atualizar a conversa existente com o estado recuperado;
- CONTEXT_REQUIREMENT compatível com contexto persistido.

A TASK não precisa duplicar o consolidado integral; ela é o envelope resolvível que aponta para ele.

Depois de criar a TASK:
1. obter TASK_ID e TASK_REF;
2. validar que pertence à MAILBOX_ROOT esperada;
3. reler a TASK por identificador estável;
4. confirmar que SOURCE_REFS apontam para o consolidado correto;
5. confirmar RUN_ID/CONTINUITY_REF esperados;
6. confirmar que a conversa receptora consegue entender a ação de assimilação/retomada;
7. marcar SHORT_DISPATCH_STATE: READY somente após os gates acima.

Se qualquer passo falhar: SHORT_DISPATCH_STATE: BLOCKED e não mostrar `/tarefa <TASK_ID>` como se estivesse pronto.

## 13. VALIDAÇÃO PÓS-GRAVAÇÃO

Após a gravação, validar sem modificar novamente o artefato integral.

### 13.1 Residência
- reler metadados por identificador estável;
- confirmar parent/diretório;
- validar ancestralidade até o projeto esperado.

### 13.2 Conteúdo — igualdade objetiva

Recuperar o artefato persistido diretamente por FILE_ID/equivalente e comparar integralmente com o conteúdo produzido.

Normalização permitida nos dois lados:
- UTF-8;
- Unicode NFC;
- line endings LF;
- remover apenas BOM inicial;
- tolerar apenas newline terminal adicional/removido pelo provedor.

É proibido colapsar espaços, remover parágrafos, reordenar conteúdo, resumir, aceitar similaridade semântica ou truncamento.

Gate:
CONTEÚDO_ORIGINAL_NORMALIZADO == CONTEÚDO_RECUPERADO_NORMALIZADO

Se não puder ser comprovado:
VALIDAÇÃO DA PERSISTÊNCIA: INCONCLUSIVA
MODO DE ENTREGA: INTEGRAL

Também confirmar RUN_ID, ESTADO: CONTINUIDADE — NÃO CANÔNICA e RETOMADA IMEDIATA.

### 13.3 Recuperação objetiva

Executar nova recuperação diretamente por FILE_ID/equivalente. Busca nominal ou semântica não substitui esse teste.

## 14. ESTADOS DA TRANSAÇÃO

Somente depois de escrita e validação determinar:

PERSISTÊNCIA: EXECUTADA — <provider>:<FILE_ID>
ou PERSISTÊNCIA: NÃO EXECUTADA — <motivo>.

VALIDAÇÃO DA PERSISTÊNCIA: CONFORME
ou INCONCLUSIVA — <motivo>
ou NÃO APLICÁVEL.

RECUPERAÇÃO PÓS-GRAVAÇÃO: CONFORME — <provider>:<FILE_ID>
ou INCONCLUSIVA — <motivo>
ou NÃO APLICÁVEL.

MODO DE PERSISTÊNCIA: CURRENT
ou CURRENT + SNAPSHOT.

SNAPSHOT: NÃO APLICÁVEL
ou CONFORME — <provider>:<FILE_ID>
ou INCONCLUSIVO — <motivo>.

TASK_HANDOFF: READY — <TASK_ID>
ou BLOCKED — <motivo>
ou NÃO APLICÁVEL.

MODO DE ENTREGA: TAREFA
ou RECIBO
ou INTEGRAL.

## 15. CONTINUITY_REF

Quando houver identificador estável:
CONTINUITY_REF: <PROJECT_ID>|<RUN_ID>|<provider>:<FILE_ID>|consolidar:<versao>

FILE_ID/equivalente é a rota primária do consolidado. TASK_REF é a rota primária da TASK. Busca por título é fallback de diagnóstico.

## 16. GATES DE MODO DE ENTREGA

### 16.1 Gate comum do artefato

Antes de compactar a interface, todos os aplicáveis devem ser verdadeiros:
G1 artefato integral finalizado;
G2 RUN_ID presente;
G3 projeto/residência confirmados;
G4 persistência executada;
G5 parent/ancestralidade validados;
G6 igualdade integral normalizada comprovada;
G7 FILE_ID/equivalente estável;
G8 RETOMADA IMEDIATA válida;
G9 recuperação pós-gravação direta confirmou o artefato;
G10 snapshot conforme quando obrigatório;
G11 usuário não pediu bloco integral;
G12 não existe dúvida material nos itens anteriores.

Falha em qualquer gate aplicável => MODO DE ENTREGA: INTEGRAL.

### 16.2 Gate TAREFA

Depois de G1-G12, usar MODO DE ENTREGA: TAREFA somente se:
T1 protocolo/caixa postal `/tarefa` aplicável foi resolvido;
T2 TASK de handoff foi criada na residência correta;
T3 TASK_ID e TASK_REF existem;
T4 parent/ancestralidade da TASK foram validados;
T5 readback da TASK passou;
T6 SOURCE_REFS apontam para o consolidado validado;
T7 RUN_ID/CONTINUITY_REF correspondem;
T8 SHORT_DISPATCH_STATE = READY;
T9 não há evidência de que o destino indicado pelo usuário seja incapaz de acessar a rota persistida.

Se T1-T9 não passarem e houver portabilidade imediata, usar INTEGRAL.
Se não houver portabilidade imediata, ainda pode ser usado RECIBO se os gates comuns passarem.

Não existe parâmetro adicional que o usuário precise decorar.

## 17. PORTABILIDADE IMEDIATA E POSTERIOR

Portabilidade imediata deve PREFERIR TAREFA VALIDADA.

Quando T1-T9 passarem:
MODO DE ENTREGA: TAREFA

Quando o handoff curto não estiver conforme:
- se a portabilidade for imediata, INTEGRAL;
- se não houver transporte imediato e G1-G12 passarem, RECIBO pode ser usado.

Destino explicitamente sem acesso comum, ou pedido por bloco completo/portável, força INTEGRAL.

Se uma TASK inicialmente válida chegar a uma superfície sem acesso ao repositório, a IA receptora deve declarar blocker real. Quando a IA de origem ainda estiver disponível e puder recuperar o artefato, fornecer o integral automaticamente em vez de exigir procura manual.

## 18. ENTREGA DE UMA LINHA

Quando MODO DE ENTREGA: TAREFA, a resposta visível ao usuário deve ser EXATAMENTE uma única linha:

`/tarefa <TASK_ID>`

Não incluir cabeçalho, recibo, explicação, link, CONTINUITY_REF, rodapé, menu de continuidade, pergunta final ou qualquer outra linha nessa mesma resposta.

A linha é destinada a ser colada na conversa nova ou existente que deve ser inicializada/atualizada.

Ao receber essa linha, a conversa destinatária deve resolver a TASK pelo protocolo vivo, recuperar o consolidado por SOURCE_REFS, validar identidade, assimilar o estado e prosseguir da RETOMADA IMEDIATA. Não deve apenas responder “tarefa localizada”.

## 19. RECIBO DE CONTINUIDADE

Quando MODO DE ENTREGA: RECIBO, apresentar recibo curto com projeto, RUN_ID, modo de persistência, snapshot, validação, recuperação, arquivo/ID, CONTINUITY_REF, estado não canônico e RETOMADA IMEDIATA.

O recibo não é consolidado integral, bootstrap, Bíblia Canônica nem substituto do artefato persistido.

## 20. FALLBACK INTEGRAL

Apresentar o artefato integral quando:
- persistência falhar;
- validação/releitura/recuperação for inconclusiva;
- residência for incerta;
- conteúdo divergir;
- identificador estável faltar;
- TASK_HANDOFF estiver BLOCKED em situação de portabilidade imediata;
- destino for conhecido como incapaz de resolver a rota;
- usuário pedir o bloco.

Pode precedê-lo apenas envelope transacional mínimo.

## 21. DESCOBERTA INTERCONVERSAS

Para consolidado: CONTINUITY_REF conhecido; FILE_ID; CURRENT registrado; registro governante; descoberta restrita; busca nominal só como fallback.

Para handoff: TASK_REF; TASK_ID dentro da MAILBOX_ROOT; nunca busca global no Drive quando a raiz/referência estiver disponível.

CURRENT validado é o ponteiro operacional para o estado mais recente. SNAPSHOT representa marco histórico.

Não afirmar que outra conversa verá automaticamente o consolidado apenas porque ele foi salvo. Essa afirmação só é aceitável quando a rota de recuperação realmente foi executada/validada.

## 22. RELAÇÃO COM A BÍBLIA CANÔNICA

Consolidado e TASK de handoff não são Bíblia Canônica. Não promover integralmente ao mestre. Candidatos canônicos seguem mecanismo próprio.

## 23. CICLO DE VIDA DA CONVERSA

Quando houver protocolo especializado vigente de governança de conversas, `/consolidar` pode invocá-lo semanticamente depois da persistência/handoff.

Não reproduzir a taxonomia completa de lifecycle aqui. Indisponibilidade do protocolo de lifecycle não invalida o consolidado. EXCLUÍVEL nunca significa exclusão automática.

## 24. EFICIÊNCIA

O artefato integral é prioritariamente máquina-a-máquina. Usar formato simples, compacto e sem ornamentação redundante.

A interface do usuário deve tender a uma única linha quando os gates TAREFA passarem.

Não gerar relatório intermediário ao usuário quando a própria IA pode persistir, validar e criar o handoff.

## 25. TESTE DE BOOTSTRAP

Antes de aceitar o artefato, perguntar: uma IA sem o restante do histórico, depois de recuperar este artefato, saberia o que fazer imediatamente?

Reprovar se ela ficar esperando, pedir confirmação já dada, repetir etapa concluída ou não souber executar RETOMADA IMEDIATA.

## 26. TESTE DO HANDOFF CURTO

Antes de entregar `/tarefa <TASK_ID>`:
1. recuperar a TASK criada;
2. validar TASK_ID/TASK_REF/residência;
3. validar SOURCE_REFS;
4. recuperar o consolidado pelo FILE_ID referenciado;
5. confirmar RUN_ID;
6. confirmar presença de RETOMADA IMEDIATA;
7. simular semanticamente a interpretação: “assimilação/atualização + continuidade”, não “nova análise da TASK”.

Se esse teste não fechar, não entregar a linha curta.

## 27. GATE DE ACEITAÇÃO

REPROVAR e corrigir se:
1. consolida apenas o tema;
2. RETOMADA IMEDIATA está ausente/vazia/genérica;
3. reativa pausa consumida;
4. presume acesso inexistente;
5. inventa arquivo, ID, versão, TASK ou capacidade;
6. promove estado epistêmico indevidamente;
7. deixa ambígua a natureza não canônica;
8. seleciona destino apenas por nome;
9. persiste em projeto errado;
10. declara validação antes da releitura;
11. altera artefato apenas para inserir estados pós-validação;
12. compacta interface sem artefato persistido;
13. compacta sem FILE_ID estável;
14. compacta sem igualdade integral comprovada;
15. compacta sem recuperação direta;
16. usa busca nominal no lugar do teste objetivo;
17. entrega `/tarefa` sem TASK_HANDOFF READY;
18. entrega `/tarefa` sem readback da TASK;
19. entrega `/tarefa` com SOURCE_REFS divergentes;
20. entrega `/tarefa` e também texto extra no mesmo MODO DE ENTREGA: TAREFA;
21. entrega RECIBO quando portabilidade imediata exige TAREFA ou INTEGRAL;
22. usa ponteiro para omitir estado necessário;
23. transfere ao usuário recuperação manual que a IA poderia executar;
24. converte não localizado em inexistente;
25. cria snapshot rotineiro sem gatilho quando CURRENT atualizável existe;
26. cria múltiplos pseudo-CURRENT sem necessidade;
27. com gatilho obrigatório, declara conformidade sem snapshot validado;
28. cria Caixa Postal paralela em vez de usar a existente.

## 28. REGRAS FINAIS

A. O artefato integral sempre existe.
B. Deve estar finalizado antes da persistência.
C. CURRENT é o padrão; SNAPSHOT é excepcional por marco/gatilho.
D. Estados transacionais não exigem reescrever o artefato.
E. Integridade precede economia de tokens.
F. Igualdade integral e recuperação direta precedem compactação.
G. Portabilidade imediata prefere TAREFA validada; sem handoff conforme, usa INTEGRAL.
H. `/consolidar` deve tentar o handoff curto quando a infraestrutura `/tarefa` aplicável estiver disponível.
I. `/nova-conversa` continua alias e sinaliza transporte imediato.
J. Não criar parâmetro novo que o usuário precise lembrar.
K. A TASK de handoff aponta para o consolidado; não o substitui.
L. Em MODO DE ENTREGA: TAREFA, a saída do chat é exatamente `/tarefa <TASK_ID>` e nada mais.
M. A conversa destinatária deve assimilar/atualizar seu estado e continuar da RETOMADA IMEDIATA.
N. Falha de resolução da TASK não prova inexistência; tentar rotas autorizadas antes de pedir o bloco integral ao usuário.
O. Não criar infraestrutura paralela apenas para esse fluxo.

FIM DA DEFINIÇÃO.
