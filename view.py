import sqlite3 as lite

conexao = lite.connect('dados.db')

lista = ['Lucas F. Rogério', 'lucas@mail.com', '48 99999-9999', '01/01/22', 'Masculino', 'Teste']

# Inserir informações (C)
with conexao:
    cursor = conexao.cursor()
    query = 'INSERT INTO formulario1(nome, email, telefone, dia_em, sexo, observacoes) VALUES (?, ?, ?, ?, ?, ?)'
    cursor.execute(query, lista)


# Acessar informações (R)
with conexao:
    cursor = conexao.cursor()
    query = 'SELECT * FROM formulario1'
    cursor.execute(query)
    info = cursor.fetchall()
    print(info)


# Atualizar informações (U)
with conexao:
    cursor = conexao.cursor()
    query = 'UPDATE formulario1 SET nome=? WHERE id=?'
    cursor.execute(query, lista)


# Deletar informações (D)
with conexao:
    cursor = conexao.cursor()
    query = 'DELETE FROM formulario1 WHERE id=?'
    cursor.execute(query, lista)