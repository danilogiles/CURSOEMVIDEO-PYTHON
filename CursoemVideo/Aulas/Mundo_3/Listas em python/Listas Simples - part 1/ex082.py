lista = []
listapar = []
listaimpar = []
choice = 'A'
while choice not in 'N':
    num = (int(input("type a number: ")))
    lista.append(num)
    choice = 'A'
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    while choice not in 'YN':
        choice = str(input("Continue? [Y/N]: ").upper().strip()[0])
        if choice not in 'YN':
            print("invalid option!")
print(f"Typed numbers are {lista}")
print(f"Even numbers are {listapar}")
print(f"Odd numbers are {listaimpar}")



