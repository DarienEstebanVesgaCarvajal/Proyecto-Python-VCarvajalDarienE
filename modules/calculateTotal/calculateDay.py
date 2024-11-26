from datetime import datetime  # Se importa la clase datetime para trabajar con fechas y horas.  
import json  # Se importa el módulo json para manejar archivos JSON.  

def calculateDay(filePath):  
    """Se encarga de calcular el total de gastos del día actual a partir de un archivo JSON."""  
    try:  
        # Se lee el contenido del archivo JSON.  
        with open(filePath, 'r') as file:  
            expenses = json.load(file)  # Se cargan los datos del archivo en la variable 'expenses'.  
        
        # Se valida si hay datos en el archivo.  
        if not expenses:  # Si la lista de gastos está vacía.  
            print("No hay gastos registrados.")  # Se muestra un mensaje informativo.  
            return  # Se sale de la función si no hay gastos registrados.  

        # Se obtiene la fecha de hoy.  
        today = datetime.today().date()  

        # Se filtran los gastos por la fecha de hoy y se calcula el total.  
        totalToday = sum(  
            expense['monto'] for expense in expenses   
            if datetime.strptime(expense['fecha'], '%Y-%m-%d').date() == today  # Se compara la fecha de cada gasto con la fecha actual.  
        )  

        # Se muestra el total de gastos del día.  
        print(f"El total de gastos del día es: COP {totalToday}")  
    
    except Exception as e:  
        # Se captura cualquier error que ocurra durante la ejecución.  
        print(f"Ocurrió un error al calcular los gastos: {e}")  # Se muestra un mensaje de error.