#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 26/11/2020 7:43pm 
#Fecha de última Modificación: 5/12/2020 9:32pm
#Versión: 3.9.0
#Importaciones
from Archrequests import *
import random
import names
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
    #print(listaNueva)
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


def crearDicPrimerIngreso(matrizSedesEst,diccPrimerIngreso):
    for sede in matrizSedesEst:
        for carrera in sede[2]:
            cantEst=sede[2][carrera]
            while cantEst>0:
                nombre=names.get_first_name()
                apellido1=names.get_last_name()
                apellido2=names.get_last_name()
                nombreCompleto=nombre+' '+apellido1+' '+apellido2
                if sede[0]=='CTCC':
                    sedeEst='CAMPUS TECNOLÓGICO CENTRAL CARTAGO'
                    carnet='202101'+str(random.randint(1000,9999))
                    while int(carnet) in diccPrimerIngreso:
                        carnet='202101'+str(random.randint(1000,9999))
                    carnet=int(carnet)
                if sede[0]=='CTLSC':
                    sedeEst='CAMPUS TECNOLÓGICO LOCAL SAN CARLOS'
                    carnet='202102'+str(random.randint(1000,9999))
                    while int(carnet) in diccPrimerIngreso:
                        carnet='202102'+str(random.randint(1000,9999))
                    carnet=int(carnet)
                if sede[0]=='CTLSJ':
                    sedeEst='CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ'
                    carnet='202103'+str(random.randint(1000,9999))
                    while int(carnet) in diccPrimerIngreso:
                        carnet='202103'+str(random.randint(1000,9999))
                    carnet=int(carnet)
                if sede[0]=='CAA':
                    sedeEst='CENTRO ACADÉMICO DE ALAJUELA'
                    carnet='202104'+str(random.randint(1000,9999))
                    while int(carnet) in diccPrimerIngreso:
                        carnet='202104'+str(random.randint(1000,9999))
                    carnet=int(carnet)
                if sede[0]=='CAL':
                    sedeEst='CENTRO ACADÉMICO DE LIMÓN'
                    carnet='202105'+str(random.randint(1000,9999))
                    while int(carnet) in diccPrimerIngreso:
                        carnet='202105'+str(random.randint(1000,9999))
                    carnet=int(carnet)
                values=list(diccPrimerIngreso.values())
                numTel=random.randint(60000000,99999999)
                for i in range(len(values)):
                    if numTel in values[i]:
                        numTel=random.randint(60000000,99999999)
                        i=0
                correo=nombre[0].lower()+apellido1.lower()+'@estudiantec.cr'
                for i in range(len(values)):
                    letra=2
                    if correo in values[i]:
                        correo=nombre[0:letra].lower()+apellido1.lower()+'@estudiantec.cr'
                        letra+=1
                        i=0 
                carreraEst=carrera
                carnetMentor=0
                datos=[nombreCompleto,numTel,correo,sedeEst,carreraEst,carnetMentor]
                diccPrimerIngreso[carnet]=datos
                cantEst-=1
    return diccPrimerIngreso

       


