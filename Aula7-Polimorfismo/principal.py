from produto import Produto, Eletronico

eletro1 = Eletronico('TV', 3000, 30)
prod1 = Produto('Camiseta', 80)

prod1.descrever()
prod1.caucularDesconto(10)

eletro1.descrever()
eletro1.caucularDesconto(30)