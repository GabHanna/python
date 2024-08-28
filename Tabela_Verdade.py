a = 2
b = 6
c = 3

operacaoAnd = a == b and c * a == b
print (operacaoAnd)
operacaoOR = a == b or c * a == b
print (operacaoOR)

operacaoAnd2 = a == (c+b) and b == c
print (operacaoAnd2)
operacaoOR2 = a == (c+b) or b == c
print (operacaoOR2)

operacaoAnd3 = a > 5 and b > 3
print (operacaoAnd3)
operacaoOR3 = a > 5 or b > 3
print (operacaoOR3)

operacaoAnd4 = a < 5 and c >= 3
print (operacaoAnd4)
operacaoOR4 = a < 5 or c >= 3
print (operacaoOR4)

operacaoAnd5 = not b == 6 and 3 * 2 == b
print (operacaoAnd5)
operacaoOR5 = not b == 6 or 3 * 2 == b
print (operacaoOR5)

operacaoAnd6 = c < 5 and not b > 6
print(operacaoAnd6)
operacaoOR6 = c < 5 or not b > 6
print(operacaoOR6)

