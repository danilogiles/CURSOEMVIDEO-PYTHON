num1=int(input('Digite o primeiro numero: '))
num2=int(input('Digite o segundo numero: '))
print('\033[031m-=\033[m' * 30)
if num1 > num2:
    print(f"O primeiro numero {num1} e maior que o segundo numero {num2}.")
elif num1 == num2:
    print(f"O primeiro numero {num1} e o segundo numero {num2} sao iguais")
else:
    print(f"O segundo numero {num2} e maior que o primeiro numero {num1}.")
print('\033[031m-=\033[m' * 30)
