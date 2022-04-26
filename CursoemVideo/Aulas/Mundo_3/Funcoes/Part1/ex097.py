#Digita um texto e as linhas acompanham o tamanho do texto
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f"{msg}".center(tam))
    print('~' * tam)

#Programa Principal
texto = str(input("Digite uma mensagem:"))
escreva(texto)