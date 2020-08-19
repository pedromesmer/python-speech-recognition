'''
    Desenvolvido por Pedro Mesmer
'''

import speech_recognition as sr
from expressions import *

# inicializa o microfone
rec = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source)
        # escutando
        frase = ''
        
        print('Para encerrar, diga \'Encerrar\'')

        while (verifyExpression(frase)):
            try:
                audio = rec.listen(source)
                frase = rec.recognize_google(audio, language='pt-BR')
                print(frase)
            except sr.UnknownValueError:
                print('> Não entendi, pode repetir?')

listen()