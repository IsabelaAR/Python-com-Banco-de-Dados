import sqlite3 as conector

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
        VALUES (1234567890, 'João', '2000-01-31', 1);'''
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()