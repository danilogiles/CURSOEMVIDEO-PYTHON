cores={'end':'\033[m',
       'red':'\033[031m',
       'green':'\033[032m',
       'yellow':'\033[033m',
       'blue':'\033[034m',
       'purple':'\033[035m',
       'cyan':'\033[036m',
       'gray':'\033[037m'
       }
casa=float(input(f'Digite o Valor {cores["green"]}casa{cores["end"]} que deseja comprar: R$'))
salario=float(input(f"Digite seu {cores['red']}salario{cores['end']}: R$"))
pagamento=int(input(f"Digite quanto {cores['yellow']}anos{cores['end']} ira pagar: "))
prestacao=float(f'{casa/(pagamento*12):.2f}')
sal_percent=float(f'{salario*30/100:.2f}')
print(f'O valor da prestacao sera de R${prestacao}')
print(f'O percentual o seu salario e R${sal_percent}')
if prestacao > sal_percent:
    print(f"{cores['red']}Infelizmente voce nao pode financiar essa casa{cores['end']}")
else:
    print(f"{cores['green']}Parabens voce pode pegar um emprestimo!{cores['end']}")


