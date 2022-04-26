#dicionarios
# criando dicionario
dados = dict()# usando o metodo de criacao de lista
dados = {'nome': 'Pedro', 'idade':25}
print(dados['nome'])#imprime somente nome
print(dados['idade'])#imprime somente idade
dados['Sexo']='M'# Adiciona elemento ao dicionario
del dados['idade'] #Deleta o elemento idade

# importante os itens da lista estarem entre {}
filme = {'Titulo':'Star Wars',
         'Ano':1977,
         'Director':'George Lucas'
         }
print(filme.values())# print the inside value i.e Star Wars
print(filme.keys())#print the keys (Titulo, ano, diretor)
print(filme.items())#imprime values e keys
for k v in filme.items():
    print(f"O {k} e {v}")

pessoas = {'nome': 'Danilo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k,v in pessoas.items():
    print(f'{k} = {v}')
del pessoas['sexo'] # Apaga o elemento sexo
for k, v in pessoas.items():
    print(f'{k.upper()} = {v}')
pessoas['nome'] = 'Leandro' #troca o nome da lista
pessoas['peso'] = 85 #Adiciona um elemento
for k, v in pessoas.items():
    print(f'{k.upper()} = {v}')

#printando listas e dicionarios
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1) # printa dicionario estado1
print(estado2) # printa dicionario estado2
print(brasil) # printa lista com os dicionarios dentro
print(brasil[0]) #printa a lista com o dicionario na posicao 0
print(brasil[1]) #printa a lista com o dicionario na posicao 1
print(brasil[0]['uf']) #printa uf do dicionario estado 1 na lista brasil
print(brasil[1]['sigla']) #printa sigla do dicionario estado 2 na lista brasil

estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy()) # Utilize o metodo .copy() quando copiando um dicionario
for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}.")
    for v in e.values():
        print(v, end=' ')
    print()

#ordenar uma lista usando itemgetter
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
