# Se importan las clases datetime y json para trabajar con fechas y manejar archivos JSON  
from datetime import datetime  
import json  

# Se define la función generateMonth que recibe la ruta del archivo como parámetro  
def generateMonth(filePath):  
    try:  
        # Se abre el archivo JSON para leer los datos de gastos  
        with open(filePath, 'r') as file:  
            data = json.load(file)  # Se carga el contenido del archivo en la variable data  

        # Se verifica si no hay datos en el archivo  
        if not data:  
            print("No hay gastos registrados.")  # Mensaje si no hay gastos  
            return  # Se sale de la función si no hay datos  

        today = datetime.today().date()  # Se obtiene la fecha actual  
        startDate = today.replace(day=1)  # Se establece la fecha de inicio del mes actual  

        # Filtrar gastos del mes actual  
        monthlyExpenses = [  
            expense for expense in data  # Se recorre cada gasto en los datos  
            if 'fecha' in expense and 'monto' in expense and 'nombre' in expense and 
               startDate <= datetime.strptime(expense['fecha'], '%Y-%m-%d').date() <= today  
            # Se verifica si la fecha del gasto está dentro del rango del mes actual  
        ]  

        # Se verifica si no hay gastos registrados para el mes actual  
        if not monthlyExpenses:  
            print("No hay gastos registrados para este mes.")  # Mensaje si no hay gastos del mes  
            return  # Se sale de la función si no hay gastos  

        # Calcular el total mensual de los gastos  
        total = sum(expense['monto'] for expense in monthlyExpenses)  
        # Se suma el monto de todos los gastos del mes  

        # Se imprime el reporte mensual  
        print("Reporte Mensual:")  # Encabezado del reporte  
        print(f"Total del mes: {total}")  # Total de gastos del mes  
        
        # Se imprime cada gasto del mes actual  
        for expense in monthlyExpenses:  
            print(f"{expense['nombre']} - {expense['monto']} - {expense['fecha']}")  
            # Detalle de cada gasto  
    except KeyError as e:  
        # Se captura un error si falta una clave en los datos  
        print(f"Error en el formato de los datos: falta la clave {e}")  # Mensaje de error específico  
    except Exception as e:  
        # Se captura cualquier otra excepción que ocurra  
        print(f"Ocurrió un error al generar el reporte mensual: {e}")  # Mensaje de error general