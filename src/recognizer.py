import speech_recognition as sr
import verify_expressions

def listen():
    # inicializa o microfone
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        
        frase = ''
        
        print('\nEscutando...\nPara encerrar, basta pedir!')

        while (verify_expressions.verifyExpression(frase)):
            try:
                rec.adjust_for_ambient_noise(source)
                # escutando
                audio = rec.listen(source, timeout=None, phrase_time_limit=5)
                #print('> ouviu')
                frase = rec.recognize_google(audio, language='pt-BR')
                print(frase)
            except sr.UnknownValueError:
                print('> Não entendi, pode repetir?')
