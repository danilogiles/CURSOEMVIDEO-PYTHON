#listas compostas
dados = ['Pedro',19]
pessoas = dados [:] #adiciona a copia de uma lista dentro de outra lista
print(pessoas)
pessoas = [['Pedro',25],['Maria', 19],['Joao', 32]]#Exemplo de lista dentro de lista
print(pessoas)
print(pessoas[0][0])#Printa alista 0 (Pedro,25) na posicao zero da sublista (Pedro)
print(pessoas[1][1])#Printa a lista 1 (Maria, 19) an posicao 1 da sublista (19)
print(pessoas[2][0])#Printa a lista 2 (joao, 32) na posicao 0 da sublista (Joao)
print(pessoas[1])#printa a sublista inteira com aspas inclusive ('Maria','19')

#exemplo de uso de copia de lista
#caso na hora de copiar vc nao coloque [:] ele vai linkar as listas ao inves de copiar
teste = list()
teste.append('Danilo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

#looping na lista
galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 15], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

#looping na lista para um cadastro simples
galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

#looping na lista para um cadastro simples mostrando quem e maior e menor
galera = list()
dado = list()
totmai = totmen = 0
#Esse bloco adiciona os dados em dados, copia pra galera e limpa dados pra o proximo looping
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
#Esse bloco trata os dados para saber quem e maior e menor
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} e maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} e menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
