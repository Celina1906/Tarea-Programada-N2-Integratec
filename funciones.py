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
            

matriz=[['CTCC', {2020011605: ['Robert Randall Baca', 'Ingeniería en Biotecnología', 'rrandall@estudiantec.cr'], 2020016890: ['Orlando Harness Keith', 'Administración de Empresas', 'oharness@estudiantec.cr'], 2020011165: ['Rebecca Obrian Reid', 'Ingeniería en Computación', 'robrian@estudiantec.cr'], 2020017789: ['Juan Frazer Aldana', 'Gestión en Turismo Sostenible', 'jfrazer@estudiantec.cr'], 2020017045: ['Cindy Lee Sanchez', 'Enseñanza de la Matemática con Entornos Tecnológicos', 'clee@estudiantec.cr'], 2020017560: ['Paul Jephson Ortega', 'Administración de Tecnología de Información', 'pjephson@estudiantec.cr'], 2020014689: ['John Lawrence Maugeri', 'Ingeniería Agrícola', 'jolawrence@estudiantec.cr'], 2020015486: ['James Rm Dauphin', 'Ingeniería Ambiental', 'jrm@estudiantec.cr'], 2020017239: ['Susan Boren Drennen', 'Ingeniería en Electrónica', 'sboren@estudiantec.cr'], 
2020019828: ['Valerie Chung Taylor', 'Ingeniería Agronegocios', 'vchung@estudiantec.cr'], 2020014497: ['John Nevels Grundy', 'Ingeniería en Computadores', 'jnevels@estudiantec.cr'], 2020015982: ['Scott Bostwick Lundquist', 'Ingeniería en Construcción', 'sbostwick@estudiantec.cr'], 2020019799: ['Deana Gentry Sweet', 'Ingeniería en Diseño Industrial', 'dgentry@estudiantec.cr'], 2020014565: ['Karla Macaluso Adams', 'Ingeniería en Materiales', 'kmacaluso@estudiantec.cr'], 2020019841: ['John Brammer Dupre', 'Ingeniería en Producción Industrial', 'jbrammer@estudiantec.cr'], 2020016869: ['Vincent Watkins Greene', 'Ingeniería en Seguridad Laboral e Higiene Ambiental', 'vwatkins@estudiantec.cr'], 2020015832: ['Dorothy Rehrig Torres', 'Ingeniería Física', 'drehrig@estudiantec.cr'], 2020017431: ['Belinda Pack Bowers', 'Ingeniería Forestal', 'bpack@estudiantec.cr'], 2020011456: ['Benjamin Mitchell Creagh', 'Ingeniería Mecatrónica', 'bmitchell@estudiantec.cr'], 2020016486: ['Phillip Kimmel Budge', 'Ingeniería en Mantenimiento Industrial', 'pkimmel@estudiantec.cr']}], ['CTLSC', {2020024462: ['Frances Albrecht Mayle', 'Administración de Empresas', 'falbrecht@estudiantec.cr'], 2020025755: ['Luz Campas Campbell', 'Ingeniería en Computación', 'lcampas@estudiantec.cr'], 2020023808: ['Kathleen Zoellner Barnett', 
'Gestión en Turismo Rural Sostenible', 'kzoellner@estudiantec.cr'], 2020029536: ['Alma Cromer Frey', 'Ingeniería en Electrónica', 'acromer@estudiantec.cr'], 2020023887: ['Victor Gearhart Vang', 'Ingeniería en Agronomía', 'vgearhart@estudiantec.cr'], 2020025626: ['John Lane Estrada', 'Ingeniería en Producción Industrial', 'jlane@estudiantec.cr']}], ['CTLSJ', {2020037885: ['Frank Campbell Bailey', 'Arquitectura y Urbanismo', 'fcampbell@estudiantec.cr'], 2020035643: ['Jose Mallory Hogan', 'Administración de Empresas', 'jmallory@estudiantec.cr'], 2020034341: ['Philip Moore Poremski', 'Ingeniería en Computación', 'pmoore@estudiantec.cr']}], ['CAA', {2020044062: ['Joyce Wilson Hughes', 'Ingeniería en Computación', 'jwilson@estudiantec.cr'], 2020043610: ['Paul Bradley Babers', 'Ingeniería en Computación', 'pbradley@estudiantec.cr'], 2020047180: ['Christine Brinkman Bradley', 'Ingeniería en Electrónica', 'cbrinkman@estudiantec.cr']}], ['CAL', {2020059008: ['Allan Garcia Welke', 'Administración de Empresas', 'agarcia@estudiantec.cr'], 2020058125: ['Scott Smith Bravo', 'Ingeniería en Computación', 'scsmith@estudiantec.cr'], 2020053092: ['Carol Ivy Ray', 'Ingeniería en Producción de Industrial', 'civy@estudiantec.cr']}]]

