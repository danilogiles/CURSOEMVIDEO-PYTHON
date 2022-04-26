temp = list()
galera = list()
pesados = list()
leves = list()
peso = numpess = cont = maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    galera.append(temp[:])
    resp = ' '
    numpess += 1
    if maior and menor == 0:
        maior = menor = temp[1]
    elif maior <= temp[1]:
        maior = temp[1]
    elif menor >= temp [1]:
        menor = temp[1]
    else:
        x=0
    temp.clear()
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ').strip().upper()[0])
        if resp not in 'SN':
            print('Voce digitou uma opcao invalida!')
    if resp == 'N':
        break
for c in galera:
    if c[1] == maior:
        pesados.append(c[0])
    elif c[1] == menor:
        leves.append(c[0])
    else:
        x=0
print(f"Ao todo foram cadastradas {numpess} pessoas na lista.")
print(f"O maior peso foi {maior}Kg. Peso de {pesados}")
print(f"O menor peso foi {menor}Kg. Peso de {leves}.")


