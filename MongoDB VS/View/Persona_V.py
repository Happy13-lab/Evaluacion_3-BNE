from Controller import stockController, ventaController, reporteController
from View.Objeto_V import View

class UsuarioController:
    def __init__(self, usuarioModel):
        self.usuarioModel = usuarioModel
        self.usuario_actual = None
        self.stockCtrl = stockController()
        self.ventaCtrl = ventaController()
        self.reporteCtrl = reporteController()

    def menu_administrador(self):
        while True:
            View.mostrar_menu_admin()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                tipo = input("Ingrese tipo de salmón a actualizar: ")
                cantidad = int(input("Nueva cantidad (Enter para omitir): ") or 0)
                precio = int(input("Nuevo precio de venta (Enter para omitir): ") or 0)
                actualizado = self.stockCtrl.actualizar_stock_precio(tipo, cantidad if cantidad > 0 else None, precio if precio > 0 else None)
                if actualizado:
                    View.mostrar_mensaje("Stock/precio actualizado correctamente.")
                else:
                    View.mostrar_mensaje("No se realizó ninguna actualización.")

            elif opcion == "2":
                self.reporteCtrl.reporte_ventas()

            elif opcion == "3":
                print("\n--- Reportes ---")
                print("1. Coste-Ganancia")
                print("2. Salmón más vendido")
                subopcion = input("Seleccione reporte: ")
                if subopcion == "1":
                    self.reporteCtrl.reporte_coste_ganancia()
                elif subopcion == "2":
                    self.reporteCtrl.reporte_mas_vendido()

            elif opcion == "4":
                self.usuario_actual = None
                View.mostrar_mensaje("Sesión cerrada.")
                break

            else:
                View.mostrar_mensaje("Opción no válida.")
