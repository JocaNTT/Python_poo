from aluno import Aluno

def exibir_menu():
    print("\n--- Menu de Gerenciamento da Academia ---")
    print("1. Cadastrar Aluno")
    print("2. Consultar Todos os Alunos")
    print("3. Consultar Aluno Individual")
    print("4. Atualizar Aluno")
    print("5. Deletar Aluno")
    print("6. Consultar Todos os Planos")
    print("7. Sair")

def main():
    aluno = Aluno()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome do aluno: ")
            idade = int(input("Idade do aluno: "))
            data_inicio = input("Data de início (AAAA-MM-DD): ")
            print("Qual plano você gostaria de assinar agora?")
            print("Pressione 1 para escolher o Plano de Day use")
            print("Pressione 2 para escolher o Plano Light")
            print("Pressione 3 para escolher o Plano Plus")
            print("Pressione 4 para escolher o Plano Premium Plus")
            plano = input("Escolha um plano: ")
            aluno.cadastrarAluno(nome, idade, plano, data_inicio)
        
        elif opcao == '2':
            print(f"\n--- Lista de Alunos ---")
            aluno.consultarAlunos()
        
        elif opcao == '3':
            codigo_aluno = int(input("Digite o código do aluno: "))
            print(f"\n--- Informações do Aluno ---")
            aluno.consultarAlunoIndividual(codigo_aluno)
        
        elif opcao == '4':
            codigo_aluno = int(input("Digite o código do aluno que deseja atualizar: "))
            nome = input("Novo nome: ")
            idade = input("Nova idade: ")

            if nome == '':
                nome = None
            if idade == '':
                idade = None
            else:
                idade = int(idade)
            
            aluno.atualizarAluno(codigo_aluno, nome, idade, data_inicio)
        
        elif opcao == '5':
            codigo_aluno = int(input("Digite o código do aluno que deseja deletar: "))
            aluno.deletarAluno(codigo_aluno)
        
        elif opcao == '6':
            print(f"\n--- Lista de Planos ---\n")
            print(f"Plano Day Use: Por R$ 29.90, o Day Use permite experimentar a academia por um dia completo. Durante esse período, o usuário pode usufruir de musculação, ergometria e Cross Training, conforme a grade de aulas e o funcionamento da unidade. Uma ótima opção para quem quer conhecer a academia antes de se comprometer com um plano maior.")
            print(f"\nPlano Light: Por R$ 99.90 mensais, o Plano Light é ideal para quem busca um bom custo-benefício. Sem exigências de fidelidade ou anuidade, o usuário pode treinar na unidade em que se matriculou, com acesso a horários livres. O plano inclui musculação e ergometria, além de 30 dias gratuitos no aplicativo Weburn para acompanhamento dos treinos.")
            print(f"\nPlano Plus: Com um custo de apenas R$ 0.99 no primeiro mês, o Plano Plus oferece total flexibilidade aos seus usuários. Sem fidelidade e sem anuidade, você poderá treinar em qualquer unidade da rede no Brasil. O plano inclui um acompanhante gratuito até 5 vezes por mês, acesso ao aplicativo Weburn, além de musculação, ergometria, ginástica, danças e Cross Training, sujeitos à disponibilidade da unidade. O horário é livre e também conta com aulas online via Self Digital.")
            print(f"\nPlano PremiumPlus: Com valor de R$ 149.90 ao mês, o Plano Mega Plus é uma opção premium para quem deseja mais benefícios. Assim como os outros, não exige fidelidade nem anuidade. Você poderá treinar em qualquer unidade da academia no Brasil, e ainda tem direito a levar um acompanhante até 10 vezes por mês. O plano inclui acesso ao App Weburn, musculação, ergometria, ginástica, danças e Cross Training, conforme a disponibilidade da unidade. O horário de treino é livre e oferece aulas online com a Self Digital.\n")
        
        elif opcao == '7':
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()