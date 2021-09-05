class Pilha:
    def __init__(self):
        self.__topo = None


    @property
    def topo(self):
        return self.__topo

    @topo.setter
    def topo(self, novoTopo):
        self.__topo = novoTopo

    def is_empty(self):
        return self.topo is None


    ## MÉTODOS

    def push(self, elemento):
        novoNode = StackNode(elemento) #cria novo nó
        novoNode.abaixo = self.topo #referencia o topo atual como abaixo do novo nó
        self.topo = novoNode #coloca o novo nó como topo
