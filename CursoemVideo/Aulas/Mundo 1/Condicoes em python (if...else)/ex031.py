from time import sleep
dist=int(input('Digite a distancia da sua viagem em km:'))
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print('Calculando o valor da passagem...')
sleep(2)
print('-=' * 25)
print(f'O valor da sua passagem sera \033[32mR${preco:.2f}\033[m')
print('-=' * 25)