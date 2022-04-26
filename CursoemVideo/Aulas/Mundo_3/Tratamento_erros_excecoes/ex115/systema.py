from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cadastro.txt'
if not arquivoexiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('CADASTRAR NOVA PESSOA')
        nome = str(input('Digite o nome: '))
        idade = leiaint('Digite a idade: ')
        cadastraDados(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... ate logo')
        break
    else:
        print('ERRO! Digite uma opcao valida!')
    sleep(1)