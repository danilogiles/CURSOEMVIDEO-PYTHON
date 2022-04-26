from time import sleep
from random import randint
temp = list()
lista = list()
cont = 0
print(" MEGA SENA PALPITER 2.0 ".center(40,'='))
jogos = int(input("Quantos jogos deseja gerar:"))
for c in range(0, jogos):
    for d in range(0,6):
        while True:
            num = randint(1, 60)
            if num not in lista:
                lista.append(num)
                break
    lista.sort()
    temp.append(lista[:])
    lista.clear()
print(f' SORTEANDO {jogos} JOGOS '.center(35, '='))
while cont != len(temp):
    print(f'Jogo {cont+1}: {temp[cont]}  ')
    sleep(1)
    cont +=1
print(' <BOA SORTE> '.center(35, '='))