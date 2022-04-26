nome = list()
notas = list()
nota1 = []
nota2 = []
cadastro = list()
media = []
print('=' * 40)
print('Cadastre o aluno e as notas'.upper().center(40, '='))
print('=' * 40)
while True:
    nome.append(str(input("Nome: ").capitalize()))
    nota1.append(float(input("Nota 1: ")))
    nota2.append(float(input("Nota 2: ")))
    resp = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]
    if resp not in 'SN':
        print('Voce digitou uma opcao invalida!')
    if resp in 'N':
        break
for c in range(0, len(nota1)):
    media.append((nota1[c]+nota2[c])/2)
notas.append(nota1[:])
notas.append(nota2[:])
notas.append(media[:])
cadastro.append(nome)
cadastro.append(notas)
print('-=' * 30)
print("No.".ljust(5), "Nome".ljust(15), 'Media'.center(2))
print('-' * 30)
for c in range(0, len(nota1)):
    n = cadastro[0][c]
    m = cadastro[1][2][c]
    count = c
    print(f"{c}".ljust(5), f'{n}'.ljust(15), f'{m}'.center(7))
print('-' * 30)
resp = int(0)
while True:
    resp = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if resp == 999:
        break
    print(f"As notas de {cadastro[0][resp]} sao [{cadastro[1][0][resp]}, {cadastro[1][1][resp]}]")

#Solucao Guanabara
ficha = lista
while true:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([[nome], [[nota1], [nota2], [media]]])
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    :if resp in 'Nn'
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
print('-=' * 30)
for i, a in enumerate(ficha):
    print(f'{i:4<}{a[0]<10}{a[2]:>8.1f}')
while True:
    print('_' * 35)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        print("Finalizando...")
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')
print("volte sempre".upper().center(30,'='))




'''