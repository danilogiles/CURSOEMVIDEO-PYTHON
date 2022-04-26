#Le nome, idade e sexo de 4 pessoas e diga: idade media do grupo, o nome do homem mais velho e quantas mulheres tem menos de 20 anos.
#utilizando listas
nlist=[]
ilist=[]
slist=[]
mvidade=0
mvnome=""
media=int(0)
xc=0
for c1 in range(0, 4):
    print(f"--------{c1}ª Pessoa---------")
    nlist.append(str(input("Digite o nome: ")).strip())
    ilist.append(int(input("Digite a idade: ")))
    slist.append(str(input("Sexo [M/F]: ")).upper().strip())
    print(nlist, ilist, slist)
#Calcula a media de idade do grupo
for c2 in range (0, len(ilist)):
    media=(media + ilist[c2])
#Calcula qual e o mais velho
for c3 in range (0, len(nlist)):
    if slist[c3] == 'M' and ilist[c3] > mvidade:
        mvidade = ilist[c3]
        mvnome = nlist[c3]
        print(f"{mvidade} {mvnome}")
    else:
        hmvx=0
#Calcula o numero de mulheres no grupo com menos de 20 anos
for c4 in range (0, len(ilist)):
    if slist[c4] in 'Ff' and ilist[c4] < 20:
        xc = xc + 1
print('-=' * 30)
print(f"A Media de idade do grupo e de {media/c2:.0f}")
if hmvx != 0:
    print("Nao existem homens nesse grupo")
else:
    print(f"O Homem mais velho do grupo e {mvnome} com {mvidade}. ")
print(f"Existem {xc} mulheres nesse grupo com menos de 20 anos de idade.")
print('-=' * 30)

