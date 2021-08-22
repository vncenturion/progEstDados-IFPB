from DoubleNode import DoubleNode

class ListaDupla():
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
    def inserirInicio(self, valor):
        novoNode = DoubleNode(valor)
        if self.cabeca == None:
            self.cabeca = novoNode
            self.cauda = novoNode
        else:
            self.cabeca.ant = novoNode
            novoNode.prox = self.cabeca
            self.cabeca = novoNode
        self.tamanho += 1

    def inserirFinal(self, valor):
        novoNode = DoubleNode(valor)
        if self.cauda == None:
            self.cabeca = novoNode
            self.cauda = novoNode
        else:
            novoNode.ant = self.cauda
            self.cauda.prox = novoNode
            self.cauda = novoNode
        self.tamanho += 1

    def inserirPosicao(self, valor, posicao):
        novoNode = DoubleNode(valor)
        atual = self.cabeca
        contador = 0
        if (posicao<=0):
            self.inserirInicio(valor)
        elif (posicao>=self.tamanho):
            self.inserirFinal(valor)
        else:
            while (posicao>contador):
                atual=atual.prox
                contador+=1
            predecessor = atual.ant
            predecessor.prox = novoNode
            novoNode.ant = atual.ant
            atual.ant = novoNode
            novoNode.prox = atual
        self.tamanho +=1
        return

    def removerInicio(self):
        if self.listaVazia():
            print("Lista vazia")
            return
        elif self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cabeca = self.cabeca.prox
            self.cabeca.ant = None
        self.tamanho -= 1

    def removerFinal(self):
        if self.listaVazia():
            print("Lista vazia")
            return
        elif self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cauda = self.cauda.ant
            self.cauda.prox = None
        self.tamanho -= 1

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
            while (posicao > contador):
                atual = atual.prox
                contador += 1
            predecessor = atual.ant
            sucessor = atual.prox
            predecessor.prox = sucessor
            sucessor.ant = predecessor
            atual.prox = atual.ant = None
        self.tamanho -= 1
        return

    def removerElemento(self, elemento):
        for x in range (self.tamanho):
            contador = 0
            atual = self.cabeca
            while atual is not None:
                if atual.carga == elemento:
                    print("removeu elemento encontrado: "+str(elemento))
                    self.removerPosicao(contador)
                    self.imprimirLista()
                atual=atual.prox
                contador+=1
        return

    def removerElemento2(self, elemento):

        contador = 0
        atual = self.cabeca
        while atual is not None:
            if atual.carga == elemento:
                atual=atual.ant
                print("removeu elemento encontrado: "+str(elemento))
                self.removerPosicao(contador)
                self.imprimirLista()
                contador-=1
            atual=atual.prox
            contador+=1
        return

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

    def imprimirListaRev(self):
        atual = self.cauda
        if self.listaVazia():
            print("lista vazia")
            return
        print("cauda->[", end="")
        while atual.ant is not None:
            print(str(atual.carga) + ", ", end="")
            atual = atual.ant
        print(str(atual.carga) + "]<-cabeça")
        return

    def listaVazia(self):
        return self.cabeca is None