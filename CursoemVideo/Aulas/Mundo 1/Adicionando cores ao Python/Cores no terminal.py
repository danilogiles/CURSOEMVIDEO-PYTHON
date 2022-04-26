"""
A Sintaxe para adicionar cores a um texto e \033[style:text:background m]
onde:
Style           Text        Background
0 none          30 white    40 white
1 Bold          31 red      41 red
4 underline     32 green    42 green
7 negative      33 yellow   43 yellow
                34 Blue     44 Blue
                35 Purple   45 Purple
                36 Cyan     46 Cyan
                37 gray     47 gray
"""
nome='Danilo'
# Usando modo hardcore
print('\033[01;31m Ola mundo!\033[m')
print('\033[7:44m Ola mundo!\033[m')
#Usando variaveis
corred='\033[01;31m'
corgreen='\033[32m'
endcor='\033[m'
print(f' Ola e um prazer te conhecer, {corred}{nome}{endcor}')
print(f'{corgreen}{nome}{endcor}')
#Usando dicionario "lista" de cores
cores={'limpa':'\033[m',
       'red':'\033[31m',
       'green':'\033[32m',
       'yellow':'\033[33m',
       'blue':'\033[34m',
       'pb':'\033[7;40m'
       }
print(f" Ola {cores['pb']}{nome}{cores['limpa']}")