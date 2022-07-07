from cgitb import text
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkcalendar import Calendar, DateEntry


# Cores
cor_cinza, cor_cinzaclaro, cor_branca, cor_verde, cor_1, cor_2 = "#696969", "#DCDCDC", "#feffff", "#4fa882", "#38576b", "#403d3d"
cor_3, cor_azul, cor_vermelha, cor_verde2, cor_azulsky, cor_preta = "#e06636", "#038cfc", "#ef5350", "#263238", "#e9edf5", "#000000"

# Método para reduzir o código das labels
def texto(frame, x, y, string, fonte):
    label = Label(frame, text=string, relief='flat', anchor=NW, font=(fonte), bg=cor_cinzaclaro, fg=cor_preta)
    label.place(x=x, y=y)

# Janela
janela = Tk()
janela.title('CRUD')
janela.geometry('1043x453')
janela.configure(background=cor_azulsky)
janela.resizable(width=FALSE, height=FALSE)

# Frames
    # Frame de cima (titulo)
frame_cima = Frame(janela, width=310, height=50, bg=cor_cinza, relief='flat')
frame_cima.grid(row=0, column=0)

    # Frame baixo (formulário)
frame_baixo = Frame(janela, width=310, height=403, bg=cor_cinzaclaro, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

    # Frame direita (dados salvos)
frame_direita = Frame(janela, width=588, height=403, bg=cor_cinzaclaro, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# Label frame_cima (texto: Formulário de Cadastro)
label_framecima = Label(frame_cima, text='Formulário de Cadastro', relief='flat', anchor='center', font=('Tahoma 13 bold'), bg=cor_cinza, fg=cor_branca)
label_framecima.place(x=50, y=12)

# Entrada (nome)
texto(frame_baixo, 10, 10, 'Nome: ', 'Tahoma 10') # Label
entrada_nome = Entry(frame_baixo, width=45, justify='left')
entrada_nome.place(x=13, y=40)

# Entrada (e-mail)
texto(frame_baixo, 10, 70, 'E-mail: ', 'Tahoma 10') # Label
entrada_email = Entry(frame_baixo, width=45, justify='left')
entrada_email.place(x=13, y=100)

# Entrada (contato)
texto(frame_baixo, 10, 130, 'Contato: ', 'Tahoma 10') # Label
entrada_contato = Entry(frame_baixo, width=45, justify='left')
entrada_contato.place(x=13, y=160)

# Entrada (data)
texto(frame_baixo, 10, 190, 'Data de entrada: ', 'Tahoma 10') # Label
entrada_calendario = DateEntry(frame_baixo, width=12, background=cor_cinza, foreground='white', borderwidth=2)
entrada_calendario.place(x=13, y=220)

# Entrada (sexo)
values = ['', 'Masculino', 'Feminino']
texto(frame_baixo, 160, 190, 'Sexo: ', 'Tahoma 10') # Label
entrada_sexo = ttk.Combobox(frame_baixo, width=15, justify='left', values=values, font=('Tahoma 10'))
entrada_sexo.place(x=160, y=220)

# Observações (etc)
texto(frame_baixo, 10, 250, 'Observações: ', 'Tahoma 10') # Label
entrada_observacoes = Entry(frame_baixo, width=45, justify='left')
entrada_observacoes.place(x=13, y=280)

# Botões

    # Inserir
botao_inserir = Button(frame_baixo, width=10, text='Inserir', font=('Tahoma 10'), bg='#191970', fg=cor_cinzaclaro, relief='raised', overrelief='ridge', anchor='center')
botao_inserir.place(x=13, y=340)

    # Atualizar
botao_atualizar = Button(frame_baixo, width=10, text='Atualizar', font=('Tahoma 10'), bg='#2F4F4F', fg=cor_cinzaclaro, relief='raised', overrelief='ridge', anchor='center')
botao_atualizar.place(x=109, y=340)

    # Deletar
botao_deletar = Button(frame_baixo, width=10, text='Deletar', font=('Tahoma 10'), bg='#A52A2A', fg=cor_cinzaclaro, relief='raised', overrelief='ridge', anchor='center')
botao_deletar.place(x=205, y=340)

# Tabela de dados

    # Lista de pessoas cadastradas
lista_cadastrada = [
    ['1', 'Lucas F. Rogério', 'lucas@mail.com', '48 99999-9999', '01/01/22', 'Masculino', 'Teste'],
    ['2', 'Lucas F. Rogério', 'lucas@mail.com', '48 99999-9999', '01/01/22', 'Masculino', 'Teste'],
    ['3', 'Lucas F. Rogério', 'lucas@mail.com', '48 99999-9999', '01/01/22', 'Masculino', 'Teste'],
    ['4', 'Lucas F. Rogério', 'lucas@mail.com', '48 99999-9999', '01/01/22', 'Masculino', 'Teste'],
    ['5', 'Lucas F. Rogério', 'lucas@mail.com', '48 99999-9999', '01/01/22', 'Masculino', 'Teste'],
    ['6', 'Lucas F. Rogério', 'lucas@mail.com', '48 99999-9999', '01/01/22', 'Masculino', 'Teste']
]

    # Cabeçalho
info_header = ['ID', 'Nome', 'E-mail', 'Contato', 'Data entrada', 'Sexo', 'Observações']

    # Método de criação da tabela (tree)
tree = ttk.Treeview(frame_direita, selectmode='extended', columns=info_header, show='headings')

    # Barra de rolagem vertical
barra_vertical = ttk.Scrollbar(frame_direita, orient='vertical', command=tree.yview)

    # Barra de rolagem horizontal
barra_horizontal = ttk.Scrollbar(frame_direita, orient='horizontal', command=tree.xview)

    # Setando a tabela (tree)
tree.configure(yscrollcommand=barra_vertical.set, xscrollcommand=barra_horizontal.set)
tree.grid(column=0, row=0, sticky='nsew')
barra_vertical.grid(column=1, row=0, sticky='ns')
barra_horizontal.grid(column=0, row=1, sticky='ew')
frame_direita.grid_rowconfigure(0, weight=12)

header_pos = ['nw', 'nw', 'nw', 'nw', 'nw', 'nw', 'nw']
header_tam = [35, 170, 140, 100, 120, 65, 100]
i = 0

for coluna in info_header:
    tree.heading(coluna, text=coluna.title(), anchor=CENTER)
    tree.column(coluna, width=header_tam[i], anchor=header_pos[i])
    i += 1

for item in lista_cadastrada:
    tree.insert('', 'end', values=item)

# Abrir janela
if __name__ == '__main__':
    janela.mainloop()