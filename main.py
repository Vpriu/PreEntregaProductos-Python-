# Crear un menú con opciones
# 1- Agregar producto nuevo
# 2- Remover un producto
# 3- Ver productos
# 4- Buscar producto
# 5- Salir


#productos = [] ya no va mas esta lista, ahora armamos una base de datos 

import sqlite3


# Crear la base de datos 
def crearBaseDatos():
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio INTEGER NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()


# Guardar producto en la base de datos porque eliminamos el archivo .txt

def guardarProductoEnBD(nombre, categoria, precio):
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (nombre, categoria, precio) VALUES (?, ?, ?)", (nombre, categoria, precio))
    conexion.commit()
    conexion.close()


# Agregar producto desde input

def agregarProducto():
    nombre = input("¿Cuál es el nombre del producto?: ")
    categoria = input("¿Cuál es la categoría del producto?: ")
    precio = input("¿Cuál es el precio del producto (sin centavos)?: ")
    
    if precio.isdigit():
        precio = int(precio)
        guardarProductoEnBD(nombre, categoria, precio)
        print("Producto agregado exitosamente 🎉!")
    else:
        print("Chequeá que el número sea un entero 🙏")


# Mostrar todos los productos guardados desde la BD

def mostrarProductosDesdeBD():
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    if not productos:
        print("\nTodavía no hay productos guardados en la base de datos.")
    else:
        print("\n🧾 Productos guardados en la base de datos:\n")
        for producto in productos:
            print(f" 🔢ID: {producto[0]}")
            print(f" 🏷️ Nombre: {producto[1]}")
            print(f" 🗂️ Categoría: {producto[2]}")
            print(f" 💲 Precio: {producto[3]}")
            print("-" * 30)

    conexion.close()


# Buscar producto por nombre o categoría desde la BD

def buscarProductoDesdeBD():
    tipo = input("¿Buscamos por ID, nombre o categoría?: ").lower()

    if tipo not in ["id", "nombre", "categoria"]:
        print("Solo se puede buscar por id, nombre o categoría.")
        return

    palabra = input("¿Qué estás buscando?: ").lower()

    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()
    
    if tipo == "id":
        if not palabra.isdigit():
            print("El ID solo puede ser un número.")
            return
        cursor.execute("SELECT * FROM productos WHERE id = ?", (int(palabra),))
    else:
        cursor.execute(f"SELECT * FROM productos WHERE LOWER({tipo}) LIKE ?", ("%" + palabra + "%"))

    resultados = cursor.fetchall()

    if resultados:
        print("\n🔎 Resultado de la búsqueda:")
        for producto in resultados:
            print(f"\n🛒 Producto {i}:")
            print(f" 🔢ID: {producto[0]}")
            print(f" 🏷️ Nombre: {producto[1]}")
            print(f" 🗂️ Categoría: {producto[2]}")
            print(f" 💲 Precio: {producto[3]}")
    else:
        print("No se encontraron productos que coincidan con la búsqueda.")

    conexion.close()


# Eliminar producto por nombre desde la BD

def eliminarProductoDesdeBD():
    nombre = input("¿Qué producto necesitás eliminar?: ").lower()

    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE LOWER(nombre) = ?", (nombre,))
    conexion.commit()

    if cursor.rowcount == 0:
        print("No se encontró ningún producto con ese nombre.")
    else:
        print(f"Producto '{nombre}' eliminado exitosamente.")

    conexion.close()


# MENÚ PRINCIPAL

crearBaseDatos()  

while True:
    print("\n📦 ¿En qué te puedo ayudar?")
    print("1. Agregar un producto nuevo ➕")
    print("2. Ver los productos ya cargados 📋")
    print("3. Buscar un producto 🔎")
    print("4. Eliminar producto 🗑️")
    print("5. Salir ")

    opcion = input("Elegí una opción (1-5): ")

    if opcion == "1":
        agregarProducto()
    elif opcion == "2":
        mostrarProductosDesdeBD()
    elif opcion == "3":
        buscarProductoDesdeBD()
    elif opcion == "4":
        eliminarProductoDesdeBD()
    elif opcion == "5":
        print("Gracias! Esperamos que vuelvas pronto! 👋🏻")
        break
    else:
        print("Esa opción no existe, probá con números del 1 al 5.")

    volver = input("\n↩️ ¿Querés volver al menú principal? (si/no): ").lower()
    if volver != "si":
        print("Hasta la próxima! 👋🏻")
        break