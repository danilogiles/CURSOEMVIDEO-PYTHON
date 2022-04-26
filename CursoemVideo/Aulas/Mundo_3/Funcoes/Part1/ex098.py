from time import sleep
def linha():
    print('-=' * 50)

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:

    if inicio <= fim and passo >= 0:
        linha()
        print(f"Contagem de {inicio} ate {fim} de {passo} em {passo}")
        sleep(2)
        for count in range(inicio, fim+1, passo):
            print(count, end=" ")
            sleep(0.3)
        print("FIM!")
        linha()
    elif inicio > fim and passo >= 0:
        linha()
        print(f"Contagem de {inicio} ate {fim} de {passo} em {passo}")
        sleep(2)
        passo = passo - passo * 2
        for count in range(inicio, fim-1, passo):
            print(count, end=" ")
            sleep(0.3)
        print("FIM!")
        linha()
    else:
        linha()
        print(f"Contagem de {inicio} ate {fim} de {passo} em {passo}")
        sleep(2)
        for count in range(inicio, fim-1, passo):
            print(count, end=' ')
            sleep(0.3)
        print('FIM!')
        linha()

#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print("Agora e sua vez de personalizar a contagem!")
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i, f, p)




