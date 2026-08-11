---
Gerado por: GPT-5.6 Sol
Data de geração: 11/08/2026
Versão: 2.2.2
Estado: canônico sanitizado
---

COMANDO: /consolidar

O QUE É: gera UM bloco único de continuidade que serve simultaneamente como:
1. resumo auditável da conversa atual; e
2. prompt autocontido de retomada, pronto para ser colado como primeira mensagem de nova conversa, na mesma IA ou em outra.

QUANDO USAR: quando a conversa ficou longa, antes de trocar de conversa/IA, diante de muitos anexos, decisões, versões, testes, mudança de fase ou risco de perda de continuidade.

RELAÇÃO COM /nova-conversa: `/nova-conversa` é alias de compatibilidade. Não existe segunda etapa obrigatória. O próprio resultado de `/consolidar` já é o prompt de retomada.

## REGRA ANTIRREGRESSÃO — CONSOLIDAR A CONVERSA, NÃO APENAS O OBJETO

`/consolidar` nunca significa apenas resumir, compilar ou sintetizar o tema trabalhado.

Mesmo em pesquisa bibliográfica, análise documental, revisão jurídica, auditoria, programação, produção/revisão de artefatos ou comparação entre IAs, o resultado deve preservar o **ESTADO OPERACIONAL DA CONVERSA** e permitir sua continuação em outro contexto.

Relatório temático sem regras para a próxima IA, bootstrap e RETOMADA IMEDIATA executável é defeituoso, ainda que factual.

## DEFINIÇÃO OPERACIONAL

Ao receber `/consolidar`, gerar **UM ÚNICO BLOCO DE CÓDIGO**, autocontido e pronto para copiar, contendo somente o necessário para continuidade confiável.

Os 14 itens abaixo são dimensões semânticas, não obrigação de exatamente 14 títulos visíveis. Seções podem ser fundidas ou omitidas quando realmente irrelevantes, desde que nenhuma informação necessária à continuidade seja perdida.

### 1. IDENTIFICAÇÃO E PROVENIÊNCIA
- plataforma/IA/modelo quando documentados;
- data;
- projeto/conversa;
- comandos/protocolos materialmente relevantes;
- escopo;
- nunca inventar metadados não expostos;
- usar, quando necessário: `PLATAFORMA NÃO DISPONÍVEL`, `MODELO NÃO DISPONÍVEL`, `TÍTULO NÃO DISPONÍVEL`, `ID NÃO DISPONÍVEL`;
- declarar próximo ao início: `ESTADO: CONTINUIDADE — NÃO CANÔNICA`, ou classificação equivalente definida pelo projeto.

### 2. IDENTIDADE E ESTILO
- somente preferências/restrições documentadas que alterem materialmente a continuidade;
- não copiar perfis globais irrelevantes;
- se regra externa for indispensável para a próxima IA compreender como continuar, incorporar o subconjunto mínimo necessário sem presumir acesso ao mesmo projeto, memória, Space ou arquivo.

### 3. CONTEXTO, OBJETO E OBJETIVO
- o que está sendo feito;
- para quê;
- escopo real;
- o que está fora do escopo quando isso evitar erro;
- ponto real em que o trabalho parou;
- priorizar estado atual sobre cronologia completa.

### 4. ARQUITETURA E GOVERNANÇA
- hierarquia de fontes;
- documentos governantes;
- comandos/protocolos relevantes;
- versões vigentes;
- relações mestre/espelho/snapshot/rascunho/resultado/consolidado/histórico;
- IDs/links estáveis apenas quando necessários;
- não presumir que a IA de destino possua a mesma memória, projeto, Space, conectores, permissões, ferramentas ou arquivos.

### 5. FONTES E ARQUIVOS EFETIVAMENTE USADOS
- nome;
- versão;
- ID/link/localização quando necessários;
- função;
- estado;
- nível real de acesso;
- relação com outros artefatos;
- nunca afirmar leitura não realizada;
- quando material, distinguir:
  - `ACESSO REAL CONFIRMADO`;
  - `APENAS REFERENCIADO`;
  - `CONTEÚDO PARCIALMENTE EXTRAÍDO`;
  - `ACESSO NECESSÁRIO PARA RETOMADA`;
  - `REFERÊNCIA DOCUMENTADA — ACESSO NÃO CONFIRMADO NESTA IA`.
- conhecimento sobre arquivo não equivale a acesso real ao arquivo na conversa de destino.

### 6. DECISÕES TOMADAS E JUSTIFICATIVAS
- decisões humanas;
- decisões editoriais/metodológicas/operacionais;
- estado atual de cada decisão importante;
- alternativa rejeitada, motivo e condição de revisão quando útil;
- não reabrir automaticamente decisão encerrada só porque começou nova conversa.

