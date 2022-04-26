num=int(input("type a number: "))
c = num
fat = ''
tot = 1
while c != 0:
    fat = fat+(f'{c} ')
    tot = tot * c
    c -= 1
print(f"{num}!={fat.strip().replace(' ',' x ')}={tot}")

'''#using the factorial on the math library
from math import factorial
n = int(input("Digite o numero que deseja calcular o fatorial: "))
f = factorial(n)
print(f"O fatorial de {n} e {f}.")
'''
