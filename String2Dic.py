class Str2Dic(object):
    """
    Convierte las filas de un archivo CSV en un diccionario utilizando un esquema definido.
    """
    def __init__(self, schemaStr:str, separator=","):
        """
        Inicializa el convertidor con un esquema y un separador.
        """
        self.schema = schemaStr.split(separator) #Se proporciona un string. Cada palabra estre los separadores es una clave del futuro diccionario. Se separan las claves en una lista.
        self.separator = separator

    def convert(self, row:str):
        """
        Convierte una fila de datos en un diccionario utilizando el esquema definido.
        """
        temp = row.split(self.separator) #Se proporciona un string. El contenido que hay entre los separadores se los separa en una lista. Estos representan los valores del futuro diccionario.
        if len(temp) == len(self.schema):
            i = 0
            dic = {}
            while i < len(temp):
                dic[self.schema[i]] = temp[i] #Se crea un diccionario vinculando la lista de las claves con la lista del contenido. Se determina que clave va con que valor si sus índices coinciden.
                i = i + 1
            return dic