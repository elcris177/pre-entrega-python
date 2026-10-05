productos = ["arroz","fideo","pan","agua"]

while True:
    
    opcion = input("A - Para Agregar\nB - Para Buscar\nL - Para listar\nR - Para Remover\nQ - para Quitar\n-------------------\nS - Para salir\n\n")
    
    if opcion == "S":
        break
    
    elif opcion == "L":
     for producto in productos:
        print(producto)
    
    elif opcion == "A":
        agregar = input("Producto a agregar: \n")
        productos.append(agregar)
        print(f"\n{agregar} se ha agregado con exito!\n")
        
    elif opcion == "R":
        remover = input("Producto a remover: \n")
        productos.remove(remover)
        print(f"\n{remover} se ha removido con exito!\n")

    elif opcion == "B":
        buscar = input("Producto a buscar: \n")
        if buscar in productos:
            print("\nHay stock!\n")
        else:
            print(f"\nNo hay stock de {buscar}\n")
