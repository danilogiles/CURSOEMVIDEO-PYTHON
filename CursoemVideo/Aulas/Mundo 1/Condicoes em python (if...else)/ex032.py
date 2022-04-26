import datetime
from datetime import date
ano=int(input('Digite um ano qualquer, ou digite 0 para usar a data atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} e bixesto')
else:
    print(f'O ano {ano} nao e bixesto!')