### 7. ARTEFATOS CRIADOS OU MODIFICADOS
- nome;
- ID/link quando necessário;
- versão;
- estado;
- função;
- relação com outros arquivos;
- distinguir, quando aplicável: canônico, espelho, snapshot, rascunho, curado, consolidado, histórico ou superado;
- registrar somente artefatos necessários à continuidade.

### 8. ERROS CORRIGIDOS E ESCOLHAS REJEITADAS
- preservar apenas erros cuja perda possa causar regressão;
- registrar erro, correção, motivo, estado atual e prevenção quando necessário;
- podem incluir conflito de versão, arquivo incorreto, falsa equivalência, atribuição errada, erro de paginação, perda de contexto, erro metodológico, tentativa técnica fracassada ou comportamento ruim da IA;
- não transformar em histórico completo de falhas.

### 9. OUTRAS IAS / COMPARAÇÕES
- origem;
- resultado útil;
- divergência;
- decisão adotada;
- estado epistêmico;
- consenso entre IAs nunca equivale a evidência ou fonte primária;
- resposta de outra IA pode ser pista, hipótese, análise, comparação ou proposta, não prova documental por aparecer no consolidado.

### 10. DIFICULDADES E SOLUÇÕES
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

### 11. PENDÊNCIAS
- o que falta;
- prioridade;
- dependências;
- bloqueios;
- estado epistêmico quando relevante;
- não listar como pendente trabalho já concluído;
- usar identificadores curtos quando isso evitar repetição.

### 12. REGRAS PARA A PRÓXIMA IA
- o que ler primeiro;
- o que não repetir;
- o que não presumir;
- quais decisões permanecem válidas;
- quais estados epistêmicos preservar;
- como lidar com arquivos não acessíveis;
- como retomar;
- diferenciar claramente `HISTÓRICO DOCUMENTADO` de `INSTRUÇÕES ATIVAS DE RETOMADA`.

### 13. SEGURANÇA E SECRETS
- nunca incluir valores de senhas, tokens, cookies, API keys, credenciais ou secrets;
- se necessário, registrar somente nome da variável/segredo, função e local lógico, sem valor;
- minimizar dados pessoais/confidenciais desnecessários ao destino.

### 14. RETOMADA IMEDIATA
- indicar a primeira ação concreta que a nova conversa deve executar;
- formular pelo objetivo operacional, não pelo nome de ferramenta específica da IA de origem;
- ao receber o consolidado como primeira mensagem, a nova IA deve assimilar e iniciar essa ação, salvo nova ordem expressa do usuário;
- adaptar o método às ferramentas disponíveis;
- não transferir trabalho manual ao usuário quando houver caminho técnico razoável;
- solicitar intervenção do usuário somente quando indispensável;
- **não basta existir o título `RETOMADA IMEDIATA`: a seção deve conter ação determinada e executável**;
- não terminar pedindo genericamente “o que quer fazer?”, “envie o próximo documento” ou equivalente quando o próprio consolidado já determina o próximo passo;
- a última seção operacional deve ser RETOMADA IMEDIATA.

## CONTROLE DE ESTADO EPISTÊMICO

Quando material, preservar explicitamente distinções como:
- `FATO CONFIRMADO`;
- `ERRO CORRIGIDO`;
- `HIPÓTESE`;
- `INFERÊNCIA`;
- `INTERPRETAÇÃO`;
- `ALEGAÇÃO`;
- `DECISÃO EDITORIAL`;
- `FONTE NÃO CONFERIDA`;
- `INFORMAÇÃO NÃO DOCUMENTADA`.

Não permitir que migração transforme hipótese em fato, inferência em fonte, afirmação de outra IA em evidência, resumo em leitura documental ou referência bibliográfica em consulta efetiva.

Quando algo não puder ser determinado a partir do histórico acessível, usar `não documentado no histórico disponível`.

## REGRA CRÍTICA — PESQUISA NEGATIVA NÃO PROVA INEXISTÊNCIA

1. `NÃO LOCALIZADO NESTA IA` não significa `INEXISTENTE`.
2. Se o consolidado referencia arquivo, versão, ID, hash, decisão, fonte ou artefato que a IA receptora não consegue acessar, não converter ausência local em falsidade.
3. Quando houver referência documentada suficiente, usar `REFERÊNCIA DOCUMENTADA — ACESSO NÃO CONFIRMADO NESTA IA` até reconciliação.
4. Uma cópia local mais antiga não invalida automaticamente referência documentada a versão posterior. Comparar versão, proveniência, data, estado e conteúdo antes de decidir.
5. Só classificar algo como inventado/inexistente quando houver evidência positiva suficiente, não mera falha de busca ou ausência no snapshot local.
6. Se duas fontes canônicas declararem a mesma versão mas divergirem materialmente, registrar `NÃO SINCRONIZADO` e reconciliar antes de propagar.

