#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 18/11/2020 6:12pm 
#Fecha de última Modificación: 5/12/2020 12:52pm
#Versión: 3.9.0
#Importaciones
def registroMentor(diccionario,matrizMentores):
    """
    Funcion:Guarda el archivo 
    Entrada:El nombre del archivo y la lista con los elementos
    Salida:nada o un mensaje de error
    """
    nomArchGrabar="Reporte_por_mentor.html"
    listaMentoresReportados=[]
    ultimaSede=""
    f=open(nomArchGrabar,"w",encoding="utf-8")
    f.writelines("<!DOCTYPE html>\n")
    f.writelines("<html lang="+"es"+">\n")
    f.writelines('<html>\n')
    f.writelines('<head>\n')
    f.writelines('<meta charset="UTF-8">\n')
    f.writelines('<title>Reporte Por Mentor</title>\n')
    f.writelines('</head>\n')
    f.writelines('<body>\n')
    f.writelines('\t<ul>\n')
    f.writelines('<h1>Proyecto IntegraTEC - Reporte por mentor.</h1>\n')
    f.writelines('<h2>Ordenamiento lista numerada.</h2>\n')
    for i in diccionario:
        if diccionario[i][3] != ultimaSede:
            ultimaSede= diccionario[i][3]
            f.writelines('<h3>'+str(ultimaSede)+'</h3>\n')
        if diccionario[i][5] not in listaMentoresReportados:
            listaMentoresReportados.append(diccionario[i][5])
            f.writelines('\t<li>'+'Mentor:'+buscarMentor(diccionario[i][5],matrizMentores)+'</li>\n')
            f.writelines('\t\t<ol>\n')
            for j in diccionario:
                if diccionario[i][5] in diccionario[j]:
                    f.writelines('\t\t\t<li>'+str(diccionario[j][0])+' '+str(diccionario[j][1])+' '+str(diccionario[j][2])+' '+str(diccionario[j][3])+' '+str(diccionario[j][4])+'</li>\n')
            f.writelines('\t\t</ol>\n')      
    f.writelines('\t</ul>\n')
    f.writelines("<!-- Documento HTML5 -->\n")
    f.writelines('</body>\n')
    f.writelines('</html>\n')
    print("¡Archivo html creado correctamente!\n")
    return ""

def buscarMentor(carnet,matrizMentores):
    for i in matrizMentores:
        for j in i[1]:
            if j==carnet:
                return i[1][j][0]

def registroCarrera(diccionario):
    """
    Funcion:Guarda el archivo 
    Entrada:El nombre del archivo y la lista con los elementos
    Salida:nada o un mensaje de error
    """
    nomArchGrabar="Reporte_por_carrera.html"
    listaCarreras=[]
    ultimaSede=''
    f=open(nomArchGrabar,"w",encoding="utf-8")
    f.writelines("<!DOCTYPE html>\n")
    f.writelines("<html lang="+"es"+">\n")
    f.writelines('<html>\n')
    f.writelines('<head>\n')
    f.writelines('<meta charset="UTF-8">\n')
    f.writelines('<title>Reporte Por Carrera</title>\n')
    f.writelines('</head>\n')
    f.writelines('<body>\n')
    f.writelines('<h1>Proyecto IntegraTEC - Reporte por carrera.</h1>\n')
    f.writelines('<h2>Ordenamiento lista no numerada.</h2>\n')
    f.writelines('\t<ul>\n')
    for i in diccionario:
        if diccionario[i][3] != ultimaSede:
            ultimaSede= diccionario[i][3]
            f.writelines('<h3>'+str(ultimaSede)+'</h3>\n')
        if (diccionario[i][4] + diccionario[i][3]) not in listaCarreras:
            listaCarreras.append(diccionario[i][4] + diccionario[i][3])
            f.writelines('\t<li>'+'Carrera: '+str(diccionario[i][4])+'</li>\n')
            f.writelines('\t\t<ul>\n')
            for j in diccionario:
                if diccionario[i][5] in diccionario[j]:
                    f.writelines('\t\t\t<li>'+str(diccionario[j][0])+' '+str(diccionario[j][1])+' '+str(diccionario[j][2])+' '+str(diccionario[j][3])+' '+str(diccionario[j][4])+'</li>\n')
            f.writelines('\t\t</ul>\n')      
    f.writelines('\t</ul>\n')
    f.writelines("<!-- Documento HTML5 -->\n")
    f.writelines('</body>\n')
    f.writelines('</html>\n')
    print("¡Archivo html creado correctamente!\n")

def registroSede(diccionario):
    """
    Funcion:Guarda el archivo 
    Entrada:El nombre del archivo y la lista con los elementos
    Salida:nada o un mensaje de error
    """
    nomArchGrabar="Reporte_por_sede.html"
    ultimaSede=''
    f=open(nomArchGrabar,"w",encoding="utf-8")
    f.writelines("<!DOCTYPE html>\n")
    f.writelines("<html lang="+"es"+">\n")
    f.writelines('<html>\n')
    f.writelines('<head>\n')
    f.writelines('<meta charset="UTF-8">\n')
    f.writelines('<title>Reporte Por Sede</title>\n')
    f.writelines('</head>\n')
    f.writelines('<body>\n')
    f.writelines('<h1>Proyecto IntegraTEC - Reporte por sede.</h1>\n')
    f.writelines('<h2>Ordenamiento tabla de datos.</h2>\n')
    for i in diccionario:
            if diccionario[i][3] != ultimaSede:
                ultimaSede= diccionario[i][3]
                f.writelines('<table class="egt">\n')
                f.writelines('<caption>'+str(ultimaSede)+'</caption>\n')
                f.writelines('\t<tr>\n')
                f.writelines('\t\t<th>'+"Carné"+'</th>\n')
                f.writelines('\t\t<th>'+"Nombre Completo"+'</th>\n')
                f.writelines('\t\t<th>'+"Numero de teléfono"+'</th>\n')
                f.writelines('\t\t<th>'+"Correo Electrónico"+'</th>\n')
                f.writelines('\t\t<th>'+"Sede"+'</th>\n')
                f.writelines('\t\t<th>'+"Carrera"+'</th>\n')
                f.writelines('\t\t<th>'+"Carnet del mentor"+'</th>\n')
                f.writelines('\t</tr>\n')
                for j in diccionario:
                    if diccionario[j][3]== ultimaSede:
                        f.writelines('\t<tr>\n')
                        f.writelines('\t\t<td>'+str(j)+'</td>\n')
                        f.writelines('\t\t<td>'+str(diccionario[j][0])+'</td>\n')
                        f.writelines('\t\t<td>'+str(diccionario[j][1])+'</td>\n')
                        f.writelines('\t\t<td>'+str(diccionario[j][2])+'</td>\n')
                        f.writelines('\t\t<td>'+str(diccionario[j][3])+'</td>\n')
                        f.writelines('\t\t<td>'+str(diccionario[j][4])+'</td>\n')
                        f.writelines('\t\t<td>'+str(diccionario[j][5])+'</td>\n')
                        f.writelines('\t</tr>\n')
    f.writelines("<!-- Documento HTML5 -->\n")
    f.writelines('</body>\n')
    f.writelines('</html>\n')
    print("¡Archivo html creado correctamente!\n")
    return 
