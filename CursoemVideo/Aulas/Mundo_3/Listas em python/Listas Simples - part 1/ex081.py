lista = []
posicao = []
digitados = validacao = 0
escolha = 'A'
while escolha not in 'N':
    lista.append(int(input("Digite um valor: ")))
    digitados += 1
    escolha = 'A'
    while escolha not in 'SN':
        escolha = str(input("Deseja continuar? [S/N]").upper().strip()[0])
        if escolha not in 'SN':
            print("Valor digitado invalido.")
print(f"Voce digitou {digitados} elementos.")
print(f'Os valores em ordem decrescente sao {sorted(lista, reverse=True)}')
for c in range(0, len(lista)):
    if 5 == lista[c]:
        validacao = 1
        posicao.append(c)
if validacao == 1:
    print(f"O valor 5 faz parte da lista! e esta nas posicoes {posicao}")
else:
    print("A Lista nao contem o valor 5.")



