import datetime
import time

print("-=" * 40)
print("Bem vindo ao software de avaliacao da Confederacao nacional de natacao!")
ano=int(input("Digite seu ano de nascimento: "))
print("-=" * 40)
atual=(datetime.date.today().year)
idade=atual-ano
print(f"O aluno tem {idade} anos.")
print("Calculando a sua categoria...")
time.sleep(2)
print("-=" * 30)
if idade <= 9:
    categoria="\033[034mMIRIM\033[m"
elif idade > 9 and idade <= 14:
    categoria="\033[034mINFANTIL\033[m"
elif idade > 14 and idade <= 19:
    categoria="\033[034mJUNIOR\033[m"
elif idade > 19 and idade < 20:
    categoria="\033[033mSENIOR\033[m"
else:
    categoria="\033[031mMASTER\033[m"
print(f"Voce tem {idade} e esta na categoria \033[032m{categoria}\033[m!")
print("-=" * 30)

