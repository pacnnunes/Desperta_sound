# Despertador em Python

Este código em Python permite que você defina uma hora para um despertador tocar um som. O usuário pode inserir as horas e os minutos para o despertador, que funcionará até que a hora atual seja igual à hora do despertador.

## Pré-requisitos
- [pydub](https://github.com/jiaaro/pydub)
- [gTTS](https://pypi.org/project/gTTS/)
- [playsound](https://pypi.org/project/playsound/)
- ffmpeg

## Como usar
1. Instale as dependências necessárias.
2. Abra o terminal e execute o arquivo Python.
3. Digite as horas e os minutos para o despertador.
4. Espere o despertador tocar.

## Observações
- O arquivo de áudio padrão é gerado usando o Google Text-to-Speech (gTTS), mas você pode especificar o caminho para o arquivo de áudio desejado na função `playsound()`.
- Certifique-se de ter o ffmpeg instalado e configurado corretamente.

Este código é apenas um exemplo básico e pode ser modificado para atender às suas necessidades específicas. Aproveite e divirta-se!
