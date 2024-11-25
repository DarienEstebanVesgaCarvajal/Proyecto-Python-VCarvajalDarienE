import json

def readJSON(filePath):
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"El archivo {filePath} no existe. Creando uno nuevo...")
        with open(filePath, 'w', encoding='utf-8') as file:
            json.dump({"gastos": []}, file, indent=4)
        return {"gastos": []}
    except json.JSONDecodeError:
        print(f"Error al leer el archivo JSON: {filePath}. Reiniciando contenido.")
        return {"gastos": []}

def writeJSON(filePath, data):
    try:
        with open(filePath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al escribir en el archivo {filePath}: {e}")