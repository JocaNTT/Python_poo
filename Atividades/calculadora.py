class Calculadora:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    #Soma
    def montante(self):
        resultado = self.__num1 + self.__num2
        print(f"\nA soma de {self.__num1} + {self.__num2} = {resultado}")

    #Subtração
    def abatimento(self):
        resultado = self.__num1 - self.__num2
        print(f"\nA subtração de {self.__num1} - {self.__num2} = {resultado}")

    #Multiplicação
    def proliferacao(self):
        resultado = self.__num1 * self.__num2
        print(f"\nA multiplicação de {self.__num1} * {self.__num2} = {resultado}")

    #Divisão
    def desmembramento(self):
        if self.__num2 == 0:
            print(f"\nErro: Você não pode dividir algo por zero!")
            return None
        resultado = self.__num1 / self.__num2
        print(f"\nA divisão de {self.__num1} / {self.__num2} = {resultado}")

    #Potenciação
    def aprimoramento(self):
        if self.__num1 > 0 and self.__num2 >= 0:
            resultado = self.__num1 ** self.__num2
            print(f"\nA potenciação de {self.__num1} ^ {self.__num2} = {resultado}")
        else:
            print(f"\nErro: O número 1 deve ser maior que zero e número 2 não pode ser negativo para funcionar a potenciação!")
            return None

    def verificaParImpar(self, valor):
        if valor % 2 == 0:
            print(f"{valor} é Par.\n")
        else:
            print(f"{valor} é Ímpar.\n")