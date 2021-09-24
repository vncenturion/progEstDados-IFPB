from HashTable import HashTable
class Switch:
    def __init__(self, nome, marca, mac, num_portas, ip=None):
        self.__nome = nome
        self.__marca = marca
        self.__mac = mac
        self.__num_portas = int(num_portas)
        self.__ip = ip
        self.__tabelaMac = HashTable(num_portas)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, novoMarca):
        self.__marca = novoMarca

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, novoIp):
        self.__ip = novoIp

    @property
    def mac(self):
        return self.__mac

    @mac.setter
    def mac(self, novoMac):
        self.__mac = novoMac

    @property
    def num_portas(self):
        return self.__num_portas

    @num_portas.setter
    def num_portas(self, novoPortas):
        self.__num_portas = novoPortas

    @property
    def tabela(self):
        return self.__tabelaMac

    def __str__(self):
        return f'''
Nome: {self.nome}
Marca: {self.marca}
MAC do equipamento: {self.mac}
IP do equipamento: {self.ip}
Número de portas: {self.num_portas}
'''