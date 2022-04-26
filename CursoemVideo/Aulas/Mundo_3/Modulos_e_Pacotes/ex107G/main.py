import moedaG

p =  float(input("Digite um preco: R$"))
print(f"A metade de {p} e {moedaG.metade(p)}")
print(f"O dobro de {p} e {moedaG.dobro(p)}")
print(f"Aumentando 10%, temos {moedaG.aumentar(p, 10)}")
print(f"Descontando de 15%, {moedaG.diminuir(p, 15)}")