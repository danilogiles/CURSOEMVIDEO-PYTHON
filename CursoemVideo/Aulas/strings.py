'''
Fatiamento e transformacao de string
'''
frase='Curso em video Python'
Texto='''Usando 3 aspas vc pode digitar um
        texto em quantas linhas quiser.'''
print(frase)
print(len(frase))#conta o tamanho da string
print(frase.count('o'))#conta o numero de caracteres 'o' dentro da string
print(frase.count('o',0,13))#mesma coisa do anterior, so que conta da posicao 0 ate a posicao 13
print(frase[9:21:2])#pega do caracter 9 vai ate o 21 pulando de 2 em 2
print(frase[:5])#quando nao tem inicio setado ele vai sempre comecar da posicao 0
print(frase[15:])#quando nao tem fim setado ele vai ate o ultimo caracter
print(frase[9::3])#vai da posicao setada ate o fim pulando de 3 em 3
print(frase.find('deo'))#indica a posicao onde comeca deo na string
print(frase.find('naoexiste'))#se o texto nao existir na string ele retorna o valor -1
print('Curso' in frase)# o comando in trara um valor boleano se existe ou nao o procurado na frase(case sensitive)
print(frase.replace('Python','Android'))#busca e substitui uma palavra na string
print(frase.upper())#transforma a string em maiuscula
print(frase.lower())#transforma a string em minuscula
print(frase.capitalize())#coloca todos os caracteres minusculo e a primeira letra para maiusculo
print(frase.title())#analisa quantas palavras tem na string e coloca todas a primeiras letras de cada palavra maiuscula
print(frase.strip())# remove blank spaces do comeco e do fim da string
print(frase.rstrip())#remove blank spaces do lado direito da string
print(frase.lstrip())#remove blank spaces do lado esquerdo da string
print('-'.join(frase))#adiciona caracter entre os existentes
print(frase.split())#Divide uma string em lista e cada palavra vai ser separada com seus proprios indexes
palavra=(frase.split())#colocar a lista de palavras da string na variavel
print(palavra[0])#pega a primeira palavra da lista
print(palavra[0][4])#mostra a 4 letra da primeira palavra

#tuplas, use () na string, nao e necessario em python mais novo mas use por fins didaticos
#Tuplas sao imutaveis
#ex. lanche[1]='refrigerante vai dar um erro de que a tuple nao pode receber valore
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[2])#mostra a tupla inteira
print(lanche[-2])#conta de tras pra frente
print(lanche[1:3])#mostra do 1 ao 2 desconsiderando o ultimo elemento 3 no caso
print(lanche[1:])# se nao tive nada depois dos : ele vai ate o final
print(lanche[:2])#mostra do inicio ate o elemento 1 ignorou o ultimo elemento 2
print(lanche[-3:])#varre de tras pra frente comecando do 3
print(sorted(lanche))#mostra a lista em ordem alfabetica

#Usando mais de uma tupla
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # adiciona um valor apos o outro
print(c)
print(c.count(5))#mostra quantas vezes o numero aparece na variavel
print(c.index(8))#mostra em que posicao a primeira ocorrencia do numero esta
pessoa = ('Danilo', 38, 'M', 99.8)#tuplas podem receber multiplos dados
del (pessoa) #deleta a tupla, so pode ser deletada por completa, nao e possivel deletar o conteudo