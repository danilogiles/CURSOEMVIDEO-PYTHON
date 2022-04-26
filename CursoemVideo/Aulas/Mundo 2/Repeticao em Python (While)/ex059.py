exit = 0
while exit != 5:
    num1 = int(input("Primeiro valor: "))
    num2 = int(input("Segundo valor: "))
    novosnumeros = 0
    while novosnumeros != 1:
        menu = int(input("[1] Somar\n"
                         "[2] multiplicar \n"
                         "[3] Maior\n"
                         "[4] Novos numeros\n"
                         "[5] Sair do programa\n"
                         ""))
        if menu in range(1,6):
            if menu == 1:
                resposta = num1 + num2
                print(f"{num1} + {num2} = {num1 + num2}")
            elif menu == 2:
                print(f"{num1} * {num2} = {num1 * num2}")
            elif menu == 3:
                if num1 > num2:
                    print(f"O maior numero e {num1}")
                else:
                    print(f"O maior numero e {num2}")
            elif menu == 4:
                novosnumeros = 1
                print("Digite os novos numeros: ")
            else:
                novosnumeros = 1
                exit = 5
        else:
            print("voce digitou um valor incorreto, digite novamente")
print("Obrigado e volte sempre!")
