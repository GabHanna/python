## Declarando variaveis
dataMaximaInscricao = 28
diaInscricao = 29
indicacao = True
listadeEspera = False
idadeMinima = 14
idadeMaxima = 17
idadeMarcelo = 15


if diaInscricao > dataMaximaInscricao:
    print("Marcelo tem indicacao especial")
else:
    print("Marcelo não tem indicacao especial")

if idadeMinima < idadeMarcelo and idadeMarcelo < idadeMaxima:
    print("Marcelo pode se inscrever")
else:
    print("Marcelo nao tem idade permitida")

if listadeEspera == False:
    print("Marcelo nao esta na lista de espera")
