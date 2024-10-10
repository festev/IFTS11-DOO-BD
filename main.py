from String2Dic import Str2Dic
from db import Coleccion
from db import Documento

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

#TESTS
if __name__ == "__main__": #talvez esto no haga falta porque no creo que se importe main.py?
    coleccion = import_collection("datos_personales.csv","Personas")
    print(coleccion)
    i = 1
    while i<=len(coleccion.documentos):
        print(coleccion.search_documento(i))
        i += 1
