COMANDO: /pafe audio
ARQUIVO: pafe/audio.md
PARENTE: pafe/README.md

O QUE É: política técnica e operacional do áudio de estudo gerado pelo P.A.F.E.

QUANDO USAR: acionar quando o usuário pedir áudio, MP3, roteiro de áudio, audio.yaml, script Python, gerar_audio.py, revisão oral, ElevenReader, ElevenLabs API ou usar /pafe audio.

REGRA DE OURO: a IA pode gerar roteiro, audio.yaml ou script Python local. A IA nunca afirma ter gerado MP3 sem que o arquivo real exista.

1. ESCOPO

1.1. Este arquivo regula o fluxo de áudio do P.A.F.E.

1.2. O padrão do P.A.F.E. é execução local controlada e reprodutível, embora o edge-tts dependa de conexão e serviço externo online.

1.3. O áudio pode assumir quatro modos:
1.3.1. roteiro textual para leitura humana ou TTS;
1.3.2. pipeline local com edge-tts;
1.3.3. modo manual premium com ElevenReader;
1.3.4. modo programático premium condicional com ElevenLabs API.

1.4. O modo usado deve ser declarado antes da entrega.

2. ROTEIRO TEXTUAL

2.1. Estruturar o roteiro em blocos curtos, com títulos faláveis e pausas naturais.

2.2. Priorizar frases claras, ritmo estável e baixa carga cognitiva.

2.3. Incluir, quando útil:
2.3.1. abertura curta;
2.3.2. módulos numerados;
2.3.3. conceitos essenciais;
2.3.4. autores e fundamentos;
2.3.5. pegadinhas;
2.3.6. revisão relâmpago;
2.3.7. fechamento objetivo.

2.4. Criar dicionário fonético quando houver termos jurídicos, latinos, estrangeiros ou nomes com pronúncia delicada.

2.5. Quando o roteiro for para ElevenReader, evitar Markdown pesado, tabelas, YAML, JSON, código e marcações técnicas.

3. audio.yaml

3.1. audio.yaml descreve blocos, vozes, ordem, pausas e parâmetros de síntese.

3.2. Deve ser validável por PyYAML antes da síntese.

3.3. Campos mínimos:
3.3.1. id do bloco;
3.3.2. voz;
3.3.3. texto;
3.3.4. pausa pós-bloco;
3.3.5. ordem.

3.4. Campos opcionais:
3.4.1. engine;
3.4.2. voice_id;
3.4.3. model_id;
3.4.4. output_format;
3.4.5. speed;
3.4.6. pitch;
3.4.7. chapter_title;
3.4.8. observações de fallback.

3.5. Quando usar API premium, registrar metadados disponíveis, sem expor chave.

4. SCRIPT PYTHON LOCAL

4.1. O script padrão deve ser gerar_audio.py.

4.2. O script deve:
4.2.1. ler audio.yaml;
4.2.2. sintetizar blocos;
4.2.3. concatenar com pydub;
4.2.4. exportar com ffmpeg;
4.2.5. inserir metadados com mutagen quando aplicável;
4.2.6. registrar falhas de forma clara;
4.2.7. não instalar dependências sem autorização.

4.3. O script deve parar em erro relevante. Não deve gerar áudio degradado apenas para cumprir tarefa.

4.4. Se a plataforma não permitir execução, entregar roteiro, audio.yaml e script, declarando:
[ARTEFATO: execução local necessária]

5. MOTOR DE TTS

5.1. Padrão gratuito do P.A.F.E.: edge-tts, executado localmente, mas dependente de conexão e serviço externo online.

5.2. Vozes pt-BR principais para edge-tts:
5.2.1. pt-BR-FranciscaNeural — conceitos e sínteses;
5.2.2. pt-BR-AntonioNeural — autores e fundamentação;
5.2.3. pt-BR-ThalitaNeural — revisão, alertas e zona de perigo.

5.3. gTTS não é solução principal.

5.4. Piper TTS pode ser plano offline eventual, com qualidade inferior assumida e declarada.

5.5. espeak, espeak-ng, pyttsx3 e Festival são proibidos como fallback padrão.

5.6. espeak, espeak-ng, pyttsx3 e Festival só podem ser usados se:
5.6.1. o usuário pedir expressamente;
5.6.2. a perda de qualidade for declarada;
5.6.3. não houver falsa promessa de áudio neural.

6. DEPENDÊNCIAS LOCAIS

