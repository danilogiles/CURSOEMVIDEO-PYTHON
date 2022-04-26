n=float(input('Uma distancia em metros: '))
print(f'A medida de {n}m corresponde a:\n'
      f'{n/1000}km\n'
      f'{n/100}hm\n'
      f'{n/10}dam\n'
      f'{n*10 :.0f}dm\n'
      f'{n*100 :.0f}cm\n'
      f'{n*1000 :.0f}mm')