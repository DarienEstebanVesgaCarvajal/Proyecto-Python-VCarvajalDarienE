import json
import os

#Se lee un archivo JSON y se devuelve su contenido como un diccionario
def readJSON(filePath):
    try:
        #Se verifica si el archivo existe
        if os.path.exists(filePath):
            #Se abre el archivo en modo lectura y se carga el contenido
            with open(filePath, 'r', encoding='utf-8') as file:
                return json.load(file)
        else:
            #Se retorna un diccionario vacío si el archivo no existe
            return {}
    except Exception as error:
        #Se maneja cualquier error durante la lectura
        print(f"Error al leer el archivo {filePath}: {error}")
        return {}

#Se escribe un diccionario en un archivo JSON
def writeJSON(filePath, data):
    try:
        #Se abre el archivo en modo escritura y se guarda el contenido
        with open(filePath, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as error:
        #Se maneja cualquier error durante la escritura
        print(f"Error al escribir en el archivo {filePath}: {error}")