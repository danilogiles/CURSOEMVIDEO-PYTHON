from moedaG import moeda, metade, dobro, aumentar, diminuir

p =  float(input("Digite um preco: R$"))
print(f"A metade de {moeda(p)} e {metade(p, True)}")
print(f"O dobro de {moeda(p)} e {dobro(p, True)}")
print(f"Aumentando 10% temos {aumentar(p, 10, True)}")
print(f"Descontando de 15% {diminuir(p, 15, True)}")