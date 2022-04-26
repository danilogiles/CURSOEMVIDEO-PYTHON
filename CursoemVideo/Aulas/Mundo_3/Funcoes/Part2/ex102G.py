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
        if show:
            print(c, end = '')
            if c > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
        f *= c
    return f

#Programa principal
print('-=' * 30)
print(fatorial(5, show=True))
print('-=' * 30)
#help(fatorial)