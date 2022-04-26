from time import sleep
num=int(input('Digite um numero qualquer: '))
print('Pensando no numero...')
sleep(2)
if (num%2) == 1:
    print(f'O numero {num} e impar')
else:
    print(f'O numero {num} e par')