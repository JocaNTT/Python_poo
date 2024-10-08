class Funcionario:
    def __init__(self, nome, salario):
        '''Estamos mudando a visibilidade dos atributos de privado para protegido,
        dessa forma, as classes filhas poderão acessar os atributos da classe mãe.'''
        self._nome = nome
        self._salario = salario

    def informacoes(self):
        print(f"Olá {self._nome} seu salário atual é {self._salario}")    

#Criando classes filhas
class Engenheiro(Funcionario): # a classe Engenheiro está herdando as características da classe Funcionário, que será sua classe mãe.
    def bonusEng(self):
        self._salario = self._salario * 1.1 #Estamos aumentando o salário em 10%

class Supervisor(Funcionario):
    def relatorio(self):
        print(f"Olá {self._nome} seu relatário está em processo de andamento.")    