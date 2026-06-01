---
Gerado por: Claude (Anthropic) — modelo Opus 4.8
Data de geração: 30/05/2026
---

COMANDO: /id

O QUE É: ativa, na conversa em curso, o hábito de carimbar cada
resposta com um cabeçalho de identificação curto. Útil em comparações
multi-IA (sete, oito, nove IAs em paralelo) para saber a origem de
cada resposta sem confusão.

QUANDO USAR: ao iniciar uma rodada de comparação multi-IA, antes da
pergunta que será também feita às outras IAs.

POR QUE USAR: você ativa uma vez e o carimbo vale para a conversa
inteira, sem redigitar a cada mensagem.

NÃO CONFUNDIR COM: /comandos (que lista os comandos disponíveis).
/id apenas LIGA o carimbo de identidade.

---

DEFINIÇÃO OPERACIONAL

Após /id, iniciar TODA resposta seguinte com este cabeçalho, em uma
linha só:

[Plataforma: Claude.ai | Modelo: <modelo atual> | Versão: <versão> | Data: <YYYY-MM-DD HH:MM> | Objeto: <4-6 palavras sobre o que está sendo respondido>]

Manter o carimbo até /id off, que desativa.

Se a versão exata não for conhecida com certeza: escrever "versão não
disponível", nunca inventar.
