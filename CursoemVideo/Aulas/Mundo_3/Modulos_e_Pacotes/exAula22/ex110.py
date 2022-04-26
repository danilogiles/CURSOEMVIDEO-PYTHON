from moeda import dobro, metade, aumentar, diminuir

#funcao criada no ex110
def resumo(n, aumento, reducao):
    valor = n
    if type(valor) == float:
        print('-' * 30)
        print('RESUMO DO VALOR'.center(30))
        print('-' * 30)
        print(f"Preco analisado:    R${valor:.2f}")
        print(f"Dobro do preco:     R${dobro(valor):.2f}")
        print(f"Metade do preco:    R${metade(valor):.2f}")
        print(f"80% de aumento:     R${aumentar(n, aumento):.2f}")
        print(f"35% de reducao:     R${diminuir(valor, reducao):.2f}")
    if type(valor) not in float:
        print("Erro!")


