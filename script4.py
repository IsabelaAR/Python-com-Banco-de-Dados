import sqlite3 as conector

try:
    # Abertura de conexão e aquisição de cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    # Execução do comando CREATE
    comando = '''CREATE TABLE Pessoa (
        cpf INTERGER NOT NULL,
        nome TEXT NOT NULL,
        oculos BOOLEAN NOT NULL,
        PRIMARY KEY (cpf)
        );'''
    cursor.execute(comando)

    # Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    if conexao:
        cursor.close()
        conexao.close()