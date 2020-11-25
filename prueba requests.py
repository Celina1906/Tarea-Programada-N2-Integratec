import requests
import re
from bs4 import BeautifulSoup

lista=[]
r = requests.get('https://www.tec.ac.cr/carreras')
contenido = r.text
#contenido = re.sub('<[^<]+?>', '',contenido)
#contenido= contenido.replace("\\n","")
contenido= contenido.rsplit('\n')
#print(contenido)
cont=-1
for i in contenido:
    #print(i)
    if '<div class="panel-pane pane-views-panes pane-directory-academic-programs-per-type-panel-pane-2"  >' in i:
            break
    if '<h3 class = "group-title">' in i or '<div class="title"><a href=' in i:
        if '<div class="title"><a href="/programas-academicos/' in i:
            continue
        soup = BeautifulSoup(i, 'html.parser')
        if '<h3 class = "group-title">' in i:
            cont+=1
            print(soup.h3.string)
            lista+=[[soup.h3.string]]
        else:
            print("\t",soup.div.string)
            lista[cont]+=[soup.div.string]
print(lista)

