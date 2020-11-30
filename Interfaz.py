#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 18/11/2020 6:12pm 
#Fecha de última Modificación: 5/12/2020 9:32pm
#Versión: 3.9.0
#Importaciones
from tkinter import*
from funciones import *
#Variables globales
matrizSedesYCarreras=quitaRepetidos(obtenerCarreras())
matrizSedesEst=[]
dicPrimerIngreso={}
matrizMentores=[['CTCC',{}],['CTLSC',{}],['CTLSJ',{}],['CAA',{}],['CAL',{}]]
#Ventana Principal
ventanaPrincipal=Tk()
ventanaPrincipal.title('Integratec')
ventanaPrincipal.geometry('800x300')
ventanaPrincipal.resizable(FALSE,FALSE)
ventanaPrincipal.configure(bg='blue')
labelTitulo = Label(ventanaPrincipal, text = "Integratec" , bg="blue", fg="yellow", font = ('calibri', 40))
labelTitulo.place(x=20,y=30)
#Funciones
#Función botón 1
def estudiantesPorSede():   
    ventana1=Tk()
    ventana1.title('Estudiantes por sede')
    ventana1.geometry('800x600')
    ventana1.resizable(FALSE,FALSE)
    labelTitulo1 = Label(ventana1, text = "Estudiantes por sede" , bg="blue", fg="yellow", font = ('calibri', 40))
    labelTitulo.place(x=20,y=30)
    ventana1.configure(bg='blue')
    labelTitulo1.place(x=40, y=20)
    labelEstudiantes=Label(ventana1,text='Digite la cantidad de estudiantes de primer ingreso por cada sede ', bg='blue', font=('arial',15))
    labelEstudiantes.place(x=50,y=120)
    labelCartago=Label(ventana1,text='CAMPUS TECNOLÓGICO CENTRAL CARTAGO:', bg='blue')
    labelCartago.place(x=20,y=200)
    entryCartago=Entry(ventana1)
    entryCartago.place(x=280,y=200)
    labelSanCarlos=Label(ventana1,text='CAMPUS TECNOLÓGICO LOCAL SAN CARLOS:', bg='blue')
    labelSanCarlos.place(x=20,y=250)
    entrySanCarlos=Entry(ventana1)
    entrySanCarlos.place(x=280,y=250)
    labelSanJose=Label(ventana1,text='CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ:', bg='blue')
    labelSanJose.place(x=20,y=300)
    entrySanJose=Entry(ventana1)
    entrySanJose.place(x=280,y=300)
    labelAlajuela=Label(ventana1,text='CAMPUS TECNOLÓGICO LOCAL ALAJUELA:', bg='blue')
    labelAlajuela.place(x=20,y=350)
    entryAlajuela=Entry(ventana1)
    entryAlajuela.place(x=280,y=350)
    labelLimon=Label(ventana1,text='CAMPUS TECNOLÓGICO LOCAL LIMÓN:', bg='blue')
    labelLimon.place(x=20,y=400)
    entryLimon=Entry(ventana1)
    entryLimon.place(x=280,y=400)
    def obtenerCantidades():
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
            ventanaExito.geometry('600x300')
            ventanaExito.resizable(FALSE,FALSE)
            labelExito=Label(ventanaExito,text='Datos ingresados con éxito ', bg='blue', font=('arial',20))
            labelExito.place(x=100,y=150)
            ventanaExito.configure(bg='blue')
            ventanaExito.mainloop()
        except:
            ventanaError=Tk()
            ventanaError.title('ERROR')
            ventanaError.geometry('600x300')
            ventanaError.resizable(FALSE,FALSE)
            labelError=Label(ventanaError,text='ERROR: Datos ingresados no válidos ', bg='red', font=('arial',20))
            labelError.place(x=50,y=150)
            ventanaError.configure(bg='red')
            ventanaError.mainloop()
    botonAceptar=Button(ventana1,text='Aceptar',width=18,height=2,command=obtenerCantidades)
    botonAceptar.place(x=200,y=500)
    botonVolver=Button(ventana1,text='Volver al menú principal',width=20,height=2,command= lambda:ventana1.destroy())
    botonVolver.place(x=400,y=500) 
    ventana1.mainloop()
