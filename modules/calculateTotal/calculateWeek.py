from datetime import datetime, timedelta  # Se importan las clases datetime y timedelta para trabajar con fechas.  
import json  # Se importa el módulo json para manejar archivos JSON.  

def calculateWeek(filePath):  
    """  
    Se encarga de calcular el total de gastos de la semana actual a partir de un archivo JSON.  
    
    :param filePath: Se especifica la ruta del archivo JSON que contiene los gastos.  
    """  
    try:  
        # Se lee el contenido del archivo JSON.  
        with open(filePath, 'r') as file:  
            expenses = json.load(file)  # Se cargan los datos del archivo en la variable 'expenses'.  
        
        # Se valida si hay datos en el archivo.  
        if not expenses:  # Si la lista de gastos está vacía.  
            print("No hay gastos registrados.")  # Se muestra un mensaje informativo.  
            return  # Se sale de la función si no hay gastos registrados.  

        # Se obtiene la fecha de hoy y se calcula el rango de la semana.  
        today = datetime.today().date()  # Se obtiene la fecha actual.  
        startOfWeek = today - timedelta(days=7)  # Se calcula la fecha de inicio de la semana (hace 7 días).  

        # Se filtran los gastos por el rango semanal y se calcula el total.  
        totalWeek = sum(  
            expense['monto'] for expense in expenses   
            if startOfWeek <= datetime.strptime(expense['fecha'], '%Y-%m-%d').date() <= today  # Se verifica si la fecha del gasto está dentro del rango de la semana.  
        )  

        # Se muestra el total de gastos de la semana.  
        print(f"El total de gastos de la semana es: COP {totalWeek}")  
    
    except Exception as e:  
        # Se captura cualquier error que ocurra durante la ejecución.  
        print(f"Ocurrió un error al calcular los gastos: {e}")  # Se muestra un mensaje de error.