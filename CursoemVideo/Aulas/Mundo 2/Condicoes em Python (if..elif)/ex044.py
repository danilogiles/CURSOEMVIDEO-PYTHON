# Calcule o preco do produto de acordo com a condicao de pagamento
print("========== LOJAS GILES =============")
preco=float(input("Digite o preco do produto: \n"
                  "R$"))
escolha=float(input("Escolha a forma de pagamento\n"
                    "----------------------------\n"
                    "[ 1 ] Dinheiro a vista\n"
                    "[ 2 ] Cartao a vista\n"
                    "[ 3 ] 2X no cartao\n"
                    "[ 4 ] 3x ou mais no cartao\n"
                    "----------------------------\n"
                   ""))
print("-"*40)
print(f"O seu pagamento total sera de ", end='')
if escolha == 1:
    total = preco - (preco * 10/100)
elif escolha == 2:
    total = preco-((preco * 5)/100)
elif escolha == 3:
    total = (preco)
elif escolha == 4:
    total = preco+(preco * 20 / 100)
    totalparc = int(input("Quantas parcelas? "))
    parcela = total / totalparc
    print(f"Sua compra sera parcelada em {totalparc:.0f}x de R${parcela:.2f}")
else:
    print(" Voce digitou uma opcao invalida de pagamento, tente novamente")
print(f"Sua compra total custara R${total:.2f}")
print("-"*40)


