numeros = ('um', 'dois' , 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
escolha = 'A'
while True:
    if escolha == 'N':
        break
    user = int(input("Digite um numero entre 0 e 20: "))
    if user >= 0 and user <= 20:
        print(f"Voce digitou o numero {numeros[user-1]}")
    else:
        print("Numero invalido! \n", end='')
    escolha = 'A'
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar [S/N]: ').upper().strip()[0])
        if escolha == 'N':
            print('FIM DO PROGRAMA')
        elif escolha == 'S':
            print('-=' * 30)
        else:
            print('Escolha invalida!')
