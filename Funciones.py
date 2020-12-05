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
def crearDiccionario(cantidad, diccionario):
    '''
    Funcionamiento: Crea un diccionario y divide la cantidad de estudiantes de forma aleatoria
    Entradas: cantidad (int) y diccionario
    Salidas: diccionario
    '''
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
    '''
    Funcionamiento: Crea una lista con la cantidad de llaves
    Entradas: int
    Salidas: lista
    '''
    lista=[]
    while cant!= 0:
        lista+=[0]
        cant-=1
    return lista
def sacaListaKeys(diccionario):
    '''
    Funcionamiento: Extrae las llaves de un diccionario
    Entradas: Diccionario
    Salidas: lista
    '''
    llaves=diccionario.keys()
    listaNueva=[]
    for i in llaves:
        listaNueva+=[i]
    return listaNueva
def crearMatrizGeneral(MatrizCarreras, listaCantidad, listaSede):
    '''
    Funcionamiento: Crea una matriz con las sedes y las carreras de cada sede, y divide los cupos
    que serán ocupados por estudiante.
    Entradas: Matriz con las carreras, lista con las cantidades de estudiantes y lista con los acronimos de las sedes
    Salidas: Matriz
    '''
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
    print([matrizCAR,matrizSC,matrizSJ,matrizA,matrizL])
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
    print(diccPrimerIngreso)
    return diccPrimerIngreso

def sacarDatosMentores(matrizMentores):
    datosMentores=[]
    datosMentores2=[]
    for sede in matrizMentores:
        datosMentores+=sede[1].values()
    for datos in datosMentores:
        for dato in datos:
            datosMentores2+=[dato]
    return datosMentores2

def sacarDatosPrimerIngreso(dicPrimerIngreso):
    datosPrimerIngreso=list(dicPrimerIngreso.values())
    datosPrimerIngreso2=[]
    for datos in datosPrimerIngreso:
        for dato in datos:
            datosPrimerIngreso2+=[dato]
    return datosPrimerIngreso2

def sacarCarnetsMentores(matrizMentores):
    carnetsMentores=[]
    for sede in matrizMentores:
        carnetsMentores+=sede[1].keys()
    return carnetsMentores


def crearMatMentores(matrizSedesEst,diccPrimerIngreso,matrizMentores):
    for sede in matrizSedesEst:
        for carrera in sede[2]:
            cantEst=sede[2][carrera]
            cantMentores=abs(cantEst*0.05)
            while cantMentores>0:
                carnetsMentores=sacarCarnetsMentores(matrizMentores)
                datosMentores=sacarDatosMentores(matrizMentores)
                datosPrimerIngreso=sacarDatosPrimerIngreso(diccPrimerIngreso)
                nombre=names.get_first_name()
                apellido1=names.get_last_name()
                apellido2=names.get_last_name()
                nombreCompleto=nombre+' '+apellido1+' '+apellido2
                correo=nombre[0].lower()+apellido1.lower()+'@estudiantec.cr'
                letra=2
                while correo in datosMentores or correo in datosPrimerIngreso:
                    correo=nombre[0:letra].lower()+apellido1.lower()+'@estudiantec.cr'
                    letra+=1
                carreraMentor=carrera
                if sede[0]=='CTCC':
                    carnet='202001'+str(random.randint(1000,9999))
                    while int(carnet) in carnetsMentores:
                        carnet='202001'+str(random.randint(1000,9999))
                    carnet=int(carnet)
                    datos=[nombreCompleto,carrera,correo]
                    matrizMentores[0][1][carnet]=datos
                if sede[0]=='CTLSC':
                    carnet='202002'+str(random.randint(1000,9999))
                    while int(carnet) in carnetsMentores:
                        carnet='202002'+str(random.randint(1000,9999))
                    carnet=int(carnet)
                    datos=[nombreCompleto,carrera,correo]
                    matrizMentores[1][1][carnet]=datos
                if sede[0]=='CTLSJ':
                    carnet='202003'+str(random.randint(1000,9999))
                    while int(carnet) in carnetsMentores:
                        carnet='202003'+str(random.randint(1000,9999))
                    carnet=int(carnet)
                    datos=[nombreCompleto,carrera,correo]
                    matrizMentores[2][1][carnet]=datos
                if sede[0]=='CAA':
                    carnet='202004'+str(random.randint(1000,9999))
                    while int(carnet) in carnetsMentores:
                        carnet='202004'+str(random.randint(1000,9999))
                    carnet=int(carnet)
                    datos=[nombreCompleto,carrera,correo]
                    matrizMentores[3][1][carnet]=datos
                if sede[0]=='CAL':
                    carnet='202005'+str(random.randint(1000,9999))
                    while int(carnet) in carnetsMentores:
                        carnet='202005'+str(random.randint(1000,9999))
                    carnet=int(carnet)
                    datos=[nombreCompleto,carrera,correo]
                    matrizMentores[4][1][carnet]=datos
                cantMentores-=1
    return matrizMentores


