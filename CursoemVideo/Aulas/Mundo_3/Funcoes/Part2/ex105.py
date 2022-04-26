def notas(*n, sit=False):
    '''
    -> Funcao para analisar a situacao de varios alunos
    :param n: Uma ou mais notas dos Alunos (aceita varias)
    :param sit: True ou False, se True exibe a situacao do aluno
    :return:
    '''
    r = {}
    r['total'] = len (n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = "RAZOAVEL"
        else:
            r['situacao'] = 'RUIM'
    return r

#Programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
#help(notas)


