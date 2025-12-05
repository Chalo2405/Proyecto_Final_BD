from conexion import obtener_bd


def ventas_por_categoria():
    bd = obtener_bd()
    ventas = bd.ventas

    pipeline = [
        {
            "$group": {
                "_id": "$categoria.nombre",
                "total_ventas": {"$sum": 1},
                "total_unidades": {"$sum": "$cantidad"},
                "monto_total": {"$sum": "$monto_total"}
            }
        },
        {"$sort": {"monto_total": -1}}
    ]

    print("\n--- RESUMEN DE VENTAS POR CATEGORÍA ---")
    for doc in ventas.aggregate(pipeline):
        categoria = doc["_id"] if doc["_id"] is not None else "Sin categoría"
        print(
            f"Categoría: {categoria} | "
            f"Órdenes: {doc['total_ventas']} | "
            f"Unidades vendidas: {doc['total_unidades']} | "
            f"Monto total: {doc['monto_total']}"
        )


def ventas_por_producto():
    bd = obtener_bd()
    ventas = bd.ventas

    pipeline = [
        {
            "$group": {
                "_id": "$nombre_producto",
                "total_unidades": {"$sum": "$cantidad"},
                "monto_total": {"$sum": "$monto_total"}
            }
        },
        {"$sort": {"monto_total": -1}}
    ]

    print("\n--- RESUMEN DE VENTAS POR PRODUCTO ---")
    for doc in ventas.aggregate(pipeline):
        print(
            f"Producto: {doc['_id']} | "
            f"Unidades vendidas: {doc['total_unidades']} | "
            f"Monto total: {doc['monto_total']}"
        )


def ventas_por_dia():
    bd = obtener_bd()
    ventas = bd.ventas

    pipeline = [
        {
            "$group": {
                "_id": {
                    "anio": {"$year": "$fecha"},
                    "mes": {"$month": "$fecha"},
                    "dia": {"$dayOfMonth": "$fecha"}
                },
                "monto_total": {"$sum": "$monto_total"},
                "total_ventas": {"$sum": 1}
            }
        },
        {"$sort": {"_id.anio": 1, "_id.mes": 1, "_id.dia": 1}}
    ]

    print("\n--- RESUMEN DE VENTAS POR DÍA ---")
    for doc in ventas.aggregate(pipeline):
        fecha = doc["_id"]
        print(
            f"Fecha: {fecha['dia']:02d}/{fecha['mes']:02d}/{fecha['anio']} | "
            f"Órdenes: {doc['total_ventas']} | "
            f"Monto total: {doc['monto_total']}"
        )


if __name__ == "__main__":
    ventas_por_categoria()
    ventas_por_producto()
    ventas_por_dia()
