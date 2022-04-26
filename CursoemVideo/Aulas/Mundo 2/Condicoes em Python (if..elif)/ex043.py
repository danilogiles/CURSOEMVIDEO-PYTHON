#Calculo de IMC
Enunsiado= 'Calculadora de IMC'
barmenu=('-=' * 30)
peso=float(input("Digite seu peso (kg): "))
altura=float(input('Digite sua altura (m): '))
imc=peso/(altura**2)
print(barmenu)
print(Enunsiado)
print(barmenu)
print(f"O IMC dessa pessoa e de {imc:.1f}, ", end='')
if imc < 18.5:
    print(f"\033[033mEssa pessoa esta abaixo do peso.\033[m")
elif 18.5 <= imc < 25:
    print(f"\033[032mEssa pessoa esta no peso ideal.\033[m")
elif 25 <= imc < 30:
    print(f"\033[033mEssa pessoa esta com sobrepeso.\033[m")
elif 30 <= imc < 40:
    print(f"\033[031mEssa pessoa esta obesa!\033[m")
elif imc >= 40:
    print(f"\033[031mVoce esta com obesidade morbida, Cuidado!\033[m")
print(barmenu)
