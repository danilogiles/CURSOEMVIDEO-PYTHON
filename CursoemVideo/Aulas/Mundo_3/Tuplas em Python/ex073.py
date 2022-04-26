times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino',
         'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional',
         'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print('-=' * 30)
print(f"Lista de times do Brasileirao:\n{times}")
print('-=' * 30)
print(f"Os 5 primeiros sao :\n{times[0:5]}")
print('-=' * 30)
print(f"Os 4 ultimos sao:\n{times[-4:]}")
print('-=' * 30)
print(f"Times em ordem alfabetica:\n{sorted(times)}")
print('-=' * 30)
print(f"O Chapecoense esta na {times.index('Chapecoense')+1} posicao")

