#Cria 10 termos em PA usando while
print("Gerador de PA")
print('-=' * 10)
termo=int(input("Primeiro termo: "))
razao=int(input("Razao: "))
c = 1
while c <= 10:
    print(f"{termo}", end=' -> ')
    termo += razao
    c += 1
print("ACABOU")