import sqlite3


def connect_db():
    conn = sqlite3.connect('..\db\expressions.db')
    conn.close()