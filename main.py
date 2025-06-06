# Crear un menú con opciones
# 1- Agregar producto nuevo
# 2- Remover un producto
# 3- Ver productos
# 4- Buscar producto
# 5- Salir


#Lista para guardar los productos.
productos = []

#Función para pedir nombre, categoria y precio y que guarde los datos en una sublista
def agregarProducto():
    nombre = input("¿Cuál es el nombre del producto?: ")
    categoria = input("¿Cuál es la categoría del producto?: ")

    # El precio tiene que ser un entero
    precio = input("¿Cuál es el precio del producto (sin centavos)?: ")
    if precio.isdigit():
        precio = int(precio)
        productos.append([nombre, categoria, precio])
        print("Producto agregado exitosamente 🎉!")
    else:
        print("Chequeá que el número sea un entero 🙏")

#Creamos una función que muestre los productos
def mostrarProductos():
    print("\nLos productos guardados son:")
    if len(productos) == 0:
        print ("Todavia no guardaste ningún producto.")
    else:
        contador = 1
        for producto in productos:
            print(f"\n🛒 Producto {contador}:")
            print(f"  🏷️ Nombre: {producto[0]}")
            print(f"  🗂️ Categoría: {producto[1]}")
            print(f"  💲 Precio: {producto[2]}")
            contador += 1

#Función para buscar productos
def buscarProducto():
    tipo = input("Buscamos por nombre o categoría?: ").lower()

    if tipo!="nombre" and tipo !="categoria":
        print("Perdón, por ahora solo se puede buscar por nombre o categoría")
        return
    palabra = input("Qué estás buscando?: ").lower()

    print("\n🔎Resultado de la búsqueda:" )
    encontrados = False
    contador = 1
    for producto in productos:
        campo = producto [0].lower() if tipo == "nombre" else producto[1].lower()
        if palabra in campo:
            print(f"\n🛒 Producto {contador}:")
            print(f" 🏷️ Nombre: {producto[0]}")
            print(f" 🗂️ Categoría: {producto[1]}")
            print(f" 💲 Precio: {producto[2]}")
            encontrados = True
            contador += 1

    if not encontrados:
        print("Todavía no tenemos productos que coincidan con lo que estás buscando")


#Función para eliminar productos
def eliminarProducto():
    if len(productos) == 0:
        print("No hay productos para eliminar.")
        return
    nombreBuscado = input("Qué producto necesitás eliminar?: ").lower()

    i = 0
    while i < len (productos):
        producto = productos[i]
        if producto[0].lower() == nombreBuscado:
            productos.pop(i)
            print(f"Producto '{producto[0]}' eliminado exitosamente.")
            return
        else:
            i += 1

    print("No tenemos ningún producto con ese nombre")


#Armamos el menú principal
while True:
    print("\nEn qué te puedo ayudar?")
    print("1. Agregar un producto nuevo ➕")
    print("2. Ver los productos ya cargados 📋")
    print("3. Buscar un producto 🔎")
    print("4. Eliminar producto 🗑️")
    print("5. Salir ")

    opcion = input ("Elegiste una opción?: ")

    if opcion == "1":
        agregarProducto()
    elif opcion == "2":
        mostrarProductos()
    elif opcion == "3":
        buscarProducto()
    elif opcion == "4":
        eliminarProducto()
    elif opcion == "5":
        print("Gracias! Esperamos que vuelvas pronto! 👋🏻")
        break
    else:
        print("Esa opción no existe, probá con números del 1 al 5.")

    volver = input("\n↩️ Querés volver al menú principal? (si/no): ").lower()
    if volver != "si":
        print("Hasta la próxima!👋🏻")
        break

