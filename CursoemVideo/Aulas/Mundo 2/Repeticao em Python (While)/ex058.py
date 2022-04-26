from time import sleep
from random import randrange, randint
n = 0
count = 0
acertou = False
print('-=' * 30)
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
print('-=' * 30)
numr = int(randint(0, 10))  # randomiza o int tambem
while not acertou:
    usernum = int(input('Qual o numero que estou pensando? '))
    if usernum in range(0,11):
        if numr == usernum:
            print(f'Voce acertou na {count+1}ª tentativa(s), Parabens!')
            numr = True
        else:
            if numr < usernum:
                print("Menos... Tente outra vez.")
                count += 1
            else:
                print("Mais... Tente outra vez.")
                count += 1
    else:
        print('O numero digitado e invalido.')
