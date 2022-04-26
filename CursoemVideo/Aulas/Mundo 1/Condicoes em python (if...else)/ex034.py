sal=float(input('Digite o salario do funcionario: '))
if sal >= 1250.00:
    newsal=sal+((sal*10)/100)
else:
    newsal=sal+((sal*15)/100)
print(f'O salario de \033[31mR${sal:.2f}\033[m foi aumentado para \033[32mR${newsal:.2f}\033[m')


