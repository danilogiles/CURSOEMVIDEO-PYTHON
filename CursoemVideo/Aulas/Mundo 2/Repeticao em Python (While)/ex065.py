resp = 'S'
soma = quant = media =  maior = menor = 0
while resp in 'Ss':
    num = int(input("Digite um numero:"))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp= str(input("Deseja continuar [S/N]: "))
media = soma / quant
print(f"{quant} numeros fora digitados")
print(f"A media dos numeros digitados e igual a {media:.2f}")
print(f"O maior numero digitado e {maior} e o menor numero digitado e {menor}")
