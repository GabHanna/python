bandeiras = {54: "MasterCard", 53: "Visa", 33: "Elo", 22: "Alelo"}
digito = None

while True:
    try:
        digito = int(input("Digite um número (ou digite -1 para sair): "))

        if digito == -1:
            print("Saindo do programa.")
            break

        if digito in bandeiras:
            print(f"A bandeira corresponde é: {bandeiras[digito]}")
            break
        else:
            print("Número inválido. Tente novamente.")
    except ValueError as vr:
        print("Não foi digitado um valor inteiro! Tente novamente")
    except Exception as e:
        print("Erro :: ", e)

