class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    def infoResponsavel(self):
        print(f"Nome: {self._nome}")
        print(f"Idade: {self._idade}")

# Classe filha 1 - Aluno
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, escola):
        super().__init__(nome, idade, matricula, escola)  # Utilizando o construtor da classe mãe
        self._matricula = matricula  # Atributo exclusivo da classe filha
        self._escola = escola  # Atributo exclusivo da classe filha
    def estudar(self):

        print(f"\n{self._nome} está matriculado com o código: {self._matricula} e continua estudando normalmente no(a) {self._escola}!")

# Classe filha 2 - Professor
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self._disciplina = disciplina
    def ensinar(self):
        print(f"\n{self._nome}, professor(a) da disciplina {self._disciplina}, está ensinando na instituição!\n")