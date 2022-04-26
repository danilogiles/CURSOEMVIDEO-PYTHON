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

#printa o que tme na variavel lanche usando for
lanche = ('Hamburgue', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for c in lanche:
    print(c)

#printa usando o for e ponto de parada o len da tupla
lanche = ('Hamburgue', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posicao {[cont]}")
print('Comi demais!')

#Print usando enumerate
for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posicao {pos}")
#Usando mais de uma tupla
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # adiciona um valor apos o outro
print(c)
print(c.count(5))#mostra quantas vezes o numero aparece na variavel
print(c.index(8))#mostra em que posicao a primeira ocorrencia do numero esta
pessoa = ('Danilo', 38, 'M', 99.8)#tuplas podem receber multiplos dados
del (pessoa) #deleta a tupla, so pode ser deletada por completa, nao e possivel deletar o conteudo
