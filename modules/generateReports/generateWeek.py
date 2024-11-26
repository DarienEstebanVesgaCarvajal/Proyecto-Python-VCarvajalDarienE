# Se importan las clases datetime y timedelta del módulo datetime para trabajar con fechas y calcular intervalos  
from datetime import datetime, timedelta  
# Se importa el módulo json para manejar archivos JSON  
import json  

# Se define la función generateWeek que recibe la ruta del archivo como parámetro  
def generateWeek(filePath):  
    try:  
        # Se leen los datos del archivo JSON  
        with open(filePath, 'r') as file:  
            data = json.load(file)  # Se carga el contenido del archivo en la variable data  

        # Se verifica si no hay datos en el archivo  
        if not data:  
            print("No hay gastos registrados.")  # Mensaje si no hay gastos  
            return  # Se sale de la función si no hay datos  

        today = datetime.today().date()  # Se obtiene la fecha actual  
        startDate = today - timedelta(days=7)  # Se calcula la fecha de inicio de la semana (hace 7 días)  

        # Se filtran los gastos de la última semana  
        weeklyExpenses = [  
            expense for expense in data  # Se recorre cada gasto en los datos  
            if 'fecha' in expense and 'monto' in expense and 'nombre' in expense and 
               startDate <= datetime.strptime(expense['fecha'], '%Y-%m-%d').date() <= today  # Se verifica si la fecha del gasto está dentro del rango  
        ]  

        # Se verifica si no hay gastos registrados para la última semana  
        if not weeklyExpenses:  
            print("No hay gastos registrados para la última semana.")  # Mensaje si no hay gastos de la semana  
            return  # Se sale de la función si no hay gastos  

        # Se calcula el total semanal de los gastos  
        total = sum(expense['monto'] for expense in weeklyExpenses)  # Se suma el monto de todos los gastos de la semana  

        # Se imprime el reporte semanal  
        print("Reporte Semanal:")  # Encabezado del reporte  
        print(f"Total de la semana: {total}")  # Total de gastos de la semana  
        
        # Se imprime cada gasto de la última semana  
        for expense in weeklyExpenses:  
            print(f"{expense['nombre']} - {expense['monto']} - {expense['fecha']}")  # Detalle de cada gasto  
    except KeyError as e:  
        # Se captura un error si falta una clave en los datos  
        print(f"Error en el formato de los datos: falta la clave {e}")  # Mensaje de error específico  
    except Exception as e:  
        # Se captura cualquier otra excepción que ocurra  
        print(f"Ocurrió un error al generar el reporte semanal: {e}")  # Mensaje de error general