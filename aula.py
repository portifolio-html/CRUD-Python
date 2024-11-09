import mysql.connector


def Database_create(name):
    comando = f'CREATE DATABASE {name}'
    cursor.execute(comando)
    conexao.commit()


def Inserir_dados():
    comando = 'INSERT INTO PRODUTO (id, produto, valor) VALUES (1, "FEIJÃO", 5.0)'
    cursor.execute(comando)
    conexao.commit()

def Exibir_dados():
    comando = 'select * from vendas'
    cursor.execute(comando)
    #conexao.commit()
    res = cursor.fetchall()
    print(res)

def Editar_dados():
    comando = f'update PRODUTO set produto = "PEIXE" where ID = 0'
    cursor.execute(comando)
    conexao.commit()

conexao = mysql.connector.Connect(
    host='localhost',
    user='root',
    password='382536',
    database='bdyoutube'
)

cursor = conexao.cursor()

#create

Editar_dados()


cursor.close()
conexao.close()