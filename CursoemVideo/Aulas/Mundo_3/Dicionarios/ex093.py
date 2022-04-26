dados = dict()
gols = []
soma = 0
dados['nome'] = str(input("Nome do jogador: "))
dados['partidas'] = int(input(f"Quantas partidas {dados['nome']} jogou? "))
for c in range(0,dados['partidas']):
    tmp = int(input(f"Quantos gols na partida {c+1}?"))
    gols.append(tmp)
dados['gols'] = gols[:]
for c in range(0,dados['partidas']):
    soma += dados['gols'][c]
dados['total'] = soma
print('-=' *30)
print(dados)
print('-=' * 30)
print(f"O campo nome tem o valor {dados['nome']}")
print(f"O campo gols tem o valor {dados['gols']}")
print(f"O campo total tem o valor {dados['total']}")
print('-=' * 30)
print(f"O jogador {dados['nome']} jogou {dados['partidas']} partidas.")
for c in range(0,dados['partidas']):
    print(f"=> Na partida {c+1}, fez {dados['gols'][c]}".center(25))
#    soma += dados['gols'][c]
#dados['total'] = soma
print("-=" * 30)
print(f"Foi um total de {dados['total']} gols.")
print("-=" * 30)