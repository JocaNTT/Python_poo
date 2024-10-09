class Produto:
  def __init__(self, nome, valor):
    self._nome = nome
    self._valor = valor

  def descrever(self):
    print(f"O produto {self._nome} custa R${self._valor:.2f}")

  def caucularDesconto(self, valor):
    print(f"o desconto não será fornecido por aqui")

#Classe filha 1 - Eletrônico
class Eletronico(Produto):
  def __init__(self, nome, preco, voltagem):
    super().__init__(nome, preco)
    self._voltagem = voltagem

  def descrever(self):
    print(f"e possui a voltagem {self._voltagem}")

  def caucularDesconto(self, valor):
    desconto = valor/100
    print(f"O produto eletrônico {self._nome} tem um desconto de {desconto:.2f}%")