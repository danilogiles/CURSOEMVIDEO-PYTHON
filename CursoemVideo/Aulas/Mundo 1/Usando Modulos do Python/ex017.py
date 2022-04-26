from math import hypot

cat_o=float(input('Digite o valor do cateto oposto: '))
cat_a=float(input('Digite o valor da cateto adjacente: '))
hi=(cat_o ** 2 + cat_a ** 2) ** (1/2)
hipo=hypot(cat_o,cat_a)
print(f'A hipotenusa e igual a {hi:.2f}')
print(f"O comprimento da hipotenusa eh {hipo:.2f}")