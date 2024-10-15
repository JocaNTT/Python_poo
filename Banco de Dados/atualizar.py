import sqlite3

#Passo 1 - Estabelecendo a conexão
conexao = sqlite3.connect("departamento.db")

#Passo 2 - Acessar o objeto cursor da biblioteca sqlite3, para manipular dados do banco
consulta = conexao.cursor()

#Passo 3 - Criar a tabela
tabela = """
  CREATE TABLE IF NOT EXISTS funcionario(
   codigo INTEGER PRIMARY KEY AUTOINCREMENT,
   nome VARCHAR(100),
   salario FLOAT,
   cargo VARCHAR(100)
  );
"""

#Passo 4 - Executar o comando de criação da tabela
consulta.execute(tabela)

#Passo 5 - Atualizar os dados
nome = input("Informe o novo nome do funcionário: ")
codigo = int(input("Informe o código do funcionário: "))

#Passo 6 - Criando o comando SQL para atualizar os dados na tabela
sql = "UPDATE funcionario SET nome = ? WHERE codigo = ?"

#Passo 7 - Passando os dados
campos = (nome, codigo)

#Passo 8 - Executar o comando SQL
consulta.execute(sql, (nome, codigo))

#Passo 9 - Encerrar a conexão
conexao.commit()
print(consulta.rowcount,"linha(s) atualizada(s) com sucesso")
conexao.close()