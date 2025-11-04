import sqlite3 as conector

try:
    # Abertura de conexão e aquisição de cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    # Execução do comando CREATE
    comando = '''CREATE TABLE Veiculo (
        placa CHARACTER(7) NOT NULL,
        ano INTERGER NOT NULL,
        cor TEXT NOT NULL,
        proprietario INTEGER NOT NULL,
        marca INTEGER NOT NULL,
        PRIMARY KEY (placa),
        FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
        FOREIGN KEY(marca) REFERENCES Marca(id)
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