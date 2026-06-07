
COMANDO: /pafe audio
ARQUIVO: pafe/audio.md
PARENTE: pafe/README.md

O QUE É: política técnica e operacional do áudio de estudo gerado pelo P.A.F.E.

QUANDO USAR: só é acionado quando o usuário pedir áudio, MP3, roteiro, audio.yaml, script Python ou usar /pafe audio.

REGRA DE OURO: a IA gera roteiro, audio.yaml ou script Python local; o MP3 é gerado na máquina local do usuário. A IA NUNCA afirma ter gerado MP3 sem que o arquivo real exista.

1. ROTEIRO TEXTUAL
1.1. estrutura clara em blocos curtos, com títulos e pausas naturais.
1.2. variação de voz entre blocos para sustentar atenção.
1.3. dicionário fonético quando houver termos jurídicos, latinos ou estrangeiros com pronúncia delicada.

2. audio.yaml
2.1. arquivo YAML que descreve blocos, voz, ritmo, pausas e referências do roteiro.
2.2. validado por PyYAML antes da síntese.
2.3. campos mínimos: id do bloco, voz, texto, pausa pós-bloco, ordem.

3. SCRIPT PYTHON LOCAL
3.1. arquivo gerar_audio.py standalone.
3.2. lê o audio.yaml, sintetiza com edge-tts, concatena com pydub e exporta com ffmpeg.
3.3. insere capítulos ID3 com mutagen e fade de 1 segundo quando aplicável.
3.4. verifica dependências e informa claramente o que estiver faltando.
3.5. não instala dependências automaticamente sem autorização do usuário.

4. MOTOR DE TTS
4.1. padrão: edge-tts.
4.2. vozes pt-BR principais:
4.2.1. FranciscaNeural — conceito e síntese;
4.2.2. AntonioNeural — autores e fundamentação;
4.2.3. ThalitaNeural — revisão e zona de perigo.
4.3. proibição absoluta de fallback robótico: espeak, espeak-ng, pyttsx3, Festival.
4.4. gTTS não é solução principal.
4.5. plano B offline persistente: Piper TTS, vozes pt-BR (faber ou edresson), modelos ONNX em CPU; qualidade neural inferior assumida e declarada ao usuário.

5. ESTRUTURA DE ARQUIVO E LOOP
5.1. um único MP3 master por padrão.
5.2. caminho fixo: audio/master_audio.mp3.
5.3. loop é responsabilidade do HTML; jamais multiplicar o MP3 no Python.

6. DEPENDÊNCIAS LOCAIS
6.1. via pip install --user: edge-tts, pydub, mutagen, PyYAML, python-dotenv.
6.2. binário de sistema: ffmpeg.
6.3. PATH ativo: export PATH="$HOME/.local/bin:$PATH".
6.4. .env e cache em ~/.pafe-local; nunca sincronizar com Drive público.
6.5. não instalar dependências automaticamente sem autorização do usuário.

7. PREFLIGHT OBRIGATÓRIO ANTES DE ÁUDIO LONGO
7.1. DNS: nslookup speech.platform.bing.com.
7.2. voz disponível: edge-tts --list-voices | grep pt-BR.
7.3. teste curto: edge-tts --voice pt-BR-FranciscaNeural --text "Teste PAFE." --write-media teste_pafe.mp3.
7.4. validação: ffprobe -v error -show_entries format=duration,bit_rate -of default=noprint_wrappers=1 teste_pafe.mp3.
7.5. master: rodar o script completo apenas depois do teste curto aprovado.

8. DIAGNÓSTICO DE FALHAS (CLASSE DO ERRO)
8.1. DNS ("Temporary failure in name resolution"):
8.1.1. ambiente sem rede externa real, típico de sandbox de IA;
8.1.2. não corrigível por código Python;
8.1.3. solução: rodar em máquina local com rede; SSL relaxado não corrige DNS.
8.2. CERTIFICADO ("CERTIFICATE_VERIFY_FAILED"):
8.2.1. indica proxy com inspeção TLS;
8.2.2. SSL relaxado (CERT_NONE) é exceção, com log obrigatório;
8.2.3. proibido com senha, token, API key ou dado sensível;
8.2.4. proibido como padrão e proibido na máquina local, onde é desnecessário.
8.3. ENDPOINT FORA (HTTP 5xx ou "services aren't available"):
8.3.1. aguardar e repetir;
8.3.2. migrar para plano B offline (Piper).
8.4. em qualquer falha: parar com erro claro; nunca gerar áudio degradado para "cumprir a tarefa".

9. AMBIENTE INDISPONÍVEL — DECLARAR LIMITAÇÃO
9.1. se a máquina local não permitir internet, ffmpeg ou dependências TTS, entregar o roteiro e o script e declarar [ARTEFATO: execução local necessária].
9.2. contingência automatizada: GitHub Actions com runner externo.
9.3. contingência manual: GitHub Codespaces.
9.4. APIs pagas (OpenAI TTS, ElevenLabs, Narakeet) só como fallback premium; chaves fora do repositório.

10. PROIBIÇÕES
10.1. afirmar geração de MP3 sem arquivo real.
10.2. instalar dependências sem autorização do usuário.
10.3. usar fallback robótico (4.3).
10.4. colocar chave, token ou .env em repositório público.
10.5. SSL relaxado fora da exceção 8.2.
