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
    ### REAJUSTAR PRECO
    if opcao == 'r': 
      idFilme = int(self.validaID()) #Metodo de validação de entrada de ID
      filme = self.pesquisaFilme(idFilme)
      if filme != None:
        print('Titulo:', filme.titulo)
        print('Preco anterior:', filme.preço)
        novoPreco = float(self.validaPreco()) # exceção para preço em float no metodo validaPreço
        self.reajustarPreco(idFilme, novoPreco)
      return True
   
    ### AVALIAR FILME
    elif opcao == 'a': 
      idFilme = int(self.validaID())
      filme = self.pesquisaFilme(idFilme)
      if filme == None:
        print(f'Filme com id {idFilme} não está cadastrado')
      else:
        print('Titulo:', filme.titulo)
        nota = float(self.validaNota()) # exceção para nota em float
        print("Nota: {} atribuída".format(nota))
        self.avaliarFilme(idFilme, nota)
      return True

    ### LISTAR FILMES NO CATALOGO
    elif opcao == 'l':
      print()
      self.listarFilmes()
      return True

    ### CADASTRAR NOVO FILME
    elif opcao == 'c':
      idFilme = int(self.validaID())
      filme = self.pesquisaFilme(idFilme) #verifica se o ID já existe
      if (filme == None): #caso não existe procede ao cadastro
        titulo = input('Título do filme para cadastro:')
        preço = float(self.validaPreco())
        self.cadastrarFilme(Filme(idFilme, titulo, preço))
      else: #caso o id já exista, informa ao usuário
        print("ID já existente!")
        print()
      self.listarFilmes()
      return True

    ### PESQUISAR
    elif opcao == 'p':
      idFilme = self.validaID()
      filme = self.pesquisaFilme(idFilme)
      if filme != None:
        print('Titulo:', filme.titulo)
        print('Preço:', filme.preço)
        print('Nota:', filme.nota)
      return True

    ### SAIR
    elif opcao == 's':
      sair = input("Deseja sair (s/n)?: ")
      sair = sair.lower()
      if sair == 's':
        return False
      else:
        return True
      
    ### OPÇÃO INVALIDA
    else:
      print("Opção invalida!")
      return True