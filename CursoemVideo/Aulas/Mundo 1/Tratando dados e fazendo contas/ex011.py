larg=float(input('Largura da parede: '))
alt=float(input('Altura da parede: '))
area=(larg * alt)
tinta=area/2
print(f'Sua parede tem a dimensao de {larg:.2f}m x {alt:.2f}m e sua area e de {area:.3f}m².\n'
      f'Para pintar essa parede, voce precisara de {tinta:.4f}l de tinta')