import math

n1 = (int(input('Digite um valor: \n')))
d = n1 * 2
t = n1 * 3
sq = math.sqrt(n1)
sqo= n1 ** (1/2)
print(f'O dobro de {n1} vale {d}. \n'
      f'O triplo de {n1} vale {t}. \n'
      f'A raiz quadrada usando funcao de {n1} vale {sq :.2f}. \n'
      f'A raiz quadrada calculando de {n1} vale {sqo :.2f}. \n'
      f'Raiz usando funcao pow {pow(n1,(1/2)) :.2f}')
