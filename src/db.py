import sqlite3
import os

def realPath():
    return os.path.dirname(os.path.realpath(__file__))

def wait(text = '\nTecle Enter para continuar'):
    input(text)

def create():
    # o python não assume o caminho do arquivo como raiz, essa função faz esse 'ajuste técnico'
    filePath = realPath()

    conn = sqlite3.connect(filePath  + '/../db/actions.db') # banco criado na pasta ../db
    cursor = conn.cursor()
    try:
        cursor.execute("""
        CREATE TABLE actions (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            expression TEXT NOT NULL,
            action TEXT NOT NULL
        )
        """)
    except sqlite3.OperationalError as err:
        print(err)
        return
    
    print('> Tabela criada com sucesso!')
    conn.close()

    wait()

def insertExpression(expression, action):

    filePath = realPath()

    conn = sqlite3.connect(filePath  + '/../db/actions.db') # banco criado na pasta ../db
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO actions (expression, action)
    VALUES (?,?)
    """, (expression, action))

    conn.commit()
    print('> Dados cadastrados com sucesso!')
    conn.close()


def deleteExpression(id):
    
    filePath = realPath()

    conn = sqlite3.connect(filePath + '/../db/actions.db')
    cursor = conn.cursor()

    
    try:
        cursor.execute("""
        DELETE FROM actions
        WHERE id = ?
        """, (id,))
    except:
        print('Ocorreu um erro!\nA expressão foi digitada corretamente?\n')
        conn.close()
        wait()
        return

    conn.commit()
    conn.close()
    
    print('> Expressão deletada com sucesso!')

    wait()

def readExpression(table = 'actions'):
    filePath = realPath()
    conn = sqlite3.connect(filePath  + '/../db/actions.db') # banco criado na pasta ../db
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM {};
    """.format(table))

    expressions = cursor.fetchall()

    # percorre todos os itens da tabela e salva na lista
    # print(cursor.fetchall())
    """
    for line in expressions:
        print(line)   
    """
    conn.close()
    return expressions

def viewAll(table = 'actions'):
    filePath = realPath()
    conn = sqlite3.connect(filePath  + '/../db/actions.db') # banco criado na pasta ../db
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM {};
    """.format(table))

    expressions = cursor.fetchall()

    # percorre todos os itens da tabela e salva na lista
    # print(cursor.fetchall())
    print('ID','Expressão','Função', sep = '\t')
    print('------------------------------')
    for line in expressions:
        print(line[0], end = '\t')
        print(line[1], end = '')
        for space in range((9 - len(line[1]) + 7)):
            print(' ', end= '')
        print(line[2])   
    
    conn.close()

    wait()
    


# Menu do DB

def menuDB():
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
        create()
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
                insertExpression(expression, action)
                primeiro = False
            else:
                print('Encerrando cadastro...')
                break
        menuDB()

    elif (opt == 3): # deletar expressão
        expression = -1
        
        view = input('Deseja ver a lista de IDs?\n(Sim / S / Yes / Y): ')
        if ((view.lower() == 'sim') or (view.lower() == 'yes') or (view.lower() == 's') or (view.lower() == 'y')):
            viewAll()

        try:
            expression = int(input('Insira o ID da expressão para exclusão: '))
        except:
            print('A opção so aceita inteiros!\n')
            menuDB()

        sair = input('Confirma? (Sim / S / Yes / Y): ')
        if ((sair.lower() == 'sim') or (sair.lower() == 'yes') or (sair.lower() == 's') or (sair.lower() == 'y')):
            deleteExpression(expression)
        else:
            print('Fim da exclusão...\n')
        menuDB()

    elif (opt == 4): # ver todas as expressões e IDs
        viewAll()
        menuDB()
    elif (opt == 0): # menu principal
        print('Saindo...')
    else:
        print('Opção inválida!\n')
        menuDB()

menuDB()
