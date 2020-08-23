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

def insertExpressions(expression, action):

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
    for line in expressions:
        print(line)   
    
    conn.close()
    return expressions


create()
# gambiarra pra cadastro

#text = ''
"""
while (True):
    sair = input('Digite 0 para sair: ')
    if (text == '0'):
        break
    expression = input('Expressão: ')
    action = input('Ação: ')

    insertExpressions(expression, action)
"""
readExpressions()