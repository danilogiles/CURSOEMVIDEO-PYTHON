#lacos de repeticao parte 3
#loop infinito
import time
count =1
while True:
    print(count, '->', end='')
    count += 1
    time.sleep(1)
print('Acabou')

#usando o break para parar
n = s = 0
while True:
    n = int(input('Digite um numero:'))
    if n == 999:
        break
    s += n
print(f"A soma vale {s}")
