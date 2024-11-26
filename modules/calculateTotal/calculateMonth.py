from datetime import datetime  # Se importa la clase datetime para trabajar con fechas y horas.  
import json  # Se importa el módulo json para manejar archivos JSON.  

def calculateMonth(filePath):  
    """  
    Se encarga de calcular el total de gastos del mes actual a partir de un archivo JSON.  
    
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

        # Se obtiene el mes y año actuales.  
        today = datetime.today()  # Se obtiene la fecha y hora actuales.  
        currentMonth = today.month  # Se extrae el mes actual.  
        currentYear = today.year  # Se extrae el año actual.  

        # Se filtran los gastos por el mes y año actuales y se calcula el total.  
        totalMonth = sum(  
            expense['monto'] for expense in expenses   
            if datetime.strptime(expense['fecha'], '%Y-%m-%d').month == currentMonth and  # Se compara el mes de cada gasto.  
               datetime.strptime(expense['fecha'], '%Y-%m-%d').year == currentYear  # Se compara el año de cada gasto.  
        )  

        # Se muestra el total de gastos del mes.  
        print(f"El total de gastos del mes es: COP {totalMonth}")  
    
    except Exception as e:  
        # Se captura cualquier error que ocurra durante la ejecución.  
        print(f"Ocurrió un error al calcular los gastos: {e}")  # Se muestra un mensaje de error.