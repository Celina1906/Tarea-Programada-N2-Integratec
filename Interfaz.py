#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 18/11/2020 6:12pm 
#Fecha de última Modificación: 5/12/2020 9:32pm
#Versión: 3.9.0
#Importaciones
from tkinter import*
from funciones import *
from GenerarBD import *
from Archrequests import *
from Archivos import *
from Correo import *
from Registros import registroCarrera,registroSede,registroMentor
#Variables globales
matrizSedesYCarreras=quitaRepetidos(obtenerCarreras())
matrizSedesEst=[]
dicPrimerIngreso={}
matrizMentores=[['CTCC',{}],['CTLSC',{}],['CTLSJ',{}],['CAA',{}],['CAL',{}]]
ultimoArchivoCreado=None
nomArchivo='mentores'
archivoDB=""
#Ventana Principal
ventanaPrincipal=Tk()
ventanaPrincipal.title('Integratec')
ventanaPrincipal.geometry('800x300')
ventanaPrincipal.resizable(FALSE,FALSE)
ventanaPrincipal.configure(bg='Teal')
labelTitulo = Label(ventanaPrincipal, text = "Integratec" , bg="Teal", fg="Azure", font = ('calibri', 40))
labelTitulo.place(x=20,y=30)
#Funciones
#Función botón 1
def estudiantesPorSede(): 
    '''
    Funcionamiento: Define la cantidad de estudiantes de primer ingreso que entran por sede 
    Entradas: NA
    Salidas: NA
    '''  
    ventana1=Tk()
    ventana1.title('Estudiantes por sede')
    ventana1.geometry('800x600')
    ventana1.resizable(FALSE,FALSE)
    labelTitulo1 = Label(ventana1, text = "Estudiantes por sede" , bg="Teal", fg="Azure", font = ('calibri', 40))
    labelTitulo.place(x=20,y=30)
    ventana1.configure(bg='Teal')
    labelTitulo1.place(x=40, y=20)
    labelEstudiantes=Label(ventana1,text='Digite la cantidad de estudiantes de primer ingreso por cada sede ', bg='Teal', font=('arial',15))
    labelEstudiantes.place(x=50,y=120)
    labelCartago=Label(ventana1,text='CAMPUS TECNOLÓGICO CENTRAL CARTAGO:', bg='Teal',font=('',13))
    labelCartago.place(x=50,y=200)
    entryCartago=Entry(ventana1)
    entryCartago.place(x=420,y=200)
    labelSanCarlos=Label(ventana1,text='CAMPUS TECNOLÓGICO LOCAL SAN CARLOS:', bg='Teal',font=('',13))
    labelSanCarlos.place(x=50,y=250)
    entrySanCarlos=Entry(ventana1)
    entrySanCarlos.place(x=420,y=250)
    labelSanJose=Label(ventana1,text='CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ:', bg='Teal',font=('',13))
    labelSanJose.place(x=50,y=300)
    entrySanJose=Entry(ventana1)
    entrySanJose.place(x=420,y=300)
    labelAlajuela=Label(ventana1,text='CAMPUS TECNOLÓGICO LOCAL ALAJUELA:', bg='Teal',font=('',13))
    labelAlajuela.place(x=50,y=350)
    entryAlajuela=Entry(ventana1)
    entryAlajuela.place(x=420,y=350)
    labelLimon=Label(ventana1,text='CAMPUS TECNOLÓGICO LOCAL LIMÓN:', bg='Teal',font=('',13))
    labelLimon.place(x=50,y=400)
    entryLimon=Entry(ventana1)
    entryLimon.place(x=420,y=400)
    def obtenerCantidades():
        '''
        Funcionamiento: Revisa si los datos ingresados son correctos y de ser así crea el diccionario de primeros ingresos
        Entradas: NA
        Salidas: NA
        '''  
        global matrizSedesYCarreras
        global matrizSedesEst
        try:
            cantCartago=int(entryCartago.get())
            cantSanCarlos=int(entrySanCarlos.get())
            cantSanJose=int(entrySanJose.get())
            cantAlajuela=int(entryAlajuela.get())
            cantLimon=int(entryLimon.get())
            listaCantidad=[cantSanJose,cantCartago,cantSanCarlos,cantLimon,cantAlajuela]
            listaSede=["CTLSJ","CTCC","CTLSC","CAL","CAA"]
            matrizSedesEst=crearMatrizGeneral(matrizSedesYCarreras,listaCantidad,listaSede)
            boton2['state']=NORMAL
            boton3['state']=NORMAL
            ventanaExito=Tk()
            ventanaExito.title('Datos Ingresados')
            ventanaExito.geometry('550x150')
            ventanaExito.resizable(FALSE,FALSE)
            labelExito=Label(ventanaExito,text='Datos ingresados con éxito ', bg='Teal', font=('arial',20))
            labelExito.place(x=100,y=50)
            ventanaExito.configure(bg='Teal')
            ventanaExito.mainloop()
        except:
            ventanaError=Tk()
            ventanaError.title('ERROR')
            ventanaError.geometry('600x200')
            ventanaError.resizable(FALSE,FALSE)
            labelError=Label(ventanaError,text='ERROR: Datos ingresados no válidos ', bg='Tomato', fg='AliceBlue', font=('arial',20))
            labelError.place(x=50,y=100)
            ventanaError.configure(bg='Tomato')
            ventanaError.mainloop()
    botonAceptar=Button(ventana1,text='Aceptar',width=18,height=2,command=obtenerCantidades)
    botonAceptar.place(x=200,y=500)
    botonVolver=Button(ventana1,text='Volver al menú principal',width=20,height=2,command= lambda:ventana1.destroy())
    botonVolver.place(x=400,y=500) 
    ventana1.mainloop()
