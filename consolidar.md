---
Gerado por: GPT-5.6 Sol
Data de geração: 12/08/2026
Versão: 2.4.0
Estado: CANÔNICO SANITIZADO
Base: consolidar.md v2.3.0 + política CURRENT/SNAPSHOT por marco + hardening de persistência
---


COMANDO: /consolidar


## O QUE É


Produz um ARTEFATO INTEGRAL DE CONTINUIDADE que funciona simultaneamente como registro auditável do estado operacional da conversa atual e prompt autocontido de retomada para a mesma IA ou outra.


O artefato integral é obrigatório. Sua APRESENTAÇÃO NO CHAT é adaptativa: pode ser exibido integralmente ou substituído visualmente por um RECIBO DE CONTINUIDADE quando todos os gates de persistência, validação, recuperação e portabilidade forem satisfeitos.


O recibo nunca substitui semanticamente o artefato integral.


A operação possui duas camadas distintas:


A. ARTEFATO INTEGRAL DE CONTINUIDADE
- contém o estado necessário para continuidade;
- é finalizado antes da persistência;
- possui RUN_ID próprio;
- não depende do resultado posterior da transação;
- não é reescrito apenas para inserir estados pós-gravação.


B. TRANSAÇÃO DE PERSISTÊNCIA E ENTREGA
- resolve residência;
- grava;
- relê;
- valida;
- testa recuperação pelo identificador estável;
- determina MODO DE ENTREGA;
- produz RECIBO ou FALLBACK INTEGRAL.


Estados pós-gravação como PERSISTÊNCIA, VALIDAÇÃO DA PERSISTÊNCIA, RECUPERAÇÃO PÓS-GRAVAÇÃO, MODO DE ENTREGA e CONTINUITY_REF pertencem à transação/recibo posterior.


## QUANDO USAR


Quando a conversa ficou longa, antes de trocar de conversa/IA, diante de muitos anexos, decisões, versões, testes, mudança de fase ou risco de perda de continuidade.


## RELAÇÃO COM /nova-conversa


/nova-conversa continua alias de compatibilidade de /consolidar. A própria invocação sinaliza portabilidade imediata e, por padrão, resulta em MODO DE ENTREGA: INTEGRAL, salvo se a plataforma efetivamente criar e inicializar a sucessora com o artefato integral sem intervenção manual.


## 1. REGRA ANTIRREGRESSÃO


/consolidar nunca significa apenas resumir, compilar ou sintetizar o tema. O artefato deve preservar o ESTADO OPERACIONAL DA CONVERSA e permitir continuação confiável em outro contexto. Relatório temático sem regras para a próxima IA, bootstrap e RETOMADA IMEDIATA executável é defeituoso.


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


As dimensões são semânticas e podem ser fundidas quando isso reduzir redundância sem perda de continuidade.


Próximo ao início declarar:
ESTADO: CONTINUIDADE — NÃO CANÔNICA
RUN_ID: <identificador único da execução>


Nunca inventar plataforma, modelo, título, IDs, arquivos, versões, leituras ou capacidades.


## 3. AUTOCONTENÇÃO E PONTEIROS


Autocontenção significa que uma IA receptora, recebendo apenas o artefato integral, consegue compreender o estado e executar corretamente RETOMADA IMEDIATA.


Ponteiros como nome, ID, link, versão, hash, caminho e referência externa podem substituir a reprodução integral de documentos, fontes, prompts, relatórios ou artefatos externos quando seu conteúdo completo não for necessário.


Ponteiros NÃO podem substituir, quando necessários à continuidade: fatos materiais, decisões vigentes, restrições, resultados estabelecidos, erros corrigidos cuja perda cause regressão, estados epistêmicos, pendências, dependências, regras operacionais, instruções para a próxima IA ou conteúdo necessário à RETOMADA IMEDIATA.


Regra: PONTEIRO PODE SUBSTITUIR O DOCUMENTO EXTERNO; NÃO PODE SUBSTITUIR O ESTADO NECESSÁRIO DA CONVERSA.


Se a próxima IA precisar acessar objeto externo para prosseguir, declarar isso explicitamente.


## 4. ESTADOS DE ACESSO


Quando material, distinguir: ACESSO REAL CONFIRMADO; APENAS REFERENCIADO; CONTEÚDO PARCIALMENTE EXTRAÍDO; ACESSO NECESSÁRIO PARA RETOMADA; REFERÊNCIA DOCUMENTADA — ACESSO NÃO CONFIRMADO NESTA IA; FONTE CANÔNICA: IDENTIFICADA — CONTEÚDO NÃO MATERIALIZADO.