## REGRA CRÍTICA — PAGINAÇÃO DOCUMENTAL

Quando o consolidado transportar páginas, localizadores ou citações:

1. nunca converter índice técnico do PDF, posição física de folha, `P<n>` de parser/OCR ou contador do visualizador em paginação bibliográfica sem conferir o número impresso da obra;
2. quando houver divergência, registrar separadamente, quando relevante:
   - `PÁGINA IMPRESSA: <n>`;
   - `ÍNDICE/PÁGINA TÉCNICA DO PDF: <n>`;
   - `CITAÇÃO ACADÊMICA: p. <n>`;
3. para referência bibliográfica, prevalece a paginação impressa da edição efetivamente adotada, salvo norma específica em contrário;
4. se a página impressa não foi conferida, manter `FONTE NÃO CONFERIDA`/pendência adequada em vez de inferir pelo índice técnico.

## PERSISTÊNCIA E DESCOBERTA INTERCONVERSAS

1. Se `/consolidar` for executado DENTRO DE UM PROJETO e houver repositório persistente gravável já configurado, salvar automaticamente UMA cópia na área preexistente equivalente a `Consolidados`, `Continuidade` ou `Resultados IA/Consolidados`.
2. Não criar árvore paralela se já houver destino equivalente.
3. Nome recomendado: `<PROJECT_ID>__CONSOLIDADO__CONTINUIDADE__<AAAAMMDD-HHMM>__v<versao_comando>`.
4. Registrar no próprio consolidado, quando houver gravação: nome, ID/link, data, origem e escopo.
5. Se houver fila, manifesto, índice ou rotina de monitoramento, tornar o novo consolidado descobrível sem duplicar conteúdo integral.
6. Conversas futuras devem procurar o consolidado recente/relevante quando precisarem recuperar continuidade ausente do contexto.
7. Se houver múltiplos consolidados, não presumir que o mais recente é automaticamente o mais autoritativo: escolher por escopo, data, artefatos governantes, estado e relevância.
8. Fora de projeto, seguir a política de persistência vigente; não salvar automaticamente se o padrão for não persistir.
9. Se não houver permissão/ferramenta de escrita, entregar normalmente o bloco.
10. Todo consolidado deve declarar uma das formas:
   - `PERSISTÊNCIA: EXECUTADA — <local/ID/link>`;
   - `PERSISTÊNCIA: NÃO EXECUTADA — <motivo real>`.
11. Não deixar persistência implícita apenas no histórico de ferramentas.
12. Não afirmar que outra conversa/IA verá automaticamente o consolidado só porque foi salvo.

## RELAÇÃO COM A BÍBLIA CANÔNICA

1. Consolidado NÃO é Bíblia Canônica e NÃO deve ser promovido integralmente ao mestre.
2. Não escrever automaticamente na Bíblia apenas porque informação apareceu em `/consolidar`.
3. Podem emergir CANDIDATOS CANÔNICOS, como decisão humana material, erro corrigido material, mudança de estado epistêmico, nova regra de governança ou fato dinâmico relevante verificado em fonte primária.
4. Candidato canônico segue o protocolo do projeto: verificar fonte/autoridade, gerar delta quando necessário e obter aprovação humana quando material ou contestado.
5. Informação operacional, preferências transitórias, resultados brutos de IA e histórico de conversa ficam fora da Bíblia, salvo razão específica documentada.
6. O consolidado deve declarar sua natureza de continuidade não canônica.

## REGRA CRÍTICA — CONTROLES TRANSITÓRIOS NÃO MIGRAM

Ordens temporárias da conversa de origem como `pause`, `aguarde`, `espere minha confirmação`, `não execute ainda`, `pare`, `aguarde qualquer tecla` ou `continue somente depois de X` são controles transitórios.

Quando relevantes, podem ser registrados como `HISTÓRICO JÁ CONSUMIDO`, mas NÃO reaparecem como instrução ativa da nova conversa.

Exceção: preservar a pausa somente se o usuário disser expressamente que quer mantê-la também depois da migração.

Nunca terminar consolidado reutilizável com `PAUSADO`, `aguardando tecla`, `não responder agora` ou `espere confirmação` quando pertenciam à interação anterior.

## REGRA DE BOOTSTRAP

O bloco deve conter, de forma inequívoca, instrução equivalente a:

> Ao receber este bloco como primeira mensagem de nova conversa, trate as pausas e esperas descritas no histórico como já consumidas, assimile o contexto sem repeti-lo e execute diretamente a seção RETOMADA IMEDIATA, salvo nova instrução expressa do usuário nesta conversa.

