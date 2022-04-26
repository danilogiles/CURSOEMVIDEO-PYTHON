#Jogo do jokenpo(pedra, papel e tesoura)
import random
import time
#menu do jogo
barmenu=('-=' * 20)
print(f"{barmenu}")
j1=int(input(f"Suas Opcoes: \n"
      f"[ 1 ] Pedra\n"
      f"[ 2 ] Tesoura \n"
      f"[ 3 ] Papel\n"
      f"Qual a sua jogada? "))
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!!!")
time.sleep(1)
print(barmenu)
#Escolha do computador randomica e conversao dos numeros para string
comp=random.randint(1,3)
if comp == 1:
    escomp=str("Pedra")
elif comp == 2:
    escomp=str("Tesoura")
else:
    escomp=str("Papel")
#Conversao Jogador
if j1 == 1:
    escj = "Pedra"
elif j1 == 2:
    escj = "Tesoura"
elif j1 == 3:
    escj = "Papel"
# Jogo
print(f"O Computador escolheu {escomp}.")
print(f"O Jogador escolheu {escj}")
print(barmenu)
if comp == j1:
    print(f"Esse jogo empatou!")
elif (comp == 3 and j1 == 1) or (comp == 2 and j1 == 3) or (comp == 1 and j1 == 2):
    print(f"O Computador Venceu!")
else:
    print(f"Parabens voce Venceu!")
