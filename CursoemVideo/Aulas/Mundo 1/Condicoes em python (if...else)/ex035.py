
print('-=' * 20)
print('Analisador de triangulos')
print('-=' * 20)
r1=float(input('Digite o valor da primeira reta: '))
r2=float(input('Digite o valor da segunda reta: '))
r3=float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('E possivel criar um triangulo')
else:
    print('Nao e possivel criar um triangulo')
