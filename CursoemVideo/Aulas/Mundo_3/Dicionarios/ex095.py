dados = dict()
statitica = []
soma = count = totalgols = 0
resp = 'a'
while True:
    gols = []
    dados['nome'] = str(input("Nome do jogador: "))
    dados['partidas'] = int(input(f"Quantas partidas {dados['nome']} jogou? "))
    for c in range(0,dados['partidas']):
        tmp = int(input(f"   Quantos gols na partida {c+1}?"))
        gols.append(tmp)
        totalgols += tmp
    dados['gols'] = gols[:]
    dados['total'] = totalgols
    statitica.append(dados.copy())
    dados.clear()
    del gols
    totalgols = 0
    resp = str(input("Quer continuar? [S/N]"))
    print('-' * 30)
    if resp not in 'SsNn':
        print("Opcao invalida!")
    elif resp in 'Nn':
        break
print('-=' *30)
print(statitica)
print('-=' * 60)
print('cod'.ljust(4), 'nome'.ljust(15), 'gols'.ljust(15), 'total'.ljust(6))
print('=' * 60)
for c in statitica:
    print(f"{count}".center(5),
          f"{statitica[count]['nome']}".capitalize().ljust(20),
          f"{statitica[count]['gols']}".ljust(20),
          f"{statitica[count]['total']}".ljust(6)
          )
    count += 1
while resp != 999:
    resp = int(input("Mostrar dados de qual jogador?(999 para sair) "))
    if resp == 999:
        break
    elif resp >= len(statitica):
        print(f"ERRO! Nao Existe jogador com o codigo {resp}! Tente Novamente")
    else:
        count = 0
        print(f"-- LEVANTAMENTO DO JOGADOR {statitica[resp]['nome']}")
        for c in statitica[resp]['gols']:
            print(f"   No {count+1}o jogo {statitica[resp]['nome']} fez {statitica[resp]['gols'][count]} gols.")
            count += 1
print('')
print("programa finalizado com sucesso".upper().center(50,'='))

#print(f"O campo gols tem o valor {dados['gols']}")
#print(f"O campo nome tem o valor {dados['nome']}")
#print(f"O campo total tem o valor {dados['partidas']}")
#print('-=' * 30)
#print(f"O jogador {dados['nome']} jogou {dados['partidas']} partidas.")
#for c in range(0,dados['partidas']):
#    print(f"=> Na partida {c+1}, fez {dados['gols'][c]}".center(25))
#    soma += dados['gols'][c]
#dados['total'] = soma
#print("-=" * 30)
#print(f"Foi um total de {dados['total']} gols.")
#print(dados)