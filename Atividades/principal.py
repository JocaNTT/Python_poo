from livro import Livro

def adicionarLivro():
    titulo = input("Informe o título do livro: ")
    autor = input("Informe o autor do livro: ")
    anoPublicacao = int(input("Informe o ano de publicação do livro: "))
    
    return Livro(titulo, autor, anoPublicacao)

def main():
    livros = []

    while True:
        livro = adicionarLivro()
        livros.append(livro)

        continuar = input("Deseja adicionar outro livro? (sim/não): ").lower()
        if continuar != 'sim':
            break
    for i, livro in enumerate(livros, 1):
        print(f"\nInformações do Livro {i}:")
        livro.exibirInformacoes()
        livro.verificarIdadeLivro()

main()