#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 18/11/2020 6:40pm 
#Fecha de última Modificación: 5/12/2020 9:32pm
#Versión: 3.9.0

from tkinter import*

ventana=Tk()
ventana.title('Integratec')
ventana.geometry('800x300')
ventana.resizable(FALSE,FALSE)

panel=Frame(ventana,bg='blue',width=1000,height=600)
panel.place(x=0,y=0)

labelTitulo = Label(panel, text = "Integratec" , bg="blue", fg="yellow", font = ('calibri', 40))
labelTitulo.place(x=20,y=30)


#Botones
boton1=Button(ventana,text='1. Estudiantes por sede',width=18,height=2)
boton2=Button(ventana,text='2. Estudiantes de carrera por sede',state=DISABLED,width=25,height=2)
boton3=Button(ventana,text='3. Crear mentores', state=DISABLED,width=14,height=2)
boton4=Button(ventana,text='4. Asignar mentores',state=DISABLED,width=16,height=2)
boton5=Button(ventana,text='5. Actualizar estudiante',state=DISABLED,width=18,height=2)
boton6=Button(ventana,text='6. Generar reportes',width=18,height=2)
boton7=Button(ventana,text='7. Crear base de datos en Excel',width=25,height=2)
boton8=Button(ventana,text='8. Enviar correo',width=13,height=2)
boton9=Button(ventana,text='9. Eliminar mentor',width=16,height=2)
boton10=Button(ventana,text='10. Salir',width=10,height=2,command= lambda:ventana.destroy())

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
ventana.mainloop()