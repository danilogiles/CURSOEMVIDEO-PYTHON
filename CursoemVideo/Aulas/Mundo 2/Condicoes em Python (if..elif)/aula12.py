nome=str(input('Qual o seu nome: ')).strip()
if nome == 'Danilo':
    print(f'Que nome bonito {nome}')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print(f'O nome {nome} e bem popular no Brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print(f'O nome {nome} e um belo nome feminino')
else:
    print(f'O nome {nome} e bem normal')
print(f'Tenha um bom dia')