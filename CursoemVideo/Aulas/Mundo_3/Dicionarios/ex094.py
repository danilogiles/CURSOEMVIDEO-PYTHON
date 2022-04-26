cadastro = []
lista = []
dadostemp = dict()
resp = 'A'
idadetotal = media = count = 0
while True:
    dadostemp['nome'] = str(input("Nome: "))
    dadostemp['idade'] = int(input("Idade: "))
    while True:
        dadostemp['sexo'] = str(input("Sexo: [M/F] ").upper().strip()[0])
        if dadostemp['sexo'] not in 'MF':
            print("ERRO! Por favor, Digite apenas M ou F.")
        else:
            break
    cadastro.append(dadostemp.copy())
    if dadostemp['sexo'] == 'F':
        lista.append(dadostemp['nome'])
    idadetotal += dadostemp['idade']
    dadostemp.clear()
    resp = str(input("Quer continuar? [S/N]")).upper()[0]
    if resp in 'nN':
        break
    elif resp not in 'SsNn':
        print("ERRO! Responda apenas S ou N.")
print(cadastro)
media = idadetotal/len(cadastro)
print(f"A) Ao todo temos {len(cadastro)} pessoas cadastradas.")
print(f"B) A media de idade e de {media:.2f} anos")
print(f"C) As mulheres cadastradas foram : ", end='')
for c in range(0,len(lista)):
    print(lista[c].capitalize(), end=' ')
print("\nD) Lista de pessoas que estao acima da media: ")
for c in cadastro:
    for k, v in c.items():
        if int(cadastro[count]['idade']) >= media:
            print(f"{k} = {v};", end=' ')
    count +=1
print("\n<< ENCERRADO >>")

