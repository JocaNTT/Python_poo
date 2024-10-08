from pessoa import Pessoa, Aluno, Professor

# Função para coletar dados do usuário
def criar_pessoa():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    return Pessoa(nome, idade)

def criar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    matricula = input("Digite o código de matrícula: ")
    return Aluno(nome, idade, matricula)

def criar_professor():
    nome = input("Digite o nome do professor: ")
    idade = int(input("Digite a idade do professor: "))
    disciplina = input("Digite a disciplina que o professor ensina: ")
    return Professor(nome, idade, disciplina)

# Exemplo de uso
pessoa1 = criar_pessoa()
prof1 = criar_professor()

pessoa1.info()
prof1.ensinar()