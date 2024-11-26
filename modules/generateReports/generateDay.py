# Se importa la clase datetime del módulo datetime para trabajar con fechas  
from datetime import datetime  
# Se importa el módulo json para manejar archivos JSON  
import json  

# Se define la función generateDay que recibe la ruta del archivo como parámetro  
def generateDay(filePath):  
    try:  
        # Se leen los datos del archivo JSON  
        with open(filePath, 'r') as file:  
            data = json.load(file)  # Se carga el contenido del archivo en la variable data  
        
        # Se verifica si no hay datos en el archivo  
        if not data:  
            print("No hay gastos registrados.")  # Mensaje si no hay gastos  
            return  # Se sale de la función si no hay datos  

        today = datetime.today().date()  # Se obtiene la fecha actual  

        # Se filtran los gastos del día actual  
        dailyExpenses = [  
            expense for expense in data  # Se recorre cada gasto en los datos  
            if 'fecha' in expense and 'monto' in expense and 'nombre' in expense and 
               datetime.strptime(expense['fecha'], '%Y-%m-%d').date() == today  # Se compara la fecha del gasto con la fecha actual  
        ]  

        # Se verifica si no hay gastos registrados para el día de hoy  
        if not dailyExpenses:  
            print("No hay gastos registrados para el día de hoy.")  # Mensaje si no hay gastos del día  
            return  # Se sale de la función si no hay gastos  

        # Se calcula el total diario de los gastos  
        total = sum(expense['monto'] for expense in dailyExpenses)  # Se suma el monto de todos los gastos del día  

        # Se imprime el reporte diario  
        print("Reporte Diario:")  # Encabezado del reporte  
        print(f"Total del día: {total}")  # Total de gastos del día  
        
        # Se imprime cada gasto del día actual  
        for expense in dailyExpenses:  
            print(f"{expense['nombre']} - {expense['monto']} - {expense['fecha']}")  # Detalle de cada gasto  
    except KeyError as e:  
        # Se captura un error si falta una clave en los datos  
        print(f"Error en el formato de los datos: falta la clave {e}")  # Mensaje de error específico  
    except Exception as e:  
        # Se captura cualquier otra excepción que ocurra  
        print(f"Ocurrió un error al generar el reporte diario: {e}")  # Mensaje de error general