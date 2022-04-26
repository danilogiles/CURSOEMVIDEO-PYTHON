def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[031m Erro! Digite um numero inteiro \033[m")
        if ok:
            break
    return valor


#Programa principal
n = leiaint('Digite um numero: ')
print('-' * 40)
print(f"Voce acabou de digitar o numero {n}".center(35))
print('-' * 40)
