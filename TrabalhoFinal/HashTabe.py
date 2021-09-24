class HashTable:

    def __init__(self, portas:int):
        self.__portas = portas
        self.__disponivel = portas
        self.__slots = []
        self.__data = [None] * portas
        for n in range(portas):
            self.__slots.append('porta '+str(n+1))

    @property
    def portas(self):
        return self.__portas

    @portas.setter
    def portas(self, novoPortas):
        self.__portas = novoPortas

    @property
    def slots(self):
        return self.__slots

    @slots.setter
    def slots(self, novoSlots):
        self.__slots=novoSlots

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self,novodata):
        self.__data=novodata

    @property
    def disponivel(self):
        return self.__disponivel

    @disponivel.setter
    def disponivel(self, novoDisponivel):
        self.__disponivel= novoDisponivel

    #METODOS

    def imprime(self):
        lista = []
        for n in range(self.portas):
            valor=''
            if self.data[n] == None:
                valor='disponível'
            else:
                valor=self.data[n]
            lista.append(self.slots[n]+" : "+valor)
        return (lista)

    def put(self, macHost, chave=None):
        if self.disponivel==0:
            print('Não há portas disponíveis')
            return
        if chave==None:
            hashValue = self.hash(macHost)
        else:
            hashValue = self.hash(chave)
        if self.data[hashValue]==None:
            self.data[hashValue]=macHost
            self.disponivel-=1
            print('Endereço MAC do host acionado a tabela MAC do dispositivo')
            return
        elif self.data[hashValue] == macHost:
            print('Endereço MAC do host já consta na tabela MAC do dispositivo')
            return
        else:
            novachave=hashValue+1
            self.put(macHost,novachave)
        return

    def get(self, macHost):
        if self.disponivel==self.portas:
            print('Tabela vazia')
            return

        chave=macHost
        for n in range(self.portas): #EVITAR QUE O PROGRAMA RETORNE "NÃO ENCONTRADO" CASO UM VALOR ANTERIOR TENHA OCUPADO PRIMEIRO O INDEX E TENHA SIDO EXCLUIDO
            hashValue = self.hash(chave)
            if self.data[hashValue]==macHost:
                print('Endereço MAC {} consta na Tabela MAC na {}'.format(macHost, self.slots[hashValue]))
                return hashValue
            else:
                chave=chave+1
        print('Endereço MAC {} não consta na Tabela MAC do dispositov'.format(macHost))
        return

    def remove(self, macHost):
        index=self.get(macHost)
        if index is not None:
            self.data[index]=None
            print('Endereço MAC {} removido com suscesso!'.format(macHost))
        return

    def __key(self, valor) -> int:
        x = valor.split(":")
        hex = ''
        for item in x:
            hex = hex.join(item)
        return int(hex, 16)

    def hash(self, chave):
        if chave is not int:
            chave=self.__key(chave)
        return chave%(self.__portas)

'''
x=HashTable(4)
print(x.imprime())
print()
print(x.hash('11:11:11:11'))
x.put('11:11:11:11')
print(x.imprime())
print()
print(x.hash('11:11:11:12'))
x.put('11:11:11:12')
print(x.imprime())
print()
x.put('11:11:11:12')
print(x.imprime())
print(x.get('11:11:11:12'))
x.remove('11:11:11:12')
print(x.imprime())
'''