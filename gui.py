import tkinter as tk

productos = []  # lista donde guardamos los productos

def agregar_producto():
    # Crear una ventana nueva (hija)
    ventana_agregar = tk.Toplevel()
    ventana_agregar.title("Agregar producto")
    ventana_agregar.geometry("300x250")

    # Etiquetas y campos de entrada
    tk.Label(ventana_agregar, text="Nombre:").pack(pady=5)
    entrada_nombre = tk.Entry(ventana_agregar)
    entrada_nombre.pack()

    tk.Label(ventana_agregar, text="Categoría:").pack(pady=5)
    entrada_categoria = tk.Entry(ventana_agregar)
    entrada_categoria.pack()

    tk.Label(ventana_agregar, text="Precio (entero):").pack(pady=5)
    entrada_precio = tk.Entry(ventana_agregar)
    entrada_precio.pack()

    # Función interna para guardar el producto
    def guardar():
        nombre = entrada_nombre.get()
        categoria = entrada_categoria.get()
        precio = entrada_precio.get()

        if not precio.isdigit():
            tk.messagebox.showerror("Error", "El precio debe ser un número entero.")
            return

        productos.append([nombre, categoria, int(precio)])
        tk.messagebox.showinfo("Éxito", "¡Producto guardado con éxito!")
        ventana_agregar.destroy()  # cerramos la ventana

    # Botón para guardar
    boton_guardar = tk.Button(ventana_agregar, text="Guardar", command=guardar)
    boton_guardar.pack(pady=10)

def mostrar_productos():
    print("📋 Mostrar productos (función en desarrollo)")

def buscar_producto():
    print("🔍 Buscar producto (función en desarrollo)")

def eliminar_producto():
    print("🗑 Eliminar producto (función en desarrollo)")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("🛒 Gestor de Productos")
ventana.geometry("300x350")
ventana.resizable(False, False)

# Etiqueta de título
titulo = tk.Label(ventana, text="Gestor de Productos", font=("Arial", 16))
titulo.pack(pady=20)

# Estilo común para botones
estilo_boton = {
    "width": 25,
    "height": 2,
    "bg": "#C9ADA1",   # rosa antiguo
    "fg": "red",
    "font": ("Georgia", 12),
    "bd": 0,
    "activebackground": "#D4A5A5"
}

# Botones
tk.Button(ventana, text="➕ Agregar producto", width=25, command=agregar_producto).pack(pady=5)
tk.Button(ventana, text="📋 Mostrar productos", width=25, command=mostrar_productos).pack(pady=5)
tk.Button(ventana, text="🔍 Buscar producto", width=25, command=buscar_producto).pack(pady=5)
tk.Button(ventana, text="🗑 Eliminar producto", width=25, command=eliminar_producto).pack(pady=5)
tk.Button(ventana, text="❌ Salir", width=25, command=ventana.destroy).pack(pady=20)

# Iniciar la ventana
ventana.mainloop()