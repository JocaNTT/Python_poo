class Livro:
  def __init__(self, titulo, autor, anoPublicacao):
    self.titulo = titulo
    self.autor = autor
    self.anoPublicacao = anoPublicacao
  def exibirInformacoes(self):
    print(f"Seu {self.titulo} escrito por {self.autor}, publicado no ano de {self.anoPublicacao}")
  
  def verificarIdadeLivro(self):
    if self.anoPublicacao < 1974:
      print("Este livro é um clássico")
    else:
      print("Seu livro não é um clássico")