class Pessoa:
  nome = 'Joaquim'
  peso = 62
  escolaridade = 'Ensino Médio'

  def falar(self,texto):
    print(f'Tenho algo para te dizer: {texto}')

pessoa1 = Pessoa()
print(pessoa1.nome)
pessoa1.falar('Boa tarde, hoje é segunda-feira')