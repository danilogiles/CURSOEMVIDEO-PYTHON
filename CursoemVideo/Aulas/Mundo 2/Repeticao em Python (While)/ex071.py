print("="*40)
print("Banco giles".upper().center(35))
print("="*40)
valor=int(input("Qual o valor que deseja sacar? R$"))
cont50 = cont20 = cont10 = cont1 = 0
sobradivisao = 1
while True:
    if valor >= 50:
        cont50 += 1
        valor -= 50
    elif valor >= 20:
        cont20 += 1
        valor -= 20
    elif valor >= 10:
        cont10 += 1
        valor -= 10
    elif valor >= 1:
        cont1 +=1
        valor -= 1
    else:
        break
if cont50 > 0:
    print(f"Total de {cont50} cedulas de R$50")
if cont20 > 0:
    print(f"Total de {cont20} cedulas de R$20")
if cont10 > 0:
    print(f"Total de {cont10} cedulas de R$10")
if cont1 > 0:
    print(f"Total de {cont1} cedulas de R$1")
print("=" * 40)
print("Volte sempre ao BANCO GILES! Tenha um bom dia!")