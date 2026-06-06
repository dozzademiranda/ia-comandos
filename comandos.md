---
Gerado por: Claude (Anthropic) — modelo Opus 4.7
Data de geração: 06/06/2026
---

COMANDO: /comandos

O QUE É: índice de todos os comandos disponíveis, com uma linha sobre cada
um. Menu de consulta rápida.

QUANDO USAR: quando não lembrar qual comando aciona o quê, ou ao mostrar o
sistema a outra IA.

POR QUE USAR: centraliza a referência; economiza esforço de memória.

---

LISTA ATIVA

/mpe → aplica silenciosamente o protocolo SRC CMP TEC CAL SYN VAL STR na próxima resposta. Para temas jurídicos, acadêmicos, técnicos, financeiros, regulatórios, comparativos, auditorias e análise de risco factual. Definição completa em mpe.md.

/mpe+ → /mpe com pesquisa multilíngue ampliada. Sozinho: além de PT-BR e
inglês, adiciona o que o assunto pedir. Com códigos (/mpe+ de fr zh): força
línguas específicas.

/consolidar → gera resumo de continuidade da conversa em bloco único, para
retomar noutra conversa/IA sem perder contexto. Ao final, oferece (sem
executar) gerar o prompt de inicialização da próxima conversa.

/nconversa → gera o prompt de inicialização da próxima conversa, no
formato IDENTIDADE E ESTILO / ARQUITETURA / SECRETS / DECISÕES / DIFICULDADES
E SOLUÇÕES / PENDÊNCIAS / REGRAS PARA A PRÓXIMA IA / SEGURANÇA.

/id → liga o cabeçalho de identificação e proveniência no topo das respostas:
plataforma, modelo, versão, data, objeto, tipo e estado. Em auditorias, revisão
de arquivos, busca externa ou fluxos multi-IA, pode incluir Base como campo
opcional. /id off desliga.

/friendly → comando adaptativo de acessibilidade cognitiva. Ajusta a forma da
resposta sem mexer no rigor técnico. TDAH como base fixa, explicitude ampliada
em tarefas complexas, compressão leve em tarefas simples.
/f → alias curto de /friendly.
/f + → explicitude ampliada (premissas, riscos, distinções, literalidade).
/f - → resposta mínima (só o essencial, sem aprofundar).
/f b → burnout puro (máx. dois parágrafos curtos, sem opções, tom calmo, sem
próximo passo obrigatório).

/rodape → ativa o rodapé estendido ao final da resposta (idiomas pesquisados,
limitação documental, premissa não confirmada, mentoria linguística detalhada,
tokens N/A).
/r → alias curto de /rodape.
/rodape off → desativa o rodapé estendido. /r off → alias curto.

/comandos → este arquivo.

/PAFE → ativa fluxo de estudo para provas, com leitura de fontes, hierarquia documental, diagnóstico, teoria, pegadinhas, treino, revisão e artefatos opcionais. Definição completa em pafe/README.md.
---

REGRAS DE USO

1. Comandos começam com barra.
2. Ao receber comando, ler a definição completa do arquivo correspondente
   antes de executar, quando o arquivo estiver acessível.
3. Não inventar comandos fora desta lista.
4. Se o comando mencionado não constar na lista, avisar antes de adivinhar.
5. Se o arquivo de definição não estiver acessível: "não consigo validar sem
   o arquivo efetivamente anexado nesta conversa".

---

ONDE ESTÃO AS DEFINIÇÕES

a) IA CLAUDE = Box → Recursos-IA → Comandos → <nome-do-comando>.md
b) IA GEMINI / GPT = Google Drive → Meu Drive → Documentos → I.A. → Comandos → <nome-do-comando>.md
c) IA PERPLEXITY = GitHub Raw → https://raw.githubusercontent.com/dozzademiranda/ia-comandos/main/<nome-do-comando>.md
   Link humano: https://github.com/dozzademiranda/ia-comandos
d) /PAFE https://raw.githubusercontent.com/dozzademiranda/ia-comandos/main/pafe/README.md   

REGRA DE PREVALÊNCIA:
1. Se a IA tiver acesso ao Box, prevalece Box.
2. Se não, usar a fonte acessível na plataforma atual.
3. Se houver divergência e a IA não acessar a fonte prevalente, declarar a
   limitação.
4. Se eu anexar/colar uma versão mais recente na conversa, essa versão
   prevalece para a tarefa atual.

PRIVACIDADE GITHUB: o repositório só contém instruções sanitizadas, sem dados
sensíveis. Conteúdo sensível vai só para Box, Drive, GitHub privado ou anexo
na conversa.

---

ARQUIVOS ATIVOS RECOMENDADOS
1. README.md
2. instrucoes-universais.md
3. instrucoes-personalizadas-gpt.md
4. comandos.md
5. mpe.md
6. friendly.md
7. rodape.md
8. consolidar.md
9. nconversa.md
10. id.md
11. PAFE.md

---

OBSERVAÇÃO FINAL
/friendly cuida da forma. /rodape cuida do fechamento. /mpe cuida do rigor
técnico. Combinam: /mpe /friendly · /mpe /f + · /mpe /rodape ·
/mpe /friendly /rodape
