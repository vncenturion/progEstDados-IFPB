from Switch import Switch
from TabelaMac import TabelaMac
import os, re
from time import sleep

def exibirMenu():
    print('Menu principal')
    print('1: Casdastrar dispositivo')
    print('2: Exibir lista de dispositivos')
    print('3: Adicionar HOST')
    print('4: Pesquisar')
    print('5: Sair')
    return

def cadastrar():
    os.system('clear')
    print('Cadastro de dispositivo\n')
    nome = input("Digite o nome do dispositivo: ")
    marca = input("Digite a marca do dispositivo: ")
    macSWITCH = input("Digite o MAC do dispositivo: ")
    while not re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", macSWITCH.lower()):
        print("Endereço MAC invalido!")
        macSWITCH = input("Digite o MAC do dispositivo: ")
    ip = None
    portas = int(input("Digite o número de portas do dispositivo: "))
    return Switch(nome, marca, macSWITCH, ip, portas)


def listar_dispositivos(lista):
    for item in lista:
        print(item)
        print('PORTAS: '+str(TabelaMac.imprime(item.tabela)))
        #print('fim listar dispositivos')
    return

def inserirHost(lista: list):
    nomeDispositivo=input('Digite o nome do disposivo em que deseja adicionar o HOST: ')
    indexSWITCH = buscaDispositivo(lista, nomeDispositivo)
    if indexSWITCH != -1:
        switch = lista[indexSWITCH]
        macHOST = input('Digite o MAC do HOST: ')
        while not re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", macHOST.lower()):
            print("Endereço MAC invalido!")
            macHOST = input("Digite o MAC do dispositivo: ")

        TabelaMac.inserirMac(switch.tabela,macHOST,TabelaMac.criaChave(switch.tabela,macHOST))
    else:
        print('Dispositivo não encontrado')
    input('\n<digite qualquer tecla para voltar ao menu>')
    return

def buscaDispositivo(lista: list, nome):
    for index, item in enumerate(lista):
        if item.nome == nome:
            return index
    return -1

def pesquisar_dispositivos():
    pass


def menu(lista:list):
    os.system('clear')
    exibirMenu()
    opcao = int(input('\nDigite a opção selecionada: '))
    if opcao == 1:
        lista.append(cadastrar())
        input('\n<digite qualquer tecla para voltar ao menu>')
        return True
    elif opcao == 2:
        listar_dispositivos(lista)
        input('\n<digite qualquer tecla para voltar ao menu>')
        return True
    elif opcao == 3:
        inserirHost(lista)
        return True
    elif opcao == 4:
        pesquisar_dispositivos(lista)
        return True
    elif opcao == 5:
        return False
    else:
        print('Opção inválida')
        return True

listaDispositivos=[]
controle=True
while(controle):
    controle=menu(listaDispositivos)

print('fim do programa')
