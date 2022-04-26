#Interactive Help (ajuda interativa)
#use help() no console pra chamar a funcao de ajuda ou digitar o nome da funcao que deseja entre ()
help(print)
#pode se usar o doc tbm dando um print(<funcao>.__doc__)
print(print.__doc__)

#DOCSTRING - Documentacao da funcao que vc cria
#Para cria uma doc string basta colocar """ na primeira linha da funcao
def contador(i, f, p):  # funcao criada para chamar no help()
    """
    -> Faz uma contagem de mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """#fim da docstring
    c = 1
    while c <= f:
        print(f"{c}", end='.. ')
        c += p
    print('FIM!')
help(contador)

#PARAMETROS OPCIONAIS
#na funcao vc pode colocar a variavel = valoropcional em caso nenhum valor seja passado
def somar(a=0,b=0,c=0): #colocando =0 diz que caso nao receba nenhum valor ele passa 0
    s=a+b+c
    print(f"A soma vale {s}")
somar(c=2,a=4)
somar(3,5,4)

#ESCOPO DE VARIAVEIS
#E onde a variavel vai e nao vai existir
def teste():
    x=8 #x esta dentro da funcao e por tanto e uma variavel local
    print(f"Na funcao teste, n vale {n}")
    print(f"Na funcao teste, x vale {x}")

#Programa Principal
n=2 #n esta no programa principal e portanto e uma variavel global
print(f"Na funcao teste, n vale {n}")
teste()
print(f"Na funcao teste, x vale {x}")# esse x vai dar erro porque a variavel x so existe dentro da funcao

#para usar uma variavel global dentro de uma funcao vc deve usar global <variavel>
def teste(b):
    global a #usa a variavel global
    a = 8 #muda a variavel global
    b += 4
    c = 2
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")

a=5
teste(a)
print(f"A fora vale {a}")#imprime a com valor da funcao

#RETURN
#para retornar uma variavel coloque a funcao return <variavel> dentro da funcao
def somar(a=0,b=0,c=0):
    s=a+b+c
    print(f"A soma vale {s}")
    return s #Retorna a variavel s

#para usar o retorno da funcao utilize uma variavel recebendo o seu valor
r1 = somar(3,2,1)
r2 = somar(1,7)
r3 = somar(4)
print(f"Meus calculos deram {r1}, {r2}, {r3}")

#PARTE PRATICA
#Usando uma funcao para calcular o fatorial
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
#programa principal
n = int(input('Digite um numero:'))
print(f"O fatorial de {n} e igual a {fatorial(n):.0f}")

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f"Os resultados sao {f1}, {f2}, {f3}")

#Usando true or false no retorno da funcao
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um numero: '))
if par(num):
    print('E par!')
else:
    print('Nao e par!')




