from datetime import datetime
import json

def calculateDay(filePath):
    try:
        # Leer el JSON
        with open(filePath, 'r') as file:
            expenses = json.load(file)
        
        # Validar si hay datos
        if not expenses:
            print("No hay gastos registrados.")
            return

        # Obtener fecha de hoy
        today = datetime.today().date()

        # Filtrar por la fecha de hoy
        totalToday = sum(
            expense['monto'] for expense in expenses 
            if datetime.strptime(expense['fecha'], '%Y-%m-%d').date() == today
        )

        print(f"El total de gastos del día es: COP {totalToday}")
    except Exception as e:
        print(f"Ocurrió un error al calcular los gastos: {e}")