Conhecimento sobre arquivo não equivale a acesso real. Metadados, SHA, tamanho, path ou confirmação de download não equivalem à leitura do corpo textual.


## 5. CONTROLE DE ESTADO EPISTÊMICO


Quando material, preservar: FATO CONFIRMADO; ERRO CORRIGIDO; HIPÓTESE; INFERÊNCIA; INTERPRETAÇÃO; ALEGAÇÃO; DECISÃO EDITORIAL; FONTE NÃO CONFERIDA; INFORMAÇÃO NÃO DOCUMENTADA.


Não transformar hipótese em fato, inferência em fonte, resposta de IA em evidência, referência em leitura ou perda de acesso em perda automática de confirmação documental anterior.


Quando não determinável pelo histórico acessível, usar não documentado no histórico disponível ou estado mais preciso.


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


Ordens como pause, aguarde, espere confirmação, não execute ainda ou equivalentes pertencentes à interação de origem não se tornam automaticamente instruções da sucessora. Podem ser preservadas como HISTÓRICO JÁ CONSUMIDO. Somente permanecem ativas por determinação expressa do usuário.


## 9. RETOMADA IMEDIATA


A última seção operacional do artefato integral deve ser RETOMADA IMEDIATA. Ela deve conter ação concreta, executável, com objetivo operacional; adaptar-se às ferramentas disponíveis; não reabrir trabalho concluído; não pedir genericamente o próximo passo quando já determinável; minimizar transferência de trabalho manual.


Teste: Uma IA sem o restante do histórico saberia o que fazer imediatamente ao receber somente este artefato? Se não, corrigir.


## 10. PORTABILIDADE INTER-IA


O artefato integral deve funcionar mesmo quando a IA receptora não possui memória da origem, Project/Space, conectores, arquivos ou ferramentas equivalentes. Não tornar limitação da origem uma limitação universal. Quando o destino não possuir capacidade necessária, adaptar o método. A existência de ponteiros externos não reduz a obrigação de autocontenção do estado necessário.


## 11. RESIDÊNCIA POR PROJETO

Antes de persistir:
1. identificar PROJECT_ID/PROJECT_KEY ou residência documental suficientemente confirmada;
2. identificar PROJECT_ROOT_ID/REPOSITORY_ROOT_ID ou diretório governante equivalente;
3. resolver destino na ordem: destino explícito do usuário; destino canônico registrado; Bíblia/registro governante; descoberta restrita à árvore confirmada do projeto;
4. preferir ID estável de pasta a busca nominal;
5. restringir busca nominal à árvore do projeto;
6. validar ancestralidade real;
7. nome igual ou semanticamente semelhante não prova equivalência;
8. nunca gravar em outro projeto só porque existe pasta chamada Consolidados, Continuidade ou equivalente;
9. diante de candidatos conflitantes, não adivinhar;
10. não criar árvore paralela quando destino válido já existe;
11. se residência não puder ser confirmada, não declarar persistência correta.


## 12. PERSISTÊNCIA — FASE DE ESCRITA

Depois que o artefato integral estiver finalizado:
1. atribuir RUN_ID;
2. resolver projeto e residência;
3. aplicar a política CURRENT + SNAPSHOT da seção 12.1;
4. obter FILE_ID ou identificador estável equivalente de cada objeto efetivamente gravado;
5. não alterar o artefato integral para inserir resultados posteriores da persistência.

Registrar na transação posterior, quando disponíveis: RUN_ID, PROJECT_ID, provider, nomes, FILE_ID(s), path lógico, link(s) estável(is), modo de persistência e versão de /consolidar.

A persistência não está conforme até passar pela validação.

### 12.1. POLÍTICA CURRENT + SNAPSHOT POR MARCO

Objetivo: reduzir proliferação de consolidados sem perder continuidade, auditabilidade nem marcos imutáveis.

1. **CURRENT é o padrão.** Em `/consolidar` comum, manter um único artefato estável por projeto, preferencialmente denominado `<PROJECT_ID>__CONSOLIDADO__CONTINUIDADE__CURRENT`, atualizado em lugar quando o provedor oferecer atualização do mesmo objeto/FILE_ID.
2. Se CURRENT ainda não existir, criá-lo uma única vez na residência validada. Execuções posteriores devem atualizar esse mesmo objeto sempre que tecnicamente possível.
3. O histórico nativo de versões do provedor é suficiente para mudanças ordinárias do CURRENT; não criar novo arquivo timestampado em cada execução apenas para preservar histórico rotineiro.
4. **SNAPSHOT é adicional e excepcional.** Criar snapshot imutável somente quando ocorrer pelo menos um destes gatilhos:
   - `/nova-conversa` explícita;
   - fechamento ou congelamento de fase;
   - antes de mudança estrutural de alto risco;
   - marco material que precise de referência histórica estável;
   - pedido expresso do usuário por snapshot/histórico imutável.
