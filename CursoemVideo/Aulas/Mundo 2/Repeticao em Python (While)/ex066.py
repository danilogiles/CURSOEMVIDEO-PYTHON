cont = soma = 0
while True:
    n = int(input("Digite um numero (999 para parar):"))
    if n == 999:
        break
    soma += n
    cont += 1
print(f"{cont} numeros foram digitados e a sua soma deles e {soma}.")

