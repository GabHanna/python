saldoinicial = 50.00
custorefrigerante = 8.00
custopao = 4
custoMortadela = 39.90

valorCompra = (custorefrigerante * 2) + custopao + ((custoMortadela / 1000) * 300)

saldofinal = saldoinicial - valorCompra
print(f"Jose chegou com R${saldoinicial} e saiu com R${saldofinal}")
