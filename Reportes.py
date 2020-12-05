def reporteMentor(matriz,matrizMentores):
    """
    Funcion:Guarda el archivo 
    Entrada:El nombre del archivo y la lista con los elementos
    Salida:nada o un mensaje de error
    """
    nomArchGrabar="Reporte_por_mentor.html"
    listaMentoresReportados=[]
    f=open(nomArchGrabar,"w",encoding="utf-8")
    f.writelines("<!DOCTYPE html>\n")
    f.writelines("<html lang="+"es"+">\n")
    for i in matriz:     
        if matriz[i][5] not in listaMentoresReportados:
            
            f.writelines("\t\t<Mentor>"+str(buscarMentor(matriz[i][5],matrizMentores)))
            for j in matriz:
                if matriz[j][5] == matriz[i][5]:
                    f.writelines("\n\t\t\t<Carnet>"+str(j)+"</Carnet>\n")
                    f.writelines("\t\t\t<Nombre>"+str(matriz[j][0])+"</Nombre>\n")
                    f.writelines("\t\t\t<Telefono>"+str(matriz[j][1])+"</Telefono>\n")
                    f.writelines("\t\t\t<Correo>"+str(matriz[j][2])+"</Correo>\n")
                    f.writelines("\t\t\t<Sede>"+str(matriz[j][3])+"</Sede>\n")
                    f.writelines("\t\t\t<Carrera>"+str(matriz[j][4])+"</Carrera>\n")
            listaMentoresReportados.append(matriz[i][5])
            f.writelines("\t\t</Mentor>\n\n")
    f.close()
    print("¡Archivo html creado correctamente!")
    return ""

def buscarMentor(carnet,matrizMentores):
    for i in matrizMentores:
        for j in i[1]:
            if j==carnet:
                return i[1][j][0]