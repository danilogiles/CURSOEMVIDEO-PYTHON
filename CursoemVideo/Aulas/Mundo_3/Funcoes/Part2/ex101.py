def voto(anonasc):
    from datetime import date
    idade = date.today().year - anonasc
    if idade >= 18 and idade <= 65:
        texto = str(f"Com {idade} anos: VOTO E OBRIGATORIO.")
    elif idade < 16:
        texto = str(f"Com {idade} anos : NAO VOTA. ")
    else:
        texto = str(f"Com {idade} anos : VOTO OPCIONAL.")

    return texto

#Programa principal
frase = voto(int(input('Em que ano voce nasceu? ')))
print(frase)


