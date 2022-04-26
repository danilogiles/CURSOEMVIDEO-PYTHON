#utilizacao do for
#contando de tras pra frente range(primeiro num, segundo num, iteracao)
for c in range(6, 0, -2):
    print(c)
print("FIM")
---------------------------
#usando o valor n para controle do range a printando c a cada iteracao
n = int(input("Digite um numero: "))
for c in range(0, n+1):
      print(c, end=' ')
print("\nFIM")
----------------------------
# usando variavel pra controlar toda a estrutura do for
i=int(input("Inicio: "))
f=int(input("Fim: "))
p=int(input("Passo: "))
for c in range(i, f+1, p):
      print(c, end=' ')
print("\nFIM")
------------------------------
#Fazendo somatoria de todos os valores digitados dentro do loop
s = 0
for c in range(0, 4):
    n=int(input("Digite um valor: "))
    s += n #isso e a mesma coisa que s = s + n
print(f"A somatoria de todos os valores e {s}")