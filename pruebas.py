from String2Dic import Str2Dic
from db import Coleccion
from db import Documento
from db import BD

'''
###PRIMER IMPORT###

def import_collection(nombre_archivo, nombre): #el profe no puso 'nombre' como entrada, pero lo agregue para que se pueda crear la Coleccion
    cole = Coleccion(nombre)
    with open(nombre_archivo,"r") as archivo: #with abre el archivo y lo cierra solo
        linea = archivo.readline().replace("\n","") #a cada linea hay que quitarle \n porque sino se refleja en el Documento
        str2dic = Str2Dic(linea)
        i=1
        while(linea!=""): #se repite hasta que no haya nada más en el csv
            cole.add_documento(Documento(i,str2dic.convert(linea))) #agregamos a la colección un documento con el id 'i' y el diccionario obtenido de str2dic
            linea = archivo.readline().replace("\n","")
            i += 1
    return cole
'''

#TESTS
if __name__ == "__main__":
    '''
    coleccion = import_collection("datos_personales.csv","Personas")
    print(coleccion)
    i = 1
    while i<=len(coleccion.documentos):
        print(coleccion.search_documento(i))
        i += 1
    '''

    '''
    #TESTS
    a = Documento(1,"holi")
    print(a)

    b = Documento(2)
    b.setter("nombre","Federico")
    b.setter("edad","54")
    b.setter("altura","1,30")

    print(b)

    BD1 = BD()
    BD1.add_coleccion("Animales")
    BD1.search_coleccion("Animales").add_documento(b)
    print(BD1)
    print(BD1.search_coleccion("Animales"))
    print(BD1.search_coleccion("Animales").search_documento(2))
    '''

    #TESTS
    schema = "Nombre,Apellido,Edad,Mail"
    row = "Roberto,Gutierrez,33,abc123@gmail.com"
    obj1 = Str2Dic(schema)
    diccionario = obj1.convert(row)
    print(diccionario)