# le o ano de nascimento de 7 pessoas e determina quantas sao maiores e quandas sao menores
from datetime import date
maior = 0
menor = 0
atual = date.today().year
for c in range(1, 8):
    nasc = int(input(f"Em que ano a {c} Nasceu? "))
    idade = (atual - nasc)
    #print(f"Essa pessoa tem {idade}")
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f"{maior} Atingiram a maioridade.")
print(f"{menor} Ainda sao Menor de idade.")