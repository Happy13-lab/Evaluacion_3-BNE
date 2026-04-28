from Config.db_config import db_config

class salmonModel():
    def __init__(self):
        self.db = db_config()
    
    def insertar_salmon(self):

        if self.coleccion.count_documents({}) == 0:
            productos_iniciales = [{
                 "tipo": "Atlantico", "coste": 8000, "valor_venta": 12000, "cantidad": 10},
                 {"tipo": "Nordico", "coste": 10000, "valor_venta": 15000, "cantidad": 10},
                 {"tipo": "Pacifico", "coste": 5000, "valor_venta": 7000, "cantidad": 10}
            ]
            self.coleccion.insert_many(productos_iniciales)
            print("Productos iniciales insertados en la colección.")
    
    def obtener_salmon(self, tipo):
        return self.coleccion.find_one({"tipo": tipo})
    
    def actualizar_stock_precio(self, tipo, cantidad, precio):
        actualizar = {}
        if cantidad is not None:
            actualizar["cantidad"] = cantidad
        if precio is not None:
            actualizar["valor_venta"] = precio
        
        if actualizar:
            self.coleccion.update_one({"tipo": tipo}, {"$set": actualizar})
            return True
        return False
