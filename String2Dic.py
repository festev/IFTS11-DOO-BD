class Str2Dic(object):
    def __init__(self, schemaStr:str, separator=","):
        self.schema = schemaStr.split(separator)
        self.separator = separator

    def convert(self, row:str):
        temp = row.split(self.separator)
        if len(temp) == len(self.schema):
            i = 0
            dic = {}
            while i < len(temp):
                dic[self.schema[i]] = temp[i]
                i = i + 1
            return dic

if __name__ == "__main__":
    #TESTS
    schema = "Nombre,Apellido,Edad,Mail"
    row = "Roberto,Gutierrez,33,abc123@gmail.com"
    obj1 = Str2Dic(schema)
    diccionario = obj1.convert(row)
    print(diccionario)