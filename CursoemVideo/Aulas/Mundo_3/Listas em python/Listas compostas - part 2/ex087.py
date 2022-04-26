#monta uma matriz apos 9 numeros digitados
matriz = list()
dados = list()
numpar = soma = maior = 0
print('-=' * 40)
for c in range(0,3):
    for d in range(0,3):
        num = int(input(f"Digite um valor para [{c}, {d}]: "))
        if num % 2 == 0:
            numpar += num
        dados.append(num)
    matriz.append(dados[:])
    dados.clear()
print('-=' * 40)
for c in range(0,3):
    for d in range(0,3):
        print(f"[{matriz[c][d]:^5}]",end='')
        if d == 2:
            soma += matriz[c][d]
        if maior < matriz[1][d]:
            maior = matriz[1][d]
    print(' ')
print('-=' * 40)
print(f'A soma dos numeros pares e {numpar}')
print(f'A soma dos valores da terceira coluna e {soma}')
print(f'O maior valor da segunda linha e {maior}')
