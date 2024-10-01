class Aluno:
  def __init__(self, nome, idade, peso, altura):
    self.nome = nome
    self.idade = idade
    self.peso = peso
    self.altura = altura
  def exibirDados(self):
    print(f"Olá {self.nome}, você tem {self.idade} anos de idade, um peso de {self.peso}Kg e você tem {self.altura} metros de altura.")
  
  def calcularImc(self):
        imc = self.peso / (self.altura ** 2)
        print(f"O IMC de {self.nome} é {imc:.2f}")

        if imc < 18.5:
            print("Abaixo do peso.")
        elif 18.5 <= imc < 24.9:
            print("Peso normal.")
        elif 25 <= imc < 29.9:
            print("Sobrepeso.")
        else:
            print("Obesidade.")