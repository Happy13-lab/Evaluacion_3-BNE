from Config.db_config import db_config
from Model.Objeto_M import stockModel, ventaModel, registroVentaModel
from Model.Persona_M import usuarioModel
import datetime
import View
        
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
    
    def actualizar_stock_precio(self, tipo, cantidad = 0, precio_coste = 0, precio_venta = 0):
        salmon = {"tipo": tipo}
        if cantidad != 0:
            self.coleccion.update_one(salmon, {"$inc": {"cantidad": cantidad}})
        act_precio = {}
        if precio_coste is not None and precio_coste > 0:
            act_precio["coste"] = precio_coste
        if precio_venta is not None and precio_venta > 0:
            act_precio["valor_venta"] = precio_venta
        if act_precio:
            self.coleccion.update_one(salmon, {"$set": act_precio})
            
        return cantidad != 0

class ventaController():
    def __init__(self):
        self.db = db_config()
        self.coleccion = self.db.db["ventas"]
    
    def registrar_venta(self):
        pedido = []
        for salmon in self.db.db["stock"].find():
            while True:
                try:
                    entrada = input(f"Ingrese la cantidad de {salmon['tipo']} a vender (stock disponible: {salmon['cantidad']} : ")
                    cantidad = int(entrada)
                    if cantidad < 0:
                        print("Cantidad no puede ser negativa.")
                        continue
                    if cantidad > 0 and cantidad <= salmon["cantidad"]:
                        pedido.append({"tipo": salmon["tipo"], "cantidad": cantidad, "precio": salmon["valor_venta"]})
                        self.db.db["stock"].update_one({"tipo": salmon["tipo"]}, {"$inc": {"cantidad": -cantidad}})
                    elif cantidad == 0:
                        break
                    else:
                       print(f"Cantidad excede el stock disponible para {salmon['tipo']}.")
                except ValueError:
                    print("Solo se permiten Numeros enteros.")
                    
        if pedido:
            venta = ventaModel(pedido=pedido)
            self.coleccion.insert_one({"pedido": venta.pedido, "fecha": venta.fecha})
            print("Venta registrada exitosamente.")
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
            print(f"Pedido: {venta['pedido']}, Fecha: {venta['fecha']}")
            for p in venta["pedido"]:
                print(f" - {p['tipo']}: {p['cantidad']} kilos a ${p['precio']}")

    def reporte_mas_vendido(self):
        print("Reporte de producto más vendido:")
        ultimas_ventas = self.ventas.find().sort("fecha", -1).limit(5)
        conteo = {}
        for venta in ultimas_ventas:
            for p in venta["pedido"]:
                conteo[p["tipo"]] = conteo.get(p["tipo"], 0) + p["cantidad"]
        if conteo:
            mas_vendido = max(conteo, key=conteo.get)
            print(f"Producto más vendido: {mas_vendido} con {conteo[mas_vendido]} unidades vendidas.")
        else:
            print("No se han registrado ventas aún.")

    def reporte_coste_ganancia(self):
        print("\n--- Reporte Coste/Ganancia ---")
        for salmon in self.stock.find():
            ganancia_unitaria = salmon["valor_venta"] - salmon["coste"]
            print(f"{salmon['tipo']}: coste {salmon['coste']} | venta {salmon['valor_venta']} | ganancia por kilo {ganancia_unitaria}")
