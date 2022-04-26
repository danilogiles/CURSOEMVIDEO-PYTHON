#contagem regressiva de 10 a 0
import time
i=0
for c in range(10, -1, -1):
   print(f"{c}", end=' ')
   time.sleep(1)
print("\nFeliz Ano novo!")