#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 25/11/2020 6:40pm 
#Fecha de última Modificación: 5/12/2020 9:32pm
#Versión: 3.9.0
#Importaciones
import requests
import re
from bs4 import BeautifulSoup
#Funciones
def obtenerCarreras():
    lista=[]
    r = requests.get('https://www.tec.ac.cr/carreras')
    contenido = r.text
    contenido= contenido.rsplit('\n')
    cont=-1
    for i in contenido:
        if '<div class="panel-pane pane-views-panes pane-directory-academic-programs-per-type-panel-pane-2"  >' in i:
                break
        if '<h3 class = "group-title">' in i or '<div class="title"><a href=' in i:
#            if '<div class="title"><a href="/programas-academicos/' in i:
#                continue
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