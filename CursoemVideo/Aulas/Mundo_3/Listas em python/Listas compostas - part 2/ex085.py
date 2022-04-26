listapar = list()
listaimpar = list()
lista = list()
for c in range(0,7):
    num = int(input(f"Digite o {c+1}o. valor: "))
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
lista.append(listapar)
lista.append(listaimpar)
print(f'O valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores impares digitados foram {sorted(lista[1])}')

#Solucao Guanabara
'''
num = [[],[]]
valor = 0
for c in range(1,8);
    valor = int(input('Digite um valor: ')
    if valor % 2 == 0;
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')
'''