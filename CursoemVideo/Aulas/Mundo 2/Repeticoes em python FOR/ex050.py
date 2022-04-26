#Le 6 numeros e mostra a soma apenas do numeros pares, discarta valores impar
s=0
np=[]
for c in range(1, 7):
    d=int(input(f"Digite o {c} valor: "))
    if (d%2) == 0:
        s = s + d
        np.append(d)
print(f"A soma dos numeros pares e igual a {s}.")
print(f"Esses sao os numeros pares digitados {np}.")
print("Fim")

