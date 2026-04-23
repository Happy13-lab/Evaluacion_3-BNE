import pymongo as pm
import sys
import asyncio
import bcrypt
from Config.db_config import MongoConfing

mongo = MongoConfing(
    host="mongodb://localhost:27017",
    database="AcmeDB"
)



def main():
    db = mongo.createCollection("Prueba01")
    prueba01_coleccion = db["Prueba01"]

    # usuario = {
    #     "nombre": "Juan",
    #     "apellido": "Perez",
    #     "edad": 30
    # }

    # resultado = prueba01_coleccion.insert_one(usuario)

    # print(resultado.inserted_id)

    # resultado = prueba01_coleccion.find_one()
    # print(resultado)
   
    # for x in resultado:
    #     print(x)

    resultado = prueba01_coleccion.update_one({"nombre": "Juan"}, {"$set": { "Correo": "juan@gmail.com" }})

    print(resultado.modified_count)

main()