# pafe_prompt_outras_ias.md

**Versão:** 1.6  
**Data:** 2026-07-17  
**Escopo:** GPT, Gemini, Perplexity e outras IAs.

## 1. Regra de plataforma

1. Aplicar primeiro o overlay específico da plataforma, quando existir.
2. ChatGPT/GPT: ler `pafe_gpt.md`.
3. Claude com execução ativa: ler `pafe_claude.md`.
4. Gemini, Perplexity e outras IAs: usar somente capacidades efetivamente disponíveis.

## 2. Regras comuns

1. Um MP3 neural por assunto.
2. Nenhum master único por padrão.
3. Não usar fallback robótico.
4. Não declarar MP3 gerado sem arquivo físico validado.
5. Se houver HTML, aplicar `html.md`: HTML separado, sem áudio, player ou impressão.

## 3. Lançador

```text
/mpe
P.A.F.E. — INICIALIZAÇÃO

DISCIPLINA: [nome]
OBJETIVO: [resultado]
ANEXOS: [listar]

1. Leia README.md, audio_modos.md, audio.md e pafe_governanca_overlays.md.
2. Leia o overlay específico da plataforma: pafe_gpt.md para GPT ou pafe_claude.md para Claude.
3. Leia os anexos acessíveis e não invente conteúdo.
4. Para áudio, gere um MP3 neural por assunto e valide cada arquivo.
5. Não use voz robótica nem gere apenas um master.
6. Para HTML, gere arquivo separado, sem áudio, player ou impressão.
```

## 4. Teste bloqueante

Reprovar se a IA ignorar o overlay da própria plataforma, fingir geração, usar voz robótica, produzir apenas um master ou inserir áudio no HTML.
