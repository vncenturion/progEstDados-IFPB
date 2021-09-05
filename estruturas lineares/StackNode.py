class StackNode:
    def __init__(self, carga=0, abaixo=None):
        self.__carga = carga
        self.__abaixo = abaixo

    @property
    def carga(self):
        return self.__carga

    @carga.setter
    def carga(self, novaCarga):
        self.__carga = novaCarga

    @property
    def abaixo(self):
        return self.__abaixo

    def abaixo(self, novo_abaixo):
        self.__abaixo = novo_abaixo

    def __repr__(self):
        return '%s -> %s' % (self.carga, self.abaixo)