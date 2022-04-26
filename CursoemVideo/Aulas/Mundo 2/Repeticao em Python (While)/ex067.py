resul = cont =  0
while True:
    num = int(input("Quer ver qual tabuada? "))
    print("=" * 30)
    mult = 1
    if num <= 0:
        break
    while True:
        resul = num * mult
        print(f"{num} X {mult} = {resul}")
        if mult == 10:
            break
        mult += 1
    print("=" * 30)
print("Muito Obrigado por usar o tabuator! volte sempre!")

