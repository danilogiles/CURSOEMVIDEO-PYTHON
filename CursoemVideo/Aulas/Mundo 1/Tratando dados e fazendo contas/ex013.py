sal=float(input('Qual o salario do funcionario? \n'))
aum_perc=float(input('Quantos % deseja dar de aumento ao funcionario? \n'))
perc_sal=sal*aum_perc/100
print(f'Um funcionario que Ganhava R${sal:.2f}, com {aum_perc:.0f}% de aumento passou a ganhar {sal + perc_sal:.2f}')