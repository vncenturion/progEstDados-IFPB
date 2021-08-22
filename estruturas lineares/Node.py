class Node:
    def __init__(self, carga, prox: 'Node' = None):
        self.__carga = carga
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

    '''
    def __str__(self):
        return '%s -> %s' % (self.carga, self.prox)
    '''

    def __repr__(self):
        pass