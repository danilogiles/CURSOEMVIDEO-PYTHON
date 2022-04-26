'''
If else
'''
#jeito normal de fazer o if

tempo=int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Seu carro e novo')
else:
    print('Seu carro e velho')
print('----FIM----')

#jeito simplificado de usar if
#tempo=int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <=3 else 'carro velho')
print('====FIM====')

#exemplo de if
nome = str(input('Qual e seu nome:')).strip()
if nome.upper() == 'DANILO':
    print('Que nome legal voce tem!')
else:
    print(f'{nome} parece tao normal!')
print(f'Bom dia, {nome}!')

#
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota:'))
m = (n1+n2)/2
print(f'A sua media foi {m:.1f}')

if m >=6 :
    print(f'Sua media {m} foi boa! Voce passou de ano! ')
else:
    print(f'Sua media {m} foi ruim! Te vejo na recuperacao ')
print('Continue estudando!')



