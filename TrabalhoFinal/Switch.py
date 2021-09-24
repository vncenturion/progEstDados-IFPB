from TabelaMac import TabelaMac
class Switch:
    def __init__(self, nome, marca, mac, ip, portas):
        self.__nome = nome
        self.__marca = marca
        self.__mac = mac
        self.__ip = ip
        self.__portas = portas
        self.__tabela = TabelaMac(portas)

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
    def portas(self):
        return self.__portas

    @portas.setter
    def portas(self, novoPortas):
        self.__portas = novoPortas

    @property
    def tabela(self):
        return self.__tabela

    '''
    def adicionarMAC(self, macHOST): #tabela hash
        chave = hash(macHOST)
        indexHASH = chave % (self.portas)
        self.tabela.data[indexHASH] = macHOST
        return
    '''

    def __str__(self):
        return f'''
Nome/modelo: {self.nome}
Marca: {self.marca}
MAC do equipamento: {self.mac}
IP do equipamento: {self.ip}
Número de portas: {self.portas} '''