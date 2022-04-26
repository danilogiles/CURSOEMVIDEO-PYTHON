#checa se uma frase e palindromo
#Jeito curto sem for
'''
frase=str(input("Digite a frase: ")).strip().replace(" ","").upper()
rev=str(frase[len(frase)::-1]).upper()
print(frase, rev)
if frase == rev:
    print("Essa frase e Palindromo")
else:
    print("Essa frase nao e Palindromo")'''

#Utilizando o For
frase=str(input("Digite a frase: ")).strip().upper()
palavras = frase.split()
junto=''.join(palavras)
inverso=''
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f"O inverso de {junto} e {inverso}")
if inverso == junto:
    print("Essa frase e Palindromo!")
else:
    print("Essa frase nao e Palindromo!")

