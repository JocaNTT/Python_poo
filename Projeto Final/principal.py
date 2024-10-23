# Importa a classe Aluno do arquivo aluno.py
from aluno import Aluno

def exibir_menu():
    """Função para exibir o menu principal do sistema"""
    print("\n--- Menu de Gerenciamento da Academia ---")
    print("1. Cadastrar Aluno")
    print("2. Consultar Todos os Alunos")
    print("3. Consultar Aluno Individual")
    print("4. Atualizar Aluno")
    print("5. Deletar Aluno")
    print("6. Consultar Todos os Planos")
    print("7. Sair")

def main():
    # Cria uma instância da classe Aluno
    aluno = Aluno()
    
    # Loop principal do programa
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        # Opção 1: Cadastrar novo aluno
        if opcao == '1':
            nome = input("Nome do aluno: ")
            
            # Tratamento de erro para entrada da idade
            try:
                idade = int(input("Idade do aluno: "))
            except ValueError:
                print("Por favor, digite uma idade válida (número inteiro)")
                continue
                
            data_inicio = input("Data de início (AAAA-MM-DD): ")
            
            # Exibe os planos disponíveis
            print("\nQual plano você gostaria de assinar agora?")
            print("Pressione 1 para escolher o Plano de Day use")
            print("Pressione 2 para escolher o Plano Light")
            print("Pressione 3 para escolher o Plano Plus")
            print("Pressione 4 para escolher o Plano Premium Plus")
            plano = input("Escolha um plano: ")
            
            # Chama o método para cadastrar aluno
            aluno.cadastrarAluno(nome, idade, plano, data_inicio)
        
        # Opção 2: Listar todos os alunos
        elif opcao == '2':
            print(f"\n--- Lista de Alunos ---")
            aluno.consultarAlunos()
        
        # Opção 3: Consultar aluno específico
        elif opcao == '3':
            # Tratamento de erro para entrada do código
            try:
                codigo_aluno = int(input("Digite o código do aluno: "))
                print(f"\n--- Informações do Aluno ---")
                aluno.consultarAlunoIndividual(codigo_aluno)
            except ValueError:
                print("Por favor, digite um código válido (número inteiro)")
                continue
        
        # Opção 4: Atualizar dados de um aluno
        elif opcao == '4':
            # Tratamento de erro para entrada do código
            try:
                codigo_aluno = int(input("Digite o código do aluno que deseja atualizar: "))
            except ValueError:
                print("Por favor, digite um código válido (número inteiro)")
                continue
            
            # Coleta os novos dados, permitindo campos em branco
            nome = input("Novo nome (deixe em branco para não alterar): ")
            idade = input("Nova idade (deixe em branco para não alterar): ")
            data_inicio = input("Nova data de início (AAAA-MM-DD) (deixe em branco para não alterar): ")

            # Tratamento dos campos vazios
            if nome == '':
                nome = None
            if idade == '':
                idade = None
            else:
                try:
                    idade = int(idade)
                except ValueError:
                    print("Por favor, digite uma idade válida (número inteiro)")
                    continue
            
            # Chama o método para atualizar aluno
            aluno.atualizarAluno(codigo_aluno, nome, idade, data_inicio)
        
        # Opção 5: Deletar um aluno
        elif opcao == '5':
            # Tratamento de erro para entrada do código
            try:
                codigo_aluno = int(input("Digite o código do aluno que deseja deletar: "))
                aluno.deletarAluno(codigo_aluno)
            except ValueError:
                print("Por favor, digite um código válido (número inteiro)")
                continue
        
        # Opção 6: Exibir informações dos planos
        elif opcao == '6':
            print(f"\n--- Lista de Planos ---\n")
            print(f"Plano Day Use: Por R$ 29.90, o Day Use permite experimentar a academia por um dia completo. "
                  "Durante esse período, o usuário pode usufruir de musculação, ergometria e Cross Training, "
                  "conforme a grade de aulas e o funcionamento da unidade. Uma ótima opção para quem quer conhecer "
                  "a academia antes de se comprometer com um plano maior.")
            print(f"\nPlano Light: Por R$ 99.90 mensais, o Plano Light é ideal para quem busca um bom custo-benefício. "
                  "Sem exigências de fidelidade ou anuidade, o usuário pode treinar na unidade em que se matriculou, "
                  "com acesso a horários livres. O plano inclui musculação e ergometria, além de 30 dias gratuitos "
                  "no aplicativo Weburn para acompanhamento dos treinos.")
            print(f"\nPlano Plus: Com um custo de apenas R$ 0.99 no primeiro mês, o Plano Plus oferece total flexibilidade "
                  "aos seus usuários. Sem fidelidade e sem anuidade, você poderá treinar em qualquer unidade da rede no Brasil. "
                  "O plano inclui um acompanhante gratuito até 5 vezes por mês, acesso ao aplicativo Weburn, além de musculação, "
                  "ergometria, ginástica, danças e Cross Training, sujeitos à disponibilidade da unidade. O horário é livre e "
                  "também conta com aulas online via Self Digital.")
            print(f"\nPlano PremiumPlus: Com valor de R$ 149.90 ao mês, o Plano Mega Plus é uma opção premium para quem deseja "
                  "mais benefícios. Assim como os outros, não exige fidelidade nem anuidade. Você poderá treinar em qualquer "
                  "unidade da academia no Brasil, e ainda tem direito a levar um acompanhante até 10 vezes por mês. O plano "
                  "inclui acesso ao App Weburn, musculação, ergometria, ginástica, danças e Cross Training, conforme a "
                  "disponibilidade da unidade. O horário de treino é livre e oferece aulas online com a Self Digital.\n")
        
        # Opção 7: Sair do programa
        elif opcao == '7':
            print("Saindo do sistema...")
            break
        
        # Opção inválida
        else:
            print("Opção inválida. Tente novamente.")

# Verifica se este arquivo está sendo executado diretamente
if __name__ == '__main__':
    main()