def asignarMentores(matrizMentores,dicPrimerIngreso):
    print(matrizMentores)
    carnetsMentores=[]
    for estudiante in dicPrimerIngreso:
        for sede in matrizMentores:
            if dicPrimerIngreso[estudiante][3]=='CAMPUS TECNOLÓGICO CENTRAL CARTAGO' and sede[0]=='CTCC':
                for mentor in sede[1]:
                    if dicPrimerIngreso[estudiante][4]==sede[1][mentor][1]:
                        carnetsMentores.append(mentor)
                dicPrimerIngreso[estudiante][5]=random.choice(carnetsMentores)
                carnetsMentores=[]
            if dicPrimerIngreso[estudiante][3]=='CAMPUS TECNOLÓGICO LOCAL SAN CARLOS' and sede[0]=='CTLSC':
                for mentor in sede[1]:
                    if dicPrimerIngreso[estudiante][4]==sede[1][mentor][1]:
                        carnetsMentores+=[mentor]
                dicPrimerIngreso[estudiante][5]=random.choice(carnetsMentores)
                carnetsMentores=[]
            if dicPrimerIngreso[estudiante][3]=='CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ' and sede[0]=='CTLSJ':
                for mentor in sede[1]:
                    if dicPrimerIngreso[estudiante][4]==sede[1][mentor][1]:
                        carnetsMentores+=[mentor]
                dicPrimerIngreso[estudiante][5]=random.choice(carnetsMentores)
                carnetsMentores=[]
            if dicPrimerIngreso[estudiante][3]=='CENTRO ACADÉMICO DE ALAJUELA' and sede[0]=='CAA':
                for mentor in sede[1]:
                    if dicPrimerIngreso[estudiante][4]==sede[1][mentor][1]:
                        carnetsMentores+=[mentor]
                dicPrimerIngreso[estudiante][5]=random.choice(carnetsMentores)
                carnetsMentores=[]
            if dicPrimerIngreso[estudiante][3]=='CENTRO ACADÉMICO DE LIMÓN' and sede[0]=='CAL':
                for mentor in sede[1]:
                    if dicPrimerIngreso[estudiante][4]==sede[1][mentor][1]:
                        carnetsMentores+=[mentor]
                dicPrimerIngreso[estudiante][5]=random.choice(carnetsMentores)
                carnetsMentores=[]
    return dicPrimerIngreso

def sacarMentores(matrizMentores):
    dicMentores={}
    for sede in matrizMentores:
            dicMentores.update(sede[1])
    return dicMentores

