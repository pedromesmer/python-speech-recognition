# Apresentação

Reconhecedor de voz simples com python

Esse programa é a base para integração de comando de voz em programas, basta importar a lista de parametros e realizar as funcões desejadas.

## Preparação da máquina

Foi utilizado o **Python 3.8.3**

Realizar os seguintes comandos antes da inicialização:

```pip install SpeechRecoginition```
### Linux
```
pip install pyaudio
sudo pip3 install --upgrade speechrecognition
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
sudo apt-get install ffmpeg libav-tools
sudo pip3 install pyaudio
```

### Windows
```
pip install pyaudio
pip install pipwin
pip install pyaudio
```
## Interface

Embora amigavável, a interface do programa é em linha de comando.
Para iniciar o programa, basta executar o comando:

> py ./src/main.py

 Na tela inicial, onde podemos escolher as seguintes opções pelo teclado.

![Alt text](/assets/menu%20inicial.png?raw=true "Menu inicial")

Na primeira opção, é iniciado o reconhecimento de voz (exemplo de funcionamento);

![Alt text](/assets/speech%20recognition.png?raw=true "recognizer")

Na segunda, é possivel acessar o menu do banco de dados, onde cadastramos, alteramos, excluimos e visualizamos todos os comandos de voz, amarrados pelo verbo ou radical da palavra.

![Alt text](/assets/menu%20banco%20de%20dados.png?raw=true "menu db")

Por padrão, foram cadastrados 5 comandos, quatro deles chamam a função ``quit()`` e o último a função ``menu()``. 

![Alt text](/assets/visualização%20banco%20de%20dados.png?raw=true "db")

Essas funções estão no arquivo ``./src/functions.py``. Nesse arquivo devem ser cadastradas as novas funções.

Bons estudos! :grin:
