import sqlite3 as lite

conexao = lite.connect('dados.db')

# Inserir informações (C)
def create_info(lista):
    with conexao:
        cursor = conexao.cursor()
        query = 'INSERT INTO formulario1(nome, email, telefone, dia_em, sexo, observacoes) VALUES (?, ?, ?, ?, ?, ?)'
        cursor.execute(query, lista)

# Acessar informações (R)
def read_info():
    lista = []
    with conexao:
        cursor = conexao.cursor()
        query = 'SELECT * FROM formulario1'
        cursor.execute(query)
        info = cursor.fetchall()
        
        for i in info:
            lista.append(i)
    
    return lista

# Atualizar informações (U)
def update_info(lista):
    with conexao:
        cursor = conexao.cursor()
        query = 'UPDATE formulario1 SET nome=?, email=?, telefone=?, dia_em=?, sexo=?, observacoes=? WHERE id=?'
        cursor.execute(query, lista)

'''
# Deletar informações (D)
with conexao:
    cursor = conexao.cursor()
    query = 'DELETE FROM formulario1 WHERE id=?'
    cursor.execute(query, lista)
'''