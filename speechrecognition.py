'''
Importante!
Pacotes necessários:
    > pip install SpeechRecoginition
    > pip install pyaudio
        Caso esse der errado:
        > pip install pipwin
        > pip install pyaudio

    Desenvolvido por Pedro Mesmer
'''

import speech_recognition as sr

# inicializa o microfone
rec = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source)
        # escutando
        frase = ''
        
        print('Para encerrar, diga \'encerrar programa\'')

        while ((frase.lower() != 'encerrar programa') or (frase.lower() != 'sair')):
            try:
                audio = rec.listen(source)
                frase = rec.recognize_google(audio, language='pt-BR')
                print(frase)
            except sr.UnknownValueError:
                print('> Não entendi, pode repetir?')

listen()