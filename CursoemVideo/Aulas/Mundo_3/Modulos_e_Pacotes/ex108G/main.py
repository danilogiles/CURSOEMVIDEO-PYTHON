import moedaG

p =  float(input("Digite um preco: R$"))
print(f"A metade de {moedaG.moeda(p)} e {moedaG.moeda(moedaG.metade(p))}")
print(f"O dobro de {moedaG.moeda(p)} e {moedaG.moeda(moedaG.dobro(p))}")
print(f"Aumentando 10%, temos {moedaG.moeda(moedaG.aumentar(p, 10))}")
print(f"Descontando de 15%, {moedaG.moeda(moedaG.diminuir(p, 15))}")