matriz=[['CTCC', {2020019969: ['Cindy Garcia Eller', 'Ingeniería en Biotecnología', 'cgarcia@estudiantec.cr'], 2020018289: ['Janice Sparks Lewis', 'Administración de Empresas', 'jsparks@estudiantec.cr'], 2020011736: ['Kevin Laguire Brickell', 'Ingeniería en Computación', 'klaguire@estudiantec.cr'], 2020012464: ['John Campbell Fallis', 'Gestión en Turismo Sostenible', 'jcampbell@estudiantec.cr'], 2020015952: ['Adrienne Westlake Fisher', 'Enseñanza de la Matemática con Entornos Tecnológicos', 'awestlake@estudiantec.cr'], 2020014540: ['Shaun Coke Weaver', 'Administración de Tecnología de Información', 'scoke@estudiantec.cr'], 2020012719: ['Ryan Folse Blackaby', 'Ingeniería Ambiental', 'rfolse@estudiantec.cr'], 2020019876: ['Kristina Mcdonald Snow', 'Ingeniería en Electrónica', 'kmcdonald@estudiantec.cr'], 2020011084: ['Wanda Bisom Smith', 'Ingeniería Agronegocios', 'wbisom@estudiantec.cr'], 2020015205: ['Josephine Russell Risinger', 'Ingeniería en Computadores', 'jrussell@estudiantec.cr'], 2020018442: ['George Pat Chevrier', 'Ingeniería en Construcción', 'gpat@estudiantec.cr'], 2020016601: ['Hattie Cowell Renfrow', 'Ingeniería en Diseño Industrial', 'hcowell@estudiantec.cr'], 2020013254: ['Barbara Johnson Secor', 'Ingeniería en Materiales', 'bjohnson@estudiantec.cr'], 2020012913: ['Mallory James Propps', 'Ingeniería en Seguridad Laboral e Higiene Ambiental', 'mjames@estudiantec.cr'], 2020014941: ['Jason Dortch Morris', 'Ingeniería Física', 'jdortch@estudiantec.cr'], 2020016339: ['Amy Bush Spiney', 'Ingeniería Mecatrónica', 'abush@estudiantec.cr'], 2020013695: ['Jason Smith Moran', 'Ingeniería en Mantenimiento Industrial', 'jsmith@estudiantec.cr']}], ['CTLSC', {2020026032: ['John Dillard Chase', 'Administración de Empresas', 'jdillard@estudiantec.cr'], 2020023370: ['Quinn Celestin Waterbury', 'Ingeniería en Computación', 'qcelestin@estudiantec.cr'], 2020022827: ['Jacquelyn Hoffman Brow', 'Gestión en Turismo Rural Sostenible', 'jhoffman@estudiantec.cr'], 2020024563: ['Daniel Paletta Abston', 'Ingeniería en Electrónica', 
'dpaletta@estudiantec.cr'], 2020021179: ['William Erikson Ramirez', 'Ingeniería en Agronomía', 'werikson@estudiantec.cr'], 2020023250: ['Earnest Turner Smith', 'Ingeniería en Producción Industrial', 'eturner@estudiantec.cr']}], ['CTLSJ', {2020036372: ['Raeann Gardner Schaus', 'Arquitectura y Urbanismo', 'rgardner@estudiantec.cr'], 2020035685: ['Frances Williams Cater', 'Administración de Empresas', 'fwilliams@estudiantec.cr'], 2020037347: ['Barbara Edwards Griffin', 'Ingeniería en Computación', 'bedwards@estudiantec.cr'], 2020039302: ['Jose Jeffries James', 'Ingeniería en Computación', 'jjeffries@estudiantec.cr']}], ['CAA', {2020042789: ['Wade Garcia Wolfrom', 'Ingeniería en Computación', 'wgarcia@estudiantec.cr'], 2020045240: ['David Chambers Lombardo', 'Ingeniería en Computación', 'dchambers@estudiantec.cr'], 2020045454: ['David Buckman Lewis', 'Ingeniería en Electrónica', 'dbuckman@estudiantec.cr']}], ['CAL', {2020056602: ['Tom Cox Morgan', 'Administración de Empresas', 'tcox@estudiantec.cr'], 2020058582: ['Bessie Stacy Remus', 'Ingeniería en Computación', 'bstacy@estudiantec.cr'], 2020052485: ['Nancy Patrick Nakken', 'Ingeniería en Producción de Industrial', 'npatrick@estudiantec.cr']}]]

print(sacarMentores(matriz))