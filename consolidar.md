---
Gerado por: GPT-5.6 Sol
Data de geração: 07/08/2026
Versão: 2.2.0
Estado: canônico sanitizado
---

COMANDO: /consolidar

O QUE É: gera UM bloco único de continuidade que serve simultaneamente como:
1. resumo auditável da conversa atual; e
2. prompt autocontido de retomada, pronto para ser colado como primeira mensagem de uma nova conversa, na mesma IA ou em outra.

QUANDO USAR: quando a conversa ficou longa, antes de trocar de conversa/IA, diante de muitos anexos, decisões, versões, testes ou risco de perda de continuidade.

POR QUE USAR: preserva decisões, fontes, artefatos, erros, soluções e pendências sem exigir um segundo comando para transformar o resumo em prompt de retomada.

RELAÇÃO COM /nova-conversa: /nova-conversa é alias de compatibilidade de /consolidar. Não existe segunda etapa obrigatória.

DEFINIÇÃO OPERACIONAL

Ao receber /consolidar, gerar UM ÚNICO BLOCO DE CÓDIGO, autocontido e pronto para copiar, contendo somente o necessário para continuidade confiável.

1. IDENTIFICAÇÃO E PROVENIÊNCIA
- plataforma/IA/modelo quando documentados;
- data;
- projeto/conversa;
- comandos/protocolos materialmente relevantes.

2. IDENTIDADE E ESTILO
- somente preferências e restrições documentadas que alterem materialmente a continuidade.

3. CONTEXTO, OBJETO E OBJETIVO
- o que está sendo feito;
- para quê;
- ponto real em que o trabalho parou.

4. ARQUITETURA E GOVERNANÇA
- hierarquia de fontes;
- documentos governantes;
- comandos/protocolos relevantes;
- IDs/links estáveis apenas quando necessários para recuperar artefatos.

5. FONTES E ARQUIVOS EFETIVAMENTE USADOS
- nome;
- ID/link/localização quando necessários;
- função da fonte;
- nunca afirmar leitura não realizada.

6. DECISÕES TOMADAS E JUSTIFICATIVAS
- decisões humanas;
- decisões editoriais/operacionais;
- estado atual de cada decisão importante.

7. ARTEFATOS CRIADOS OU MODIFICADOS
- nome;
- ID/link quando necessário;
- versão/estado;
- relação canônico/espelho/rascunho/curado/consolidado/histórico.

8. ERROS CORRIGIDOS E ESCOLHAS REJEITADAS
- erro;
- correção;
- motivo;
- prevenção de recorrência quando útil.

9. OUTRAS IAS / COMPARAÇÕES
- origem;
- resultado útil;
- divergências;
- conclusão comparativa;
- nunca tratar consenso de IAs como prova.

10. DIFICULDADES E SOLUÇÕES
- limitações técnicas;
- permissões;
- tentativas que falharam;
- solução já encontrada;
- não repetir tentativa fracassada sem motivo novo.

11. PENDÊNCIAS
- o que falta;
- prioridade;
- dependências;
- bloqueios.

12. REGRAS PARA A PRÓXIMA IA
- o que ler primeiro;
- o que não repetir;
- o que não presumir;
- como retomar do ponto atual.

13. SEGURANÇA E SECRETS
- nunca incluir valores de senhas, tokens, cookies, API keys ou credenciais;
- se necessário, registrar apenas nomes de variáveis/segredos e sua função.

14. RETOMADA IMEDIATA
- indicar a primeira ação concreta que a nova conversa deve executar;
- ao receber o consolidado como primeira mensagem, a nova IA deve assimilá-lo e iniciar essa ação, salvo nova ordem expressa do usuário na conversa nova.

PERSISTÊNCIA E DESCOBERTA INTERCONVERSAS

1. Se /consolidar for executado DENTRO DE UM PROJETO e houver repositório persistente gravável já configurado para esse projeto, salvar automaticamente UMA cópia do consolidado na área preexistente equivalente a `Consolidados`, `Continuidade` ou `Resultados IA/Consolidados`.
2. Não criar uma árvore paralela se já existir destino equivalente.
3. Nome recomendado: `<PROJECT_ID>__CONSOLIDADO__CONTINUIDADE__<AAAAMMDD-HHMM>__v<versao_comando>`.
4. Registrar no próprio consolidado, quando a gravação ocorrer: nome, ID/link, data, origem e escopo.
5. Se o projeto possuir fila, manifesto, índice ou rotina de monitoramento de continuidade, registrar ou tornar descobrível o novo consolidado por esse mecanismo, sem duplicar o conteúdo integral.
6. Conversas futuras devem procurar o consolidado recente/relevante do projeto quando precisarem recuperar continuidade não presente no contexto atual.
7. Se houver múltiplos consolidados, não presumir que o mais recente é automaticamente o mais autoritativo: escolher pelo escopo, data, artefatos governantes e relevância para a tarefa.
8. Fora de projeto, seguir a política de persistência vigente; não salvar automaticamente se o padrão do ambiente for não persistir.
9. Se não houver permissão de escrita, entregar normalmente o bloco e registrar `PERSISTÊNCIA: NÃO EXECUTADA — <motivo real>`.
10. Não afirmar que outra conversa ou IA verá o consolidado automaticamente apenas porque ele foi salvo: a recuperação depende de busca, índice, fila, tarefa agendada ou conector disponível.

