#Tratamento de errors e excecoes
#try:
#   tenta uma operacao
#except:
#   caso de erro executa a excecao, podem ter varios excepts
#para printar o erro por tipo use except(ValueError, TypeError, <Tipoqualquerquequiser>):
# para printar o erro generico utilize Exception
# I.e: except Exception as erro:
#           print(f'Problema encontrado foi (erro.<escolha o erro que quer printar como __class__>)'
#else:
#   printa o resultado  se der certo
#Finally:
#   printa o resultado independente do que acontece

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except(ValueError,TypeError):
    print('Tivemos um problema com os tipos de dados que vc digitou.')
except ZeroDivisionError:
    print('Nao e possivel dividir por zero!')
except KeyboardInterrupt:
    print('O usuario preferiu nao digitar os dados:')
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado e {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')