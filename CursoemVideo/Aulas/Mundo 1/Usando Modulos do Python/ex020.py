import random
n1=str(input('Primeiro aluno: '))
n2=str(input('Segundo aluno: '))
n3=str(input('Terceiro aluno: '))
n4=str(input('Quarto aluno: '))
nomes='joao','maria','jose','paulo','judas','samara'
lista=[n1,n2,n3,n4]
random.shuffle(lista)
print(f'A sequencia e : {lista}')
print(f'A sequencia de apresentacao do trabalho sera: \n {random.sample(nomes,6)}')
print(f'A sequencia de apresentacao e: \n{random.sample(lista,4)}')