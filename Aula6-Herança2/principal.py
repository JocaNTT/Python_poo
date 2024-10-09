from pessoa import Pessoa, Aluno, Professor

# Função para coletar dados do usuário
def criar_pessoa():
    nome = input("Digite o nome do responsável: ")
    idade = int(input("Digite a idade do responsável: "))
    return Pessoa(nome, idade)

def criar_aluno():
    escola = input("Digite o nome da escola: ")
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    matricula = int(input("Digite o número do código de matrícula: "))
    return Aluno(nome, idade, matricula, escola)

def criar_professor():
    nome = input("Digite o nome do professor: ")
    idade = int(input("Digite a idade do professor: "))
    disciplina = input("Digite a disciplina que o professor ensina: ")
    return Professor(nome, idade, disciplina)

# Exemplo de uso
pessoa1 = criar_pessoa()
aluno1 = criar_aluno()
prof1 = criar_professor()

pessoa1.infoResponsavel()
aluno1.estudar()
prof1.ensinar()