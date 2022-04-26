from time import sleep
vel=float(input('Digite a velocidade do carro: '))
print('Calculando a velocidade...')
sleep(2)
if vel <= 80:
    print('-='*15)
    print('\033[4:32m Parabens por respeitar a velocidade de transito!\033[m')
    print('-='*15)
else:
    print('-='*15)
    print(f'Voce ultrapassou o limite permitido de \033[31m 80km\033[m e foi \033[31m Multado. \033[m \n'
          f'O valor da sua multa e de \033[31m R${(vel-80)*7:.2f} \033[m')
    print('-='*15)