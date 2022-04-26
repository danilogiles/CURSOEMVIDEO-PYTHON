from datetime import date

ano=int(input('Digite o seu ano de nascimento: '))
atual=date.today().year
idade=atual-ano
militar=int(18)
print("-=" * 40)
if idade == militar:
    print(f"Voce tem {idade} e esta na hora de se alistar ao servico militar!")
elif idade < militar:
    print(f"Voce tem {idade} e faltam {(militar - idade)} anos para voce poder se alistar!")
else:
    print(f"Voce esta com {idade} e ja passou {idade - 18} anos da hora de se alistar no servico militar!")
print("-=" * 40)
