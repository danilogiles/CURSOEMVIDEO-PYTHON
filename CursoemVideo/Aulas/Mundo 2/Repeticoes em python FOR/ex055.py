# le o peso de 5 pessoas e mostra no final qual foi o maior e o menor
import random
import time

peso=float(0.0)
pessoa=[]
peso = [0, 0, 0, 0, 0]
maior=float(0)
menor=float(0)
t=0
for c in range(1, 6):
    pr = float(input(f"Digite o peso da {c} pessoa: "))
    #pr=random.randint(60, 100)
    peso[c-1]=pr
    if c == 1:
        maior = pr
        menor = pr
    else:
        for i in range(1, 6):
            if peso[c-1] > maior:
                maior=peso[c-1]
            elif peso[c-1] < menor:
                menor=peso[c-1]
            else:
                nada=0
print("Calculando resultados...")
time.sleep(2)
print("-=" * 30)
print(f"A pessoa de maior peso tem {maior:.1f}Kg.")
print(f"A pessoa de menor peso tem {menor:.1f}Kg.")
print("-=" * 30)
