def linha(texto = '', cor = '', backcor = '', ultlinha = False):
    '''
    -> Imprime o menu nas cores selecionadas
    :param texto: Recebe o texto que vai ser adiconado e impresso no menu
    :param cor: A Sintaxe para adicionar cores a um texto e \033[style:text:background m]
    :param backcor: A sintaxe para adicionar cores de fundo
    :param ultlinha: finaliza a impressao da cor de fundo, utilize na ultima linha do seu cabecalho
    onde:
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
             'white': '\033[030m',
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
    if cor == '' :
        corin = ''
    else:
        corin = cores[f'{cor}']
    if backcor == '':
        fundo = ''
    else:
        fundo = bgcor[backcor]
    if texto == '':
        texto = '~' * 30
    elif texto == 'noline':
        texto = end=''
    else:
        texto = texto
    tamlin= '~' * (len(texto) + 4)
    print(fundo, corin, tamlin)
    print(texto)
    print(fundo, corin, tamlin)
    print(cores['end'], end='')
    if ultlinha == True:
        print(cores['end'], end='')


#PROGRAMA PRINCIPA;
while True:
    linha(backcor='green')
    linha("   SISTEMA DE AJUDA PyHELP", backcor='green')
    linha(ultlinha=True)
    resp = str(input("Funcao ou biblioteca > "))
    if resp.upper() in 'FIM':
        linha(backcor= 'red')
        linha("ATE LOGO!", backcor='red')
        linha(backcor='red', ultlinha=True)
        break
    funcao(resp)
