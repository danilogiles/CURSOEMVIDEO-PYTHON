#Cria 10 termos em PA usando while e pergunta quantos termos a mais deseja mostrar
pt = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
decimo = razao
c = 10
termos = 1
mostra = ''
x = 0
while termos != 0:
    while termos <= c:
        mostra = mostra + (f"{pt} ")
        pt += razao
        c -= 1
        x += 1
    print(f"{mostra.rstrip().replace(' ', ' -> ')} -> PAUSA")
    c = int(input("\nDeseja mostrar mais quantos termos [0 para sair]?"))
    mostra = ''
    if c == 0:
        termos = 0
print('-=' * 20)
print(f"Progressao finalizada com {x} termos mostrados.")
print("Programa finalizado com sucesso, volte sempre!")