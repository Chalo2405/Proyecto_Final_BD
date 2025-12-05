from pymongo import MongoClient

URI_MONGO = "mongodb://localhost:27017/"
NOMBRE_BD = "catalogo_nosql"


def obtener_bd():
    cliente = MongoClient(URI_MONGO)
    bd = cliente[NOMBRE_BD]
    return bd


if __name__ == "__main__":
    bd = obtener_bd()
    print("Conectado a la base de datos:", bd.name)
