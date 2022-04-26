import math

num=float(input('Digite um angulo: '))
angulo=math.radians(num)
seno=math.sin(angulo)
coss=math.cos(angulo)
tangente=math.tan(angulo)

print(f'O valor de Seno e {seno:.2f}\n'
      f'O valor de cosseno e {coss:.2f}\n'
      f'O valor de tangente e {tangente:.2f}')