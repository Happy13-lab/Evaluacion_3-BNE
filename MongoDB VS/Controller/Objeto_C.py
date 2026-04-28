from Config.db_config import db_config
from Model.Objeto_M import stockModel, ventaModel, registroVentaModel
from View.Objeto_V import View
import datetime
        
class stockController():
    def __init__(self):
        self.db = db_config()
        self.coleccion = self.db.db["stock"]
    
    def insertar_stock(self):

        if self.coleccion.count_documents({}) == 0:
            productos_iniciales = [{
                 "tipo": "Atlantico", "coste": 8000, "valor_venta": 12000, "cantidad": 10},
                 {"tipo": "Nordico", "coste": 10000, "valor_venta": 15000, "cantidad": 10},
                 {"tipo": "Pacifico", "coste": 5000, "valor_venta": 7000, "cantidad": 10}
            ]
            self.coleccion.insert_many(productos_iniciales)
            print("Productos iniciales insertados en la colección.")
    
    def obtener_stock(self, tipo):
        return self.coleccion.find_one({"tipo": tipo})
    
    def actualizar_stock_precio(self, tipo, cantidad = None, precio = None):
        actualizar = {}
        if cantidad is not None:
            actualizar["cantidad"] = cantidad
        if precio is not None:
            actualizar["valor_venta"] = precio
        
        if actualizar:
            self.coleccion.update_one({"tipo": tipo}, {"$set": actualizar})
            return True
        return False

class ventaController():
    def __init__(self):
        self.db = db_config()
        self.coleccion = self.db.db["ventas"]
    
    def registrar_venta(self):
        pedido = []
        for salmon in self.db.db["stock"].find():
            cantidad = int(input(f"Ingrese la cantidad de {salmon['tipo']} a vender (stock disponible: {salmon['cantidad']}): "))
            if cantidad > 0 and cantidad <= salmon["cantidad"]:
                pedido.append({"tipo": salmon["tipo"], "cantidad": cantidad, "precio": salmon["valor_venta"]})
                self.db.db["stock"].update_one({"tipo": salmon["tipo"]}, {"$inc": {"cantidad": -cantidad}})
            else:
                View.mostrar_mensaje(f"Cantidad inválida para {salmon['tipo']}. Se omitirá este producto.")
        if pedido:
            venta = ventaModel(pedido=str(pedido))
            self.coleccion.insert_one({"pedido": venta.pedido, "fecha": datetime.datetime.now()})
            View.mostrar_mensaje("Venta registrada exitosamente.")
            return True
        return False

class reporteController():
    def __init__(self):
        self.db = db_config()
        self.stock= self.db.db["stock"]
        self.ventas= self.db.db["ventas"]
    
    def reporte_ventas(self):
        ventas = self.ventas.find()
        for venta in ventas:
            View.mostrar_mensaje(f"Pedido: {venta['pedido']}, Fecha: {venta['fecha']}")

    def reporte_mas_vendido(self):
        View.mostrar_mensaje("Reporte de producto más vendido:")
        ultimas_ventas = self.ventas.find().sort("fecha", -1).limit(5)
        conteo = {}
        for venta in ultimas_ventas:
            for p in venta["pedido"]:
                conteo[p["tipo"]] = conteo.get(p["tipo"], 0) + p["cantidad"]
        if conteo:
            mas_vendido = max(conteo, key=conteo.get)
            View.mostrar_mensaje(f"Producto más vendido: {mas_vendido} con {conteo[mas_vendido]} unidades vendidas.")
        else:
            View.mostrar_mensaje("No se han registrado ventas aún.")