#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 2/11/2020 7:29pm 
#Fecha de última Modificación: 5/12/2020 9:32pm
#Versión: 3.9.0
#Importaciones
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
def enviarEmail(destinatario,nombreArchivo):
    '''
    Funcionamiento: envia el correo con el archivo 
    Entradas: el correo del destinatario y el nombre del archivo 
    Salidas: True
    '''
    # Iniciamos los parámetros del script
    remitente = 'ProyectoIntegraTEC.Taller2020@gmail.com'
    destinatarios = str(destinatario)
    asunto = 'Base de datos en Excel'
    cuerpo = 'Saludos encargado, se le adjunta la base de datos con los estudiantes y mentores inscritos a día de hoy.\n¡Los programadores le desean un hermoso día! \n\n\n\n ¡No responda a este mensaje, ha sido generado automaticamente!.'
    ruta_adjunto = str(nombreArchivo) 
    nombre_adjunto = str(nombreArchivo)
    # Creamos el objeto mensaje
    mensaje = MIMEMultipart()
    # Establecemos los atributos del mensaje
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto
    # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    # Abrimos el archivo que vamos a adjuntar
    archivo_adjunto = open(ruta_adjunto, 'rb')
    # Creamos un objeto MIME base
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    # Y le cargamos el archivo adjunto
    adjunto_MIME.set_payload((archivo_adjunto).read())
    # Codificamos el objeto en BASE64
    encoders.encode_base64(adjunto_MIME)
    # Agregamos una cabecera al objeto
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
    # Y finalmente lo agregamos al mensaje
    mensaje.attach(adjunto_MIME)
    # Creamos la conexión con el servidor
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    # Ciframos la conexión
    sesion_smtp.starttls()
    # Iniciamos sesión en el servidor
    sesion_smtp.login('ProyectoIntegraTEC.Taller2020@gmail.com',"celinaleandro")
    # Convertimos el objeto mensaje a texto
    texto = mensaje.as_string()
    # Enviamos el mensaje
    sesion_smtp.sendmail(remitente, destinatarios, texto)
    # Cerramos la conexión
    sesion_smtp.quit()
    return True
