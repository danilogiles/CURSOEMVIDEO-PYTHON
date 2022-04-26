sexo = str(input("Digite o sexo [M/F]:")).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input("Dados invalidos. Por favor, informe o seu sexo [M/F]:"))
print(f"Sexo {sexo} Registrado com sucesso!")