#Función botón 2
def estudiatesDeCarreraPorSede():
    global matrizSedesEst, dicPrimerIngreso
    ventana2=Tk()
    ventana2.config(bg='blue')
    ventana2.title('Estudiantes de carrera por sede')
    ventana2.geometry('1000x300')
    ventana2.resizable(FALSE,FALSE)
    dicPrimerIngreso=crearDicPrimerIngreso(matrizSedesEst,dicPrimerIngreso)
    print(dicPrimerIngreso)
    labelTitulo2 = Label(ventana2, text = "Base de datos creada satisfactoriamente" , bg="blue", fg="yellow", font = ('calibri', 40))
    labelTitulo2.place(x=50,y=50)
    botonVolver=Button(ventana2,text='Volver al menú principal',width=20,height=2,command= lambda:ventana2.destroy())
    botonVolver.place(x=400,y=200)
    boton5['state']=NORMAL
    ventana2.mainloop()

def crearMentores():
    global matrizSedesEst, dicPrimerIngreso,matrizMentores 
    matrizMentores=crearMatMentores(matrizSedesEst,dicPrimerIngreso,matrizMentores)
    print(matrizMentores)
    ventana3=Tk()
    ventana3.config(bg='blue')
    ventana3.title('Crear mentores')
    ventana3.geometry('1000x300')
    ventana3.resizable(FALSE,FALSE)
    labelTitulo3 = Label(ventana3, text = "Mentores creados satisfactoriamente" , bg="blue", fg="yellow", font = ('calibri', 40))
    labelTitulo3.place(x=50,y=50)
    botonVolver=Button(ventana3,text='Volver al menú principal',width=20,height=2,command= lambda:ventana3.destroy())
    botonVolver.place(x=400,y=200)
    boton4['state']=NORMAL
    ventana3.mainloop()
def asignarMentor():
    global dicPrimerIngreso,matrizMentores 
    dicPrimerIngreso=asignarMentores(matrizMentores,dicPrimerIngreso)
    print(dicPrimerIngreso)
