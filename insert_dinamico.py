import sqlite3 as conector
from modelo import Marca

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

marca = Marca(2, 'Marca B', 'MB')

comando = '''
INSERT INTO Marca (id, nome, sigla)
VALUES (?, ?, ?);'''

cursor.execute(comando, (marca.id,
                         marca.nome,
                         marca.sigla))

conexao.commit()

cursor.close()
conexao.close()