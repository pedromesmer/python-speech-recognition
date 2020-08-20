import sqlite3
import os

def connect_db():
    # o python não assume o caminho do arquivo como raiz, essa função faz esse 'ajuste técnico'
    filePath = os.path.dirname(os.path.realpath(__file__))

    conn = sqlite3.connect(filePath  + '/../db/expressions.db') # banco criado na pasta ../db
    conn.close()

connect_db()