class Filme:
  def __init__(self, id, titulo, preço ): # construtor
    self.__id = id #observar name mangling
    self.__titulo = titulo
    self.__nota = None
    self.__preço = preço

  # método "get" para o id
  @property
  def id(self):
    return self.__id

  @property
  def titulo(self):
    return self.__titulo
    
  @property
  def nota(self):
    return self.__nota

  @property
  def preço(self):
    return self.__preço

  #criar um método "set"
  @id.setter
  def id(self, novoId):
    self.__id = novoId  
      
  @titulo.setter
  def titulo(self, novoTitulo):
    self.__titulo = novoTitulo  
  
  @nota.setter
  def nota(self, novaNota):
    if novaNota <= 0:
      self.__nota = 0
    elif novaNota < 5:
      self.__nota = novaNota
    else:
      self.__nota = 5.0
    ### foi removido o metodo avaliar e colocados os requisitos no setter
    
  @preço.setter
  def preço(self, novoPreço):
    if novoPreço < 0:
      self.__preço = 0
    else:
      self.__preço = novoPreço
    ### foi removido o metodo reajuste e colocados os requisitos no setter

  def __str__(self):
    return f'{self.__id} - {self.__titulo} - nota: {self.__nota}, preço = {self.__preço}'