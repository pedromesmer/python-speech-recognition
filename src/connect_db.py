import sqlite3
import os

def realPath():
    return os.path.dirname(os.path.realpath(__file__))

def create_db():
    # o python não assume o caminho do arquivo como raiz, essa função faz esse 'ajuste técnico'
    filePath = realPath()

    conn = sqlite3.connect(filePath  + '/../db/expressions.db') # banco criado na pasta ../db
    cursor = conn.cursor()
    try:
        cursor.execute("""
        CREATE TABLE finish (
            expression TEXT NOT NULL
        )
        """)
    except sqlite3.OperationalError as err:
        print(err)
        return
    
    print('> Tabela criada com sucesso!')

    conn.close()

def insertExpressions_db(expression):

    filePath = realPath()

    conn = sqlite3.connect(filePath  + '/../db/expressions.db') # banco criado na pasta ../db
    cursor = conn.cursor()

    finish = [
    'sair', 'finalizar', 'acabar', 'terminar', 'encerrar'
    ]

    cursor.execute("""
    INSERT INTO finish (expression)
    VALUES (?)
    """, [expression])

    conn.commit()
    print('> Dados cadastrados com sucesso!')
    conn.close()

def readExpressions_db():
    filePath = realPath()
    conn = sqlite3.connect(filePath  + '/../db/expressions.db') # banco criado na pasta ../db
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM finish;
    """)
    
    for line in cursor.fetchall():
        # print(line[0])
        if (line[0] == 'finalizar'):
            print('match')

    conn.close()


create_db()
text = ''
# gambiarra pra cadastro
"""
while (True):
    text = input('Digite a expressão para cadastrar, 0 para finalizar: ') 
    if (text == '0'):
        break
    insertExpressions_db(text)
"""
readExpressions_db()