import sqlite3 as conector

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

comando = '''ALTER TABLE Pessoa
                ADD nascimento TEXT NOT NULL;'''

cursor.execute(comando)

conexao.commit()

cursor.close()
conexao.close()