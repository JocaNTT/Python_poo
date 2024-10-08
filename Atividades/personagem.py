class Personagem:
    def __init__(self, nome, vida=100, rank="Novato"):
        self._nome = nome
        self._vida = vida
        self._rank = rank

    def receberDano(self, dano):
        self._vida -= dano
        print(f"{self._nome} recebeu {dano} de dano. Vida restante: {self._vida}")

    def verificarVida(self):
        if self._vida > 0:
            print(f"{self._nome} ainda está vivo com {self._vida} pontos de vida.")
        else:
            print(f"{self._nome} está morto.")

    def detalhes(self):
        print(f"Nome: {self._nome}; Vida: {self._vida}; Rank: {self._rank}")

class Heroi(Personagem):
    def __init__(self, nome, identidadeSecreta, energia=50, vida=100, rank="Novato"):
        super().__init__(nome, vida, rank)
        self._identidadeSecreta = identidadeSecreta
        self._energia = energia

    def executarHabilidade(self, tipoHabilidade):
        consumoEnergia = 10
        self._energia -= consumoEnergia
        print(f"{self._nome} usou a habilidade {tipoHabilidade} e consumiu {consumoEnergia} de energia. Energia restante: {self._energia}")

    def recarregarEnergia(self):
        recarga = 20
        self._energia += recarga
        print(f"{self._nome} recarregou {recarga} de energia. Energia atual: {self._energia}")

    def chamarAliado(self, nomeAliado):
        print(f"{self._nome} chamou {nomeAliado} para ajudar na luta!")

class Vilao(Personagem):
    def __init__(self, nome, malicia=70, vida=100, rank="Novato"):
        super().__init__(nome, vida, rank)
        self._malicia = malicia

    def desferirGolpe(self, tipoGolpe):
        consumoMalicia = 15
        self._malicia -= consumoMalicia
        print(f"{self._nome} desferiu o golpe {tipoGolpe}, potencializado por sua malícia. Malícia restante: {self._malicia}")

    def planejarArmadilha(self, tipoArmadilha):
        print(f"{self._nome} está planejando uma armadilha: {tipoArmadilha}.")

    def fugir(self, tipoFuga):
        print(f"{self._nome} escapou usando o método de fuga: {tipoFuga}!")
