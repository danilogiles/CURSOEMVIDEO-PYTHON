nome=str(input('Digite seu nome completo: ')).strip()
lista=nome.split()
x=nome.replace(' ', '')
print(f'O nome em letras maiusculas: {nome.upper()}')
print(f'O nome em letras minusculas: {nome.lower()}')
print(f'O nome tem : {len(x)} letras')
print(f'O nome tem : {len(nome) - nome.count(" ")} letras')
print(f'O primeiro nome tem {len(lista[0])} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')