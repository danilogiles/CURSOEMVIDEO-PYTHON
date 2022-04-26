somaidade = 0
mediaidade = 0
maioridadehome = 0
nomevelho = ''
totmulher = 0
for pessoa in range (1, 5):
    print(f"--------{pessoa}ª PESSOA ---------")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if pessoa == 1 and sexo in 'Mm':
        maioridadehome = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehome:
        maioridadehome = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4
print(f"A media de idade do grupo e de {mediaidade}")
print(f"O homem mais velho do grupo se chama {nomevelho} e tem {maioridadehome}")
print(f"Ao todo sao {totmulher} com menos de 20 anos.")