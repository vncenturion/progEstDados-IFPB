class TabelaMac:

    def __init__(self, portas):
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

    def inserirMac(self, macHost:str, chave:int):
        if self.disponivel==0:
            print('Não há portas disponíveis')
            return
        valorHash = self.funcao_hash(chave)
        if self.data[valorHash]==None:
            self.data[valorHash]=macHost
            self.disponivel-=1
            print('Endereço MAC do host acionado a tabela MAC do dispositivo')
            return
        elif self.data[valorHash]==macHost:
            self.data[valorHash] == macHost
            print('Endereço MAC do host já consta na tabela MAC do dispositivo')
            return
        else:
            novachave=valorHash+1
            self.inserirMac(macHost,novachave)

    def criaChave(self, macHost:str) -> int:
        x = macHost.split(":")
        hex=''
        for item in x:
            hex=hex.join(item)
        return int(hex,16)

    def funcao_hash(self, chave):
        return chave%self.portas

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size
