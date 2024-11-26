# Se imprime un mensaje decorativo para un menú  
def displayMenu(headerTitle, options):  
    # Se imprime una línea decorativa  
    print(":" * 40)  
    # Se imprime el título del encabezado  
    print(headerTitle.center(40))  
    # Se imprime otra línea decorativa  
    print(":" * 40)  
    
    # Se imprime las opciones del menú  
    for index, option in enumerate(options, start=1):  
        print(f"{index}. {option}")  
    
    # Se imprime una línea decorativa final  
    print(":" * 40)