from conexion import obtener_bd


def resumen_por_categoria():
    bd = obtener_bd()
    coleccion = bd.productos

    pipeline = [
        {
            "$group": {
                "_id": "$categoria.nombre",
                "total_productos": {"$sum": 1},
                "stock_total": {"$sum": "$stock"},
                "precio_promedio": {"$avg": "$precio"},
            }
        },
        {"$sort": {"precio_promedio": -1}}
    ]

    print("Resumen por categoría:")
    for doc in coleccion.aggregate(pipeline):
        print(
            f"- {doc['_id']}: "
            f"{doc['total_productos']} productos, "
            f"stock total {doc['stock_total']}, "
            f"precio promedio S/ {round(doc['precio_promedio'], 2)}"
        )


def promedio_calificaciones_por_producto():
    bd = obtener_bd()
    coleccion = bd.productos

    pipeline = [
        {"$unwind": "$calificaciones"},
        {
            "$group": {
                "_id": "$nombre",
                "promedio_puntuacion": {"$avg": "$calificaciones.puntuacion"},
                "total_calificaciones": {"$sum": 1},
            }
        },
        {"$sort": {"promedio_puntuacion": -1}}
    ]

    print("\nPromedio de calificaciones por producto:")
    for doc in coleccion.aggregate(pipeline):
        print(
            f"- {doc['_id']}: "
            f"promedio {round(doc['promedio_puntuacion'], 2)} "
            f"({doc['total_calificaciones']} calificaciones)"
        )


if __name__ == "__main__":
    resumen_por_categoria()
    promedio_calificaciones_por_producto()
