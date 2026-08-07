---
Gerado por: GPT-5.6 Sol
Data de geração: 07/08/2026
Versão: 2.0.0
Estado: canônico sanitizado
---

COMANDO: /consolidar

O QUE É: gera UM bloco único de continuidade que serve simultaneamente como:
1. resumo auditável da conversa atual; e
2. prompt autocontido de retomada, pronto para ser colado como primeira mensagem de uma nova conversa, na mesma IA ou em outra.

QUANDO USAR: quando a conversa ficou longa, antes de trocar de conversa/IA, diante de muitos anexos, decisões, versões, testes ou risco de perda de continuidade.

POR QUE USAR: preserva o que já foi decidido, o que foi tentado, o que foi corrigido e o que ainda falta, sem obrigar o usuário a executar um segundo comando apenas para transformar o resumo em prompt de retomada.

RELAÇÃO COM /nova-conversa: /nova-conversa passa a ser alias de compatibilidade de /consolidar. Não existe mais uma segunda etapa obrigatória.

---

DEFINIÇÃO OPERACIONAL

Ao receber /consolidar, gerar UM ÚNICO BLOCO DE CÓDIGO, autocontido e pronto para copiar, contendo, quando pertinente:

1. IDENTIFICAÇÃO E PROVENIÊNCIA
   - plataforma/IA/modelo, quando documentados;
   - data;
   - projeto/conversa;
   - comandos/protocolos ativos.

2. IDENTIDADE E ESTILO
   - somente preferências e restrições documentadas que sejam materialmente úteis à continuidade.

3. CONTEXTO, OBJETO E OBJETIVO
   - o que está sendo feito;
   - para quê;
   - onde a conversa parou.

4. ARQUITETURA E GOVERNANÇA
   - hierarquia de fontes;
   - documentos governantes;
   - comandos/protocolos relevantes;
   - IDs/links estáveis quando necessários.

5. FONTES E ARQUIVOS EFETIVAMENTE USADOS
   - nome;
   - ID/link/localização quando documentados;
   - função de cada fonte relevante;
   - não afirmar leitura de arquivo que não foi realmente lido.

6. DECISÕES TOMADAS E JUSTIFICATIVAS
   - decisões humanas;
   - decisões editoriais/operacionais;
   - estado atual de cada decisão quando importante.

7. ARTEFATOS CRIADOS OU MODIFICADOS
   - nome;
   - ID/link;
   - versão/estado;
   - o que é canônico, espelho, rascunho, curado, consolidado ou histórico.

8. ERROS CORRIGIDOS E ESCOLHAS REJEITADAS
   - erro anterior;
   - correção;
   - motivo;
   - prevenção de recorrência, quando útil.

9. RESPOSTAS DE OUTRAS IAS ANALISADAS
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
    - não repetir trabalho fracassado sem motivo novo.

11. PENDÊNCIAS
    - o que ainda falta;
    - prioridade;
    - dependências;
    - bloqueios.

12. REGRAS PARA A PRÓXIMA IA
    - o que deve ler primeiro;
    - o que não deve repetir;
    - o que não deve presumir;
    - como retomar exatamente do ponto atual.

13. SEGURANÇA E SECRETS
    - nunca incluir valores de senhas, tokens, cookies, API keys ou credenciais;
    - se necessário, registrar apenas NOMES de variáveis/segredos e sua função.

14. OBJETIVO IMEDIATO / PRÓXIMO PASSO
    - a ação concreta que a nova conversa deve executar primeiro.

REGRAS DE SAÍDA

A. O bloco deve funcionar sozinho como contexto inicial da próxima conversa.
B. Diferenciar claramente HISTÓRICO DOCUMENTADO de INSTRUÇÕES PARA RETOMADA.
C. Não inventar decisões, arquivos, leituras, IDs ou capacidades.
D. Onde algo for incerto, escrever: "não documentado no histórico disponível".
E. Não prometer memória futura.
F. Não pedir ao final se o usuário quer gerar /nova-conversa: o próprio resultado já cumpre essa função.
G. Não produzir dois blocos separados "resumo" e "prompt"; produzir uma única peça híbrida de continuidade.
H. Não gastar espaço com explicações genéricas que não mudem a retomada.

FIM DA DEFINIÇÃO.
