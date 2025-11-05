import sqlite3 as conector
from modelo import Pessoa

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

pessoa = Pessoa(20000000099, 'José', False, '1990-02-28')

comando = '''
INSERT INTO Pessoa (cpf, nome, oculos, nascimento)
        VALUES (:cpf, :nome, :usa_oculos, :data_nascimento);'''

cursor.execute(comando, {"cpf": pessoa.cpf,
                         "nome": pessoa.nome,
                         "usa_oculos": pessoa.usa_oculos,
                         "data_nascimento": pessoa.data_nascimento})

conexao.commit()

cursor.close()
conexao.close()