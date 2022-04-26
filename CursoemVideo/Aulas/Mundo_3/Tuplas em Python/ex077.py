lista = ('aprender', 'programar', 'linguagem', 'python',
         'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
         'mercado', 'programador', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')
palavra = result = ''
c = 0
while True:
    result = ''
    if c < len(lista):
        palavra = str(lista[c])
        c += 1
        for n in range(0, len(palavra)):
            for x in range(0, len(vogais)):
                if vogais[x] == palavra[n]:
                    result = result + ' ' + vogais[x]
        print(f"Na Palavra {palavra.upper()} temos{result}")
    else:
        break
#Usando for
for p in lista:
    print(f"\nNa palavra {p} temos", end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

