import sqlite3
import os

def realPath():
    return os.path.dirname(os.path.realpath(__file__))

def create():
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

def insertExpressions(expression):

    filePath = realPath()

    conn = sqlite3.connect(filePath  + '/../db/expressions.db') # banco criado na pasta ../db
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO finish (expression)
    VALUES (?)
    """, [expression])

    conn.commit()
    print('> Dados cadastrados com sucesso!')
    conn.close()

def readExpressions(table):
    filePath = realPath()
    conn = sqlite3.connect(filePath  + '/../db/expressions.db') # banco criado na pasta ../db
    cursor = conn.cursor()
    expressions = []

    cursor.execute("""
    SELECT * FROM {};
    """.format(table))

    # percorre todos os itens da tabela e salva na lista
    for line in cursor.fetchall():
        expressions.append(line[0])

    conn.close()
    return expressions


#create()
# gambiarra pra cadastro
"""
text = ''
while (True):
    text = input('Digite a expressão para cadastrar, 0 para finalizar: ') 
    if (text == '0'):
        break
    insertExpressions(text)
"""
#readExpressions()