RELAÇÃO COM A BÍBLIA CANÔNICA

1. Consolidado NÃO é Bíblia Canônica e NÃO deve ser promovido integralmente ao mestre.
2. Não escrever automaticamente na Bíblia apenas porque uma informação apareceu em /consolidar.
3. Do consolidado podem emergir CANDIDATOS CANÔNICOS, por exemplo:
   - decisão humana material;
   - erro corrigido material;
   - mudança de estado epistêmico;
   - nova regra de governança;
   - fato dinâmico relevante já verificado em fonte primária.
4. Candidato canônico deve seguir o protocolo do projeto: verificar fonte/autoridade, gerar delta quando necessário e obter aprovação humana quando a mudança for material ou contestada.
5. Informação operacional, preferências transitórias, resultados brutos de IA e histórico de conversa permanecem fora da Bíblia, salvo razão específica documentada.

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

Nunca terminar um consolidado reutilizável com comandos como:
- PAUSADO;
- aguardando tecla;
- não responder agora;
- espere confirmação;
quando esses comandos pertenciam à conversa anterior.

REGRA DE BOOTSTRAP

O bloco deve conter, de forma inequívoca, instrução equivalente a:

"Ao receber este bloco como primeira mensagem de nova conversa, trate as pausas e esperas descritas no histórico como já consumidas, assimile o contexto sem repeti-lo e execute diretamente a seção RETOMADA IMEDIATA, salvo nova instrução expressa do usuário nesta conversa."

Antes de entregar o consolidado, executar mentalmente o TESTE DE BOOTSTRAP:

"Se uma IA sem nenhum outro histórico receber apenas este bloco como primeira mensagem, ela saberá o que fazer imediatamente?"

Se a resposta provável for que ela:
- ficará esperando;
- pedirá confirmação já dada;
- pedirá uma tecla;
- repetirá etapa concluída;
- ou não saberá qual ação iniciar;

o consolidado está defeituoso e deve ser corrigido antes da entrega.

EFICIÊNCIA DE TOKENS / CARACTERES

O consolidado é prioritariamente uma interface máquina-a-máquina. Portanto:

1. não usar linhas decorativas repetidas com `=`, `-`, `_`, `*`, caixas ASCII ou outros caracteres sem função semântica;
2. usar Markdown simples e compacto: títulos curtos, listas e campos;
3. não repetir o mesmo fato em múltiplas seções;
4. não reproduzir prompts longos já persistidos: registrar nome, versão, ID/link e função;
5. não copiar bibliografia inteira quando bastam ponteiros para as fontes relevantes;
6. preservar detalhes necessários à continuidade, mas remover ornamentação e redundância;
7. priorizar tokens informacionais sobre tokens visuais, especialmente em transferências para plataformas com contexto limitado ou caro.

REGRAS DE SAÍDA

A. O bloco deve funcionar sozinho como contexto inicial da próxima conversa.
B. Diferenciar HISTÓRICO DOCUMENTADO de INSTRUÇÕES ATIVAS DE RETOMADA.
C. Não inventar decisões, arquivos, leituras, IDs ou capacidades.
D. Onde algo for incerto, escrever: `não documentado no histórico disponível`.
E. Não prometer memória futura.
F. Não perguntar ao final se o usuário quer gerar /nova-conversa: o próprio resultado já cumpre essa função.
G. Não produzir dois blocos separados "resumo" e "prompt".
H. Não gastar caracteres com explicações genéricas, separadores ornamentais ou repetição.
I. Não transformar pausas históricas em novas ordens de pausa.
J. A última seção operacional deve ser RETOMADA IMEDIATA, com ação executável.
K. Dentro de projeto com armazenamento gravável, persistir o consolidado automaticamente e informar o ID/link.
L. Nunca promover o consolidado inteiro diretamente à Bíblia Canônica.

FIM DA DEFINIÇÃO.