5. Quando houver gatilho de SNAPSHOT, atualizar/validar CURRENT e também persistir uma cópia snapshot do mesmo artefato integral, salvo impossibilidade técnica documentada.
6. Nome recomendado do snapshot: `<PROJECT_ID>__CONSOLIDADO__CONTINUIDADE__<AAAAMMDD-HHMM>__v<versao>`.
7. CURRENT e SNAPSHOT nunca são Bíblia Canônica. Ambos permanecem artefatos de continuidade não canônicos.
8. Se o provedor não suportar atualização em lugar, registrar `CURRENT: ATUALIZAÇÃO EM LUGAR NÃO SUPORTADA` e usar o mecanismo estável equivalente mais próximo, sem criar árvore paralela ou múltiplos pseudo-CURRENT.
9. Não transformar ausência de snapshot em falha quando nenhum gatilho existir. Quando o gatilho existir, snapshot passa a ser requisito da transação daquela execução.
10. O usuário não precisa memorizar parâmetro novo: a classificação CURRENT/SNAPSHOT é automática a partir do contexto e dos gatilhos acima.

## 13. VALIDAÇÃO PÓS-GRAVAÇÃO


Após a gravação, validar SEM modificar novamente o artefato integral.


### 13.1 Residência
- reler metadados por identificador estável;
- confirmar parent/diretório;
- validar ancestralidade até o projeto esperado.


### 13.2 Conteúdo — igualdade objetiva
Recuperar o próprio artefato persistido diretamente por FILE_ID/equivalente e comparar integralmente o conteúdo produzido com o conteúdo recuperado.


Aplicar a MESMA normalização determinística aos dois lados, limitada a transformações não semânticas inevitáveis do provedor:
- UTF-8 quando houver representação textual;
- Unicode NFC;
- line endings LF;
- remover apenas BOM inicial, se inserido pelo provedor;
- tolerar apenas newline terminal adicional/removido pelo provedor.


É proibido colapsar espaços, remover parágrafos, reordenar conteúdo, resumir, comparar por similaridade semântica ou aceitar truncamento.


Gate:
CONTEÚDO_ORIGINAL_NORMALIZADO == CONTEÚDO_RECUPERADO_NORMALIZADO


Se a igualdade integral não puder ser comprovada:
VALIDAÇÃO DA PERSISTÊNCIA: INCONCLUSIVA
MODO DE ENTREGA: INTEGRAL


Além da igualdade, confirmar RUN_ID esperado, ESTADO: CONTINUIDADE — NÃO CANÔNICA e presença de RETOMADA IMEDIATA.


### 13.3 Recuperação objetiva
Executar NOVA recuperação usando diretamente FILE_ID/equivalente. Recuperabilidade não pode ser inferida de nome, busca semântica, busca nominal ou presença da pasta.


O teste passa somente se a recuperação direta for executada, o objeto corresponder ao artefato esperado, RUN_ID ou marcador suficiente confirmar sua identidade e o conteúdo necessário puder ser materializado.


Busca nominal posterior não converte falha desse teste em CONFORME.


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
ou MODO DE PERSISTÊNCIA: CURRENT + SNAPSHOT.

SNAPSHOT: NÃO APLICÁVEL
ou SNAPSHOT: CONFORME — <provider>:<FILE_ID>
ou SNAPSHOT: INCONCLUSIVO — <motivo>.

MODO DE ENTREGA: RECIBO
ou MODO DE ENTREGA: INTEGRAL.

Esses estados pertencem à transação/recibo e não exigem segunda escrita no artefato integral.


## 15. CONTINUITY_REF


Quando houver identificador estável, gerar na transação:
CONTINUITY_REF: <PROJECT_ID>|<RUN_ID>|<provider>:<FILE_ID>|consolidar:<versao>


FILE_ID/equivalente é a rota primária de recuperação. Busca por título pode ser fallback de diagnóstico, mas não satisfaz o gate de recuperabilidade para RECIBO.


## 16. GATE DE MODO DE ENTREGA


