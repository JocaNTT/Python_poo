from funcionario_poo import Funcionario

f1 = Funcionario()

nome = input("Informe o nome do funcionário: ")
salario = float(input("Informe o salário do funcionário: "))
cargo = input("Informe o cargo do funcionário: ")

f1.inserir(nome, cargo, salario)
f1.consultar()