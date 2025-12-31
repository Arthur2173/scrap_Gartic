#importando as bibliotecas

import requests
from bs4 import BeautifulSoup

#url do site
url ="https://respostadogartic.blogspot.com/2017/10/lista-de-alimentos-gartic.html?m=1"
resposta = requests.get(url)

#pegando todo o html da pagina
soup = BeautifulSoup(resposta.text, 'html.parser')

#pegando os dados da pagina usando find_all() os dados estao na tag button
palavras = soup.find_all("button")

tamanho = int(input("informe o tamanho da dica"))
 
for palavra in palavras:
     #tratando as palavras usando replace,strip(). usando o replace para tirar os espaços do meio das palavras pois
     #acaba atrapalhando na hora de ver o tamanho delas
     tratamento = palavra.text.strip().replace(" ","")
     
     texto = palavra.text.strip()
     
     #agora as palavras estão sendo separadas por tamanho ajuda muito na hora que alguem coloca as dicas no jogo
     if len(tratamento) == tamanho:
         print(texto)
         
         
         
     
    

