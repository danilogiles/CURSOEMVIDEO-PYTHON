#Aula de utilizacao do while
#Usando variavel de controle como feito no for caso saiba o limite
c=1
while c <= 10:
    print(c)
    c += 1
print('fim')
#usando while quando sem saber o limite(nao da pra fazer no for)
n=1
while n != 0:
    n = int(input("Digite um valor: "))
print('Fim')
#while controlando fim por string
r='S'
while r in 'Ss':
    n=int(input("Digite um valor: "))
    r=input("Deseja continuar [S/N]: ")
print('Fim')
#usando if dentro
n=1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor:"))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f"Voce digitou {par} numeros pares e {impar} numeros impares")