from funcionario import Funcionario, Engenheiro, Supervisor

f1 = Funcionario("Joana", 3000)
engenheiro1 =  Engenheiro("Joaquim", 5100)
supervisor1 = Supervisor("Angelo", 4500)

f1.informacoes()
engenheiro1.bonusEng()
engenheiro1.informacoes()
supervisor1.relatorio()