from conta import Conta

minhaConta = Conta(321,"Joaquim",2000,500)

minhaConta.relatorio()
minhaConta.setLimite(19000)
minhaConta.relatorio()

print(f"O seu limite atual é {minhaConta.getLimite()}")

minhaConta.depositar(200)
minhaConta.relatorio()

minhaConta.sacar(150)
minhaConta.relatorio()