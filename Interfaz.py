#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 18/11/2020 6:40pm 
#Fecha de última Modificación: 5/12/2020 9:32pm
#Versión: 3.9.0

from tkinter import*


ventanaPrincipal=Tk()
ventanaPrincipal.title('Integratec')
ventanaPrincipal.geometry('800x300')
ventanaPrincipal.resizable(FALSE,FALSE)
ventanaPrincipal.configure(bg='blue')

#panel=Frame(ventana,bg='blue',width=1000,height=600)
#panel.place(x=0,y=0)

labelTitulo = Label(ventanaPrincipal, text = "Integratec" , bg="blue", fg="yellow", font = ('calibri', 40))
labelTitulo.place(x=20,y=30)

#Funciones
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
        try:
            cantCartago=int(entryCartago.get())
            cantSanCarlos=int(entrySanCarlos.get())
            cantSanJose=int(entrySanJose.get())
            cantAlajuela=int(entryAlajuela.get())
            cantLimon=int(entryLimon.get())
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

def estudiatesDeCarreraPorSede():
    ventana2=Tk()
    ventana2.config(bg='blue')
    ventana2.title('Estudiantes de carrera por sede')
    ventana2.geometry('1000x300')
    ventana2.resizable(FALSE,FALSE)
    labelTitulo2 = Label(ventana2, text = "Base de datos creada satisfactoriamente" , bg="blue", fg="yellow", font = ('calibri', 40))
    labelTitulo2.place(x=50,y=50)
    botonVolver=Button(ventana2,text='Volver al menú principal',width=20,height=2,command= lambda:ventana2.destroy())
    botonVolver.place(x=400,y=200)

#Botones
boton1=Button(ventanaPrincipal,text='1. Estudiantes por sede',width=18,height=2, command=estudiantesPorSede)
boton2=Button(ventanaPrincipal,text='2. Estudiantes de carrera por sede',state=DISABLED,width=25,height=2,command=estudiatesDeCarreraPorSede)
boton3=Button(ventanaPrincipal,text='3. Crear mentores', state=DISABLED,width=14,height=2)
boton4=Button(ventanaPrincipal,text='4. Asignar mentores',state=DISABLED,width=16,height=2)
boton5=Button(ventanaPrincipal,text='5. Actualizar estudiante',state=DISABLED,width=18,height=2)
boton6=Button(ventanaPrincipal,text='6. Generar reportes',width=18,height=2)
boton7=Button(ventanaPrincipal,text='7. Crear base de datos en Excel',width=25,height=2)
boton8=Button(ventanaPrincipal,text='8. Enviar correo',width=13,height=2)
boton9=Button(ventanaPrincipal,text='9. Eliminar mentor',width=16,height=2)
boton10=Button(ventanaPrincipal,text='10. Salir',width=10,height=2,command= lambda:ventanaPrincipal.destroy())

boton1.place(x=25,y=120)
boton2.place(x=175,y=120)
boton3.place(x=385,y=120)
boton4.place(x=510,y=120)
boton5.place(x=650,y=120)
boton6.place(x=25,y=200)
boton7.place(x=175,y=200)
boton8.place(x=385,y=200)
boton9.place(x=510,y=200)
boton10.place(x=675,y=200)

ventanaPrincipal.mainloop()