RECIBO somente se TODOS forem verdadeiros:
G1 artefato integral finalizado;
G2 RUN_ID presente;
G3 projeto/residência confirmados;
G4 persistência executada;
G5 parent/ancestralidade validados;
G6 conteúdo persistido recuperado e igualdade normalizada integral comprovada;
G7 existe FILE_ID/equivalente estável;
G8 RETOMADA IMEDIATA presente e válida;
G9 nova recuperação pós-gravação executada diretamente pelo identificador estável e confirmou o artefato correto;
G10 não existe necessidade atual de transferência manual do bloco;
G11 usuário não pediu bloco integral/portável/copiável;
G12 não existe dúvida material nos itens anteriores;
G13 se houver gatilho obrigatório de SNAPSHOT, o snapshot foi gravado, relido e recuperado diretamente com identidade suficiente.

Se qualquer item aplicável falhar: MODO DE ENTREGA: INTEGRAL.


Não existe parâmetro que o usuário precise lembrar para obter esse comportamento.


## 17. PORTABILIDADE IMEDIATA E POSTERIOR


Forçar INTEGRAL quando o usuário informa destino sem acesso comum, pede mostrar/copiar/portável/bloco completo, invoca /nova-conversa ou a próxima ação exige transporte imediato.


Se inicialmente foi entregue RECIBO e depois surgir destino sem acesso ao repositório: recuperar o artefato por CONTINUITY_REF/FILE_ID, confirmar identidade pelo RUN_ID e entregar o bloco integral automaticamente, sem transferir busca/cópia manual ao usuário quando a IA puder fazer isso.


## 18. RECIBO DE CONTINUIDADE


Quando MODO DE ENTREGA: RECIBO, apresentar somente recibo curto:
CONSOLIDADO — CONFORME
Tipo: RECIBO DE CONTINUIDADE — NÃO É O CONSOLIDADO INTEGRAL
Projeto: <PROJECT_ID/nome>
RUN_ID: <RUN_ID>
Persistência: EXECUTADA
Modo de persistência: <CURRENT | CURRENT + SNAPSHOT>
Snapshot: <NÃO APLICÁVEL | CONFORME>
Validação: CONFORME
Recuperação pós-gravação: CONFORME
Local: <path lógico>
Arquivo: <nome>
ID: <FILE_ID/equivalente>
Link: <link, quando disponível>
CONTINUITY_REF: <ref>
Estado: CONTINUIDADE — NÃO CANÔNICA
Modo de entrega: RECIBO
Portabilidade: REPOSITÓRIO
Retomada imediata: <uma linha concreta>


O recibo é metadado transacional/interface humana. Não é consolidado integral, bootstrap, Bíblia Canônica nem substituto do artefato persistido.


## 19. FALLBACK INTEGRAL


Apresentar o artefato integral no chat quando persistência falhar, validação for inconclusiva, residência for incerta, releitura falhar, conteúdo divergir, identificador estável faltar, recuperação direta falhar, portabilidade imediata exigir ou o usuário pedir.


Pode precedê-lo apenas envelope transacional mínimo. O envelope não integra semanticamente o artefato de continuidade.


## 20. DESCOBERTA INTERCONVERSAS


Ordem preferencial: CONTINUITY_REF conhecido; FILE_ID conhecido; CURRENT registrado do projeto; registro governante do projeto; descoberta restrita à residência confirmada; busca nominal somente como fallback.

CURRENT validado é o ponteiro operacional padrão para o estado mais recente da linha. SNAPSHOT representa marco histórico, não substitui automaticamente o CURRENT. Havendo múltiplos consolidados, não presumir que o arquivo timestampado mais recente é automaticamente o mais autoritativo. Considerar PROJECT_ID, escopo, RUN_ID, modo CURRENT/SNAPSHOT, data, artefatos governantes, estado e relevância.


Não afirmar que outra conversa verá automaticamente o consolidado apenas porque ele foi salvo.


## 21. RELAÇÃO COM A BÍBLIA CANÔNICA


Consolidado não é Bíblia Canônica. Não promover integralmente ao mestre. Candidatos canônicos seguem mecanismo próprio de delta/auditoria/promoção. Informação operacional e histórico ficam fora da Bíblia salvo decisão específica. Recibo também não é canônico.


## 22. CICLO DE VIDA DA CONVERSA


Quando houver protocolo especializado vigente de governança de conversas, /consolidar pode invocá-lo semanticamente depois do artefato e da transação. O protocolo especializado trata estado da conversa, recomendação de UI, registro operacional e elegibilidade de arquivamento/exclusão.


Não reproduzir sua taxonomia completa dentro de /consolidar. Indisponibilidade do protocolo não bloqueia /consolidar. EXCLUÍVEL nunca significa exclusão automática. Não afirmar operação de UI sem capacidade efetiva e confirmação.


