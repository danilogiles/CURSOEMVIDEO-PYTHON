def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
        except (TypeError, ValueError):
            print("\033[031m Erro: Por favor, digite um numero inteiro valido. \033[m")
            continue
        except (KeyboardInterrupt):
            print('\033[031m O usuario preferiu nao digitar nenhum valor. \033[m')
            return 0
        else:
            return valor

def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print("\033[031m Erro: Por favor, digite um numero real valido. \033[m")
            continue
        except (KeyboardInterrupt):
            print('\033[031m O usuario preferiu nao digitar nenhum valor. \033[m')
            return 0
        else:
            return valor


# Programa principal
inteiro = leiaint('Digite um valor inteiro: ')
real = leiafloat('Digite um valor real: ')
print(f"O valor inteiro digitado foi {inteiro} e o valor real e {real:.2f}")
