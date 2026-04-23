import pymongo as pm
from pymongo import MongoClient
from pymongo.errors import PyMongoError

class MongoConfing:

    def __init__(self, host: str,database:str):
        self.host = host
        self.database = database
        self.client = None
        self.db = None

    def conectar_db(self):
        try:
            self.client = MongoClient({self.host})
            self.db = self.client[self.database]
            print("Conexión exitosa a la base de datos.")
        except PyMongoError as e:
            print(f"Error al conectar a la base de datos: {e}")
            
        
    def desconectar(self):
            if self.client:
                self.client.close()
                print("Conexión a MongoDB cerrada correctamente.")
                
    def obtener_coleccion(self, colecciones: str):
        if not self.db:
            self.conectar_db()
        return self.db[colecciones]

