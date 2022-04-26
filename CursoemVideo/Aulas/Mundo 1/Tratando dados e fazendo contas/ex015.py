dias=int(input('Quantos dias alugados? '))
km=float(input('Quantos Km rodados? '))
cust_dias=dias*60
cust_km=km*0.15
total=cust_km+cust_dias
print(f'O total a pagar e de R${total:.2f}')