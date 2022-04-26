def testasite(msg):
    from ping3 import ping
    try:
        valor = str(input(msg))
    except (ValueError, TypeError):
        print('\033[031mVoce digitou um valor incorreto para o site\033[m')
    except (KeyboardInterrupt):
        print('\033[031mO programa foi interrompido!\033[m')
    else:
        r = ping(valor)
        if r == False:
            print(f'\033[031mO Site "{valor}" inacessivel! \033[m')
        else:
            print(f'\033[032mO Site "{valor}" esta online! \033[m')

#Programa principal
testasite('Digite um site: ')