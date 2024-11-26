# Se importa el menú principal
from modules.mainMenu import mainMenu
# Se importa os para limpiar la consola
import os
import signal  # Para manejar señales del sistema como SIGINT (Ctrl + C)

# Función personalizada para manejar SIGINT
def customSignalHandler(signum, frame):
    print("\nCtrl + C no está permitido. Por favor, use las opciones del programa.")

# Se asigna la función personalizada para manejar SIGINT
signal.signal(signal.SIGINT, customSignalHandler)

# Se ejecuta el programa desde aquí
if __name__ == "__main__":
    while True:
        # Limpia la consola antes de mostrar el menú
        os.system('clear')
        mainMenu()