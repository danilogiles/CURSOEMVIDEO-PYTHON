def fatorial(num=1, show=False):
    '''
    -> Calcula o valor fatorial de um numero.
    :param num: O numero a ser caculado
    :param show: Parametro opcional para mostrar ou nao a conta feita
    :return: O valor do Fatorial de um numero n.
    '''
    f = 1
    ctrue = str()
    for c in range(num, 0, -1):
        f *= c
        if c > 1:
            ctrue = ctrue + str(f"{c} x ")
    ctrue = ctrue + str(f"1 = {f}")
    if show == True:
        return ctrue
    else:
        return f

#Programa principal
print('-' * 40)
print(fatorial(5, show=True))
print('-=' * 40)
#help(fatorial)