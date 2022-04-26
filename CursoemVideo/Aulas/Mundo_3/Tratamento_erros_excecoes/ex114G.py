import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Site nao acessivel!')
else:
    print('Consegui acessar o site pudim com sucesso!')
    print(site.read())