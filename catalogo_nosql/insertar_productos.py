from conexion import obtener_bd
from datos_iniciales import obtener_productos_iniciales


def insertar_productos():
    bd = obtener_bd()
    coleccion = bd.productos

    # Limpia la colección para pruebas repetibles (opcional)
    resultado_borrado = coleccion.delete_many({})
    print("Documentos eliminados:", resultado_borrado.deleted_count)

    productos = obtener_productos_iniciales()
    resultado = coleccion.insert_many(productos)
    print("Productos insertados:", len(resultado.inserted_ids))


if __name__ == "__main__":
    insertar_productos()
