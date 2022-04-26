from random import randint
from time import sleep
from operator import itemgetter
valores = {}
for c in range(1,5):
    valores[f'jogador {c}'] = randint(1, 6)
print("JOGADAS".center(40, '='))
for k, v in valores.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
print('-=' * 30)
ranking = dict()
ranking = sorted(valores.items(), key=itemgetter(1), reverse = True) #itemgetter possibilita pegar o item do dicionario e converte ele em lista
print("RANKING DOS JOGADORES".center(40, '='))
for i, v in enumerate(ranking):
    print(f"{i+1}o lugar: {v[0]} com {v[1]}.")
    sleep(1)
