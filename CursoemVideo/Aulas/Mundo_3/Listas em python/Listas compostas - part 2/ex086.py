#monta uma matriz apos 9 numeros digitados
matriz = list()
temp = list()
print('-=' * 40)
for c in range(0,3):
    for d in range(0,3):
        num = int(input(f"Digite um valor para [{c}, {d}]: "))
        temp.append(num)
    matriz.append(temp[:])
    temp.clear()
print('-=' * 40)
for c in range(0,3):
    for d in range(0,3):
        print(f"[{matriz[c][d]}]".center(10),end='')
    print(' ')

#solucao guanabara
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para {[l], [c]}: "))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()