dic={2021011277: ['Mildred Finneran Whittington', 68391195, 'mfinneran@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Biotecnología', 0], 2021016031: ['Betty Gray Norris', 75903484, 'bgray@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Biotecnología', 0], 2021018714: ['Shon Dicostanzo Koonce', 77870418, 'sdicostanzo@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Biotecnología', 0], 2021016202: ['Alan Torres Lewis', 82497472, 'atorres@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Biotecnología', 0], 2021018105: ['Jessica Hall Freeman', 65279043, 'jhall@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Biotecnología', 0], 2021017621: ['Melissa Boone Griffin', 88697275, 'mboone@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Biotecnología', 0], 2021019745: ['Vicki Pulliam Burch', 92739438, 'vpulliam@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Biotecnología', 0], 2021019759: ['Bertha Godfrey Hughes', 87401724, 'bgodfrey@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Biotecnología', 0], 2021012915: ['Priscilla Jordan King', 98049068, 'pjordan@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Administración de Empresas', 0], 2021012869: ['Angela Hearne Salas', 74245889, 'ahearne@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Administración de Empresas', 0], 2021019986: ['Ruth Wade Ruano', 76140810, 'rwade@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Administración de Empresas', 0], 2021018133: ['Joseph Robertson Furrow', 84358687, 'jrobertson@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Administración de Empresas', 
0], 2021016382: ['Keith Velasquez Austin', 99030846, 'kvelasquez@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Administración de Empresas', 0], 2021017228: ['Courtney Gore Potthoff', 71322823, 'cgore@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Computación', 0], 2021011111: ['Faye Davis Kressler', 69551724, 'fdavis@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Computación', 0], 2021019317: ['Albert Evers Cochran', 62822605, 'aevers@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Computación', 0], 2021012374: ['Joseph Kiefer Liston', 80984908, 'jkiefer@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Computación', 0], 2021018080: ['Jose Preston Hastings', 77647015, 'jpreston@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Gestión en Turismo Sostenible', 0], 2021011012: ['Robert Despain Sigler', 60087678, 'rdespain@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Gestión en Turismo Sostenible', 0], 2021015406: ['Bryan Cooper Martinez', 66608327, 'bcooper@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Gestión en Turismo Sostenible', 0], 2021015935: ['Adrienne Christenson Micucci', 85262487, 'achristenson@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Gestión en Turismo Sostenible', 0], 2021014795: ['Steve Cole Goshay', 77842576, 'scole@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Gestión en Turismo Sostenible', 0], 2021011790: ['Alice Jackson Jackson', 93270216, 'ajackson@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Enseñanza de la Matemática con Entornos Tecnológicos', 0], 2021011672: ['Mike Dunbar Mcafee', 91169723, 'mdunbar@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Enseñanza de la Matemática con Entornos Tecnológicos', 0], 2021012163: ['Bessie Scott Mays', 64024225, 'bscott@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Enseñanza de la Matemática con Entornos Tecnológicos', 0], 2021013680: ['Edwin Ray Williams', 70463720, 'eray@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Administración de Tecnología de Información', 0], 2021014196: ['John Reynolds Loepp', 69165653, 'jreynolds@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Administración de Tecnología de Información', 0], 2021016452: ['Norman Miller Berkley', 87288470, 'nmiller@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Administración de Tecnología de Información', 0], 2021019777: ['Anthony Maisonave Mosley', 60551377, 'amaisonave@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Agrícola', 0], 2021014019: ['Ronald Nadeau Tolles', 72366522, 'rnadeau@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Agrícola', 0], 2021017792: ['Shante Shapiro Bassett', 79060291, 'sshapiro@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Agrícola', 0], 2021019568: ['Lisa Gordon Schulweis', 88085768, 'lgordon@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Agrícola', 0], 2021015211: ['Lennie Bring Rice', 89293166, 'lbring@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Agrícola', 0], 2021013390: ['Dustin Knight Morris', 66334545, 'dknight@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Agrícola', 0], 2021018485: ['Mary Llanas Castillo', 64241082, 'mllanas@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Agrícola', 0], 2021016512: ['Jason Maldonado West', 65318365, 'jmaldonado@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Agrícola', 0], 2021011429: ['John Allen Smith', 66629103, 'jallen@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Ambiental', 0], 2021018898: ['Victoria Waynick Castro', 86612837, 'vwaynick@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Ambiental', 0], 2021013507: ['Kurt Norwood Cheng', 84822984, 'knorwood@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Ambiental', 0], 2021011207: ['Oren Ward Sokol', 64365956, 'oward@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Electrónica', 0], 2021016693: ['Eugene Thomas Hornsby', 96239546, 'ethomas@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Electrónica', 0], 2021017113: ['Dianna Montiel Platt', 94162039, 'dmontiel@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Electrónica', 0], 2021012245: ['Elizebeth Hernandez Perryman', 66272085, 'ehernandez@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Agronegocios', 0], 2021018793: ['Jennifer Dison Edwards', 76723291, 'jdison@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Agronegocios', 0], 2021011689: ['Angela King Thomas', 79205782, 'aking@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Agronegocios', 0], 2021012682: ['Mary Bundy Newton', 74526087, 'mbundy@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Agronegocios', 0], 2021018197: ['Christopher Whitehead Remick', 99561774, 'cwhitehead@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Agronegocios', 0], 2021017377: ['Jeremy Pope Curtis', 93270724, 'jpope@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Agronegocios', 0], 2021014600: ['Rebecca Davidson Beeson', 74212348, 'rdavidson@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Computadores', 0], 2021019359: ['Anna Johnson Hess', 73708522, 'ajohnson@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Construcción', 0], 2021011149: ['Tina Beaumont Cardinal', 97144619, 'tbeaumont@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Diseño Industrial', 0], 2021014838: ['Robbie Alston Yamakawa', 77354089, 'ralston@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Diseño Industrial', 0], 2021016861: ['Rhonda Porter Gifford', 65090186, 'rporter@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Materiales', 0], 2021014092: ['Tarah Pierce Brooks', 93241303, 'tpierce@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Materiales', 0], 2021011326: ['Gloria Gabaldon Snyder', 80061399, 'ggabaldon@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Materiales', 0], 2021018853: ['Sheila Crowell Marlin', 83866214, 'scrowell@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Materiales', 0], 2021016140: ['Wayne Gressler Delgado', 75367722, 'wgressler@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Producción Industrial', 0], 2021019406: ['Matthew Caberto Rafter', 87082133, 'mcaberto@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Producción Industrial', 0], 2021017366: ['James Mock Boucher', 76770471, 'jmock@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Producción Industrial', 0], 2021013422: ['Thomas Foster Scribner', 90873171, 'tfoster@estudiantec.cr', 
'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Producción Industrial', 0], 2021017982: ['Evelyn Williams Campbell', 93523799, 'ewilliams@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Producción Industrial', 0], 2021016261: ['Raymond Thammavongsa Summerfield', 94485508, 'rthammavongsa@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Producción Industrial', 0], 2021015556: ['Steve Corn Renteria', 75321235, 'scorn@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Producción Industrial', 0], 2021015711: ['Jeffrey Kolasinski Young', 94626830, 'jkolasinski@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Producción Industrial', 0], 2021013775: ['Sean Smith Matthews', 69381809, 'ssmith@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Producción Industrial', 0], 2021015438: ['Brian Webb Lavelle', 62265247, 'bwebb@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Producción Industrial', 0], 2021018820: ['Rhonda Juarez Kroll', 79677597, 'rjuarez@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Producción Industrial', 0], 2021013367: ['Micheal Richardson Collins', 97142077, 'mrichardson@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Seguridad Laboral e Higiene Ambiental', 0], 2021017827: ['Virginia Sewell Fields', 64264093, 'vsewell@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Física', 0], 2021014304: ['Dana Lewis Ricardo', 72063951, 'dlewis@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Física', 0], 2021013711: ['Allen Young Pepper', 88744144, 'ayoung@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Física', 0], 2021012941: ['Sara Green Williams', 91807048, 'sgreen@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Física', 0], 2021014556: ['Graciela Crumley Hanson', 79308856, 'gcrumley@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Física', 0], 2021015919: ['Philip Roberts Seman', 91861162, 'proberts@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Física', 0], 2021012936: ['Charles Livingston Bowen', 62089000, 'clivingston@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Forestal', 0], 2021014446: ['William Canty Parker', 61743903, 'wcanty@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Forestal', 0], 2021012552: ['Dana Burt Mingo', 98225269, 'dburt@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Forestal', 0], 2021013756: ['Grace White Venice', 72471872, 'gwhite@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Forestal', 0], 2021019242: ['George Spangler Mclean', 86857575, 
'gspangler@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Forestal', 0], 2021014416: ['Ryan Kendall Bryant', 94195109, 'rkendall@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Mecatrónica', 0], 2021012618: ['Christian Bernardo Brown', 76466813, 'cbernardo@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Mecatrónica', 0], 2021015451: ['Ronald Bradshaw Simoneavd', 85873080, 'rbradshaw@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Mecatrónica', 0], 2021018715: ['Elmer Gilkerson Hernandez', 97180029, 'egilkerson@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Mecatrónica', 0], 2021013981: ['Lee Vasquez Escarcega', 75867482, 'lvasquez@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Mantenimiento Industrial', 0], 2021015906: ['Diane Ostrow Armstrong', 
86622768, 'dostrow@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Mantenimiento Industrial', 0], 2021011325: ['Melissa Lee Fissel', 76960335, 'mlee@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Mantenimiento Industrial', 0], 2021024712: ['Maria Henry Perkins', 96122172, 'mhenry@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Administración de Empresas', 0], 2021028676: ['Carole Clark May', 93694162, 'cclark@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Administración de Empresas', 0], 2021029924: ['Edward Freeman Walker', 76159456, 'efreeman@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Administración de Empresas', 0], 2021025090: ['Karen Moore Bagley', 94968382, 'kmoore@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Administración de Empresas', 0], 2021025416: ['Ricky Johnson Bass', 85165569, 'rjohnson@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Administración de Empresas', 0], 2021025321: ['Silvia Shy Waddell', 66307728, 'sshy@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Administración de Empresas', 0], 2021025940: ['Roscoe Rohrbaugh French', 87240491, 'rrohrbaugh@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Administración de Empresas', 0], 2021023262: ['Brooke Tate Smith', 60116192, 'btate@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Computación', 0], 2021021464: ['Celia Ferrell Porterfield', 94517391, 'cferrell@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Computación', 0], 2021025145: ['Kathleen Sanzo Halas', 99790227, 'ksanzo@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Computación', 0], 2021026683: ['Scott Patrick Hill', 98981399, 'spatrick@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Computación', 0], 2021024958: ['Jean Avalos Miller', 96909865, 'javalos@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Computación', 0], 2021025214: ['Paul Prewitt Jenkins', 62057812, 'pprewitt@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Computación', 0], 2021021511: ['Nathaniel Stocker Jones', 92303768, 'nstocker@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Computación', 0], 2021025297: ['Dorris Rhodes Raxter', 89988008, 'drhodes@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Computación', 0], 2021026176: ['Mary Butterfield Thompson', 62222549, 'mbutterfield@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Gestión en Turismo Rural Sostenible', 0], 2021021389: ['Robert Stoviak Boehle', 79059904, 'rstoviak@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Gestión en Turismo Rural Sostenible', 0], 2021022871: ['Dan Washington Benway', 82867601, 'dwashington@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Gestión en Turismo Rural Sostenible', 0], 2021021836: ['Alan Roberts Scriven', 92698754, 'aroberts@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Gestión en Turismo Rural Sostenible', 0], 2021027646: ['Stacy Williamson Wilson', 67701832, 'swilliamson@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Gestión en Turismo Rural Sostenible', 0], 2021024240: ['Bernadine Jacobs Hernandez', 92537448, 'bjacobs@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Gestión en Turismo Rural Sostenible', 0], 2021021637: ['Katy Craig Harvey', 88185344, 'kcraig@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Gestión en Turismo Rural Sostenible', 0], 2021029072: ['Debbie Baker Aldridge', 71987103, 'dbaker@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Gestión en Turismo Rural Sostenible', 0], 2021022398: ['Gary Blue Horne', 79441642, 'gblue@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Gestión en Turismo Rural Sostenible', 0], 2021023835: ['Barbara Cooke Mora', 83575007, 'bcooke@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Gestión en Turismo Rural Sostenible', 0], 2021021397: ['David Krieg Slaybaugh', 62783574, 'dkrieg@estudiantec.cr', 
'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Electrónica', 0], 2021028232: ['Joseph Calloway Burkett', 98067926, 'jcalloway@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Electrónica', 0], 2021025398: ['Patricia Densmore Chiarelli', 68809479, 'pdensmore@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Electrónica', 0], 2021028858: ['Kevin Cambell Shelton', 71475356, 'kcambell@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Electrónica', 0], 2021029865: ['Mark Harris Brosnan', 66696168, 'mharris@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Electrónica', 0], 2021028130: ['John Tippets Fox', 85093526, 'jtippets@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Electrónica', 0], 2021024362: ['Geoffrey James Smith', 62299411, 'gjames@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Electrónica', 0], 2021025537: ['Ronda Walsh Stockton', 77730927, 'rwalsh@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Electrónica', 0], 2021022247: ['Jennifer Johnson Oliveros', 85369679, 'jjohnson@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Electrónica', 0], 2021029733: ['Andrea Pena Sheehan', 88375832, 'apena@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Electrónica', 0], 2021022799: ['Pamela Slusser Dial', 97226852, 'pslusser@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Agronomía', 0], 2021023394: ['Amanda Camacho Milliken', 91731460, 'acamacho@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Agronomía', 0], 2021027163: ['Teresa Imler Congress', 75326189, 'timler@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Agronomía', 0], 2021024942: ['Jerry Roberson Bass', 91561603, 'jroberson@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Agronomía', 0], 2021026549: ['Donald Holm Hassler', 87065827, 'dholm@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Agronomía', 0], 2021024980: ['Marilyn Chapman Sagon', 80633930, 'mchapman@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Agronomía', 0], 2021022758: ['Donna Do Stonge', 82943044, 'ddo@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Agronomía', 0], 2021023214: ['Robin Spraglin Hunt', 92601887, 'rspraglin@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Agronomía', 0], 2021023331: ['Michael Dennis Mcbride', 97698233, 'mdennis@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Agronomía', 0], 2021024983: ['Jessie Henline Skinner', 76124815, 'jhenline@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Producción Industrial', 0], 2021023497: ['Mike Burse Miller', 95134035, 'mburse@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Producción Industrial', 0], 2021028176: ['Victor Hillin Arriola', 72409950, 'vhillin@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Producción Industrial', 0], 2021026669: ['Tom Schaible Sobus', 61750389, 'tschaible@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Producción Industrial', 0], 2021021729: ['Diana Hobson Mitchell', 74371964, 'dhobson@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Producción Industrial', 0], 2021026733: ['Bernice Delorey Walker', 96741391, 'bdelorey@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Producción Industrial', 0], 2021021563: ['Eva Hinds Myers', 90264495, 'ehinds@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Producción Industrial', 0], 2021025893: ['Joseph Weems Meyer', 92454044, 'jweems@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Producción Industrial', 0], 2021038974: ['Bethany Keiper List', 72687413, 'bkeiper@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo', 0], 2021036979: ['Frank Younglas Diamond', 68384399, 'fyounglas@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo', 0], 2021039072: ['Jason Buchanan Jones', 
76826753, 'jbuchanan@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo', 0], 2021034511: ['Randy Mcghee Tant', 79970292, 'rmcghee@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo', 0], 2021035301: ['Helen Salazar Savoie', 64110973, 'hsalazar@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo', 0], 2021037145: ['Carolyn Blanchard Soria', 83490490, 'cblanchard@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo', 0], 2021038475: ['Marian Troupe Moore', 89474555, 'mtroupe@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo', 0], 2021031438: ['Tim Vayner Davis', 61132968, 'tvayner@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo', 0], 2021038311: ['Anthony Partee Ward', 93573980, 'apartee@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo', 0], 2021034018: ['Markita Burns Cardoso', 90707332, 'mburns@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo', 0], 2021037221: ['Patrick Moss Sanchez', 78653778, 'pmoss@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo', 0], 2021034054: ['Robert Mchugh Johnson', 73307615, 'rmchugh@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo', 0], 2021039042: ['Edward Adkinson Burch', 80562677, 'eadkinson@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo', 0], 2021035159: ['Louise Hansen Lynch', 85575712, 'lhansen@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo', 0], 2021036339: ['Jesus Huey Brown', 86762462, 'jhuey@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo', 0], 2021033685: ['Esperanza Fox Bakken', 82575685, 'efox@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo', 0], 2021035265: ['Dorothy Zavala Driskell', 88157887, 'dzavala@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas', 0], 2021039378: ['Kyle Craft Groce', 78630998, 'kcraft@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas', 0], 2021033269: ['Tanya Bailey Serdula', 94308971, 'tbailey@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas', 0], 2021039733: ['Randall Mann Rodgers', 90347207, 'rmann@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas', 0], 2021033721: ['Robert Turner Faz', 79105382, 'rturner@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas', 0], 2021039742: ['Michele Calloway Stapleton', 88831831, 'mcalloway@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 
'Administración de Empresas', 0], 2021032537: ['Kenneth Burks Boyd', 71604805, 'kburks@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas', 0], 2021037900: ['Joan Adams Elrod', 60188452, 'jadams@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas', 0], 2021035430: ['Patricia Mora Alvaro', 95899171, 'pmora@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas', 0], 2021037888: ['Phillip Wheeler Lopez', 99980947, 'pwheeler@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas', 0], 2021033505: ['Phyllis Groce Rother', 64250265, 'pgroce@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas', 0], 2021033781: ['Scott Rehrig Anderson', 99464951, 'srehrig@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas', 0], 2021032920: ['Nathaniel Kawachi Barbosa', 61764811, 'nkawachi@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas', 0], 2021031663: ['James Alvarado Haley', 62625645, 'jalvarado@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas', 0], 2021036875: ['Stephen Kirkpatrick Dove', 74546041, 'skirkpatrick@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas', 0], 2021032091: ['Janice Carter Pullen', 65820260, 'jcarter@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Ingeniería en Computación', 0], 2021036879: ['Walter Hanson Gosselin', 67022050, 'whanson@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Ingeniería en Computación', 0], 2021038828: ['Russell Isaacs Neely', 98331995, 'risaacs@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Ingeniería en Computación', 0], 2021034433: ['Victor Jensen Eddy', 60167031, 'vjensen@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Ingeniería en Computación', 0], 2021039219: ['Randy Cooper Brown', 76687210, 'rcooper@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Ingeniería en Computación', 0], 2021032492: ['William Gabbard Dunn', 87647546, 'wgabbard@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Ingeniería en Computación', 0], 2021034405: ['Faye Kemper Babena', 94057730, 'fkemper@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Ingeniería en Computación', 0], 2021034943: ['Myrna Johnson Charles', 70967041, 'mjohnson@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Ingeniería en Computación', 0], 
2021036308: ['Tina Blakeley Proper', 92472927, 'tblakeley@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Ingeniería en Computación', 0], 2021035498: ['Luis Walsh Ratterree', 94693584, 'lwalsh@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Ingeniería en Computación', 0], 2021034884: ['Joanna Humphrey Lewis', 99823258, 'jhumphrey@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Ingeniería en Computación', 0], 2021036884: ['Micheal Reeves Jordan', 92071503, 'mreeves@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Ingeniería en Computación', 0], 2021031272: ['Heather Fleming Taylor', 84754051, 'hfleming@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Ingeniería en Computación', 0], 2021032016: ['Jesse Murphy Sanchez', 80569273, 'jmurphy@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Ingeniería en Computación', 0], 2021039995: ['John Cormier Ayala', 75725569, 'jcormier@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Ingeniería en Computación', 0], 2021037770: ['Judy Macias Cabrera', 67613706, 'jmacias@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Ingeniería en Computación', 0], 2021041416: ['Deborah Ratzlaff Davis', 89628050, 'dratzlaff@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021042407: ['Michael Abreu Fitzpatrick', 93809000, 'mabreu@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021042695: ['Margaret Hodge Patterson', 81558637, 'mhodge@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021042789: ['Theresa Summers Cunanan', 74641992, 'tsummers@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021047301: ['Kenneth Martz Gonzalez', 93437964, 'kmartz@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021047918: ['Doris Strahl Dey', 94327611, 'dstrahl@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021044835: ['Willard Mcvay Sullivan', 96143512, 'wmcvay@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021045921: ['John Bowie Newman', 96022226, 'jbowie@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021048316: ['Jill Sullivan Bontrager', 82592844, 'jsullivan@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021044869: ['Rex Murphy Millican', 71494146, 'rmurphy@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021043437: ['Donna Gilbertson Zambrano', 90649613, 'dgilbertson@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021044585: ['Mathew Titus Mckelvey', 78731743, 'mtitus@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021044192: ['Ellen Henry Johnson', 78724409, 'ehenry@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021042537: ['Virginia Alcantar Nolan', 78492054, 'valcantar@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021041063: ['David Mitchell Davis', 90024281, 'dmitchell@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021047790: ['Joseph Cooley Fuqua', 82722997, 'jcooley@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021046022: ['Susanne Mcclendon Alamilla', 93181488, 'smcclendon@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021041749: ['Edith Mccullough Mier', 68531762, 'emccullough@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021048338: ['Diane Lloyd Brown', 71525853, 'dlloyd@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021041189: ['Alex Calhoon Jordan', 69336253, 'acalhoon@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 
0], 2021042642: ['Elizabeth Roberts Greggs', 64997694, 'eroberts@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021045156: ['Annette Dickerson Slade', 92373309, 'adickerson@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021047361: ['Douglas Shaddox Starks', 76221650, 'dshaddox@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021049666: ['Frank Bennett Binette', 60309626, 'fbennett@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021043869: 
['Jean Welke Dueber', 95538477, 'jwelke@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación', 0], 2021048516: ['Karen Nelson Schmidt', 97578199, 'knelson@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica', 0], 2021043029: ['Gene Ahmann Rodriquez', 78964920, 'gahmann@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica', 0], 2021046720: ['Scott Haug Tingley', 71365150, 'shaug@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica', 0], 2021047251: ['Robert Contreras Williemae', 79852091, 'rcontreras@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica', 0], 2021042255: ['Mary Zazula Johnson', 71611758, 'mzazula@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica', 0], 2021046755: ['Michael Dyer Nagy', 72714335, 'mdyer@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica', 0], 2021047722: ['Homer Willian Berenbaum', 66188383, 'hwillian@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica', 0], 2021047547: ['Jaime Lawrence Logan', 62560561, 'jlawrence@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica', 0], 2021048383: ['Genevieve Mobley Towe', 66553591, 'gmobley@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica', 0], 2021048279: ['Roger Estes Granger', 93240995, 'restes@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica', 0], 2021049745: ['John Santamaria Kille', 75662283, 'jsantamaria@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica', 0], 2021046400: ['Pamula Rohm King', 99625927, 'prohm@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica', 0], 2021043384: ['Shaun Mckinney Goulet', 94234805, 'smckinney@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica', 0], 2021048314: ['Lisa Jacobs Tapper', 84013430, 'ljacobs@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica', 0], 2021048703: ['Benito Wible Bozeman', 71987688, 'bwible@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica', 0], 2021047459: ['Thomas Bohannon Lee', 87118121, 'tbohannon@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica', 0], 2021047825: ['Robert Rosen Boerger', 91428507, 'rrosen@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica', 0], 2021045812: ['Grace Williams Joyner', 63199951, 'gwilliams@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica', 0], 2021054137: ['Michael Lang Hutchins', 93986937, 'mlang@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Administración de Empresas', 0], 2021059065: ['Elizabeth Latham Doss', 67673684, 'elatham@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Administración de Empresas', 0], 2021054389: ['Tommy Shumpert Thornton', 88770593, 'tshumpert@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Administración de Empresas', 0], 2021051275: ['Mark Tatum Escobedo', 98066704, 'mtatum@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Computación', 0], 2021058475: ['Carlos Lindsey Reilly', 61681865, 'clindsey@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Computación', 0], 2021059318: ['Heriberto Holderfield Jervey', 89225763, 'hholderfield@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Computación', 0], 2021055837: ['William Guidry Wren', 63213156, 'wguidry@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Computación', 0], 2021056796: ['Mark Sandlin Gullatt', 60340773, 'msandlin@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Computación', 0], 2021059094: ['Deborah Paramo Fambrough', 98411681, 'dparamo@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Producción de Industrial', 0], 2021057371: ['Leonel Peveler Rogers', 71887141, 'lpeveler@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Producción de Industrial', 0], 2021059709: ['Krystal Smart Garrett', 69408597, 'ksmart@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Producción de Industrial', 0], 2021057901: ['Michael Spears Soto', 67936659, 'mspears@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Producción de Industrial', 0], 2021056819: ['Willis Roberts Foster', 88100922, 'wroberts@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Producción de Industrial', 0], 2021052428: ['Megan Story Coltrain', 78327839, 'mstory@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Producción de Industrial', 0], 2021056825: ['Elbert Dufrene Amos', 86943909, 'edufrene@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Producción de Industrial', 0]}

#print(asignarMentores(matriz,dic))