frase=str(input('Digite uma frase: ')).strip().upper()
print(f'A letra A aparece {frase.upper().count("A")} vezes na frase')
print(f'A primeira letra A apreceu na posicao {frase.find("A")+1}')
print(f'A ultima letra A apareceu na posicao {frase.rfind("A")+1}')