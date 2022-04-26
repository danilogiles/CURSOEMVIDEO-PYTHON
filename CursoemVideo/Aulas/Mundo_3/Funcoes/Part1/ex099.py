from random import randint
from time import sleep
def linha():
    print('-=' * 30)

def valores(n):
    lista=[]
    linha()
    print("Gerando valores...", end='')
    for c in range(0, n):
        lista.append(randint(0,10))
        sleep(0.5)
        print('.',end='')
    print(f"\nOs valores gerados foram {lista}")
    linha()
    maior(lista)

def maior(*num):
    newlista = []
    total = 0
    print(f"Analisando os valores passados....")
    for k, v in enumerate(num[0]):
        newlista.append(v)
        print(f"{v}", end=' ')
        sleep(0.5)
    print(f"Foram informados {len(newlista)} valores ao todo.")
    maiornum = newlista[0]
    for c in range(0,len(newlista)):
        if maiornum < newlista[c]:
            maiornum = newlista[c]
    sleep(1)
    print(f"O maior numero informado foi {maiornum}.")

#Programa principal
while True:
    resp = int(input("Quantas listas deseja gerar? "))
    contador = 0
    print("comecando a gerar e analisar os valores".upper().center(50,'='))
    while contador < resp:
        numrandom = randint(1, 10)
        valores(numrandom)
        contador += 1
    linha()
    print("programa encerrado com sucesso".upper().center(50, '='))
    break
