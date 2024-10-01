from academia import Aluno

alunos = []

def adicionarAluno():
    nome = input("Informe o nome do aluno: ")
    idade = int(input("Informe a idade do aluno: "))
    peso = float(input("Informe o peso do aluno: "))
    altura = float(input("Informe a altura do aluno: "))
    
    return Aluno(nome,idade,peso,altura)

while True:
  aluno = adicionarAluno()
  alunos.append(aluno)

  continuar = input(f"\nDeseja adicionar outro aluno? (sim/não): ").lower()
  if continuar != 'sim':
        break
  for i, aluno in enumerate(alunos, 1):
    print(f"\nInformações do Aluno {i}:")
    aluno.exibirDados()
    aluno.calcularImc()