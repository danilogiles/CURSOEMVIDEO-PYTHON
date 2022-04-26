prod = float(input('Qual e o preco do produto? \n R$'))
desc = float(input('Quanto de desconto deseja dar ao produto? \n %'))
desc_val = prod * desc / 100
print(f'O produto que custava R${prod} na promocao com desconto de {desc:.0f}% vai custar R${prod - desc_val:.2f}.')
