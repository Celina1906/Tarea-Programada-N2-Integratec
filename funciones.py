#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 26/11/2020 7:43pm 
#Fecha de última Modificación: 5/12/2020 9:32pm
#Versión: 3.9.0
#Importaciones
from Archrequests import *
#Variables globales
sedesCarreras=quitaRepetidos(obtenerCarreras())
#Funciones
#def dividirEstudiantes():

def crearSedeCompleta(cantEstudiantes,nombreSede):
    global sedesCarreras
    dicCarreras={}
    for sede in sedesCarreras:
        if sede[0]=='Campus Tecnológico Central Cartago':
            for carrera in sede:
                if carrera!=sede[0]:
                    dicCarreras[carrera]=cantEstudiantes #!Revisar!!!

