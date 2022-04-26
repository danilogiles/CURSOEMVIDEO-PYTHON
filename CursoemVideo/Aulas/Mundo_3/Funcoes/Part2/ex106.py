from time import sleep
def linha(texto = '', cor = 'white', backcor = '', menu = True):
    '''
    -> Imprime o menu nas cores selecionadas
    :param texto: Recebe o texto que vai ser adiconado e impresso no menu
    :param cor: A Sintaxe para adicionar cores a um texto e \033[style:text:background m]
    :param backcor: A sintaxe para adicionar cores de fundo
    :param menu: printa resultado na tela como menu padrao se True, se falso imprime help
    Tabela de cores:
    Style           Text        Background
    0 none          30 white    40 white
    1 Bold          31 red      41 red
    4 underline     32 green    42 green
    7 negative      33 yellow   43 yellow
                    34 Blue     44 Blue
                    35 Purple   45 Purple
                    36 Cyan     46 Cyan
                    37 gray     47 gray
    :return: nao ha retorno
    '''
    cores = {'end': '\033[m',
             'white': '\033[038m',
             'red': '\033[031m',
             'green': '\033[032m',
             'yellow': '\033[032m',
             'blue': '\033[034m',
             'purple': '\033[035m',
             'cyan': '\033[036m',
             'gray': '\033[037m'
             }
    bgcor = {'end': '\033[m',
            'white' : '\033[7:40m',
            'red' : '\033[41m',
            'green' : '\033[42m',
            'yellow' : '\033[43m',
            'blue' : '\033[44m',
            'purple' : '\033[45m',
            'cyan' : '\033[46m',
            'gray' : '\033[47m'
            }
    menu = menu
    corin = cores[cor.lower()]
    fundo = bgcor[backcor.lower()]
    tamlin= '~' * (len(texto) + 4)
    if menu == True:
        print(fundo,tamlin,corin)
        print(texto.center(len(texto)+5))
        print(fundo,tamlin,corin)
        print(cores['end'], end='')

    else:
        print(fundo,corin)
        help(texto)
        print(cores['end'], end='')


#PROGRAMA PRINCIPAL;
while True:
    linha("SISTEMA DE AJUDA PyHELP", backcor='green', menu=True)
    resp = str(input("Funcao ou biblioteca > "))
    if resp.upper() in 'FIM':
        linha("ATE LOGO!", backcor='red')
        break
    linha(f"Acessando o manual do comando '{resp}'", backcor='blue')
    sleep(1)
    linha(texto=resp, backcor='white', menu=False)
    sleep(1)

