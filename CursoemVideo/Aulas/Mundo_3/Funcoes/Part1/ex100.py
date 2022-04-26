from random import randint
from time import sleep
#FUNCOES
def sorteia():
    numeros = list()
    print('Sorteando os numeros da lista:', end=' ')
    for c in range(0,5):
        numeros.append(randint(1, 10))
        print(numeros[c],end=' ', flush=True)
        sleep(0.3)
    print("PRONTO!")
    somapar(numeros)

def somapar(lista):
    soma = 0
    print(f"Somando os valores pares de {lista}, temos", end=' ')
    for c in range(0, len(lista)):
        if lista[c] % 2 == 0:
            soma += lista[c]
    print(soma)

#PROGRAMA PRINCIPAL
sorteia()
