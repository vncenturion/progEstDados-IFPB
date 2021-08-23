from ListaEncadeada import ListaEncadeada
from ListaDupla import ListaDupla
from ListaCircular import ListaCircular
from Node import Node

def juntaLista(lista_aux,lista_a: 'ListaEncadeada', lista_b: 'ListaEncadeada'):
    aux = lista_a.cabeca
    while aux is not None:
        lista_aux.inserirFinal(aux.carga)
        aux = aux.prox
    aux = lista_b.cabeca
    while aux is not None:
        lista_aux.inserirFinal(aux.carga)
        aux = aux.prox
    return
'''
lista1 = ListaEncadeada()
lista2 = ListaEncadeada()
lista3 = ListaEncadeada()
lista4 = ListaEncadeada()
lista5 = ListaEncadeada()
lista6 = ListaEncadeada()

print(lista1.listaVazia())
lista1.imprimirLista()
lista1.inserirFinal(1)
lista1.inserirFinal(2)
lista1.inserirFinal(1)
lista1.imprimirLista()
print(lista1.tamanho)
lista2.imprimirLista()
lista2.inserirFinal(1)
lista2.inserirFinal(2)
lista2.inserirFinal(3)
lista2.imprimirLista()
print(lista2.tamanho)

print("\nTeste programa 01")
aux = lista1.cabeca
while aux is not None:
    lista3.inserirFinal(aux.carga)
    aux=aux.prox
aux = lista2.cabeca
while aux is not None:
    lista3.inserirFinal(aux.carga)
    aux=aux.prox

lista1.imprimirLista()
lista2.imprimirLista()
lista3.imprimirLista()
lista3.removerElemento(1)
lista3.imprimirLista()

### teste para função JUNTALISTA
lista4.inserirFinal(1)
lista4.inserirFinal(2)
lista4.inserirFinal(3)
lista5.inserirFinal('a')
lista5.inserirFinal('b')
lista5.inserirFinal('c')

print ("\nTeste programa 02 - função juntaLista")
juntaLista(lista6,lista4,lista5)
lista4.imprimirLista()
lista5.imprimirLista()
lista6.imprimirLista()

'''

### LISTAS DUPLAS ENCADEADAS

lista1 = ListaDupla()
lista1.inserirFinal(2)
lista1.inserirInicio(1)
lista1.inserirFinal(3)
lista1.inserirInicio(0)
lista1.imprimirLista()

## teste lista reversa
lista1.imprimirListaRev()
## inserir na posição dada (array)
lista1.inserirPosicao(5,3)

lista1.imprimirLista()
print(lista1.tamanho)
lista1.removerFinal()
lista1.imprimirLista()
print(lista1.tamanho)
lista1.removerPosicao(3)
lista1.imprimirLista()
lista1.removerFinal()
lista1.imprimirLista()
lista1.removerPosicao(1)
lista1.imprimirLista()
print(lista1.tamanho)

### teste remover elemento
lista1.inserirFinal(3)
lista1.inserirFinal(2)
lista1.inserirFinal(1)
lista1.inserirFinal(3)
lista1.inserirFinal(3)
lista1.inserirFinal(4)
lista1.imprimirLista()
lista1.removerElemento(3)
lista1.imprimirLista()

print("\nTESTE 2")
lista1.inserirFinal(3)
lista1.inserirFinal(2)
lista1.inserirFinal(1)
lista1.inserirFinal(3)
lista1.inserirFinal(3)
lista1.inserirFinal(4)
lista1.imprimirLista()
lista1.removerElemento2(3)
lista1.imprimirLista()

'''

lista1=ListaCircular()
lista1.inserirFinal(1)
lista1.inserirFinal(2)
lista1.inserirInicio(0)
lista1.inserirFinal(3)
lista1.inserirInicio(-1)
print("print list")
lista1.imprimirLista()
print("tamanho: "+str(lista1.tamanho))
lista1.removerElemento(0)
lista1.removerElemento(2)
print("print list")
lista1.imprimirLista()
print("tamanho: "+str(lista1.tamanho))

'''

print('fim')
print("\npalindromo")
listaPalindromo=ListaDupla()
palindromo=str(input("Digite uma palavra ou frase qualquer: "))
palindromo=palindromo.casefold()
for letra in palindromo:
    if letra != " ":
        listaPalindromo.inserirFinal(letra)

listaPalindromo.imprimirLista()
listaPalindromo.imprimirListaRev()
noCabeca = listaPalindromo.cabeca
noCauda = listaPalindromo.cauda
while noCabeca is not None:
    if noCabeca.carga == noCauda.carga:
        noCabeca=noCabeca.prox
        noCauda=noCauda.ant
    else:
        print("não é palindromo!")
        break

print(listaPalindromo.ehPalindromo())