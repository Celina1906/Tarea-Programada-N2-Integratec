#Elaborado por: Leandro Camacho y Celina Madrigal
#Fecha de creación: 2/12/2020 4:44 pm
#Fecha de última modificación: 2/12/2020 6:06 pm
#Versión 3.9.0
#Importación de librerías:
import pickle
#Definición de funciones
def graba(nomArchGrabar,mentores):
    '''
    Funcionamiento: graba un archivo binario
    Entradas: nombre del archivo y lo que se grabará
    Salidas: NA
    '''
    try:
        f=open(nomArchGrabar,"wb")
        pickle.dump(mentores,f)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)

def lee (nomArchLeer):
    '''
    Funcionamiento: Función que lee un archivo
    Entradas: nombre del archivo
    Salidas: NA
    '''
    try:
        f=open(nomArchLeer,"rb")
        mentores = pickle.load(f)
        f.close()
    except:
        print("Error al leer el archivo: ", nomArchLeer)
    return mentores