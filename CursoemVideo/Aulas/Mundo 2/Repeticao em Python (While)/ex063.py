print('-=' * 30)
print('Sequencia de Fibonnaci')
print('-='*30)
num=int(input("type the amount of numbers that you wish to see in a fibonacci: "))
count = 2
fibos = ''
pnum = 0
snum = 0
tnum = 1
while count <= num:
    fibos = fibos + (f"{tnum} ")
    pnum = snum
    snum = tnum
    tnum = pnum + snum
    count += 1
print(f"0 -> {fibos.rstrip().replace(' ',' -> ')}", end=' -> FIM')

