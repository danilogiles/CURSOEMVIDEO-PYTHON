def ficha(jogos = '', gol = 0):
    name = jogos
    golos = gol
    if name == '':
        name = '<desconhecido>'
    if golos == '':
        golos = 0
    print(f"O jogador {name} fez {golos} gol(s) no campeonato.")

#Programa Principal
n = str(input("Nome do jogador: "))
g = str(input("Numero de gols: "))
resultado = ficha(n, g)

