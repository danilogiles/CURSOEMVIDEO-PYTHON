def leiaint(x):
    while True:
        if x not in '0123456789' or x == '':
            print("\033[031m Erro! Digite um numero inteiro \033[m")
            x = input("Digite um numero: ")
        else:
            break
    return x

#Programa principal
n = leiaint(input('Digite um numero: '))
print('-' * 40)
print(f"Voce acabou de digitar o numero {n}".center(40))
print('-' * 40)
print("FIM".center(40, '-'))