## 23. EFICIÊNCIA


O artefato integral é prioritariamente máquina-a-máquina. Usar formato simples, compacto e sem ornamentação redundante. Não repetir o mesmo estado em várias seções.


Ponteiros podem evitar reprodução integral de documentos/fontes/artefatos externos, mas nunca remover fato, decisão, restrição, estado epistêmico, pendência, instrução ou conteúdo necessário à continuidade.


A economia da interface humana nunca pode reduzir a integridade do artefato integral.


## 24. TESTE DE BOOTSTRAP


Antes de considerar o artefato conforme, perguntar: Se uma IA sem nenhum outro histórico receber apenas este artefato como primeira mensagem, saberá o que fazer imediatamente?


Reprovar se ela provavelmente ficar esperando, pedir confirmação já dada, repetir etapa concluída, perguntar genericamente o que o usuário deseja, depender silenciosamente da origem ou não souber executar RETOMADA IMEDIATA.


## 25. TESTE DE PORTABILIDADE INTER-IA


Verificar se permanece compreensível para IA sem memória, Project/Space, conectores, arquivos ou ferramentas da origem. Para passar: não presumir acesso; distinguir acesso de referência; não depender desnecessariamente de ferramenta específica; incorporar semântica mínima indispensável; permitir ponteiros somente quando estado necessário estiver autocontido; adaptar método; solicitar ação manual apenas sem alternativa técnica razoável; preservar NÃO LOCALIZADO != INEXISTENTE.


## 26. GATE DE ACEITAÇÃO


REPROVAR e corrigir se:
1. consolida apenas o tema;
2. RETOMADA IMEDIATA está ausente/vazia/genérica;
3. reativa pausa consumida;
4. presume acesso inexistente;
5. inventa arquivo, ID, versão ou capacidade;
6. promove estado epistêmico indevidamente;
7. deixa ambígua a natureza não canônica;
8. seleciona destino apenas pelo nome da pasta;
9. persiste em projeto errado;
10. declara validação antes da releitura;
11. altera artefato integral apenas para inserir estados pós-validação;
12. entrega RECIBO sem artefato integral persistido;
13. entrega RECIBO sem FILE_ID/equivalente estável;
14. entrega RECIBO sem igualdade integral normalizada comprovada;
15. entrega RECIBO sem recuperação direta efetiva pelo identificador;
16. usa busca nominal no lugar do teste objetivo;
17. entrega RECIBO quando portabilidade imediata exige bloco;
18. entrega RECIBO após /nova-conversa sem transporte integral automático equivalente;
19. permite que recibo seja tratado como consolidado integral;
20. usa ponteiro para omitir estado necessário;
21. transfere ao usuário recuperação manual que a IA poderia executar;
22. deixa falha de ciclo de vida invalidar o consolidado;
23. usa paginação técnica como bibliográfica sem conferência;
24. converte não localizado em inexistente sem evidência positiva;
25. cria novo consolidado timestampado em execução ordinária sem gatilho de SNAPSHOT quando CURRENT atualizável existe;
26. cria mais de um pseudo-CURRENT para o mesmo projeto sem necessidade documentada;
27. havendo gatilho obrigatório de SNAPSHOT, declara conformidade sem gravar e validar o snapshot.


## 27. REGRAS FINAIS


A. O artefato integral sempre existe.
B. Deve estar finalizado antes da persistência.
C. Estados da transação posterior não exigem reescrita do artefato.
D. O chat não precisa sempre reproduzir o artefato integral.
E. Integridade precede economia de tokens.
F. Igualdade integral normalizada e recuperação direta pelo identificador precedem compactação.
G. Portabilidade imediata força entrega integral.
H. Persistência sem validação não autoriza recibo.
I. Busca nominal não satisfaz o gate de recuperabilidade.
J. /nova-conversa continua alias e sinaliza transporte imediato.
K. Não criar novo parâmetro que o usuário precise lembrar.
L. Se posteriormente precisar de versão portável, recuperá-la automaticamente quando possível.
M. Ponteiros podem substituir objetos externos, nunca estado necessário à continuidade.
N. A última seção operacional do artefato integral permanece RETOMADA IMEDIATA.
O. CURRENT é o padrão operacional e deve ser atualizado em lugar quando possível.
P. SNAPSHOT é excepcional e somente ocorre por marco/gatilho material ou pedido expresso.
Q. Histórico nativo do provedor substitui snapshots rotineiros, não snapshots de marco.


FIM DA DEFINIÇÃO.