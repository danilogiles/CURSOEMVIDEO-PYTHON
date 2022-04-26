idade = contidade = contsexo =contmul = 0
sexo = continuar = ''
print("-" * 40)
print("Cadastre uma pessoa".upper().center(35, '-'))
print("-" * 40)
while True:
    sexo = 'x'
    idade = int(input("Idade: "))
    if idade >= 18:
        contidade += 1
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
        if sexo in 'Mm':
            contsexo += 1
        if sexo in 'Ff' and idade <= 20:
            contmul += 1
    print("-" * 40)
    continuar = input("Deseja continuar? [S/N] ")
    print("-" * 40)
    if continuar in 'Nn':
        break
print("Fim do programa".upper().center(40))
print(f"Total de pessoa com mais de 18 anos e de {contidade}.")
print(f"Ao todo temos {contsexo} homens cadastrados.")
print(f"Temos {contmul} mulher com menos de 20 anos.")
print('=' * 46)