#Función botón 2
def estudiatesDeCarreraPorSede():
    '''
    Funcionamiento: Crea dinámicamente la base de datos de todos los admitidos en cada carrera por cada sede 
    Entradas: NA
    Salidas: NA
    '''  
    global matrizSedesEst, dicPrimerIngreso
    ventana2=Tk()
    ventana2.config(bg='Teal')
    ventana2.title('Estudiantes de carrera por sede')
    ventana2.geometry('600x200')
    ventana2.resizable(FALSE,FALSE)
    dicPrimerIngreso=crearDicPrimerIngreso(matrizSedesEst,dicPrimerIngreso)
    print(dicPrimerIngreso)
    labelTitulo2 = Label(ventana2, text = "Base de datos creada satisfactoriamente" , bg="Teal", fg="Azure", font = ('calibri', 20))
    labelTitulo2.place(x=50,y=50)
    botonVolver=Button(ventana2,text='Volver al menú principal',width=20,height=2,command= lambda:ventana2.destroy())
    botonVolver.place(x=200,y=100)
    boton5['state']=NORMAL
    ventana2.mainloop()
#Función botón 3
def crearMentores():
    '''
    Funcionamiento: Dada la cantidad de estudiantes de primer ingreso generados por sede en cada carrera, crea un 5% de mentores en esa carrera es esa sede
    Entradas: NA
    Salidas: NA
    '''  
    global matrizSedesEst, dicPrimerIngreso,matrizMentores 
    matrizMentores=crearMatMentores(matrizSedesEst,dicPrimerIngreso,matrizMentores)
    graba(nomArchivo,matrizMentores)
    print(matrizMentores)
    ventana3=Tk()
    ventana3.config(bg='Teal')
    ventana3.title('Crear mentores')
    ventana3.geometry('600x200')
    ventana3.resizable(FALSE,FALSE)
    labelTitulo3 = Label(ventana3, text = "Mentores creados satisfactoriamente" , bg="Teal", fg="Azure", font = ('calibri', 20))
    labelTitulo3.place(x=50,y=50)
    botonVolver=Button(ventana3,text='Volver al menú principal',width=20,height=2,command= lambda:ventana3.destroy())
    botonVolver.place(x=200,y=100)
    boton4['state']=NORMAL
    ventana3.mainloop()
