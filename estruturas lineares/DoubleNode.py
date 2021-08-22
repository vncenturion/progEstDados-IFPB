class DoubleNode:
    def __init__(self, carga, ant: 'Node' = None, prox: 'Node' = None):
        self.__carga = carga
        self.__anterior = ant
        self.__proximo = prox

    @property
    def carga(self):
        return self.__carga

    @carga.setter
    def carga(self, novaCarga):
        self.__carga = novaCarga

    @property
    def prox(self):
        return self.__proximo

    @prox.setter
    def prox(self, novoNode):
        self.__proximo = novoNode

    @property
    def ant(self):
        return self.__anterior

    @ant.setter
    def ant(self, novoNode):
        self.__anterior = novoNode

    '''
    def __str__(self):
        return '%s -> %s' % (self.carga, self.prox)
    '''

    def __repr__(self):
        pass