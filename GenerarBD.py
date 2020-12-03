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

prueba={
    2021017930: ['Zelma Griffin Dean',
        70653420, 'zgriffin@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Computación',
        0
    ],
    2021012163: ['Gonzalo Shelly Green',
        78282889, 'gshelly@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Gestión en Turismo Sostenible',
        0
    ],
    2021013436: ['Debbie Smith Lee',
        72251820, 'dsmith@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Gestión en Turismo Sostenible',
        0
    ],
    2021018066: ['Robbie Horner Wigfall',
        81374407, 'rhorner@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Administración de Tecnología de Información',
        0
    ],
    2021019892: ['Donovan Ramirez Mctigue',
        61904795, 'dramirez@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Ambiental',
        0
    ],
    2021012955: ['Jeane Leyva Arnold',
        76997898, 'jleyva@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Electrónica',
        0
    ],
    2021015501: ['Frank Sill Perkins',
        73310217, 'fsill@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Producción Industrial',
        0
    ],
    2021017707: ['Henry Forgey Girgenti',
        75553379, 'hforgey@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Seguridad Laboral e Higiene Ambiental',
        0
    ],
    2021014586: ['Joseph Metts Fleming',
        92023741, 'jmetts@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Forestal',
        0
    ],
    2021014508: ['Barbara Rosas Perez',
        80238672, 'brosas@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Mecatrónica',
        0
    ],
    2021023449: ['Richard Walker Leatherwood',
        97575427, 'rwalker@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Administración de Empresas',
        0
    ],
    2021022325: ['Jennifer Mckenzie Smith',
        72696585, 'jmckenzie@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Administración de Empresas',
        0
    ],
    2021024930: ['Tommy Hagood Adams',
        81845928, 'thagood@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Administración de Empresas',
        0
    ],
    2021028750: ['Paula Macias Reed',
        63540734, 'pmacias@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Computación',
        0
    ],
    2021022813: ['Deborah Landry Koepsell',
        96357882, 'dlandry@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Gestión en Turismo Rural Sostenible',
        0
    ],
    2021023339: ['Thomas Langerman Rau',
        81679478, 'tlangerman@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Electrónica',
        0
    ],
    2021028860: ['Kristopher Hernandez Johnson',
        66013492, 'khernandez@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Agronomía',
        0
    ],
    2021024261: ['Deborah Brant Walter',
        75699989, 'dbrant@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Producción Industrial',
        0
    ],
    2021027817: ['Chet Hunnicutt Hossain',
        74725049, 'chunnicutt@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Producción Industrial',
        0
    ],
    2021024689: ['Susan Jackson Farr',
        95814316, 'sjackson@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Producción Industrial',
        0
    ],
    2021034750: ['Isaac Godfrey Howard',
        66343288, 'igodfrey@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo',
        0
    ],
    2021036320: ['Tamiko Todd Anderson',
        77024893, 'ttodd@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo',
        0
    ],
    2021034932: ['Thomas Cochran Rollinger',
        64658140, 'tcochran@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo',
        0
    ],
    2021038588: ['Aurora Remaley Pentecost',
        67531808, 'aremaley@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo',
        0
    ],
    2021036155: ['Marion Sanders Jolissaint',
        68139235, 'msanders@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo',
        0
    ],
    2021031006: ['Myra Monteagudo Benedetto',
        72421338, 'mmonteagudo@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo',
        0
    ],
    2021032452: ['Linda Estrello Smoot',
        76551478, 'lestrello@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas',
        0
    ],
    2021031449: ['Joshua Andres Gavia',
        81238845, 'jandres@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas',
        0
    ],
    2021037096: ['Stephanie Shaw Smith',
        69514964, 'sshaw@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas',
        0
    ],
    2021036285: ['Kelly Cabrales Tarbox',
        66899456, 'kcabrales@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Ingeniería en Computación',
        0
    ],
    2021047538: ['Michael Bartholomew Becknell',
        79036456, 'mbartholomew@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación',
        0
    ],
    2021042290: ['Graciela Holmes Pillsbury',
        82545421, 'gholmes@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación',
        0
    ],
    2021047327: ['James Luna Merrick',
        76780061, 'jluna@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación',
        0
    ],
    2021041847: ['David Strom Barer',
        71811362, 'dstrom@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación',
        0
    ],
    2021041076: ['Jacquelin Edwards Quirin',
        85593391, 'jedwards@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación',
        0
    ],
    2021045937: ['Thomas Jenkins Klaus',
        71997206, 'tjenkins@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación',
        0
    ],
    2021045392: ['Donald Price Davis',
        90829028, 'dprice@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación',
        0
    ],
    2021046375: ['Carol Remington Beene',
        92879615, 'cremington@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación',
        0
    ],
    2021043434: ['Daniel Rodriguez Taylor',
        72885611, 'drodriguez@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica',
        0
    ],
    2021046614: ['Thomas Anderson Spencer',
        87260201, 'tanderson@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica',
        0
    ],
    2021053535: ['Susan Kelly June',
        80417274, 'skelly@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Administración de Empresas',
        0
    ],
    2021054716: ['Omar Mara Johnson',
        66894982, 'omara@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Administración de Empresas',
        0
    ],
    2021054232: ['Socorro Golston Macias',
        94443667, 'sgolston@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Computación',
        0
    ],
    2021057730: ['Vernon Stephens Eppler',
        67935117, 'vstephens@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Computación',
        0
    ],
    2021053362: ['Jeremiah Zadow Moorman',
        80768398, 'jzadow@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Producción de Industrial',
        0
    ],
    2021054657: ['Jessica Gordon Simpkins',
        77920282, 'jgordon@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Producción de Industrial',
        0
    ],
    2021054375: ['Duncan Pederson Braun',
        86590705, 'dpederson@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Producción de Industrial',
        0
    ],
    2021054443: ['Edmond Propes Gilling',
        60013198, 'epropes@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Producción de Industrial',
        0
    ],
    2021052548: ['Renee Clouser Clarke',
        71348278, 'rclouser@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Producción de Industrial',
        0
    ],
    2021057911: ['John Kash Bussard',
        85549811, 'jkash@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Producción de Industrial',
        0
    ],
    2021017930: ['Zelma Griffin Dean',
        70653420, 'zgriffin@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Computación',
        0
    ],
    2021012163: ['Gonzalo Shelly Green',
        78282889, 'gshelly@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Gestión en Turismo Sostenible',
        0
    ],
    2021013436: ['Debbie Smith Lee',
        72251820, 'dsmith@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Gestión en Turismo Sostenible',
        0
    ],
    2021018066: ['Robbie Horner Wigfall',
        81374407, 'rhorner@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Administración de Tecnología de Información',
        0
    ],
    2021019892: ['Donovan Ramirez Mctigue',
        61904795, 'dramirez@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Ambiental',
        0
    ],
    2021012955: ['Jeane Leyva Arnold',
        76997898, 'jleyva@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Electrónica',
        0
    ],
    2021015501: ['Frank Sill Perkins',
        73310217, 'fsill@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Producción Industrial',
        0
    ],
    2021017707: ['Henry Forgey Girgenti',
        75553379, 'hforgey@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería en Seguridad Laboral e Higiene Ambiental',
        0
    ],
    2021014586: ['Joseph Metts Fleming',
        92023741, 'jmetts@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Forestal',
        0
    ],
    2021014508: ['Barbara Rosas Perez',
        80238672, 'brosas@estudiantec.cr', 'CAMPUS TECNOLÓGICO CENTRAL CARTAGO', 'Ingeniería Mecatrónica',
        0
    ],
    2021023449: ['Richard Walker Leatherwood',
        97575427, 'rwalker@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Administración de Empresas',
        0
    ],
    2021022325: ['Jennifer Mckenzie Smith',
        72696585, 'jmckenzie@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Administración de Empresas',
        0
    ],
    2021024930: ['Tommy Hagood Adams',
        81845928, 'thagood@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Administración de Empresas',
        0
    ],
    2021028750: ['Paula Macias Reed',
        63540734, 'pmacias@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Computación',
        0
    ],
    2021022813: ['Deborah Landry Koepsell',
        96357882, 'dlandry@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Gestión en Turismo Rural Sostenible',
        0
    ],
    2021023339: ['Thomas Langerman Rau',
        81679478, 'tlangerman@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Electrónica',
        0
    ],
    2021028860: ['Kristopher Hernandez Johnson',
        66013492, 'khernandez@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Agronomía',
        0
    ],
    2021024261: ['Deborah Brant Walter',
        75699989, 'dbrant@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Producción Industrial',
        0
    ],
    2021027817: ['Chet Hunnicutt Hossain',
        74725049, 'chunnicutt@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Producción Industrial',
        0
    ],
    2021024689: ['Susan Jackson Farr',
        95814316, 'sjackson@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN CARLOS', 'Ingeniería en Producción Industrial',
        0
    ],
    2021034750: ['Isaac Godfrey Howard',
        66343288, 'igodfrey@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo',
        0
    ],
    2021036320: ['Tamiko Todd Anderson',
        77024893, 'ttodd@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo',
        0
    ],
    2021034932: ['Thomas Cochran Rollinger',
        64658140, 'tcochran@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo',
        0
    ],
    2021038588: ['Aurora Remaley Pentecost',
        67531808, 'aremaley@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo',
        0
    ],
    2021036155: ['Marion Sanders Jolissaint',
        68139235, 'msanders@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo',
        0
    ],
    2021031006: ['Myra Monteagudo Benedetto',
        72421338, 'mmonteagudo@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Arquitectura y Urbanismo',
        0
    ],
    2021032452: ['Linda Estrello Smoot',
        76551478, 'lestrello@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas',
        0
    ],
    2021031449: ['Joshua Andres Gavia',
        81238845, 'jandres@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas',
        0
    ],
    2021037096: ['Stephanie Shaw Smith',
        69514964, 'sshaw@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Administración de Empresas',
        0
    ],
    2021036285: ['Kelly Cabrales Tarbox',
        66899456, 'kcabrales@estudiantec.cr', 'CAMPUS TECNOLÓGICO LOCAL SAN JOSÉ', 'Ingeniería en Computación',
        0
    ],
    2021047538: ['Michael Bartholomew Becknell',
        79036456, 'mbartholomew@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación',
        0
    ],
    2021042290: ['Graciela Holmes Pillsbury',
        82545421, 'gholmes@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación',
        0
    ],
    2021047327: ['James Luna Merrick',
        76780061, 'jluna@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación',
        0
    ],
    2021041847: ['David Strom Barer',
        71811362, 'dstrom@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación',
        0
    ],
    2021041076: ['Jacquelin Edwards Quirin',
        85593391, 'jedwards@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación',
        0
    ],
    2021045937: ['Thomas Jenkins Klaus',
        71997206, 'tjenkins@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación',
        0
    ],
    2021045392: ['Donald Price Davis',
        90829028, 'dprice@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación',
        0
    ],
    2021046375: ['Carol Remington Beene',
        92879615, 'cremington@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Computación',
        0
    ],
    2021043434: ['Daniel Rodriguez Taylor',
        72885611, 'drodriguez@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica',
        0
    ],
    2021046614: ['Thomas Anderson Spencer',
        87260201, 'tanderson@estudiantec.cr', 'CENTRO ACADÉMICO DE ALAJUELA', 'Ingeniería en Electrónica',
        0
    ],
    2021053535: ['Susan Kelly June',
        80417274, 'skelly@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Administración de Empresas',
        0
    ],
    2021054716: ['Omar Mara Johnson',
        66894982, 'omara@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Administración de Empresas',
        0
    ],
    2021054232: ['Socorro Golston Macias',
        94443667, 'sgolston@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Computación',
        0
    ],
    2021057730: ['Vernon Stephens Eppler',
        67935117, 'vstephens@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Computación',
        0
    ],
    2021053362: ['Jeremiah Zadow Moorman',
        80768398, 'jzadow@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Producción de Industrial',
        0
    ],
    2021054657: ['Jessica Gordon Simpkins',
        77920282, 'jgordon@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Producción de Industrial',
        0
    ],
    2021054375: ['Duncan Pederson Braun',
        86590705, 'dpederson@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Producción de Industrial',
        0
    ],
    2021054443: ['Edmond Propes Gilling',
        60013198, 'epropes@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Producción de Industrial',
        0
    ],
    2021052548: ['Renee Clouser Clarke',
        71348278, 'rclouser@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Producción de Industrial',
        0
    ],
    2021057911: ['John Kash Bussard',
        85549811, 'jkash@estudiantec.cr', 'CENTRO ACADÉMICO DE LIMÓN', 'Ingeniería en Producción de Industrial',
        0
    ]
}

#crearDB(prueba,prueba)