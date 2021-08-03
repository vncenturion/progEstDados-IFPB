### importando as classes
from PlataformaStreaming import PlataformaStreaming
from Filme import Filme

### instanciando a Plataforma de Streaming com o nome desejado
netflix = PlataformaStreaming('Netflix')
netflix.cadastrarFilme(Filme(1,'Stuart Little',5.0))
netflix.cadastrarFilme(Filme(2,'Luca',15.0))

### iniciando controle do prog principal
controle = True

while(controle):
  netflix.menuPrincipal() #imprime menuPrincipal
  opcao = str(input('opção:'))
  opcao = opcao.lower() #transforma em lowercase o valor digitado acima
  controle = netflix.opcoesMenu(opcao)

print("*** FIM DO PROGRAMA ***")