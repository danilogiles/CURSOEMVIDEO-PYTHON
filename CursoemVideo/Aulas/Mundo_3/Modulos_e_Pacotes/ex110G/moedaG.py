def aumentar(preco=0, taxa=0, formatado=False):
    res = preco + (preco * taxa / 100)
    return res if formatado is False else moeda(res)

def diminuir(preco=0, taxa=0, formatado=False):
    res = preco - (preco * taxa / 100)
    return res if formatado is False else moeda(res)

def dobro(preco=0, formatado=False):
    res = preco * 2
    return res if formatado is False else moeda(res)

def metade(preco=0, formatado=False):
    res = preco / 2
    return res if formatado is False else moeda(res)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.',',')

def resumo(preco=0, taxa=10, reducao=5):
    print("-" * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f"O Preco analizado: \t{moeda(preco)}")
    print(f"O Dobro do preco: \t{dobro(preco, True)}")
    print(f"A metade do prec: \t{metade(preco, True)}")
    print(f"{taxa}% de aumento: \t{aumentar(preco, taxa, True)}")
    print(f"{reducao}% de reducao: \t\t{diminuir(preco, reducao, True)}")