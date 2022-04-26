# listas
#formas de declarar lista
lista = ['hamburguer', 'pizza', 'batata frita', 'suco']
valores = list(range(0,11))

#comandos que poder ser usados na lista
del.lista[3]#tem que passar a posicao do item
lista.pop(3)# caso nao passe uma posicao ira apagar o ultimo item pelo indice
lista.remove('hamburguer')#tem que passar o valor do item
valores.sort()#coloca em ordem os itens da lista
valores.sort(reverse=True)# ordena os valores na ordem reversa
len(valores)#le o tamanho da lista

num = [2,5,9,1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort(reverse=True)
print(num)
num.insert(2,0)
print(num)
num.insert(2,2)
print(num)
num.pop(2)#remove apenas a primeira ocorrencia do numero
print(num)
if 4 in num: # usar if para que as delecoes nao deem erro
    num.remove(4)
else:
    print('Nao achei o numero 4')

#pedindo para digitar valor e ler a lista
valores = []
for cont in range(0,5):
    valores.append(int(input("Digite um valor: ")))#colocar valor digitado na lista
for c, v in enumerate(valores): # voce esta passando o valores no enumerate por isso nao precisa de valores[c] pra pegar eles so usa c
    print(f"Na posicao {c} encontrei o valor {v}!")
print('Cheguei ao final da lista.')

#ligacao e clonagem de listas
a = [2,3,4,7]
b = a # b = a faz uma ligacao entre as listas, se alterar b, a sera alterado tbm.
c = a[:]# esse metodo cria uma copia da lista utilizando fatiamento
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')

print(lista)
print(valores)