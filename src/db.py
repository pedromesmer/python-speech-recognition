import sqlite3
import os

def realPath():
    return os.path.dirname(os.path.realpath(__file__))

def create():
    # o python não assume o caminho do arquivo como raiz, essa função faz esse 'ajuste técnico'
    filePath = realPath()

    conn = sqlite3.connect(filePath  + '/../db/actions.db') # banco criado na pasta ../db
    cursor = conn.cursor()
    try:
        cursor.execute("""
        CREATE TABLE actions (
            expression TEXT NOT NULL,
            action TEXT NOT NULL
        )
        """)
    except sqlite3.OperationalError as err:
        print(err)
        return
    
    print('> Tabela criada com sucesso!')

    conn.close()

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

def deleteExpression(expression):
    
    filePath = realPath()

    conn = sqlite3.connect(filePath + '/../db/actions.db')
    cursor = conn.cursor()

    try:
        cursor.execute("""
        DELETE FROM actions
        WHERE expression = ?
        """, expression)
        conn.commit()
    except:
        print('Ocorreu um erro!\nA expressão foi digitada corretamente?\n')

    print('> Expressão deletada com sucesso!')
    conn.close()
    


def readExpressions(table = 'actions'):
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

# Menu do DB

def menuDB():
    print('Menu do banco de dados - SpeechRecognition' +
        '1 - Criação do banco' +
        '2 - Adição de expressão e função atribuida' +
        '3 - Exclusão de expressão do banco' +
        '4 - Visualizar tudo' +
        '0 - Voltar ao menu inicial')
    try:
        opt = int(input('Inrira a opção: '))
    except:
        print('Tente novamente!\n')
        menuDB()
    
    if (opt == 1):
        create()
    elif (opt == 2):
        while (True):
            expression = input('Expressão: ')
            action = input('Ação: ')
            sair = input('Cadastrar? (Sim / S / Yes / Y)')
            if ((sair.lower() == 'sim') or (sair.lower() == 'yes') or (sair.lower() == 's') or (sair.lower() == 'y')):
                insertExpression(expression, action)
            else:
                print('Saindo do cadastro...')
                break

    elif (opt == 3):
        #deleteExpression(expression)
        pass
    elif (opt == 4):
        #viewAll()
        pass
    elif (opt == 0):
        print('Saindo...')
    else:
        print('Opção inválida!\n')
        menuDB()
