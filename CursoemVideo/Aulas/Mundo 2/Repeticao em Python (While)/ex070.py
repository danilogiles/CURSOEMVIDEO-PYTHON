preco = total = somaprod = barato = 0
produto = prodmenor = ' '
print("-" * 40)
print("LOJAS GILES".center(35))
print("-" * 40)
while True:
    produto = str(input("Digite o nome do produto: "))
    preco = float(input("Preco: R$"))
    total += preco
    if preco > 1000:
        somaprod += 1
    elif barato == 0:
        barato = preco
    else:
        if barato > preco:
            barato = preco
            prodmenor = produto
    escolha = " "
    while escolha not in 'SsNn':
        escolha = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]
    if escolha in 'Nn':
        break
print("Fim do programa".upper().center(40,'-') )
print(f"O total de sua compra foi de R${total:.2f}")
print(f"Temos {somaprod} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi o {prodmenor} e custou R${barato:.2f}")
