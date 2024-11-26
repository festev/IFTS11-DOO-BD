# main.py
import db
import String2Dic
import json

def mostrar_menu():
    print("\n--- Base de Datos Documental ---")
    print("1. Crear colección")
    print("2. Importar CSV a colección")
    print("3. Consultar documento en colección")
    print("4. Eliminar documento de colección")
    print("5. Listar todos los documentos en colección")
    print("6. Salir")
    return input("Seleccione una opción: ")

def main():
    base_de_datos = db.BD("MiBaseDeDatos")

    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            base_de_datos.add_coleccion(nombre_coleccion)
            print(f"Colección '{nombre_coleccion}' creada.")
            print(base_de_datos.search_coleccion(nombre_coleccion))
        
        elif opcion == "2":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            coleccion = base_de_datos.search_coleccion(nombre_coleccion)
            if coleccion:
                try:
                    ruta_csv = input("Ingrese la ruta del archivo CSV: ")
                    coleccion.import_csv(ruta_csv)
                    print(coleccion)
                except (FileNotFoundError):
                    print("El archivo no fue encontrado.")
            else:
                print(f"Colección '{nombre_coleccion}' no encontrada.")
        
        elif opcion == "3":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            try:
                doc_id = int(input("Ingrese el ID del documento: "))
            except (ValueError):
                print("ID inválido.")
                doc_id = None
            coleccion = base_de_datos.search_coleccion(nombre_coleccion)
            if coleccion:
                documento = coleccion.search_documento(doc_id)
                if documento:
                    print("Documento encontrado:")
                    print(documento)
                else:
                    print("Documento no encontrado.")
            else:
                print(f"Colección '{nombre_coleccion}' no encontrada.")
        
        elif opcion == "4":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            try:
                doc_id = int(input("Ingrese el ID del documento a eliminar: "))
            except (ValueError):
                print("ID inválido.")
                doc_id = None
            coleccion = base_de_datos.search_coleccion(nombre_coleccion)
            if coleccion:
                coleccion.drop_documento(doc_id)
                print(coleccion)
            else:
                print(f"Colección '{nombre_coleccion}' no encontrada.")
        
        elif opcion == "5":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            coleccion = base_de_datos.search_coleccion(nombre_coleccion)
            if coleccion:
                documentos = coleccion.documentos
                if documentos:
                    print("\n--- Lista de Documentos ---")
                    for doc in documentos:
                        print(documentos[doc])
                        print("-----------")
                else:
                    print("No hay documentos en la colección.")
        
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()