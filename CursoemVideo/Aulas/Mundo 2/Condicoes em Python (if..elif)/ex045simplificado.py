#Jogo do jokenpo(pedra, papel e tesoura)
import time
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas Opcoes:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador=int(input("Qual e a sua jogada? "))
print('-=' * 20)
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!!!")
print('-=' * 20)
time.sleep(1)
print(f"O computador jogou {itens[computador]}")
print(f"O jogador jogou {itens[jogador]}")
print('-=' * 20)
if computador == 0:
    if jogador == 0:
        print("Esse jogo empatou!")
    elif jogador == 1:
        print("Jogador Vence!")
    elif jogador == 2:
        print("Computador Vence!")
    else:
        print("Jogada invalida")
elif computador == 1:
    if jogador == 0:
        print("Computador Vence!")
    elif jogador == 1:
        print("Esse jogo empatou!")
    elif jogador == 2:
        print("Jogador Vence!")
    else:
        print("Jogada Invalida")
elif computador == 2:
    if jogador == 0:
        print("Jogador Vence!")
    elif jogador == 1:
        print("Computador Vence!")
    elif jogador == 2:
        print("Esse jogo empatou!")
    else:
        print("Jogada Invalida")

