class Funcionario:
  def __init__(self,nome,salario=10000):
    self.__nome = nome
    self.__salario = salario

  def getNome(self):
    return self.__nome
  
  def setNome(self,valor):
    self.__nome = valor

  @property #esse item irá criar um get "mais amigável"

  def salario(self):
      return self.__salario

  @salario.setter# irá criar um set para o atributo de formar "mais amigável"
  def salario(self, valor):
      if valor > 0:
          self.__salario = valor
      else:
          print("Você não pode ter um salário negativo!")