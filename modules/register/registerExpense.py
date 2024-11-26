from datetime import datetime
from modules.utils.fileHandler import readJSON, writeJSON
import tabulate

# Se define la función para verificar el máximo tamaño permitido en una cadena
def maxLength(inputString, maxLength):
    # Se retorna la cadena truncada si excede el tamaño máximo
    return inputString[:maxLength] if len(inputString) > maxLength else inputString

# Se define la función para registrar un nuevo gasto
def registerExpense(databasePath):
    try:
        # Solicitar información del gasto al usuario
        expenseName = input("Ingrese el nombre del gasto: ")
        expenseAmount = float(input("Ingrese el monto del gasto: "))
        expenseDate = input("Ingrese la fecha del gasto (YYYY-MM-DD): ")
        expenseCategory = input("Ingrese la categoría del gasto: ")  # Se solicita la categoría

        # Validar y formatear la fecha
        try:
            expenseDate = datetime.strptime(expenseDate, "%Y-%m-%d").date()
        except ValueError:
            print("La fecha ingresada no es válida. Se utilizará la fecha actual.")
            expenseDate = datetime.now().date()

        # Crear un diccionario con los datos del gasto
        expenseData = {
            "nombre": maxLength(expenseName, 50),
            "monto": expenseAmount,
            "fecha": str(expenseDate),
            "categoría": maxLength(expenseCategory, 30)  # Agregar categoría al diccionario
        }

        # Leer datos existentes del archivo JSON
        existingData = readJSON(databasePath)

        # Agregar el nuevo gasto a los datos existentes
        existingData.append(expenseData)

        # Se guardan los datos actualizados utilizando writeJSON
        writeJSON(databasePath, existingData)

        # Se confirma al usuario que el gasto se registró correctamente
        print("\nGasto registrado exitosamente:")
        # Se muestra el gasto en formato de tabla
        print(tabulate.tabulate([expenseData.values()], headers=expenseData.keys(), tablefmt="grid"))
    except Exception as e:
        # Se maneja cualquier error relacionado con la escritura o lectura del archivo
        print(f"Ocurrió un error al guardar el gasto: {e}")