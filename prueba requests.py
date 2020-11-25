import requests
import re
from bs4 import BeautifulSoup

def obtenerCarreras():
    lista=[]
    r = requests.get('https://www.tec.ac.cr/carreras')
    contenido = r.text
    contenido= contenido.rsplit('\n')
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
                lista+=[[soup.h3.string]]
            else:
                lista[cont]+=[soup.div.string]
    return lista

def quitaRepetidos(matriz):
    nuevaMatriz=[]
    for lista in matriz:
        listaTemp=[]
        for i in lista:
            if not i in listaTemp:
                listaTemp+=[i]
        nuevaMatriz+=[listaTemp]
    return nuevaMatriz

print(quitaRepetidos(obtenerCarreras()))
