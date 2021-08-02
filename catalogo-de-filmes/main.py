########################################
# instanciando a Plataforma de Streaming com o nome desejado
from PlataformaStreaming import PlataformaStreaming
from Filme import Filme

netflix = PlataformaStreaming('Netflix')

netflix.cadastrarFilme(Filme(1,'Stuart Little',5.0))
netflix.cadastrarFilme(Filme(2,'Luca',15.0))

while(True):
  filme = None
  idFilme = None
  netflix.menuPrincipal() #imprime menuPrincipal
  opcao = str(input('opção:'))
  opcao = opcao.lower() #transforma em lowercase o valor digitado acima

### REAJUSTAR PRECO
  if opcao == 'r': 
    idFilme = int(netflix.validaID()) #Metodo de validação de entrada de ID
    filme = netflix.pesquisaFilme(idFilme)
    if filme != None:
      print('Titulo:', filme.titulo)
      print('Preco anterior:', filme.preço)
      novoPreco = float(netflix.validaPreco()) # exceção para preço em float no metodo validaPreço
      netflix.reajustarPreco(idFilme, novoPreco)
 
 ### AVALIAR FILME
  elif opcao == 'a': 
    idFilme = int(netflix.validaID())
    filme = netflix.pesquisaFilme(idFilme)
    if filme == None:
      print(f'Filme com id {idFilme} não está cadastrado')
    else:
      print('Titulo:', filme.titulo)
      nota = float(netflix.validaNota()) # exceção para nota em float
      print("Nota: {} atribuída".format(nota))
      netflix.avaliarFilme(idFilme, nota)

### LISTAR FILMES NO CATALOGO
  elif opcao == 'l':
    print()
    netflix.listarFilmes()

### CADASTRAR NOVO FILME
  elif opcao == 'c':
    idFilme = int(netflix.validaID())
    filme = netflix.pesquisaFilme(idFilme) #verifica se o ID já existe
    if (filme == None): #caso não existe procede ao cadastro
      titulo = input('Título do filme para cadastro:')
      preço = float(netflix.validaPreco())
      netflix.cadastrarFilme(Filme(idFilme, titulo, preço))
    else: #caso o id já exista, informa ao usuário
      print("ID já existente!")
    print()
    netflix.listarFilmes()

### PESQUISAR
  elif opcao == 'p':
    idFilme = netflix.validaID()
    filme = netflix.pesquisaFilme(idFilme)
    if filme != None:
      print('Titulo:', filme.titulo)
      print('Preço:', filme.preço)
      print('Nota:', filme.nota)

### SAIR
  elif opcao == 's':
    break