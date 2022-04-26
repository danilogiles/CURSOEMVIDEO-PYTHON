num1 = (int(input("Digite um numero: ")),
        int(input("Digite outro numero: ")),
        int(input("Digite mais um numero:")),
        int(input("Digite o ultimo numero: ")))
tupla = (num1)
cont9 = cont3 = par = 0
valores = ''
for c in range(0, len(tupla)):
    if tupla[c] == 9:
        cont9 += 1
    if tupla[c] % 2 == 0:
        par += 1
        valores = valores + str(f"{tupla[c]-1} ")
    if tupla[c] == 3:
        cont3 += 1
print(f"Voce Digitou os valores {tupla}")
print(f"O valor 9 apareceu {cont9} vezes")
print(f"O valor 9 apareceu {tupla.count(9)} vezes")
if cont3 > 0:
    print(f"O valor 3 apareceu na {tupla.index(3)+1} posicao")
else:
    print("O valor 3 nao foi digitado em nenhuma posicao")
print(f"Os valores pares digitados foram {valores}.")




