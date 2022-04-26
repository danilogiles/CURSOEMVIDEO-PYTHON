#Define se o numero e primo ou nao
num = int(input("Digite um numero: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f"\033[33m", end ='')
        tot = tot + 1
    else:
        print(f"\033[31m", end = '')
    print(f"{c}", end = ' ')
print(f"\n\033[mO numero {num} foi divisivel {tot} vezes ")
if tot == 2:
    print("E por isso ele e primo!")
else:
    print("E por isso ele \033[31mNAO\033[m e primo!")