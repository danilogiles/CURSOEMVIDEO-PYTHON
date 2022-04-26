from time import sleep
from random import randrange, randint
numr=int(randrange(6))# randomiza o int
numr2=int(randint(0,5))# randomiza o int tambem
print('-=' * 30)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=' * 30)
usernum=int(input('Qual o numero que estou pensando? '))
print('PROCESSANDO...')
sleep(2)
if numr == usernum:
    print(f'Voce acertou o numero {numr} esta correto! voce Venceu!')
else:
    print(f'Voce errou miseravi, o numero correto era {numr}! Voce perdeu :/')
