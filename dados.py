import sqlite3 as lite

conexao = lite.connect('dados.db')

with conexao:
    cursor = conexao.cursor()
    cursor.execute(
        'CREATE TABLE formulario1(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia_em DATE, sexo TEXT, observacoes TEXT)'
    )