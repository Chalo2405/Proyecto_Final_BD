from conexion import obtener_bd


def productos_por_categoria_orden_precio(nombre_categoria: str):
    bd = obtener_bd()
    coleccion = bd.productos

    cursor = coleccion.find(
        {"categoria.nombre": nombre_categoria}
    ).sort("precio", -1)

    print(f"Productos en categoría '{nombre_categoria}' (ordenados por precio desc):")
    for doc in cursor:
        print(f"- {doc['nombre']} | S/ {doc['precio']} | stock: {doc['stock']}")


def buscar_por_texto(texto: str):
    bd = obtener_bd()
    coleccion = bd.productos

    cursor = coleccion.find(
        {"$text": {"$search": texto}},
        {"score": {"$meta": "textScore"}, "nombre": 1, "precio": 1, "descripcion": 1}
    ).sort("score", {"$meta": "textScore"})

    print(f"Resultados de búsqueda de texto: '{texto}'")
    for doc in cursor:
        print(f"- {doc['nombre']} | S/ {doc['precio']}")
        print(f"  Descripción: {doc['descripcion']}\n")


def productos_por_rango_precio(nombre_categoria: str, minimo: float, maximo: float):
    bd = obtener_bd()
    coleccion = bd.productos

    filtro = {
        "categoria.nombre": nombre_categoria,
        "precio": {"$gte": minimo, "$lte": maximo}
    }

    cursor = coleccion.find(filtro).sort("precio", 1)

    print(f"Productos en '{nombre_categoria}' con precio entre {minimo} y {maximo}:")
    for doc in cursor:
        print(f"- {doc['nombre']} | S/ {doc['precio']}")


if __name__ == "__main__":
    productos_por_categoria_orden_precio("Electrónica")
    print("=" * 60)

    buscar_por_texto("gamer laptop")
    print("=" * 60)

    productos_por_rango_precio("Hogar", 200, 1000)