#Función botón 5
def actualizarEstudiante():
    ventana5=Tk()
    ventana5.config(bg='blue')
    ventana5.title('Actualizar estudiante')
    ventana5.geometry('600x300')
    ventana5.resizable(FALSE,FALSE)
    labelTitulo=Label(ventana5,text='Actualizar estudiante', bg='blue',fg="yellow", font=('arial',20))
    labelTitulo.place(x=150,y=50)
    def pedirCarnetPrimerIngreso():
        ventana5=Tk()
        ventana5.config(bg='blue')
        ventana5.title('Actualizar estudiante')
        ventana5.geometry('600x300')
        ventana5.resizable(FALSE,FALSE)
        labelTitulo=Label(ventana5,text='Actualizar estudiante', bg='blue',fg="yellow", font=('arial',20))
        labelTitulo.place(x=150,y=50)
        labelCarnet=Label(ventana5,text='Carnet del estudiante: ',bg='blue',font=('',15))
        labelCarnet.place(x=110,y=130)
        entryCarnet=Entry(ventana5)
        entryCarnet.place(x=310,y=130,width=140,height=30)
        def buscarCarnetPrimerIngreso():
            global dicPrimerIngreso 
            bandera=0   
            for estudiante in dicPrimerIngreso:
                try:
                    int(entryCarnet.get())
                except:
                    ventanaError=Tk()
                    ventanaError.title('ERROR')
                    ventanaError.geometry('600x300')
                    ventanaError.resizable(FALSE,FALSE)
                    labelError=Label(ventanaError,text='ERROR: Dato ingresado no válido ', bg='red', font=('arial',20))
                    labelError.place(x=50,y=150)
                    ventanaError.configure(bg='red')
                    ventanaError.mainloop()
                if estudiante==int(entryCarnet.get()):
                    bandera=1
                    ventanaActualizar=Tk()
                    ventanaActualizar.config(bg='blue')
                    ventanaActualizar.title('Actualizar primer ingreso')
                    ventanaActualizar.geometry('700x500')
                    ventanaActualizar.resizable(FALSE,FALSE)
                    labelTitulo=Label(ventanaActualizar,text='Actualizar primer ingreso', bg='blue',fg="yellow", font=('arial',20))
                    labelTitulo.place(x=200,y=50)
                    labelNombre=Label(ventanaActualizar,text='Nombre completo del estudiante: ',bg='blue',font=('',15))
                    labelNombre.place(x=50,y=130)
                    entryNombre=Entry(ventanaActualizar)
                    entryNombre.place(x=360,y=130,width=200,height=30)
                    labelTelefono=Label(ventanaActualizar,text='Teléfono del estudiante: ',bg='blue',font=('',15))
                    labelTelefono.place(x=50,y=200)
                    entryTelefono=Entry(ventanaActualizar)
                    entryTelefono.place(x=360,y=200,width=200,height=30)
                    labelCorreo=Label(ventanaActualizar,text='Correo del estudiante: ',bg='blue',font=('',15))
                    labelCorreo.place(x=50,y=270)
                    entryCorreo=Entry(ventanaActualizar)
                    entryCorreo.place(x=360,y=270,width=200,height=30)
                    def actualizarPrimerIngreso():#!Falta hacer evidentemente pero mejor lo pongo por si acaso
                        if not re.match("^\d{8}$",entryTelefono.get()):
                            ventanaError=Tk()
                            ventanaError.title('ERROR')
                            ventanaError.geometry('600x300')
                            ventanaError.resizable(FALSE,FALSE)
                            labelError=Label(ventanaError,text='ERROR: Dato ingresado no válido ', bg='red', font=('arial',20))
                            labelError.place(x=50,y=150)
                            ventanaError.configure(bg='red')
                            ventanaError.mainloop()
                            botonAceptarAc=Button(ventanaActualizar,text='Aceptar',width=18,height=2,command=actualizarPrimerIngreso)
                            botonAceptarAc.place(x=260,y=380)
                        elif (entryTelefono.get()[0]!= 6 and entryTelefono.get()[0]!=7 and entryTelefono.get()[0]!=8 and entryTelefono.get()[0]!=9) and not re.match("[^@]+@[^@]+\.[^@]+",entryCorreo.get()):
                            ventanaError=Tk()
                            ventanaError.title('ERROR')
                            ventanaError.geometry('600x300')
                            ventanaError.resizable(FALSE,FALSE)
                            labelError=Label(ventanaError,text='ERROR: Datos ingresado no válido ', bg='red', font=('arial',20))
                            labelError.place(x=50,y=150)
                            ventanaError.configure(bg='red')
                            ventanaError.mainloop()
                            botonAceptarAc=Button(ventanaActualizar,text='Aceptar',width=18,height=2,command=actualizarPrimerIngreso)
                            botonAceptarAc.place(x=260,y=380)
                        else:
                            dicPrimerIngreso[int(entryCarnet.get())][0]=entryNombre.get()
                            dicPrimerIngreso[int(entryCarnet.get())][1]=int(entryTelefono.get())
                            dicPrimerIngreso[int(entryCarnet.get())][2]=entryCorreo.get()
                            print(dicPrimerIngreso)
                            ventanaCambio2=Tk()
                            ventanaCambio2.title('Datos cambiados')
                            ventanaCambio2.geometry('600x300')
                            ventanaCambio2.resizable(FALSE,FALSE)
                            labelCambio=Label(ventanaError,text='Datos cambiados con éxito ', bg='blue', font=('arial',20))
                            labelCambio.place(x=50,y=150)
                            ventanaCambio2.configure(bg='blue')
                            ventanaCambio2.mainloop()
                    botonAceptar2=Button(ventanaActualizar,text='Aceptar',width=18,height=2,command=actualizarPrimerIngreso)
                    botonAceptar2.place(x=220,y=250)
            if bandera==0:
                ventanaNo=Tk()
                ventanaNo.title('No se encontró el estudiante')
                ventanaNo.geometry('600x300')
                ventanaNo.resizable(FALSE,FALSE)
                labelNo=Label(ventanaNo,text='No se encontró un estudiante con ese carnet ', bg='red', font=('arial',20))
                labelNo.place(x=20,y=150)
                ventanaNo.configure(bg='red')
                ventanaNo.mainloop()

        botonAceptar=Button(ventana5,text='Aceptar',width=18,height=2,command=buscarCarnetPrimerIngreso)
        botonAceptar.place(x=190,y=220) 
    def pedirCarnetMentor():
        ventana5=Tk()
        ventana5.config(bg='blue')
        ventana5.title('Actualizar estudiante')
        ventana5.geometry('600x300')
        ventana5.resizable(FALSE,FALSE)
        labelTitulo=Label(ventana5,text='Actualizar mentor', bg='blue',fg="yellow", font=('arial',20))
        labelTitulo.place(x=150,y=50)
        labelCarnet=Label(ventana5,text='Carnet del mentor: ',bg='blue',font=('',15))
        labelCarnet.place(x=120,y=130)
        entryCarnet=Entry(ventana5)
        entryCarnet.place(x=300,y=130,width=140,height=30)
        def buscarCarnetMentor():#!Función provisional Hay que revisarla!!!
            global matrizMentores 
            bandera=0   
            for estudiante in matrizMentores:
                if estudiante==entryCarnet.get():
                    bandera=1
                    ventanaActualizar=Tk()
                    ventanaActualizar.config(bg='blue')
                    ventanaActualizar.title('Actualizar metor')
                    ventanaActualizar.geometry('700x400')
                    ventanaActualizar.resizable(FALSE,FALSE)
                    labelTitulo=Label(ventanaActualizar,text='Actualizar mentor', bg='blue',fg="yellow", font=('arial',20))
                    labelTitulo.place(x=200,y=50)
                    labelNombre=Label(ventanaActualizar,text='Nombre completo del mentor: ',bg='blue',font=('',15))
                    labelNombre.place(x=50,y=130)
                    entryNombre=Entry(ventanaActualizar)
                    entryNombre.place(x=360,y=130,width=200,height=30)
                    labelCorreo=Label(ventanaActualizar,text='Correo del mentor: ',bg='blue',font=('',15))
                    labelCorreo.place(x=50,y=200)
                    entryCorreo=Entry(ventanaActualizar)
                    entryCorreo.place(x=360,y=200,width=200,height=30)
                    def actualizarMentor():#!Falta hacer evidentemente pero mejor lo pongo por si acaso
                        return
                    botonAceptarAc=Button(ventanaActualizar,text='Aceptar',width=18,height=2,command=actualizarMentor)
                    botonAceptarAc.place(x=260,y=330)
            if bandera==0:
                ventanaNo=Tk()
                ventanaNo.title('No se encontró el mentor')
                ventanaNo.geometry('600x300')
                ventanaNo.resizable(FALSE,FALSE)
                labelNo=Label(ventanaNo,text='No se encontró un mentor con ese carnet ', bg='red', font=('arial',20))
                labelNo.place(x=20,y=150)
                ventanaNo.configure(bg='red')
                ventanaNo.mainloop()
        botonAceptar=Button(ventana5,text='Aceptar',width=18,height=2,command=buscarCarnetMentor)
        botonAceptar.place(x=190,y=190)
    botonPrimerIngreso=Button(ventana5,text='Primer Ingreso',width=20,height=2,command=pedirCarnetPrimerIngreso)
    botonPrimerIngreso.place(x=90,y=130)
    botonMentor=Button(ventana5,text='Mentor',width=20,height=2,command=pedirCarnetMentor)
    botonMentor.place(x=370,y=130)
    