6.1. Dependências Python usuais:
6.1.1. edge-tts;
6.1.2. pydub;
6.1.3. mutagen;
6.1.4. PyYAML;
6.1.5. python-dotenv, se houver .env local.

6.2. Binário de sistema:
6.2.1. ffmpeg.

6.3. PATH recomendado:
export PATH="$HOME/.local/bin:$PATH"

6.4. .env e cache devem ficar fora de repositório público.

6.5. Diretório local recomendado:
~/.pafe-local

6.6. Nunca salvar .env, tokens, chaves ou credenciais em GitHub, Drive público, Box compartilhado ou logs.

7. ESTRUTURA DE ARQUIVO E LOOP

7.1. Um único MP3 master por padrão.

7.2. Caminho padrão:
audio/master_audio.mp3

7.3. O loop é responsabilidade do HTML.

7.4. Jamais multiplicar o MP3 no Python para simular loop.

7.5. Se o arquivo MP3 não existir, não afirmar que foi gerado.

8. PREFLIGHT OBRIGATÓRIO ANTES DE ÁUDIO LONGO

8.1. Verificar DNS:
nslookup speech.platform.bing.com

8.2. Verificar vozes:
edge-tts --list-voices | grep pt-BR

8.3. Teste curto:
edge-tts --voice pt-BR-FranciscaNeural --text "Teste PAFE." --write-media teste_pafe.mp3

8.4. Validar arquivo:
ffprobe -v error -show_entries format=duration,bit_rate -of default=noprint_wrappers=1 teste_pafe.mp3

8.5. Rodar áudio longo apenas depois do teste curto aprovado.

9. DIAGNÓSTICO DE FALHAS

9.1. DNS — "Temporary failure in name resolution":
9.1.1. indica ambiente sem rede externa real ou falha de resolução;
9.1.2. típico de sandbox de IA;
9.1.3. não é corrigível por código Python;
9.1.4. SSL relaxado não corrige DNS;
9.1.5. solução: rodar em máquina local com rede funcional.

9.2. Certificado — "CERTIFICATE_VERIFY_FAILED":
9.2.1. pode indicar proxy com inspeção TLS;
9.2.2. SSL relaxado é exceção, nunca padrão;
9.2.3. proibido com senha, token, API key ou dado sensível;
9.2.4. se usado excepcionalmente, deve gerar log claro.

9.3. Endpoint fora — HTTP 5xx ou indisponibilidade:
9.3.1. aguardar e repetir;
9.3.2. se persistir, migrar para plano alternativo autorizado.

9.4. Autenticação — HTTP 401 ou 403:
9.4.1. pode indicar chave inválida, ausente, sem permissão, escopo insuficiente ou acesso negado;
9.4.2. não pedir ao usuário para colar chave no chat;
9.4.3. orientar verificação local da variável de ambiente.

9.5. Cota ou limite — HTTP 402 ou 429:
9.5.1. pode indicar crédito insuficiente, cota excedida, plano inadequado ou rate limit;
9.5.2. registrar falha;
9.5.3. não insistir em loop de chamadas;
9.5.4. usar fallback apenas se autorizado.

9.6. Em qualquer falha:
9.6.1. parar com erro claro;
9.6.2. não gerar áudio degradado sem autorização;
9.6.3. registrar classe do erro;
9.6.4. indicar próxima ação objetiva.

10. ELEVENREADER E ELEVENLABS API

10.1. Escopo

10.1.1. Esta seção regula o uso opcional de recursos ElevenReader e ElevenLabs no fluxo de áudio do P.A.F.E.

10.1.2. ElevenReader Ultra é modo manual premium de escuta e revisão.

10.1.3. ElevenLabs API é modo programático premium condicional.

10.1.4. ElevenReader Ultra não substitui automaticamente o pipeline local do P.A.F.E.

10.1.5. Não presumir que ElevenReader Ultra inclui créditos de ElevenLabs API.

10.2. Modo ElevenReader, sem API

10.2.1. Usar quando o objetivo for escuta rápida, revisão em mobilidade ou leitura de textos longos.

10.2.2. A IA deve gerar apenas roteiro textual limpo, pronto para colar ou importar no ElevenReader.

10.2.3. O roteiro deve evitar Markdown pesado, tabelas, blocos de código, YAML, JSON, símbolos excessivos e formatação que prejudique leitura em voz alta.

10.2.4. O roteiro deve usar frases curtas, pontuação rítmica e títulos faláveis.

10.2.5. Siglas e números relevantes devem ser escritos por extenso quando isso melhorar a pronúncia.

