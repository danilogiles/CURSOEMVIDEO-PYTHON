num1=int(input('Digite o primeiro numero: '))
num2=int(input('Digite o segundo numero: '))
num3=int(input('Digite o terceiro numero: '))
#testa quem e o maior numero
if num1 > num2 and num1 > num3:
    maior=num1
elif num2 > num1 and num2 > num3:
    maior=num2
else:
    maior=num3
#testa o menor numero
if num1 < num2 and num1 < num2:
    menor=num1
elif num2 < num1 and num2 < num3:
    menor=num2
else:
    menor=3
print(f'O maior numero e {maior}')
print(f'O menor numero e {menor}')