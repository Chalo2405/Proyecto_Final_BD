def obtener_productos_iniciales():
    productos = [
        {
            "nombre": "Laptop Gamer X15",
            "descripcion": "Laptop gamer con tarjeta gráfica dedicada y 16GB de RAM.",
            "precio": 4200.0,
            "categoria": {
                "nombre": "Electrónica",
                "subcategoria": "Laptops"
            },
            "stock": 10,
            "etiquetas": ["gamer", "laptop", "performance"],
            "calificaciones": [
                {"usuario": "u1", "puntuacion": 5},
                {"usuario": "u2", "puntuacion": 4}
            ]
        },
        {
            "nombre": "Mouse Inalámbrico Pro",
            "descripcion": "Mouse ergonómico inalámbrico con batería recargable.",
            "precio": 80.0,
            "categoria": {
                "nombre": "Electrónica",
                "subcategoria": "Accesorios"
            },
            "stock": 50,
            "etiquetas": ["mouse", "inalambrico", "oficina"],
            "calificaciones": [
                {"usuario": "u3", "puntuacion": 4},
                {"usuario": "u4", "puntuacion": 4}
            ]
        },
        {
            "nombre": "Teclado Mecánico RGB",
            "descripcion": "Teclado mecánico con iluminación RGB para gamers.",
            "precio": 260.0,
            "categoria": {
                "nombre": "Electrónica",
                "subcategoria": "Accesorios"
            },
            "stock": 20,
            "etiquetas": ["teclado", "gamer", "rgb"],
            "calificaciones": [
                {"usuario": "u5", "puntuacion": 5},
                {"usuario": "u6", "puntuacion": 5}
            ]
        },
        {
            "nombre": "Smart TV 55 pulgadas 4K",
            "descripcion": "Televisor inteligente 4K con aplicaciones de streaming.",
            "precio": 3200.0,
            "categoria": {
                "nombre": "Electrónica",
                "subcategoria": "Televisores"
            },
            "stock": 8,
            "etiquetas": ["tv", "4k", "smart"],
            "calificaciones": [
                {"usuario": "u7", "puntuacion": 4},
                {"usuario": "u8", "puntuacion": 3}
            ]
        },
        {
            "nombre": "Zapatillas Running Air",
            "descripcion": "Zapatillas ligeras para correr, con amortiguación.",
            "precio": 350.0,
            "categoria": {
                "nombre": "Ropa",
                "subcategoria": "Calzado"
            },
            "stock": 30,
            "etiquetas": ["zapatillas", "running", "deporte"],
            "calificaciones": [
                {"usuario": "u9", "puntuacion": 5},
                {"usuario": "u10", "puntuacion": 4}
            ]
        },
        {
            "nombre": "Polera Hoodie Negra",
            "descripcion": "Polera hoodie de algodón, unisex.",
            "precio": 120.0,
            "categoria": {
                "nombre": "Ropa",
                "subcategoria": "Poleras"
            },
            "stock": 40,
            "etiquetas": ["polera", "hoodie", "moda"],
            "calificaciones": [
                {"usuario": "u11", "puntuacion": 4},
                {"usuario": "u12", "puntuacion": 4}
            ]
        },
        {
            "nombre": "Silla Ergonómica Oficina",
            "descripcion": "Silla ergonómica con soporte lumbar y altura regulable.",
            "precio": 780.0,
            "categoria": {
                "nombre": "Hogar",
                "subcategoria": "Muebles"
            },
            "stock": 15,
            "etiquetas": ["silla", "oficina", "ergonomica"],
            "calificaciones": [
                {"usuario": "u13", "puntuacion": 5},
                {"usuario": "u14", "puntuacion": 3}
            ]
        },
        {
            "nombre": "Escritorio Gamer LED",
            "descripcion": "Escritorio con superficie amplia, soporte para monitor y luces LED.",
            "precio": 950.0,
            "categoria": {
                "nombre": "Hogar",
                "subcategoria": "Muebles"
            },
            "stock": 12,
            "etiquetas": ["escritorio", "gamer", "muebles"],
            "calificaciones": [
                {"usuario": "u15", "puntuacion": 4},
                {"usuario": "u16", "puntuacion": 5}
            ]
        },
        {
            "nombre": "Auriculares Inalámbricos NoiseCancel",
            "descripcion": "Audífonos inalámbricos con cancelación de ruido.",
            "precio": 600.0,
            "categoria": {
                "nombre": "Electrónica",
                "subcategoria": "Audio"
            },
            "stock": 25,
            "etiquetas": ["audifonos", "inalambricos", "musica"],
            "calificaciones": [
                {"usuario": "u17", "puntuacion": 5},
                {"usuario": "u18", "puntuacion": 4}
            ]
        },
        {
            "nombre": "Licuadora PowerMix 900W",
            "descripcion": "Licuadora de alta potencia para jugos y smoothies.",
            "precio": 280.0,
            "categoria": {
                "nombre": "Hogar",
                "subcategoria": "Electrodomésticos"
            },
            "stock": 18,
            "etiquetas": ["licuadora", "cocina", "electrodomestico"],
            "calificaciones": [
                {"usuario": "u19", "puntuacion": 4},
                {"usuario": "u20", "puntuacion": 4}
            ]
        },
    ]
    return productos


if __name__ == "__main__":
    for p in obtener_productos_iniciales():
        print(p["nombre"], "-", p["categoria"]["nombre"])