#Función botón 4
def asignarMentor():
    '''
    Funcionamiento: asigna a los estudiantes con misma carrera y sede de forma distribuida a los mentores.
    Entradas: NA
    Salidas: NA
    '''  
    global dicPrimerIngreso,matrizMentores 
    dicPrimerIngreso=asignarMentores(matrizMentores,dicPrimerIngreso)
    print(dicPrimerIngreso)
    ventana4=Tk()
    ventana4.config(bg='Teal')
    ventana4.title('Crear mentores')
    ventana4.geometry('600x200')
    ventana4.resizable(FALSE,FALSE)
    labelTitulo4 = Label(ventana4, text = "Mentores asignados satisfactoriamente" , bg="Teal", fg="Azure", font = ('calibri', 20))
    labelTitulo4.place(x=50,y=50)
    botonVolver=Button(ventana4,text='Volver al menú principal',width=20,height=2,command= lambda:ventana4.destroy())
    botonVolver.place(x=200,y=100)
    ventana4.mainloop()
#Función botón 5
def actualizarEstudiante():
    '''
    Funcionamiento: modifica los datos de algún estudiante.
    Entradas: NA
    Salidas: NA
    '''  
    ventana5=Tk()
    ventana5.config(bg='Teal')
    ventana5.title('Actualizar estudiante')
    ventana5.geometry('600x300')
    ventana5.resizable(FALSE,FALSE)
    labelTitulo=Label(ventana5,text='Actualizar estudiante', bg='Teal',fg="Azure", font=('arial',20))
    labelTitulo.place(x=150,y=50)
    def pedirCarnetPrimerIngreso():
        '''
        Funcionamiento: pide el carnet de un primer ingreso.
        Entradas: NA
        Salidas: NA
        '''  
        ventana5=Tk()
        ventana5.config(bg='Teal')
        ventana5.title('Actualizar estudiante')
        ventana5.geometry('600x300')
        ventana5.resizable(FALSE,FALSE)
        labelTitulo=Label(ventana5,text='Actualizar estudiante', bg='Teal',fg="Azure", font=('arial',20))
        labelTitulo.place(x=150,y=50)
        labelCarnet=Label(ventana5,text='Carnet del estudiante: ',bg='Teal',font=('',15))
        labelCarnet.place(x=110,y=130)
        entryCarnet=Entry(ventana5)
        entryCarnet.place(x=310,y=130,width=140,height=30)
        def buscarCarnetPrimerIngreso():
            '''
            Funcionamiento: busca el carnet de un primer ingreso.
            Entradas: NA
            Salidas: NA
            '''  
            global dicPrimerIngreso 
            bandera=0   
            for estudiante in dicPrimerIngreso:
                try:
                    int(entryCarnet.get())
                except:
                    ventanaError=Tk()
                    ventanaError.title('ERROR')
                    ventanaError.geometry('600x200')
                    ventanaError.resizable(FALSE,FALSE)
                    labelError=Label(ventanaError,text='ERROR: Dato ingresado no válido ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                    labelError.place(x=50,y=100)
                    ventanaError.configure(bg='Tomato')
                    ventanaError.mainloop()
                if estudiante==int(entryCarnet.get()):
                    bandera=1
                    ventanaActualizar=Tk()
                    ventanaActualizar.config(bg='Teal')
                    ventanaActualizar.title('Actualizar primer ingreso')
                    ventanaActualizar.geometry('700x500')
                    ventanaActualizar.resizable(FALSE,FALSE)
                    labelTitulo=Label(ventanaActualizar,text='Actualizar primer ingreso', bg='Teal',fg="Azure", font=('arial',20))
                    labelTitulo.place(x=200,y=50)
                    labelNombre=Label(ventanaActualizar,text='Nombre completo del estudiante: ',bg='Teal',font=('',15))
                    labelNombre.place(x=50,y=130)
                    entryNombre=Entry(ventanaActualizar)
                    entryNombre.place(x=360,y=130,width=200,height=30)
                    labelTelefono=Label(ventanaActualizar,text='Teléfono del estudiante: ',bg='Teal',font=('',15))
                    labelTelefono.place(x=50,y=200)
                    entryTelefono=Entry(ventanaActualizar)
                    entryTelefono.place(x=360,y=200,width=200,height=30)
                    labelCorreo=Label(ventanaActualizar,text='Correo del estudiante: ',bg='Teal',font=('',15))
                    labelCorreo.place(x=50,y=270)
                    entryCorreo=Entry(ventanaActualizar)
                    entryCorreo.place(x=360,y=270,width=200,height=30)
                    def actualizarPrimerIngreso():
                        '''
                        Funcionamiento: actualiza los datos de un primer ingreso.
                        Entradas: NA
                        Salidas: NA
                        '''  
                        if not re.match("^\d{8}$",entryTelefono.get()):
                            ventanaError=Tk()
                            ventanaError.title('ERROR')
                            ventanaError.geometry('750x200')
                            ventanaError.resizable(FALSE,FALSE)
                            labelError=Label(ventanaError,text='ERROR: El formato del número de teléfono no es válido ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                            labelError.place(x=10,y=100)
                            ventanaError.configure(bg='Tomato')
                            ventanaError.mainloop()
                            botonAceptarAc=Button(ventanaActualizar,text='Aceptar',width=18,height=2,command=actualizarPrimerIngreso)
                            botonAceptarAc.place(x=260,y=380)
                            ventanaError.mainloop()
                        elif (entryTelefono.get()[0]!='6' and entryTelefono.get()[0]!='7' and entryTelefono.get()[0]!='8' and entryTelefono.get()[0]!='9'):
                            ventanaError=Tk()
                            ventanaError.title('ERROR')
                            ventanaError.geometry('750x200')
                            ventanaError.resizable(FALSE,FALSE)
                            labelError=Label(ventanaError,text='ERROR: El formato del número de teléfono no es válido ', bg='Tomato', fg='AliceBlue',font=('arial',20))
                            labelError.place(x=5,y=150)
                            ventanaError.configure(bg='Tomato')
                            ventanaError.mainloop()
                            botonAceptarAc=Button(ventanaActualizar,text='Aceptar',width=18,height=2,command=actualizarPrimerIngreso)
                            botonAceptarAc.place(x=260,y=380)
                            ventanaError.mainloop()
                        elif not re.match("[^@]+@[^@]+\.[^@]+",entryCorreo.get()):
                            ventanaError=Tk()
                            ventanaError.title('ERROR')
                            ventanaError.geometry('600x200')
                            ventanaError.resizable(FALSE,FALSE)
                            labelError=Label(ventanaError,text='ERROR: El formato del correo no es válido ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                            labelError.place(x=5,y=150)
                            ventanaError.configure(bg='Tomato')
                            ventanaError.mainloop()
                            botonAceptarAc=Button(ventanaActualizar,text='Aceptar',width=18,height=2,command=actualizarPrimerIngreso)
                            botonAceptarAc.place(x=260,y=380)
                            ventanaError.mainloop()
                        elif entryCorreo.get() in sacarDatosMentores(matrizMentores) or entryCorreo.get() in sacarDatosPrimerIngreso(dicPrimerIngreso) or  int(entryTelefono.get()) in sacarDatosPrimerIngreso(dicPrimerIngreso):
                            ventanaError=Tk()
                            ventanaError.title('ERROR')
                            ventanaError.geometry('600x300')
                            ventanaError.resizable(FALSE,FALSE)
                            labelError=Label(ventanaError,text='ERROR: Datos ingresados repetidos  ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                            labelError.place(x=50,y=150)
                            ventanaError.configure(bg='Tomato')
                            ventanaError.mainloop()
                            botonAceptarAc=Button(ventanaActualizar,text='Aceptar',width=18,height=2,command=actualizarPrimerIngreso)
                            botonAceptarAc.place(x=260,y=380)
                            ventanaError.mainloop()
                        else:
                            dicPrimerIngreso[int(entryCarnet.get())][0]=entryNombre.get()
                            dicPrimerIngreso[int(entryCarnet.get())][1]=int(entryTelefono.get())
                            dicPrimerIngreso[int(entryCarnet.get())][2]=entryCorreo.get()
                            print(dicPrimerIngreso)
                            ventanaCambio=Tk()
                            ventanaCambio.title('Datos cambiados')
                            ventanaCambio.geometry('600x300')
                            ventanaCambio.resizable(FALSE,FALSE)
                            labelCambio=Label(ventanaCambio,text='Datos cambiados con éxito ', bg='Teal', font=('arial',20))
                            labelCambio.place(x=50,y=150)
                            ventanaCambio.configure(bg='Teal')
                            ventanaCambio.mainloop()
                    botonAceptar2=Button(ventanaActualizar,text='Aceptar',width=18,height=2,command=actualizarPrimerIngreso)
                    botonAceptar2.place(x=240,y=350)
            if bandera==0:
                ventanaNo=Tk()
                ventanaNo.title('No se encontró el estudiante')
                ventanaNo.geometry('600x300')
                ventanaNo.resizable(FALSE,FALSE)
                labelNo=Label(ventanaNo,text='No se encontró un estudiante con ese carnet ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                labelNo.place(x=20,y=150)
                ventanaNo.configure(bg='Tomato')
                ventanaNo.mainloop()
        botonAceptar=Button(ventana5,text='Aceptar',width=18,height=2,command=buscarCarnetPrimerIngreso)
        botonAceptar.place(x=190,y=220) 
    def pedirCarnetMentor():
        '''
        Funcionamiento: pide el carnet a un mentor.
        Entradas: NA
        Salidas: NA
        '''  
        ventana5=Tk()
        ventana5.config(bg='Teal')
        ventana5.title('Actualizar estudiante')
        ventana5.geometry('600x300')
        ventana5.resizable(FALSE,FALSE)
        labelTitulo=Label(ventana5,text='Actualizar mentor', bg='Teal',fg="Azure", font=('arial',20))
        labelTitulo.place(x=150,y=50)
        labelCarnet=Label(ventana5,text='Carnet del mentor: ',bg='Teal',font=('',15))
        labelCarnet.place(x=120,y=130)
        entryCarnet=Entry(ventana5)
        entryCarnet.place(x=300,y=130,width=140,height=30)
        def buscarCarnetMentor():
            '''
            Funcionamiento: busca el carnet de un mentor.
            Entradas: NA
            Salidas: NA
            '''  
            global matrizMentores 
            bandera=0   
            for estudiante in sacarMentores(matrizMentores):
                try:
                    int(entryCarnet.get())
                except:
                    ventanaError=Tk()
                    ventanaError.title('ERROR')
                    ventanaError.geometry('600x300')
                    ventanaError.resizable(FALSE,FALSE)
                    labelError=Label(ventanaError,text='ERROR: Dato ingresado no válido ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                    labelError.place(x=50,y=150)
                    ventanaError.configure(bg='Tomato')
                    ventanaError.mainloop()
                if estudiante==int(entryCarnet.get()):
                    bandera=1
                    ventanaActualizar=Tk()
                    ventanaActualizar.config(bg='Teal')
                    ventanaActualizar.title('Actualizar metor')
                    ventanaActualizar.geometry('700x400')
                    ventanaActualizar.resizable(FALSE,FALSE)
                    labelTitulo=Label(ventanaActualizar,text='Actualizar mentor', bg='Teal',fg="Azure", font=('arial',20))
                    labelTitulo.place(x=200,y=50)
                    labelNombre=Label(ventanaActualizar,text='Nombre completo del mentor: ',bg='Teal',font=('',15))
                    labelNombre.place(x=50,y=130)
                    entryNombre=Entry(ventanaActualizar)
                    entryNombre.place(x=360,y=130,width=200,height=30)
                    labelCorreo=Label(ventanaActualizar,text='Correo del mentor: ',bg='Teal',font=('',15))
                    labelCorreo.place(x=50,y=200)
                    entryCorreo=Entry(ventanaActualizar)
                    entryCorreo.place(x=360,y=200,width=200,height=30)
                    def actualizarMentor():
                        '''
                        Funcionamiento: actualiza los datos de un mentor.
                        Entradas: NA
                        Salidas: NA
                        '''  
                        if not re.match("[^@]+@[^@]+\.[^@]+",entryCorreo.get()):
                            ventanaError=Tk()
                            ventanaError.title('ERROR')
                            ventanaError.geometry('600x300')
                            ventanaError.resizable(FALSE,FALSE)
                            labelError=Label(ventanaError,text='ERROR: El formato del correo no es válido ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                            labelError.place(x=50,y=150)
                            ventanaError.configure(bg='Tomato')
                            ventanaError.mainloop()
                        elif entryCorreo.get() in sacarDatosMentores(matrizMentores) or entryCorreo.get() in sacarDatosPrimerIngreso(dicPrimerIngreso):
                            ventanaError=Tk()
                            ventanaError.title('ERROR')
                            ventanaError.geometry('600x300')
                            ventanaError.resizable(FALSE,FALSE)
                            labelError=Label(ventanaError,text='ERROR: Datos ingresados repetidos  ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                            labelError.place(x=50,y=150)
                            ventanaError.configure(bg='Tomato')
                            ventanaError.mainloop()
                        else:
                            for sede in matrizMentores:
                                for est in sede[1]:
                                    if est==int(entryCarnet.get()):
                                        sede[1][int(entryCarnet.get())][0]=entryNombre.get()
                                        sede[1][int(entryCarnet.get())][2]=entryCorreo.get()
                                        print(matrizMentores)
                                        ventanaCambio=Tk()
                                        ventanaCambio.title('Datos cambiados')
                                        ventanaCambio.geometry('600x300')
                                        ventanaCambio.resizable(FALSE,FALSE)
                                        labelCambio=Label(ventanaCambio,text='Datos cambiados con éxito ', bg='Teal', font=('arial',20))
                                        labelCambio.place(x=50,y=150)
                                        ventanaCambio.configure(bg='Teal')
                                        ventanaCambio.mainloop()
                    botonAceptarAc=Button(ventanaActualizar,text='Aceptar',width=18,height=2,command=actualizarMentor)
                    botonAceptarAc.place(x=260,y=300)
            if bandera==0:
                ventanaNo=Tk()
                ventanaNo.title('No se encontró el mentor')
                ventanaNo.geometry('600x300')
                ventanaNo.resizable(FALSE,FALSE)
                labelNo=Label(ventanaNo,text='No se encontró un mentor con ese carnet ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                labelNo.place(x=20,y=150)
                ventanaNo.configure(bg='Tomato')
                ventanaNo.mainloop()
        botonAceptar=Button(ventana5,text='Aceptar',width=18,height=2,command=buscarCarnetMentor)
        botonAceptar.place(x=190,y=190)
    botonPrimerIngreso=Button(ventana5,text='Primer Ingreso',width=20,height=2,command=pedirCarnetPrimerIngreso)
    botonPrimerIngreso.place(x=90,y=130)
    botonMentor=Button(ventana5,text='Mentor',width=20,height=2,command=pedirCarnetMentor)
    botonMentor.place(x=370,y=130)
#Función botón 6   
def generarReportes():
    '''
    Funcionamiento: genera la ventana con los botones que generan los reportes.
    Entradas: NA
    Salidas: NA
    '''  
    global dicPrimerIngreso,matrizMentores
    ventana6=Tk()
    ventana6.config(bg='Teal')
    ventana6.title('Generar reportes')
    ventana6.geometry('650x300')
    ventana6.resizable(FALSE,FALSE)
    labelTitulo=Label(ventana6,text='Generar reportes',bg='Teal',fg='Azure',font=('arial',20))
    labelTitulo.place(x=220,y=40)
    def reporteSede():
        '''
        Funcionamiento: genera el reporte por sede.
        Entradas: NA
        Salidas: NA
        '''  
        global dicPrimerIngreso
        registroSede(dicPrimerIngreso)
        ventanaExito=Tk()
        ventanaExito.title('Reporte Generado')
        ventanaExito.geometry('550x150')
        ventanaExito.resizable(FALSE,FALSE)
        labelExito=Label(ventanaExito,text='Reporte generado con éxito ', bg='Teal', font=('arial',20))
        labelExito.place(x=100,y=50)
        ventanaExito.configure(bg='Teal')
        ventanaExito.mainloop()
    def reporteCarrera():
        '''
        Funcionamiento: genera el reporte por carrera.
        Entradas: NA
        Salidas: NA
        '''  
        global dicPrimerIngreso
        registroCarrera(dicPrimerIngreso)
        ventanaExito=Tk()
        ventanaExito.title('Reporte Generado')
        ventanaExito.geometry('550x150')
        ventanaExito.resizable(FALSE,FALSE)
        labelExito=Label(ventanaExito,text='Reporte generado con éxito ', bg='Teal', font=('arial',20))
        labelExito.place(x=100,y=50)
        ventanaExito.configure(bg='Teal')
        ventanaExito.mainloop()
    def reporteMentor():
        global dicPrimerIngreso, matrizMentores
        '''
        Funcionamiento: genera el reporte por mentor.
        Entradas: NA
        Salidas: NA
        '''  
        registroMentor(dicPrimerIngreso,matrizMentores)
        ventanaExito=Tk()
        ventanaExito.title('Reporte Generado')
        ventanaExito.geometry('550x150')
        ventanaExito.resizable(FALSE,FALSE)
        labelExito=Label(ventanaExito,text='Reporte generado con éxito ', bg='Teal', font=('arial',20))
        labelExito.place(x=100,y=50)
        ventanaExito.configure(bg='Teal')
        ventanaExito.mainloop()
    botonSede=Button(ventana6,text='Reporte por sede',width=18,height=2,command=reporteSede)
    botonSede.place(x=80,y=150)
    botonCarrera=Button(ventana6,text='Reporte por carrera',width=18,height=2,command=reporteCarrera)
    botonCarrera.place(x=250,y=150)
    botonMentor=Button(ventana6,text='Reporte por mentor',width=18,height=2,command=reporteMentor)
    botonMentor.place(x=420,y=150)
    ventana6.mainloop()
#Función botón 7
def crearBD():
    '''
    Funcionamiento: crea la base de datos .csv.
    Entradas: NA
    Salidas: NA
    '''  
    global dicPrimerIngreso, matrizMentores,archivoDB
    archivoDB=crearDB(dicPrimerIngreso,matrizMentores)
#Función botón 8
def enviarCorreo():
    '''
    Funcionamiento: envia el correo con el archivo .csv.
    Entradas: NA
    Salidas: NA
    ''' 
    ventana8=Tk()
    ventana8.config(bg='Teal')
    ventana8.title('Enviar correo')
    ventana8.geometry('600x300')
    ventana8.resizable(FALSE,FALSE)
    labelTitulo=Label(ventana8,text='Enviar correo', bg='Teal',fg="Azure", font=('arial',20))
    labelTitulo.place(x=150,y=50)
    labelDestinatario=Label(ventana8,text='Correo del destinatario: ',bg='Teal',font=('',15))
    labelDestinatario.place(x=90,y=130)
    entryDestinatario=Entry(ventana8)
    entryDestinatario.place(x=300,y=130,width=150,height=30)
    def verificarCorreo():
        '''
        Funcionamiento: verifica que los datos del correo sean correctos.
        Entradas: NA
        Salidas: NA
        ''' 
        global archivoDB
        if not re.match("[^@]+@[^@]+\.[^@]+",entryDestinatario.get()):
            ventanaError=Tk()
            ventanaError.title('ERROR')
            ventanaError.geometry('600x300')
            ventanaError.resizable(FALSE,FALSE)
            labelError=Label(ventanaError,text='ERROR: El formato del correo no es válido ', bg='Tomato',fg='AliceBlue', font=('arial',20))
            labelError.place(x=10,y=150)
            ventanaError.configure(bg='Tomato')
            ventanaError.mainloop()
        elif archivoDB=='':
            ventanaError=Tk()
            ventanaError.title('ERROR')
            ventanaError.geometry('600x300')
            ventanaError.resizable(FALSE,FALSE)
            labelError=Label(ventanaError,text='ERROR: No se ha creado una base de datos todavía ', bg='Tomato',fg='AliceBlue', font=('arial',20))
            labelError.place(x=10,y=150)
            ventanaError.configure(bg='Tomato')
            ventanaError.mainloop()
        else: 
            enviarEmail(entryDestinatario.get(),archivoDB)
            ventanaCambio=Tk()
            ventanaCambio.title('Correo enviado')
            ventanaCambio.geometry('600x300')
            ventanaCambio.resizable(FALSE,FALSE)
            labelCambio=Label(ventanaCambio,text='Correo enviado con éxito ', bg='Teal', font=('arial',20))
            labelCambio.place(x=50,y=150)
            ventanaCambio.configure(bg='Teal')
            ventanaCambio.mainloop()
    botonAceptar=Button(ventana8,text='Aceptar',width=18,height=2,command=verificarCorreo)
    botonAceptar.place(x=190,y=190)
    ventana8.mainloop()
#Creación de botones de pantalla principal
boton1=Button(ventanaPrincipal,text='1. Estudiantes por sede',width=18,height=2, command=estudiantesPorSede)
boton2=Button(ventanaPrincipal,text='2. Estudiantes de carrera por sede',state=DISABLED,width=25,height=2,command=estudiatesDeCarreraPorSede)
boton3=Button(ventanaPrincipal,text='3. Crear mentores', state=DISABLED,width=14,height=2,command=crearMentores)
boton4=Button(ventanaPrincipal,text='4. Asignar mentores',state=DISABLED,width=16,height=2,command=asignarMentor)
boton5=Button(ventanaPrincipal,text='5. Actualizar estudiante',state=DISABLED,width=18,height=2, command=actualizarEstudiante)
boton6=Button(ventanaPrincipal,text='6. Generar reportes',width=18,height=2,command=generarReportes)
boton7=Button(ventanaPrincipal,text='7. Crear base de datos en Excel',width=25,height=2,command=crearBD)
boton8=Button(ventanaPrincipal,text='8. Enviar correo',width=13,height=2,command=enviarCorreo)
boton9=Button(ventanaPrincipal,text='9. Salir',width=10,height=2,command= lambda:ventanaPrincipal.destroy())
#Colocación de botones de pantalla principal
boton1.place(x=25,y=120)
boton2.place(x=175,y=120)
boton3.place(x=385,y=120)
boton4.place(x=510,y=120)
boton5.place(x=650,y=120)
boton6.place(x=100,y=200)
boton7.place(x=260,y=200)
boton8.place(x=470,y=200)
boton9.place(x=600,y=200)
ventanaPrincipal.mainloop()