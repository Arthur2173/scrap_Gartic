#importando as bibliotecas

import requests
from bs4 import BeautifulSoup

#url do site
url ="https://respostadogartic.blogspot.com/2017/10/lista-de-alimentos-gartic.html?m=1"
response = requests.get(url)

#pegando todo o html da pagina
soup = BeautifulSoup(response.text, 'html.parser')

#pegando os dados da pagina usando find_all() os dados estao na tag button
words = soup.find_all("button")

item_count = int(input("length: "))
 
for word in words:
     #tratando as palavras usando replace,strip(). usando o replace para tirar os espaços do meio das palavras pois
     #acaba atrapalhando na hora de ver o tamanho delas
     treatment = word.text.strip().replace(" ","")
     
     texto = word.text.strip()
     
     #agora as palavras estão sendo separadas por tamanho ajuda muito na hora que alguem coloca as dicas no jogo
     if len(treatment) == item_count:
         print(texto)
         
         
         
     
    

