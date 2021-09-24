def funcao_hash(macHost, numeroportas):
    soma = 0
    for posicao in range(len(macHost)):
        soma = soma + ord(macHost[posicao])
    print(soma)
    valorHash = soma % numeroportas
    return valorHash


print(hash('12AA1511161'))
print(hash('12AA1511161')%24)
print(hash(5))
print(hash(5))
print(hash('12341258'))
print(hash('12341258')%24)
print(hash('11:345:14'))
print(hash('11:345:14')%24)

print('função hash')

print(funcao_hash('12:33:44:55:66:77',12))
print(funcao_hash('ff:ff:ff:ff:ff:ff',8))
print(funcao_hash('00:00:00:00:00:00',8))

mac = 'ff:ff:ff:ff:ff:ff'
x = mac.split(":")
print(x)
soma=0
for item in x:
    soma = soma + int(item,16)
print(soma)

mac = 'ff:ff:ff:ff:ff:ff'
y = mac.split(":")
z=''
for item in y:
    z=z.join(item)
chave = z
print('z vale: {}'.format(z))
print('valor int de z: {}'.format(int(z,16)))
print(y)
soma=0
for item in y:
    soma = soma + int(item,16)
print(soma)