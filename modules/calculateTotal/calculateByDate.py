# Se importa para trabajar con archivos JSON
import json

# Se importan las clases datetime y timedelta de la librería datetime para trabajar con fechas  
from datetime import datetime, timedelta  

# Se define la función calculateByDate que recibe la ruta del archivo y el modo de cálculo como parámetros  
def calculateByDate(filePath, mode):  
    try:  
        # Se intenta abrir el archivo en modo lectura ('r')  
        with open(filePath, 'r') as file:  
            # Se carga el contenido del archivo JSON en la variable data  
            data = json.load(file)  
        
        # Se verifica si el archivo no contiene datos  
        if not data:  
            print("No hay gastos registrados.")  
            return  # Se sale de la función si no hay gastos  

        # Se obtiene la fecha de hoy  
        today = datetime.today().date()  
        
        # Se determina la fecha de inicio según el modo especificado  
        if mode == "diario":  
            startDate = today  # Para modo diario, la fecha de inicio es hoy  
        elif mode == "semanal":  
            startDate = today - timedelta(days=7)  # Para modo semanal, se resta 7 días a la fecha de hoy  
        elif mode == "mensual":  
            startDate = today.replace(day=1)  # Para modo mensual, se establece el primer día del mes actual  
        else:  
            print("Modo inválido.")  # Se maneja un modo no válido  
            return  

        # Se filtran los gastos que ocurren desde la fecha de inicio  
        filteredExpenses = [  
            expense for expense in data  
            if datetime.strptime(expense['date'], '%Y-%m-%d').date() >= startDate  
        ]  

        # Se calcula el total de los gastos filtrados  
        total = sum(expense['amount'] for expense in filteredExpenses)  
        # Se imprime el total de gastos según el modo seleccionado  
        print(f"El total de gastos {mode} es: {total}")  
    except Exception as e:  
        # Se maneja cualquier excepción que se produzca y se imprime un mensaje de error  
        print(f"Ocurrió un error al calcular los gastos: {e}")