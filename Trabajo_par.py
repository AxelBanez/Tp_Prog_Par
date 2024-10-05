
def mostrar_menu():
    print("""
          Menu:
        1- Agregar producto al inventario. 
        2- Realizar una venta. 
        3- Mostrar productos disponibles. 
        4- Salir del sistema.
          
          """)

def agregar_producto(lista: list):
 
    nombre = input("Ingrese el nombre del producto a agregar: ")
    cantidad = input("Ingrese la cantidad del producto: ")
    precio = input("Ingrese el precio del producto: ")

    lista.append([nombre, cantidad, precio])

    print(f"El producto {nombre} fue agregado al inventario correctamente.")

def mostrar_productos(lista: list):

    print("-" * 50)
    print(f"{'N°':<5} {'Producto':<30} {'Cantidad':<10} {'Precio':<10}")
    print("-" * 50)

    for i in range(len(lista)):
        producto = lista[i][0]
        cantidad = lista[i][1]
        precio = lista[i][2]
        
        print(f"{i + 1:<5} {producto:<30} {cantidad:<10} {precio:<10}")
    
    print("-" * 50)

def realizar_venta(lista: list):
    mostrar_productos(lista)

    numero_producto = int(input("Selecciona el numero del producto que desees comprar: ")) - 1

    if 0 <= numero_producto < len(lista):
        cantidad = int(input(f"Introduce la cantidad de {lista[numero_producto][0]} que desees comprar: "))

        if cantidad > 0 and cantidad <= lista[numero_producto][1]:
            total = cantidad * lista[numero_producto][2]
            lista[numero_producto][1] -= cantidad 
            print(f"Total a pagar: {total}")
        else:
            print("No hay suficiente stock.")
    else:
        print("Producto no valido.")







inventario = [
    ["Chupetin Sable de luz", 50, 200],
    ["Agua La Fuerza", 35, 3200],
    ["Gomitas Holocubo", 25, 900],
    ["Barrita de Cereal Wookiee", 48, 2500],
    ["Galletitas R2D2", 20, 15800]
    ]

corriendo = True

while corriendo:
    mostrar_menu()

    opcion = input("Elija una opcion: ")

    match opcion:
        case "1":
            agregar_producto(inventario)
        case "2":
            print("Los productos disponibles son: ")
            realizar_venta(inventario)
        case "3":
            print( "Mostrando Productos...")
            mostrar_productos(inventario)
        case "4":
            print("Saliendo de la tienda")
            break
        case _:
            print("Opcion invalida, ingrese otra: ")
    
    