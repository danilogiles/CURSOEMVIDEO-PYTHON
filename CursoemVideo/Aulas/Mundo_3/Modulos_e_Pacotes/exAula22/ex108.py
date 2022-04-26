def aumentar(n):
    p = n * 10 / 100
    n = f'R$ {n + p}
    return n

def diminuir(n):
    p = n * 13 / 100
    n = n - p
    return f'R${n}

def dobro(n):
    return n * 2

def metade(n):
    return n / 2