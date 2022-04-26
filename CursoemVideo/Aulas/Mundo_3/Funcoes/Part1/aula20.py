#Funcoes part 1

#Criando a funcao basica pra exibir linha
def lin():
    print('-' * 30)

#Programa principal
lin()
print('  Curso em video  ')
lin()

#Funcao passando um parametro
def titulo(msg):
    print('-' * 30)
    print(f"{msg}".center(30).upper())
    print('-' * 30)

titulo('Sistema de alunos')
titulo('Aprenda Python')

#funcao de soma passando dois parametros
def somabasica(a, b):
    s = a + b
    print(s)

#programa principal
somabasica(3, 5)
somabasica(b=8, a=9)# valores podem ser setados na passagem de parametro

#Desmpacotar parametros, ele cria uma tupla e joga os valores dentro
def contador(*num):
    tam = len(num)
    for valor in num:
        print(f"{valor }", end='')
    print('recebi os valores {num} e os valores sao {tam} numeros:')
#programa principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

#funcao usando lista:
def dobra(lst):
    pos=0
    while pos< len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

