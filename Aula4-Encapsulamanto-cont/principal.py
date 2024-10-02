from funcionario import Funcionario

funcionario1 = Funcionario("Ketlen", 3000)

print("Seu nome atual é",funcionario1.getNome())

funcionario1.setNome("Kaio")

print("Seu nome atual é",funcionario1.getNome())

print("Seu salário atual é",funcionario1.salario)

funcionario1.salario = 5000

print("Seu salário atual é",funcionario1.salario)