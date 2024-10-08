from personagem import Personagem, Heroi, Vilao

personagem1 = Personagem("Soldado", 120, "Intermediário")
heroi1 = Heroi("Fênix", "João Silva", energia = 70)
vilao1 = Vilao("Mestre das Sombras", malicia = 80)

personagem1.detalhes()
personagem1.receberDano(30)
personagem1.verificarVida()

heroi1.detalhes()
heroi1.executarHabilidade("Chamas Imortais")
heroi1.recarregarEnergia()
heroi1.chamarAliado("Águia Dourada")

vilao1.detalhes()
vilao1.desferirGolpe("Golpe Sombrio")
vilao1.planejarArmadilha("Armadilha de Sombra")
vilao1.fugir("Invisibilidade")