10.2.6. Este modo não gera MP3 programático.

10.2.7. Downloads offline do ElevenReader não devem ser presumidos como arquivo MP3 exportável.

10.2.8. Usar este modo como recurso temporário enquanto houver acesso Ultra ativo.

10.3. Modo ElevenLabs API

10.3.1. Usar apenas se o usuário confirmar:
10.3.1.1. API key válida;
10.3.1.2. créditos ou cota disponíveis;
10.3.1.3. autorização expressa para uso programático.

10.3.2. A chave deve ficar somente em variável de ambiente ou .env local.

10.3.3. Nunca colocar chave no chat, GitHub, Drive, Box, HTML, JavaScript client-side ou logs.

10.3.4. Variável recomendada:
ELEVENLABS_API_KEY

10.3.5. Dependência Python opcional:
elevenlabs

10.3.6. Quando disponíveis, o script pode registrar metadados como:
10.3.6.1. engine;
10.3.6.2. voice_id;
10.3.6.3. model_id;
10.3.6.4. output_format;
10.3.6.5. character_count;
10.3.6.6. request_id;
10.3.6.7. arquivo gerado;
10.3.6.8. data da geração;
10.3.6.9. observações de fallback.

10.3.7. A API não deve ser usada com material sensível, dados pessoais, peças jurídicas, documentos de clientes, processos, credenciais ou conteúdo privado sem sanitização prévia.

10.4. Relação entre motores

10.4.1. edge-tts permanece como padrão gratuito e reprodutível.

10.4.2. ElevenReader é atalho manual premium temporário.

10.4.3. ElevenLabs API é motor premium opcional e condicional.

10.4.4. Piper pode ser alternativa offline eventual.

10.4.5. Fallback automático para edge-tts só deve ocorrer se:
10.4.5.1. o usuário autorizar;
10.4.5.2. o texto não for sensível;
10.4.5.3. a falha da API estiver clara;
10.4.5.4. o script registrar a troca de motor no audio.yaml.

10.5. Proibições específicas

10.5.1. Não afirmar que ElevenReader gerou MP3 exportável.

10.5.2. Não presumir que ElevenReader Ultra inclui créditos de API.

10.5.3. Não usar ElevenLabs API sem confirmação de cota, chave e autorização.

10.5.4. Não colar API key no chat.

10.5.5. Não salvar .env, tokens ou chaves em repositório público.

10.5.6. Não usar material sensível em ElevenReader ou ElevenLabs API sem sanitização.

10.6. Roteiro textual para ElevenReader

10.6.1. Quando o usuário pedir áudio via ElevenReader, entregar apenas o roteiro textual limpo.

10.6.2. Estrutura recomendada:
10.6.2.1. abertura curta;
10.6.2.2. módulos numerados;
10.6.2.3. explicação direta;
10.6.2.4. alertas de pegadinha;
10.6.2.5. resumo final;
10.6.2.6. revisão relâmpago.

10.6.3. Não incluir tabelas, YAML, JSON, código ou marcações técnicas no roteiro para ElevenReader.

11. AMBIENTE INDISPONÍVEL

11.1. Se a máquina local não permitir internet, ffmpeg ou dependências TTS, entregar roteiro e script e declarar:
[ARTEFATO: execução local necessária]

11.2. Se a plataforma não permitir gerar arquivo, declarar:
[ARTEFATO: indisponível nesta plataforma]

11.3. Se apenas o código for entregue, declarar:
[ARTEFATO: código gerado]

11.4. Não afirmar que o MP3 foi gerado se o arquivo real não existir.

12. PROIBIÇÕES GERAIS

12.1. Proibido afirmar geração de MP3 sem arquivo real.

12.2. Proibido instalar dependências sem autorização do usuário.

12.3. Proibido usar fallback robótico como padrão.

12.4. Proibido colocar chave, token ou .env em repositório público.

12.5. Proibido usar SSL relaxado fora da exceção técnica declarada.

12.6. Proibido usar API paga sem autorização expressa.

12.7. Proibido tratar ElevenReader como API.

12.8. Proibido substituir edge-tts por ElevenReader.

13. SAÍDA

13.1. Entregar roteiro, audio.yaml ou script completo, conforme pedido.

13.2. Não entregar patch, trecho solto ou "insira aqui".

13.3. Se o arquivo for longo demais para uma resposta segura, dividir por partes apenas com controle explícito de continuidade.

13.4. Em pedido de correção de script existente, carregar o original integral antes de editar.
