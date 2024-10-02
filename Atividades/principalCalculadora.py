from calculadora import Calculadora

print(f"\nCALCULADORA 3000\n")
print(f"Informe dois números para verificar o resultado de suas 5 operações\n")

num1 = float(input("Informe o número 1: "))
num2 = float(input("Informe o número 2: "))

contagem = Calculadora(num1, num2)

contagem.montante()
contagem.abatimento()
contagem.proliferacao()
contagem.desmembramento()
contagem.aprimoramento()

valor = int(input(f"\nInforme um valor para verificar se é par ou ímpar: "))
contagem.verificaParImpar(valor)