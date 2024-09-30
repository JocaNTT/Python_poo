#Estamos acessando o arquivo "pessoa" dentro desse arquivo estamos importando a classe "Pessoa"
from pessoa import Pessoa

#Criando Objetos
p1 = Pessoa("Daniel", "Cozinhar", "Confins da Bahia")
p1.exibirHobby()
p1.mudarHobby("Playar com os cria")

#SOLICITANDO DADOS DO USUÁRIO
nomePessoa = input("Informe o nome da pessoa: ")
hobbyPessoa = input("Informe o hobby da pessoa: ")
endPessoa = input("Informe o endereço da pessoa: ")

p2 = Pessoa(nomePessoa, hobbyPessoa, endPessoa)
p2.exibirHobby