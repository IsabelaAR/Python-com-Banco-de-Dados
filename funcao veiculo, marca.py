import sqlite3 as conector
from modelo import Veiculo, Marca

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

comando = '''SELECT * FROM
                Veiculo JOIN Marca ON Marca.id = Veiculo.marca;'''
cursor.execute(comando)

registros = cursor.fetchall()
for registro in registros:
    print(registro)
    marca = Marca(*registro[6:])
    veiculo = Veiculo(*registro[:5], marca)
    print("Placa:", veiculo.placa, ", Marca:", veiculo.marca.nome)

cursor.close()
conexao.close()