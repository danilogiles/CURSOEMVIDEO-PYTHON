#Cria 10 termos em PA
pt=int(input("Primeiro termo: "))
razao=int(input("Razao: "))
decimo= pt + (10 - 1) * razao
for c in range(pt, decimo + razao, razao):
    print(f"{c}", end=' -> ')
print("ACABOU")



