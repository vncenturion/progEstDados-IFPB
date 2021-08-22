from Node import Node
import sys

class ListaEncadeada:

#CONSTRUTOR
    def __init__(self):
        self.__cabeca = None
        self.__cauda = None
        self.__tamanho = 0

#GET/SET
    @property
    def cabeca(self):
        return self.__cabeca

    @cabeca.setter
    def cabeca(self, novaCabeca):
        self.__cabeca = novaCabeca

    @property
    def cauda(self):
        return self.__cauda

    @cauda.setter
    def cauda(self, novaCauda):
        self.__cauda = novaCauda

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, novoTamanho):
        self.__tamanho = novoTamanho

#METODOS
    def inserirInicio(self, carga):
        novoNode = Node(carga)
        if self.cabeca == None:
            self.cabeca = novoNode
            self.cauda = novoNode
        else:
            novoNode.prox = self.cabeca
            self.cabeca = novoNode
        self.tamanho +=1
        return

    def inserirFinal(self, carga):
        novoNode = Node(carga)
        if self.cauda == None:
            self.cabeca = novoNode
            self.cauda = novoNode
        else:
            self.cauda.prox = novoNode
            self.cauda = novoNode
        self.tamanho += 1
        return

    def inserirPosicao(self, valor, posicao):
        novoNode = Node(valor)
        atual = self.cabeca
        contador = 0
        if (posicao <= 0):
            self.inserirInicio(valor)
        elif (posicao >= self.tamanho):
            self.inserirFinal(valor)
        else:
            while (posicao > contador+1):
                atual = atual.prox
                contador += 1
            novoNode.prox = atual.prox
            atual.prox = novoNode
        self.tamanho += 1
        return

    def removerInicio(self):
        if self.listaVazia():
            print("Lista vazia")
            return
        elif self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cabeca = self.cabeca.prox
        self.tamanho -= 1
        return


    def removerFinal(self):
        if self.listaVazia():
            print("Lista vazia")
            return
        elif self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            atual: 'Node' = self.cabeca
            while atual.prox is not self.cauda:
                atual = atual.prox
            self.cauda = atual
            self.cauda.prox = None
        self.tamanho -= 1
        return

    def removerPosicao(self, posicao):
        atual = self.cabeca
        contador = 0
        if self.listaVazia():
            print("Lista vazia")
            return
        elif (posicao <= 0):
            self.removerInicio()
            return
        elif (posicao >= self.tamanho-1):
            self.removerFinal()
            return
        else:
            while (posicao > contador + 1):
                atual = atual.prox
                contador += 1
            atual.prox = atual.prox.prox
        self.tamanho -= 1
        return

    def removerElemento(self, elemento):
        for x in range (self.tamanho):
            contador = 0
            atual = self.cabeca
            while atual is not None:
                if atual.carga == elemento:
                    print("removeu")
                    self.removerPosicao(contador)
                    self.imprimirLista()
                atual=atual.prox
                contador+=1
        return


    def buscaPosicao(self, valor):
        pass

    def buscaValor(self, posicao):
        pass

    def imprimirLista(self):
        atual = self.cabeca
        if self.listaVazia():
            print("lista vazia")
            return
        print("cabeça->[", end="")
        while atual.prox is not None:
            print(str(atual.carga) + ", ", end="")
            atual = atual.prox
        print(str(atual.carga) + "]<-cauda")
        return

    def listaVazia(self):
        return self.cauda == self.cabeca == None


    '''
    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
    '''

    def __len__(self):
        atual = self.cabeca
        c = 0
        while atual is not None:
            atual = atual.prox
            c += 1
        return c