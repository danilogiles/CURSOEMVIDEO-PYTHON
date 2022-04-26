dados={}
dados['nome'] = str(input("Digite um nome:"))
dados['media'] = float(input(f"Media de {dados['nome']}: "))
if dados['media'] >= 7:
    dados['situacao'] = 'Aprovado'
elif 5 <= dados['media'] < 7:
    dados['situacao'] = 'Recuperacao'
else:
    dados['situacao'] = 'Reprovado'
for k, v in dados.items():
    print(f"  - {k} e igual a {v}")