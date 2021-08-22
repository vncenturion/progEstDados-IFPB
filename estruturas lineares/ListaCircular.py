from Node import Node

class ListaCircular():
    #CONSTRUTOR
    def __init__(self):
        self.__cabeca=None
        self.__tamanho=0

    #GET/SET
    @property
    def cabeca(self):
        return self.__cabeca
    @cabeca.setter
    def cabeca(self, novaCabeca):
        self.__cabeca = novaCabeca

    @property
    def tamanho(self):
        return self.__tamanho
    @tamanho.setter
    def tamanho(self, novoTamanho):
        self.__tamanho = novoTamanho

    #MÉTODOS
    def inserirInicio(self, carga):
        novoNode = Node(carga)
        atual = self.cabeca
        novoNode.prox = self.cabeca

        if not self.cabeca:
            novoNode.prox = novoNode
        else:
            while atual.prox != self.cabeca:
                atual = atual.prox
            atual.prox = novoNode
        self.cabeca = novoNode
        self.tamanho += 1
        return

    def inserirFinal(self, carga):
        if not self.cabeca:
            self.cabeca = Node(carga)
            self.cabeca.prox = self.cabeca
        else:
            novoNode = Node(carga)
            atual = self.cabeca
            while atual.prox != self.cabeca:
                atual = atual.prox
            atual.prox = novoNode
            novoNode.prox = self.cabeca
        self.tamanho+=1
        return

    def imprimirLista(self):
        atual = self.cabeca
        while atual:
            print(atual.carga)
            atual = atual.prox
            if atual == self.cabeca:
                break
        return

    def __len__(self):
        atual = self.cabeca
        contador = 0
        while atual:
            contador += 1
            atual = atual.prox
            if atual == self.cabeca:
                break
        return contador

    def dividirLista(self):
        size = len(self)

        if size == 0:
            return None
        if size == 1:
            return self.cabeca

        mid = size // 2
        contador = 0

        prev = None
        atual = self.cabeca

        while atual and contador < mid:
            contador += 1
            prev = atual
            atual = atual.prox
        prev.prox = self.cabeca

        split_cllist = ListaCircular()
        while atual.prox != self.cabeca:
            split_cllist.inserirFinal(atual.carga)
            atual = atual.prox
        split_cllist.inserirFinal(atual.carga)

        self.imprimirLista()
        print("\n")
        split_cllist.imprimirLista()
        return

    def removerElemento(self, elemento):
        if self.cabeca.prox == self.cabeca and self.cabeca.carga == elemento:
            self.cabeca = None
            return
        if self.cabeca.carga == elemento:
            atual = self.cabeca
            while atual.prox != self.cabeca:
                atual = atual.prox
            atual.prox = self.cabeca.prox
            self.cabeca = self.cabeca.prox
        else:
            atual = self.cabeca
            prev = None
            while atual.prox != self.cabeca:
                prev = atual
                atual = atual.prox
                if atual.carga == elemento:
                    prev.prox = atual.prox
                    atual = atual.prox
        self.tamanho-=1
        return