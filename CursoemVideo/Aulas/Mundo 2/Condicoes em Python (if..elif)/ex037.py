cores={'end':'\033[m',
       'red':'\033[031m',
       'green':'\033[032m',
       'yellow':'\033[032m',
       'blue':'\033[034m',
       'purple':'\033[035m',
       'cyan':'\033[036m',
       'gray':'\033[037m'
       }
num=int(input(f"Digite o numero que deseja converter: "))
opcao=int(input('Escolha a opcao no menu abaixo:\n'
                '[1] Binario\n'
                '[2] Octal \n'
                '[3] Hexadecimal \n'
                'Sua Opcao: '))
if opcao == 1:
       print(f"O numero {num} na base binaria e igual a {bin(num)[2:]}")
elif opcao == 2:
       print(f"O numero {num} na base octal e igual a {oct(num)[2:]}")
elif opcao == 3:
       print(f"O numero {num} na base hexadecimal e igual a {hex(num)[2:]}")
else:
    print("\033[31mOpcao invalida, tente novamente!\033[m")