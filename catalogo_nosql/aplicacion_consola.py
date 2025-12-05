from conexion import obtener_bd
from datetime import datetime, timezone


def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL - CATÁLOGO NoSQL =====")
    print("1. Listar productos")
    print("2. Consultar stock de un producto")
    print("3. Agregar stock a un producto")
    print("4. Registrar venta")
    print("5. Agregar nuevo producto")
    print("6. Salir")


def listar_productos(bd):
    productos = bd.productos.find({}, {"nombre": 1, "precio": 1, "stock": 1})
    print("\n--- LISTA DE PRODUCTOS ---")
    for p in productos:
        print(f"ID: {p['_id']} | {p['nombre']} | Precio: {p['precio']} | Stock: {p['stock']}")


def seleccionar_producto(bd):
    coleccion = bd.productos

    print("\n--- SELECCIONAR PRODUCTO ---")
    print("1. Buscar por categoría")
    print("2. Ver todos los productos")
    opcion = input("Seleccione una opción [1/2]: ").strip()

    filtro = {}
    if opcion == "1":
        categoria = input("Ingrese el nombre de la categoría (Ej. Electrónica, Hogar, Ropa): ").strip()
        if categoria:
            filtro = {"categoria.nombre": categoria}

    productos = list(coleccion.find(filtro, {"nombre": 1, "precio": 1, "stock": 1, "categoria": 1}))

    if not productos:
        print("No se encontraron productos con ese criterio.")
        return None

    print("\nProductos encontrados:")
    for i, p in enumerate(productos, start=1):
        print(f"{i}. {p['nombre']} | Precio: {p['precio']} | Stock: {p['stock']}")

    try:
        indice = int(input("Ingrese el número del producto: ").strip())
        if indice < 1 or indice > len(productos):
            print("Número fuera de rango.")
            return None
    except ValueError:
        print("Número inválido.")
        return None

    return productos[indice - 1]


def consultar_stock(bd):
    print("\n--- CONSULTAR STOCK ---")
    producto = seleccionar_producto(bd)
    if not producto:
        return

    print(f"\nProducto: {producto['nombre']}")
    print(f"Precio: {producto['precio']}")
    print(f"Stock disponible: {producto['stock']}")


def agregar_stock(bd):
    print("\n--- AGREGAR STOCK ---")
    producto = seleccionar_producto(bd)
    if not producto:
        return

    print(f"Producto: {producto['nombre']} | Stock actual: {producto['stock']}")

    try:
        cantidad = int(input("Cantidad a agregar: ").strip())
        if cantidad <= 0:
            print("La cantidad debe ser mayor que 0.")
            return
    except ValueError:
        print("Cantidad inválida.")
        return

    bd.productos.update_one(
        {"_id": producto["_id"]},
        {"$inc": {"stock": cantidad}}
    )

    print("Stock actualizado correctamente.")


def registrar_venta(bd):
    print("\n--- REGISTRAR VENTA ---")
    producto = seleccionar_producto(bd)
    if not producto:
        return

    print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Stock actual: {producto['stock']}")

    try:
        cantidad = int(input("Cantidad a vender: ").strip())
        if cantidad <= 0:
            print("La cantidad debe ser mayor que 0.")
            return
    except ValueError:
        print("Cantidad inválida.")
        return

    if cantidad > producto["stock"]:
        print("No hay stock suficiente para esta venta.")
        return

    nuevo_stock = producto["stock"] - cantidad
    bd.productos.update_one(
        {"_id": producto["_id"]},
        {"$set": {"stock": nuevo_stock}}
    )

    # categoría del producto (si no está, ponemos una por defecto)
    categoria = producto.get("categoria", {"nombre": "Sin categoría", "subcategoria": "N/A"})

    venta = {
        "producto_id": producto["_id"],
        "nombre_producto": producto["nombre"],
        "categoria": categoria,
        "cantidad": cantidad,
        "precio_unitario": producto["precio"],
        "monto_total": cantidad * producto["precio"],
        "fecha": datetime.now(timezone.utc)  # fecha con zona horaria correcta
    }

    bd.ventas.insert_one(venta)

    print("Venta registrada correctamente.")
    print(f"Nuevo stock del producto: {nuevo_stock}")
    print(f"Monto total de la venta: {venta['monto_total']}")


def agregar_nuevo_producto(bd):
    print("\n--- AGREGAR NUEVO PRODUCTO ---")

    nombre = input("Nombre del producto: ").strip()
    descripcion = input("Descripción: ").strip()

    try:
        precio = float(input("Precio (Ej. 499.90): ").strip())
        if precio <= 0:
            print("El precio debe ser mayor que 0.")
            return
    except ValueError:
        print("Precio inválido.")
        return

    categoria_nombre = input("Categoría (Ej. Electrónica, Hogar, Ropa): ").strip()
    categoria_sub = input("Subcategoría (Ej. Laptops, Muebles, Calzado): ").strip()

    try:
        stock = int(input("Stock inicial: ").strip())
        if stock < 0:
            print("El stock no puede ser negativo.")
            return
    except ValueError:
        print("Stock inválido.")
        return

    etiquetas_texto = input("Etiquetas (separadas por comas, ej. gamer,laptop,oferta): ").strip()
    etiquetas = [e.strip() for e in etiquetas_texto.split(",") if e.strip()] if etiquetas_texto else []

    nuevo_producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "categoria": {
            "nombre": categoria_nombre,
            "subcategoria": categoria_sub
        },
        "stock": stock,
        "etiquetas": etiquetas
    }

    resultado = bd.productos.insert_one(nuevo_producto)
    print("\nProducto agregado correctamente.")
    print(f"ID generado: {resultado.inserted_id}")


def main():
    bd = obtener_bd()
    print("Conectado a la base de datos:", bd.name)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            listar_productos(bd)
        elif opcion == "2":
            consultar_stock(bd)
        elif opcion == "3":
            agregar_stock(bd)
        elif opcion == "4":
            registrar_venta(bd)
        elif opcion == "5":
            agregar_nuevo_producto(bd)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
