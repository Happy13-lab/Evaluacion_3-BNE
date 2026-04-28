import datetime

class stockModel():
    def __init__(self,tipo = str, coste = int, valor_venta = int, cantidad = int):
        self.tipo = tipo
        self.coste = coste
        self.valor_venta = valor_venta
        self.cantidad = cantidad

class ventaModel():
    def __init__(self, pedido = str):
        self.pedido = pedido

class registroVentaModel():
    def __init__(self, pedido = str, fecha = datetime):
        self.pedido = pedido
        self.fecha = fecha