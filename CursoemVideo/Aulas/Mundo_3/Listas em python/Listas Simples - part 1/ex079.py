lista = []
escolha = 'A'
while True:
    num = int(input("Digite um valor: "))
    if num in lista:
        print(f"O numero {num} ja existe e nao sera adicionado!")
    else:
        lista.append(num)
        print(f"Numero {num} foi adicionado a lista.")
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]
        if escolha not in 'SN':
            print("Voce digitou uma opcao invalida.")
    if escolha == 'N':
        break
print(f"Voce digitou os valores {sorted(lista)}")

