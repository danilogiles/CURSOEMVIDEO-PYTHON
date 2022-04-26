#Calcula  a metragem de um terreno usando funcoes
def area(largura, comprimento):
    print(f"A area de um terreno de {largura} x {comprimento} e de {largura*comprimento}m2. ")

def titulo():
    print('-=' * 30)
    print('Controle de terrenos'.capitalize().center(50))
    print('-=' * 30)

#Programa Principa
titulo()
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
area(l,c)
