'''
    Desenvolvido por Pedro Mesmer
'''

import speech_recognition as sr
from verify_expressions import verifyExpression

# inicializa o microfone
rec = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source)
        # escutando
        frase = ''
        
        print('Para encerrar, diga \'Encerrar\'')

        while (verifyExpression(frase)):
            print('> entrou')
            try:
                audio = rec.listen(source, timeout=None)
                print('> ouviu')
                frase = rec.recognize_google(audio, language='pt-BR')
                print(frase)
            except sr.UnknownValueError:
                print('> Não entendi, pode repetir?')

listen()