#Calcula a soma dos numeros impares multiplos de 2, vai de 1 a 500
#contador e acumulador
num=0
cont=0
for c in range(1, 501, 2):
    if (c%3) == 0:
       num += c
       cont += 1
       #print(f'{num}')
print(f"A soma de todos os {cont} valores solicitados e igual a {num}")