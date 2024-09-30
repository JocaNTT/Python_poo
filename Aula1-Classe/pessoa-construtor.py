class Pessoa:

  def __init__(self,nome, altura, idade):
    self.nome = nome
    self.altura = altura
    self.idade = idade

  def exibirDados(self):
    print(f'Olá {self.nome}, sua altura é {self.altura} e sua idade é {self.idade}')

p1 = Pessoa('Getúlio',1.87,99)
p2 = Pessoa('Joca',1.72,75)

p1.exibirDados()
p2.exibirDados()