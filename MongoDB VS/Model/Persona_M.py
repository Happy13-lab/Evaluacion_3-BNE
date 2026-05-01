from Config.db_config import MongoConfing
import hashlib
 
class usuarioModel():
    def __init__(self, db_config):
        self.coleccion = db_config.db["usuarios"]
    
    def hash_contraseña(self, contraseña):
        return hashlib.sha256(contraseña.encode()).hexdigest()
    
    def crear_usuario(self):
        if self.coleccion.count_documents({}) == 0:
            usuarios_iniciales = [
                {"nombre": "admin", "contraseña": self.hash_contraseña("admin123"), "rol": "administrador"},
                {"nombre": "vendedor", "contraseña": self.hash_contraseña("vendedor123"), "rol": "vendedor"}
            ]
            self.coleccion.insert_many(usuarios_iniciales)
            print("Usuarios iniciales insertados en la colección.")
    
    def verificar_usuario(self, nombre, contraseña):

        return self.coleccion.find_one({"nombre": nombre, "contraseña": self.hash_contraseña(contraseña)})