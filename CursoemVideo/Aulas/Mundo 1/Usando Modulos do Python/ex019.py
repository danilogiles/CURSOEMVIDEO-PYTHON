from random import choice
n1=input('Primeiro aluno: ')
n2=input('Segundo aluno: ')
n3=input('Terceito aluno: ')
n4=input('Quarto aluno: ')
lista=[n1,n2,n3,n4]
nomes='joao','jose','maria','pedro'
print(f'O aluno sorteado foi {choice(nomes)}')
print(f'O aluno sorteado foi: {choice(lista)}')
