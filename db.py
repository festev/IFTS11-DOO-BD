class Documento():
    def __init__(self, id, contenido = None):
        self.id = id
        self.contenido = contenido if contenido is not None else {} #si el valor es None, se crea un diccionario vacío. Creo que también hace que el código interprete a 'contenido' como diccionario

    def search_clave(self,clave):
        return self.contenido.get(clave, None)

    def setter(self, clave, valor):
        self.contenido[clave] = valor

    def __str__(self):
        return f"Documento (id={self.id}, contenido={self.contenido})"
    
class Coleccion():
    def __init__(self, nombre):
        self.nombre = nombre
        self.documentos = {}
    
    def add_documento(self, documento):
        self.documentos[documento.id] = documento

    def drop_documento(self, id_documento):
        if id_documento in self.documentos: #busca si una clave coincide, ¿podrá buscar por valores?
            del self.documentos[id_documento] #elimina el documento con el id de clave

    def search_documento(self, id_documento):
        return self.documentos.get(id_documento, None)
    
    def __str__(self):
        return f"Coleccion '{self.nombre}' con {len(self.documentos)} documentos."
    
class BD:
    def __init__(self):
        self.colecciones = {}
        
    def add_coleccion(self, nombre_coleccion):
        if nombre_coleccion not in self.colecciones:
            self.colecciones[nombre_coleccion] = Coleccion(nombre_coleccion) #no debería agregar la colección directamente en vez de crear una nueva??
            
    def drop_coleccion(self, nombre_coleccion):
        if nombre_coleccion in self.colecciones:
            del self.colecciones[nombre_coleccion]
            
    def search_coleccion(self, nombre_coleccion) -> Coleccion:
        return self.colecciones.get(nombre_coleccion, None)
    
    def __str__(self):
        return f"BD '{self.nombre}' con {len(self.colecciones)} colecciones y {len(self.documentos)} documentos."
    
a = Documento(1,"holi")
print(a.__str__())

b = Documento(2)
b.setter("nombre","Federico")
b.setter("edad","54")
b.setter("altura","1,30")

print(b.__str__())

BD1 = BD()
BD1.add_coleccion("Animales")
BD1.search_coleccion("Animales").