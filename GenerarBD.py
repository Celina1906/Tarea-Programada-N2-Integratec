import csv
import datetime
def crearDB(dic,matriz):
    tiempo=datetime.datetime.now()
    nombreArchivo=""
    with open("BDIntegraTEC" + str(tiempo.day) +"-"+ str(tiempo.month) +"-"+ str(tiempo.year) +"_"+str(tiempo.hour) +"-"+ str(tiempo.minute) +".csv","w",newline="") as cvsfile:
        nombreDeCampos=["Sede","Carrera","Carné","Nombre","Correo","Teléfono","Mentor"]
        escribir= csv.DictWriter(cvsfile,fieldnames=nombreDeCampos)
        escribir.writeheader()
        #!Espera dic Estudiantes
        for i in dic:
            escribir.writerow({"Sede":dic[i][3],"Carrera":dic[i][4],"Carné":i,"Nombre":dic[i][0],"Correo":dic[i][2],"Teléfono":dic[i][1],"Mentor":False})
        #!Espera dic Mentores
        #ToDO: De momento espera una matriz igual a estudiantes, sin embargo es facilmente adaptable, TRUE al final añadido
        for sede in matriz:
            for mentor in sede[1]:
                if sede[0] == 'CTCC':
                    nomSede='CAMPUS TECNOLÓGICO CENTRAL CARTAGO'
                elif sede[0]=='CTLSC':
                    nomSede='CAMPUS TECNOLÓGICO LOCAL SAN CARLOS'
                elif sede[0]=='CTLSJ':
                    nomSede='CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ'
                elif sede[0]=='CAA':
                    nomSede='CENTRO ACADÉMICO DE ALAJUELA'
                else:
                   nomSede='CENTRO ACADÉMICO DE LIMÓN'
                escribir.writerow({"Sede":nomSede,"Carrera":sede[1][mentor][1],"Carné":mentor,"Nombre":sede[1][mentor][0],"Correo":sede[1][mentor][2],"Teléfono":'No aplica',"Mentor":True})
        nombreArchivo="BDIntegraTEC" + str(tiempo.day) +"-"+ str(tiempo.month) +"-"+ str(tiempo.year) +"_"+str(tiempo.hour) +"-"+ str(tiempo.minute) +".csv"
        return nombreArchivo
