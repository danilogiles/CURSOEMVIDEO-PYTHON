#Mostre na tela todos os numeros pares
#Simplificado
#for c in range(0, 51, 2):
#    print(f"{c}", end=' ')
#print("\nFim")

#Avancado
for c in range(0, 51):
    d=c%2
    if d == 0:
        print(c, end="")
    else:
        print(" | ", end="")
print("\nFIM")