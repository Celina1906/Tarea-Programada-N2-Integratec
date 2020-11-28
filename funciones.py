#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 26/11/2020 7:43pm 
#Fecha de última Modificación: 5/12/2020 9:32pm
#Versión: 3.9.0
#Importaciones
from Archrequests import *
import random
#Variables globales
sedesCarreras=quitaRepetidos(obtenerCarreras())
#Funciones
#def dividirEstudiantes():

def crearDiccionario(cantidad, diccionario):
    keys = sacaListaKeys(diccionario)
    largo=len(keys)
    listaCant=crearLista(largo)
    while cantidad!=0:
        listaCant[random.randrange(0,largo)]+=1
        cantidad-=1
    for i in range(largo):
        diccionario[keys[i]]=listaCant[i]
    return diccionario
def crearLista(cant):
    lista=[]
    while cant!= 0:
        lista+=[0]
        cant-=1
    return lista
def sacaListaKeys(diccionario):
    llaves=diccionario.keys()
    listaNueva=[]
    for i in llaves:
        listaNueva+=[i]
    print(listaNueva)
    return listaNueva

def crearMatrizGeneral(MatrizCarreras, listaCantidad, listaSede):
    matrizSJ=[]
    matrizCAR=[]
    matrizSC=[]
    matrizL=[]
    matrizA=[]
    for i in MatrizCarreras:
        if i[0]=='Campus Tecnológico Local San José':
            matrizSJ=[listaSede[0],listaCantidad[0],]
            dicSJ={}
            for j in i[1:]:
                dicSJ[j]=0
            dicSJ=crearDiccionario(listaCantidad[0],dicSJ)
            matrizSJ.append(dicSJ)                 
        if i[0]=='Campus Tecnológico Central Cartago':
            matrizCAR=[listaSede[1],listaCantidad[1],]
            dicCAR={}
            for j in i[1:]:
                dicCAR[j]=0
            dicCAR=crearDiccionario(listaCantidad[1],dicCAR)
            matrizCAR.append(dicCAR)
        if i[0]=='Campus Tecnológico Local San Carlos':
            matrizSC=[listaSede[2],listaCantidad[2],]
            dicSC={}
            for j in i[1:]:
                dicSC[j]=0
            dicSC=crearDiccionario(listaCantidad[2],dicSC)
            matrizSC.append(dicSC) 
        if i[0]=='Centro Académico de Limón':
            matrizL=[listaSede[3],listaCantidad[3],]
            dicL={}
            for j in i[1:]:
                dicL[j]=0
            dicL=crearDiccionario(listaCantidad[3],dicL)
            matrizL.append(dicL)
        if i[0]=='Centro Académico de Alajuela':
            matrizA=[listaSede[4],listaCantidad[4],]
            dicA={}
            for j in i[1:]:
                dicA[j]=0
            dicA=crearDiccionario(listaCantidad[4],dicA)
            matrizA.append(dicA)  
    return [matrizCAR,matrizSC,matrizSJ,matrizA,matrizL]
    
MatrizCarreras=[['Campus Tecnológico Local San José', 'Arquitectura y Urbanismo', 'Administración de Empresas', 'Ingeniería en Computación'], ['Campus Tecnológico Central Cartago', 'Ingeniería en Biotecnología', 'Administración de Empresas', 'Ingeniería en Computación', 'Gestión en Turismo Sostenible', 'Enseñanza de la Matemática con Entornos Tecnológicos', 'Administración de Tecnología de Información', 'Ingeniería Agrícola', 'Ingeniería Ambiental', 'Ingeniería en Electrónica', 'Ingeniería Agronegocios', 'Ingeniería en Computadores', 'Ingeniería en Construcción', 'Ingeniería en Diseño Industrial', 'Ingeniería en Materiales', 'Ingeniería en Producción Industrial', 'Ingeniería en Seguridad Laboral e Higiene Ambiental', 'Ingeniería Física', 'Ingeniería Forestal', 'Ingeniería Mecatrónica', 'Ingeniería en Mantenimiento Industrial'], ['Campus Tecnológico Local San Carlos', 'Administración de Empresas', 'Ingeniería en Computación', 'Gestión en Turismo Rural Sostenible', 'Ingeniería en Electrónica', 'Ingeniería en Agronomía', 'Ingeniería en Producción Industrial'], ['Centro Académico de Limón', 'Administración de Empresas', 'Ingeniería en Computación', 'Ingeniería en Producción de Industrial'], ['Centro Académico de Alajuela', 'Ingeniería en Computación', 'Ingeniería en Electrónica']]
             #? SJ   C   SC  L   A
listaCantidad=[503,1200,400,200,300]
listaSede=["CTLSJ","CTCC","CTLSC","CAL","CAA"]

print(crearMatrizGeneral(MatrizCarreras,listaCantidad,listaSede))