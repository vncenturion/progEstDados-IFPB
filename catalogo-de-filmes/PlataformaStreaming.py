from Filme import Filme
class FilmeInexistenteException(Exception):
  ### lançada toda vez que uma tentativa de busca de um filme pelo id resulte em um resultado não encontrado no catálogo
  def __init__(self,message):
    super().__init__(message)

class PlataformaStreaming:
  def __init__(self, titulo):
    self.__titulo = titulo
    self.catalogo = []

### inserção de getter/setter
  @property
  def titulo(self):
    return self.__titulo

  @titulo.setter
  def titulo(self, novoTitulo):
    self.__titulo = novoTitulo 

### metodos

  def validaID(self): #evitar utilização de ID não INT
    while(True):
      try:
        idFilme = int(input('Digite o id do Filme:'))
        return idFilme
      except ValueError:
        print("ID informado deve ser do tipo inteiro")

  def validaPreco(self): #evitar utilização de PREÇO do tipo não real
    while(True):
      try:
        preço = float(input('Digite o preço do Filme:'))
        assert preço >=0 and preço <= 15.0
        return preço
      except ValueError:
        print("O valor para preço informado deve ser do tipo real")
      except AssertionError:
        print("O preço de locação deve ser positivo e menor que 15 reais")

  def validaNota(self): #evitar utilização de Nota de tipo não real
    while(True):
      try:
        nota = float(input('Digite a nota de avaliação para o Filme:'))
        return nota
      except ValueError:
        print("O valor para nota informado deve ser do tipo real")

  def cadastrarFilme(self, filme: Filme ):
    f = 0
    for f in self.catalogo:
      if f.id == filme.id:
        return
    self.catalogo.append(filme)
    print("{} cadastrado!".format(filme.titulo))
  
  def pesquisaFilme(self, id):
    f = 0
    contador=0
    for f in self.catalogo:
      
      try:
        if f.id == id:
          return f
        else:
          contador+=1
          if contador == len(self.catalogo):
            raise FilmeInexistenteException("Id não encontrado!")
      except FilmeInexistenteException as cee:
        print (cee)

  def listarFilmes(self):
    print("Filmes cadastrados:")
    f = 0
    for f in self.catalogo:
      print(f)
  
  def avaliarFilme(self, id, nota):
    f = 0
    for f in self.catalogo:
      if f.id == id:
        f.nota = nota
        return

  def reajustarPreco(self, id, novoPreço):
    f = 0
    for f in self.catalogo:
      if f.id == id:
        f.preço = novoPreço
        return

  def menuPrincipal(self):
    print()
    print('--------------------')
    print(self.titulo)
    print('--------------------')
    print('(r) Reajustar preço')
    print('(a) Avaliar filme')
    print('(l) Listar catálogo')
    print('(c) Cadastrar filme')
    print('(p) Pesquisar filme')
    print('(s) Sair')
    print('---------------------')
    return

    def opcoesMenu(self, opcao):
      chos