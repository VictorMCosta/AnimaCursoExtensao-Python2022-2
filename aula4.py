#1o. passo: importar a biblioteca sqlite3
import sqlite3

#2o. passo: vamos estabelcer uma
#conexão com o bancos de dados 
conexao = sqlite3.connect("dc_universe.db")

#3o. passo: criar um objeto do tipo curso
cursor = conexao.cursor()

#4o. passo: Comando SQL do banco 
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#5o. passo: Executar o comando SQL no SQLlite (no cursor)
cursor.execute(sql)

#6o. passo: Exibir as conulta com todos os nomes de herois e vilões do banco de dados 
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)
  
for pessoa in pessoas: 
  print(f"Nome: {pessoa[1]} ({pessoa[3]})")
