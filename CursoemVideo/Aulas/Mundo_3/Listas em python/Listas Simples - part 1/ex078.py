lista = []
maior = menor = 0
mp = mep = str()
for c in range(0,5):
    lista.append(int(input(f"Digite um valor para a posicao {c}: ")))
maior = menor = lista[0]
for contador, valor in enumerate(lista):
    if maior <= valor:
        maior = valor
    else:
        menor = valor
for cont, val in enumerate(lista):
    if maior == val:
        mp = mp + str(cont) + '... '
    if menor == val:
        mep = mep + str(cont) + '... '
print('-=' * 30)
print(f"Voce digitou os valores {lista}")
print(f'O maior valor digitado foi {maior} na posicao {mp}')
print(f'O menor valor digitado foi {menor} na posicao {mep}')

