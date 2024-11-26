import String2Dic

class Documento():
    """
    Representa un documento con un identificador y contenido almacenado como diccionario.
    """
    def __init__(self, id, contenido = None):
        """
        Inicializa un documento con un ID y contenido en forma de diccionario
        """
        self.id = id
        self.contenido = contenido if contenido is not None else {} #si el valor es None, se crea un diccionario vacío. Creo que también hace que el código interprete a 'contenido' como diccionario

    def search_clave(self,clave):
        """
        Busca una clave dentro del contenido del documento. Devuelve un valor asociado o None si no existe.
        """
        return self.contenido.get(clave, None) #Si encuentra la clave, devuelve el valor. Sino devuelve "None", creo que por defecto (sin el segundo argumento) también es None.

    def setter(self, clave, valor):
        """
        Establece un nuevo valor con la clave proporcionada. Todo dentro del contenido del documento.
        """
        self.contenido[clave] = valor

    def __str__(self):
        return f"Documento: id={self.id} - contenido={self.contenido}" #lo que aparece con un print al objeto.
    
class Coleccion():
    """
    Representa una colección de documentos con un identificador único.
    """
    def __init__(self, nombre):
        """
        Inicializa una colección con un nombre y un conjunto vacío de documentos. También tiene un contador (comenzado en 1) para los identificadores.
        """
        self.ids = 1
        self.nombre = nombre
        self.documentos = {}
    
    def add_documento(self, documento:Documento):
        """
        Agrega un documento a la colección.
        """
        self.documentos[documento.id] = documento
        self.ids += 1

    def drop_documento(self, id_documento):
        """
        Elimina un documento de la colección según su ID.
        """
        if id_documento in self.documentos: #busca si una clave coincide, ¿podrá buscar por valores?
            del self.documentos[id_documento] #elimina el documento con el id de clave

    def search_documento(self, id_documento) -> Documento:
        """
        Busca un documento en la colección por su ID. Devuelve un None si no existe.
        """
        return self.documentos.get(id_documento, None)
    
    def import_csv(self, ruta):
        """
        Importa documentos desde un archivo CSV y los agrega a la colección.
        """
        with open(ruta,"r") as archivo: #with abre el archivo y lo cierra solo
            schema = archivo.readline().replace("\n","") #a cada linea hay que quitarle \n porque sino se refleja en el Documento. La primera línea del csv es el esquema
            str2dic = String2Dic.Str2Dic(schema)
            linea = archivo.readline().replace("\n","")
            while(linea!=""): #se repite hasta que no haya nada más en el csv
                self.add_documento(Documento(self.ids,str2dic.convert(linea))) #agregamos a la colección un documento con el id que hay en el contador 'ids' y el diccionario obtenido de str2dic
                linea = archivo.readline().replace("\n","") #extrayendo el documento del csv
    
    def __str__(self):
        return f"Coleccion '{self.nombre}' con {len(self.documentos)} documentos."
    
class BD:
    """
    Representa una base de datos que contiene múltiples colecciones de documentos.
    """
    def __init__(self, nombre):
        """
        Inicializa una base de datos con un nombre y un conjunto vacío de colecciones.
        """
        self.nombre = nombre
        self.colecciones = {}
        
    def add_coleccion(self, nombre_coleccion):
        """
        Agrega una nueva colección a la base de datos.
        """
        if nombre_coleccion not in self.colecciones:
            self.colecciones[nombre_coleccion] = Coleccion(nombre_coleccion)
            
    def drop_coleccion(self, nombre_coleccion):
        """
        Elimina una colección de la base de datos según su nombre.
        """
        if nombre_coleccion in self.colecciones:
            del self.colecciones[nombre_coleccion]
            
    def search_coleccion(self, nombre_coleccion) -> Coleccion: #Por agregar esta notación, al poner un . el autocompletado me sugiere los métodos de la clase Coleccion
        """
        Busca una colección en la base de datos por su nombre. Devuelve un None si no existe.
        """
        return self.colecciones.get(nombre_coleccion, None)
    
    def __str__(self):
        return f"BD '{self.nombre}' con {len(self.colecciones)} colecciones."