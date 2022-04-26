from random import randint
numeros = (randint(1, 10),randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
#forma complexa usando for
maior = menor = numeros[0]
x = 0
for c in range(0, len(numeros)):
    if maior < numeros[c]:
        maior = numeros[c]
    elif menor > c:
        menor = numeros[c]
print(f"Os valores sorteados foram: {numeros}")
print(f"O maior valor sorteado foi {maior}")
print(f"O menor valor sorteado foi {menor}")

#forma resumida sem precisar do for usando funcao
print(f'O maior valor sorteado foi {max(numeros)}')
print(f"O menor valor sorteado foi {min(numeros)}")