def generarReportes():
    ventana6=Tk()
    ventana6.config(bg='blue')
    ventana6.title('Generar reportes')
    ventana6.geometry('650x300')
    ventana6.resizable(FALSE,FALSE)
    labelTitulo=Label(ventana6,text='Generar reportes',bg='blue',fg='yellow',font=('arial',20))
    labelTitulo.place(x=220,y=40)
    botonSede=Button(ventana6,text='Reporte por sede',width=18,height=2)
    botonSede.place(x=80,y=150)
    botonCarrera=Button(ventana6,text='Reporte por carrera',width=18,height=2)
    botonCarrera.place(x=250,y=150)
    botonMentor=Button(ventana6,text='Reporte por mentor',width=18,height=2)
    botonMentor.place(x=420,y=150)
#Creación de botones de pantalla principal
boton1=Button(ventanaPrincipal,text='1. Estudiantes por sede',width=18,height=2, command=estudiantesPorSede)
boton2=Button(ventanaPrincipal,text='2. Estudiantes de carrera por sede',state=DISABLED,width=25,height=2,command=estudiatesDeCarreraPorSede)
boton3=Button(ventanaPrincipal,text='3. Crear mentores', state=DISABLED,width=14,height=2,command=crearMentores)
boton4=Button(ventanaPrincipal,text='4. Asignar mentores',state=DISABLED,width=16,height=2,command=asignarMentor)
boton5=Button(ventanaPrincipal,text='5. Actualizar estudiante',state=DISABLED,width=18,height=2, command=actualizarEstudiante)
boton6=Button(ventanaPrincipal,text='6. Generar reportes',width=18,height=2,command=generarReportes)
boton7=Button(ventanaPrincipal,text='7. Crear base de datos en Excel',width=25,height=2)
boton8=Button(ventanaPrincipal,text='8. Enviar correo',width=13,height=2)
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
