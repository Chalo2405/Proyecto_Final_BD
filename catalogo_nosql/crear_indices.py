from conexion import obtener_bd


def crear_indices_productos():
    bd = obtener_bd()
    coleccion = bd.productos


    coleccion.create_index("stock", name="idx_stock")


    coleccion.create_index(
        [("categoria.nombre", 1), ("precio", -1)],
        name="idx_categoria_precio"
    )


    coleccion.create_index(
        [("nombre", "text"), ("descripcion", "text")],
        name="idx_texto_producto"
    )

    print("Índices creados:")
    for nombre, info in coleccion.index_information().items():
        print(f"- {nombre}: {info}")


if __name__ == "__main__":
    crear_indices_productos()
