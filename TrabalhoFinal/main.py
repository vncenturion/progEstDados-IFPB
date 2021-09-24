from Switch import Switch
from HashTable import HashTable
import os, re, csv
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
    return Switch(nome, marca, macSWITCH, portas, ip)

def listar_dispositivos(lista):
    for item in lista:
        print(item)
        print('PORTAS: ' + str(HashTable.imprime(item.tabela)))
        # print('fim listar dispositivos')
    return

def inserirHost(lista: list):
    nomeDispositivo = input('Digite o nome do disposivo em que deseja adicionar o HOST: ')
    indexSWITCH = buscaDispositivo(lista, nomeDispositivo)
    if indexSWITCH != -1:
        switch = lista[indexSWITCH]
        macHOST = input('Digite o MAC do HOST: ')
        while not re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", macHOST.lower()):
            print("Endereço MAC invalido!")
            macHOST = input("Digite o MAC do dispositivo: ")

        HashTable.put(switch.tabela, macHOST)
    else:
        print('Dispositivo não encontrado')
    return

def buscaDispositivo(lista: list, nome) -> int:
    for index, item in enumerate(lista):
        if item.nome == nome:
            return index
    return -1

def pesquisar_mac(lista: list):
    macPesquisado = input('Digite o MAC do HOST: ')
    while not re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", macPesquisado.lower()):
        print("Endereço MAC invalido!")
        macPesquisado = input("Digite o MAC do dispositivo: ")
    for item in lista:
        print(str(item.nome) + ':')
        resultado = HashTable.get(item.tabela, macPesquisado)
        if resultado is not None:
            return [item.nome, resultado]
    return


def menu(lista: list):
    os.system('clear')
    exibirMenu()
    opcao = str(input('\nDigite a opção selecionada: '))
    if opcao == '1':
        lista.append(cadastrar())
        input('\n<digite qualquer tecla para voltar ao menu>')
        return True
    elif opcao == '2':
        listar_dispositivos(lista)
        input('\n<digite qualquer tecla para voltar ao menu>')
        return True
    elif opcao == '3':
        inserirHost(lista)
        input('\n<digite qualquer tecla para voltar ao menu>')
        return True
    elif opcao == '4':
        pesquisar_mac(lista)
        input('\n<digite qualquer tecla para voltar ao menu>')
        return True
    elif opcao == '5':
        return False
    else:
        print('Opção inválida')
        return True

def cadastroAutomatico_switch(lista: list) -> Switch:
    nome = lista[0]
    marca = lista[1]
    mac = lista[2]
    portas = int(lista[3])
    return Switch(nome, marca, mac, portas)

def cadastroAutomatico_Host(listaSwitch: list, listaHost: list):
    for index,switch in enumerate(listaSwitch):
        for mac in listaHost[index]:
            HashTable.put(switch.tabela, mac)
    return

listaDispositivos = []
controle = True

file = open('lista_de_switches.csv')
type(file)
csvreader = csv.reader(file)
matrizSwitch = []
for linha in csvreader:
    matrizSwitch.append(linha)
for item in matrizSwitch:
    listaDispositivos.append(cadastroAutomatico_switch(item))
file.close()

file = open('lista_de_hosts.csv')
type(file)
csvreader = csv.reader(file)
linhas = []
for linha in csvreader:
    linhas.append(linha)
cadastroAutomatico_Host(listaDispositivos, linhas)
file.close()

while (controle):
    controle = menu(listaDispositivos)

print('fim do programa')