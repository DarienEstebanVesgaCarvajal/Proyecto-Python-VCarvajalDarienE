# Se importa el menú principal
from modules.mainMenu import mainMenu
# Se importa os para limpiar la consola
import os

# Se ejecuta el programa desde aquí
if __name__ == "__main__":
    try:
        # Limpia la consola antes de mostrar el menú
        os.system('clear')
        mainMenu()
    except KeyboardInterrupt:
        # Manejo de interrupciones por teclado
        print("\nInterrupción detectada.")