import time

print("-=" * 30)
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
media=float((nota1 + nota2)/2)
print("-=" * 30)

print("\033[032mCalculando sua nota...\033[m \n")
time.sleep(2)
print("*" * 50)
print(f"Tirando {nota1} e {nota2} a media do aluno e {media} ")
if media < 5.0:
    print(f"Sua media foi {media:.2f}, voce foi \033[031mReprovado!\033[m")
elif media >= 5.0 and media < 7:
    print(f"Sua media foi {media:.2f}, voce esta de \033[033mRecuperacao!\033[m")
else:
    print(f"Sua media foi {media:.2f}, \033[032mParabens voce Passou de ano!\033[m")
print("*" * 50)
