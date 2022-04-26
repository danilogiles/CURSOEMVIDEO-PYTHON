exp = str(input("Digite uma expressao: ")).split()
pardir = paresq = 0
for c in range (0, len(exp)):
    for d in range(0, len(exp[c])):
        if exp[c][d] == '(':
            paresq += 1
        if exp[c][d] == ')':
            pardir += 1
if pardir == paresq:
    print("Sua expressao e valida!")
else:
    print("Sua expressao e Invalida!")



