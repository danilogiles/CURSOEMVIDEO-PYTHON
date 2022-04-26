from datetime import date
cadastro = dict()
ano = date.today().year
cadastro['nome'] = str(input("Nome: "))
cadastro['idade'] = ano - int(input('Ano de nascimento: '))
cadastro['carteira'] = int(input('Carteira de trabalho (0 nao tem): '))
if cadastro['carteira'] != 0:
    cadastro['contratacao'] = int(input("Ano de contratacao: "))
    cadastro['salario'] = float(input("Salario: R$"))
    cadastro['aposentadoria'] = (35 - (ano - cadastro['contratacao'])) + cadastro['idade']
print("-=" * 40)
print(f" - Nome tem o valor {cadastro['nome']}")
print(f" - Idate tem o valor {cadastro['idade']}")
print(f" - CTPS tem o valor {cadastro['carteira']}")
if cadastro['carteira'] != 0:
    print(f" - Ano de contratacao {cadastro['contratacao']}")
    print(f" - Salario R${cadastro['salario']:.2f}")
    print(f" - Aposentadoria tem o valor de {cadastro['aposentadoria']}")

