from random import randint
cont = comp = resul = 0
parimpar = escolha = ''
print('-=' * 30)
print('VAMOS JOGAR PAR OU IMPAR?')
print('-=' * 30)
while True:
    num = int(input(f"Digite um valor: "))
    comp = randint(0, 10)
    resul =  comp + num
    escolha = ' '
    while escolha not in 'PI':
        escolha = input("Par ou impar? [P/I] ").strip().upper()[0]
    if resul % 2 == 0:
        if escolha in 'P':
            print('-' * 30)
            print("Voce venceu esta rodada!")
            print('-' * 30)
            parimpar = 'PAR'
            cont += 1
        else:
            break
    else:
        if escolha in 'I':
            print('-' * 30)
            print("Voce venceu esta rodada!")
            print('-' * 30)
            parimpar = "IMPAR"
            cont += 1
        else:
            break
    print(f"Voce jogou {num} e o computador {comp}. Total de {resul} deu {parimpar}")
print('-' * 40)
print("Voce perdeu!")
print('-=' * 20)
print(f"GAME OVER! Voce venceu {cont} vezes.")
print('-=' * 20)