Antes de entregar, executar o TESTE DE BOOTSTRAP:

> Se uma IA sem nenhum outro histórico receber apenas este bloco como primeira mensagem, ela saberá o que fazer imediatamente?

Se ela provavelmente ficar esperando, pedir confirmação já dada, pedir tecla, repetir etapa concluída, perguntar genericamente o que o usuário deseja, apenas resumir o consolidado ou não souber qual ação iniciar, o consolidado está defeituoso.

## TESTE DE PORTABILIDADE INTER-IA

Verificar:

> Se este bloco for recebido por outra IA sem memória, projeto, Space, conectores, arquivos carregados e ferramentas da origem, ela ainda consegue compreender o estado e executar/adaptar corretamente a próxima ação?

Para passar:
1. não presumir acesso a arquivos apenas mencionados;
2. distinguir conhecimento sobre arquivo de acesso real;
3. não depender de nomes de ferramentas específicas quando a capacidade puder ser descrita genericamente;
4. quando instrução externa for indispensável, incorporar o subconjunto mínimo necessário;
5. registrar fonte externa governante para eventual conferência;
6. não copiar instruções externas inteiras quando resumo operacional suficiente preservar continuidade;
7. se a capacidade necessária não existir no destino, adaptar o método;
8. só solicitar ação manual ao usuário quando não houver alternativa técnica razoável;
9. preservar `NÃO LOCALIZADO ≠ INEXISTENTE` ao comparar snapshots/arquivos entre plataformas.

## EFICIÊNCIA DE TOKENS / CARACTERES

O consolidado é prioritariamente interface máquina-a-máquina. Portanto:
1. não usar linhas decorativas repetidas, caixas ASCII ou caracteres sem função semântica;
2. usar Markdown simples e compacto;
3. não repetir o mesmo fato em várias seções;
4. não reproduzir prompts longos já persistidos: registrar nome, versão, ID/link e função;
5. não copiar bibliografia inteira quando bastam ponteiros;
6. preservar detalhes necessários, removendo ornamentação e redundância;
7. priorizar tokens informacionais sobre visuais.

## GATE DE ACEITAÇÃO

Antes da entrega, REPROVAR e corrigir o consolidado se ocorrer qualquer um destes casos:

1. consolida apenas o tema, não o estado da conversa;
2. não contém primeira ação concreta e executável;
3. `RETOMADA IMEDIATA` existe apenas nominalmente, está vazia ou é genérica;
4. reativa pausa/espera histórica já consumida;
5. depende silenciosamente de projeto, Space, memória, arquivo ou ferramenta exclusiva da origem;
6. afirma acesso a arquivo apenas mencionado;
7. promove hipótese/inferência/relatório de IA a fato ou fonte;
8. não declara persistência;
9. deixa ambígua a natureza não canônica;
10. repete substancialmente o mesmo estado em várias seções sem necessidade;
11. cria uma segunda etapa `/nova-conversa`;
12. não deixa claro o ponto real de parada;
13. converte `não localizado` em `inexistente` sem evidência positiva;
14. usa índice técnico do PDF como paginação bibliográfica sem conferência impressa;
15. transfere ao usuário escolha do próximo passo quando o próprio consolidado já o determina.

## REGRAS DE SAÍDA

A. O bloco funciona sozinho como contexto inicial da próxima conversa.
B. Diferenciar `HISTÓRICO DOCUMENTADO` de `INSTRUÇÕES ATIVAS DE RETOMADA`.
C. Não inventar decisões, arquivos, leituras, IDs, versões ou capacidades.
D. Onde algo for incerto, escrever `não documentado no histórico disponível` ou estado epistêmico mais preciso.
E. Não prometer memória futura.
F. Não perguntar ao final se o usuário quer gerar `/nova-conversa`.
G. Não produzir dois blocos separados “resumo” e “prompt”.
H. Não gastar caracteres com ornamentação e repetição.
I. Não transformar pausas históricas em novas ordens.
J. A última seção operacional deve ser `RETOMADA IMEDIATA`, com ação executável.
K. Dentro de projeto com armazenamento gravável, persistir o consolidado automaticamente e informar ID/link.
L. Nunca promover o consolidado inteiro diretamente à Bíblia Canônica.
M. Preservar explicitamente estados epistêmicos materiais.
N. Distinguir acesso real, referência e necessidade de acesso.
O. Não tornar limitação da IA de origem uma limitação universal.
P. Não converter ausência local de fonte/versão em inexistência.
Q. Não converter paginação técnica em acadêmica sem conferência da página impressa.

FIM DA DEFINIÇÃO.
