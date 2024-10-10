from String2Dic import Str2Dic
from db import Coleccion
from db import Documento

def import_collection(nombre_archivo, nombre):
    cole = Coleccion(nombre)
    with open(nombre_archivo,"r") as archivo:
        linea = archivo.readline().replace("\n","")
        str2dic = Str2Dic(linea)
        i=1
        while(linea!=""):
            cole.add_documento(Documento(i,str2dic.convert(linea)))
            linea = archivo.readline().replace("\n","")
            i += 1
    return cole

#TESTS
if __name__ == "__main__":
    coleccion = import_collection("datos_personales.csv","Personas")
    print(coleccion)
    i = 1
    while i<=len(coleccion.documentos):
        print(coleccion.search_documento(i))
        i += 1
