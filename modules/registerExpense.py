from datetime import datetime
from tabulate import tabulate
from modules.utils.fileHandler import readJSON, writeJSON

#Se define la función para verificar el máximo tamaño permitido en una cadena
def maxLength(inputString, maxLength):
    #Se retorna la cadena truncada si excede el tamaño máximo
    return inputString[:maxLength] if len(inputString) > maxLength else inputString

#Se define la función para registrar un nuevo gasto
def registerExpense():
    #Se solicita la fecha del gasto al usuario
    dateInput = input("Ingrese la fecha del gasto (DD-MM-AA): ")
    try:
        #Se valida y convierte la fecha a un formato estándar
        dateObject = datetime.strptime(dateInput, "%d-%m-%y")
        formattedDate = f"/{dateObject.day}/{dateObject.strftime('%b')}/{dateObject.year}/"
    except ValueError:
        #Se muestra un mensaje de error si la fecha es inválida
        print("Fecha no válida. Use el formato DD-MM-AA.")
        return

    #Se solicita el monto del gasto al usuario
    try:
        expenseAmount = float(input("Ingrese el monto del gasto: "))
        if expenseAmount <= 0:
            #Se verifica que el monto sea positivo
            print("El monto debe ser mayor que 0.")
            return
    except ValueError:
        #Se muestra un mensaje de error si el monto no es numérico
        print("Monto no válido. Ingrese un número.")
        return

    #Se solicita la categoría del gasto al usuario
    category = input("Ingrese la categoría del gasto: ").capitalize()
    category = maxLength(category, 15)  # Se aplica límite de 15 caracteres

    #Se solicita una descripción opcional del gasto
    description = input("Ingrese una descripción opcional (o presione Enter para omitir): ")
    description = maxLength(description, 50)  # Se aplica límite de 50 caracteres

    #Se crea un diccionario con los datos del gasto
    expenseData = {
        "Fecha": formattedDate,
        "Monto": round(expenseAmount, 2),
        "Categoría": category,
        "Descripción": description if description else "N/A"
    }

    #Se define la ruta del archivo JSON donde se guardarán los datos
    databasePath = "databases/expenses.json"

    try:
        #Se leen los datos existentes utilizando readJSON
        existingData = readJSON(databasePath) or []

        #Se añade el nuevo gasto a la lista existente
        existingData.append(expenseData)

        #Se guardan los datos actualizados utilizando writeJSON
        writeJSON(databasePath, existingData)
        
        #Se confirma al usuario que el gasto se registró correctamente
        print("\nGasto registrado exitosamente:")
        #Se muestra el gasto en formato de tabla
        print(tabulate([expenseData.values()], headers=expenseData.keys(), tablefmt="grid"))
    except Exception as e:
        #Se maneja cualquier error relacionado con la escritura o lectura del archivo
        print(f"Ocurrió un error al guardar el gasto: {e}")