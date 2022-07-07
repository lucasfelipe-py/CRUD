import sqlite3 as lite

conexao = lite.connect('dados.db')

with conexao:
    cursor = conexao.cursor()
    cursor.execute(
        'CREATE TABLE FORMULARIO(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia_em DATE, estado TEXT, observacoes TEXT)'
    )