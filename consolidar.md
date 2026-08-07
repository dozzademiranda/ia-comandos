---
Gerado por: GPT-5.6 Sol
Data de geração: 07/08/2026
Versão: 2.1.0
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

FIM DA DEFINIÇÃO.
