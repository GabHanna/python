# Solicitando a entrada da variavel idade
idade = int(input("Qual a sua idade?"))

# Definindo a categoria atraves da idade

if idade < 13:
    categoria = "Crianca"
elif idade >= 13 and idade < 18:
    categoria = "Adolescente"
elif idade >= 18 and idade < 60:
    categoria = "Adulto"
else :
    categoria = "Idoso"

print (f"A pessoa é classificada como: {categoria}")
