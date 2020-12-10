'''
    Desenvolvido por Pedro Mesmer
'''
import recognizer
import db
import os
from sys import platform as platform

def clearScreen(): 
    if (platform == 'win32'):
        os.system('cls')
    elif ((platform == 'linux') or (platform == 'darwin')):
        os.system('clear')
    else:
        print('\n' * 100)

def menu():
    clearScreen()
    opt = 0
    print('Speech Recognition\n' +
    '1 - Iniciar reconhecimento de voz\n' +
    '2 - Configurações do banco de dados\n' +
    '3 - Sobre\n' +
    '0 - Encerrar programa\n')

    try:
        opt = int(input('Insira a opção: '))
    except:
        print('Apenas números\n')
        menu()

    if (opt == 1): # Speech Recognition
        clearScreen()
        recognizer.listen()
    elif (opt == 2): # Menu do banco de dados
        menuDB()
    elif (opt == 3): # Menu do banco de dados
        clearScreen()
        print('\nDesenvolvido por:\n'+
            '\tPedro Mesmer\n' + 
            '\t@pedromesmer\n')
        db.wait()
        menu()
    elif (opt == 0): # Sair do programa
        print('Saindo...')
    else:
        print('Opção inválida')
        menu()

def menuDB():
    clearScreen()
    opt = 0
    print('Menu do banco de dados - SpeechRecognition\n' +
        '1 - Criação do banco\n' +
        '2 - Adição de expressão e função atribuida\n' +
        '3 - Exclusão de expressão do banco\n' +
        '4 - Visualizar tudo\n' +
        '0 - Voltar ao menu inicial\n')
    try:
        opt = int(input('Insira a opção: '))
    except:
        print('Opção inválida!\n')
        menuDB()
    
    if (opt == 1): # criar banco
        db.create()
        menuDB()

    elif (opt == 2): # cadastrar expressão
        primeiro = True
        while (True):
            
            if (not primeiro):
                sair = input('\nNovo cadastro? (Sim / S / Yes / Y): ')
                if ((sair.lower() == 'sim') or (sair.lower() == 'yes') or (sair.lower() == 's') or (sair.lower() == 'y')):
                    pass
                else:
                    print('Encerrando cadastro...')
                    break

            expression = input('\nExpressão: ')
            action = input('Ação: ')
            sair = input('Confirma? (Sim / S / Yes / Y): ')
            if ((sair.lower() == 'sim') or (sair.lower() == 'yes') or (sair.lower() == 's') or (sair.lower() == 'y')):
                db.insertExpression(expression, action)
                primeiro = False
            else:
                print('Encerrando cadastro...')
                break
        menuDB()

    elif (opt == 3): # deletar expressão
        expression = -1
        
        view = input('Deseja ver a lista de IDs?\n(Sim / S / Yes / Y): ')
        if ((view.lower() == 'sim') or (view.lower() == 'yes') or (view.lower() == 's') or (view.lower() == 'y')):
            db.viewAll()

        try:
            expression = int(input('Insira o ID da expressão para exclusão: '))
        except:
            print('A opção so aceita inteiros!\n')
            menuDB()

        sair = input('Confirma? (Sim / S / Yes / Y): ')
        if ((sair.lower() == 'sim') or (sair.lower() == 'yes') or (sair.lower() == 's') or (sair.lower() == 'y')):
            db.deleteExpression(expression)
        else:
            print('Fim da exclusão...\n')
        menuDB()

    elif (opt == 4): # ver todas as expressões e IDs
        db.viewAll()
        menuDB()

    elif (opt == 0): # menu principal
        print('Saindo...')
        menu()

    else:
        print('Opção inválida!\n')
        menuDB()

menu()
