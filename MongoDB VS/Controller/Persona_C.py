from Config.db_config import db_config
from Controller.Objeto_C import reporteController, stockController, ventaController
from Model.Persona_M import usuarioModel
from View.Objeto_V import View

class UsuarioController:
    def __init__(self, usuarioModel = usuarioModel, db_config = db_config):
        self.db_config = db_config
        self.usuarioModel = usuarioModel
        self.usuario_actual = None
        self.stockController = stockController()
        self.ventaController = ventaController()
        self.reporteController = reporteController()

    def iniciar_sesion(self):
        
        print("\n--- INICIO DE SESIÓN ---")
        nombre = input("Nombre de usuario: ").strip()
        contraseña = input("Contraseña: ").strip()

        usuario = self.usuarioModel.verificar_usuario(nombre, contraseña)

        if usuario:
            self.usuario_actual = usuario
            print(f"\n Bienvenido: {usuario['nombre']}.")
            
            if usuario['rol'] == "administrador":
                self.menu_administrador()
            elif usuario['rol'] == "vendedor":
                self.menu_vendedor()
            return True
        else:
            print("\n[!] Error: Credenciales incorrectas o el usuario no existe.")
            return False

    def menu_administrador(self):
      
        while True:
            View.mostrar_menu_admin()
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                tipo = input("Ingrese tipo de salmón a actualizar: (Atlantico, Nordico, Pacifico): ")
                try:
                    cantidad = int(input("Cantidad a añadir/restar: ") or 0)
                    precio = int(input("Nuevo precio de venta: ") or 0)
                    if self.stockController.actualizar_stock_precio(tipo, cantidad, precio):
                        print("Stock/precio actualizado correctamente.")
                except ValueError:
                    print("Error: ingrese valores numéricos.")
                    
            elif opcion == "2":
                self.reporteController.reporte_ventas()
            elif opcion == "3":
                print("\n--- Reportes ---")
                print("1. Coste--Ganancia")
                print("2. Salmon más vendido")
                subopcion = input("Seleccione reporte: ")
                if subopcion == "1":
                    self.reporteController.reporte_coste_ganancia()
                elif subopcion == "2":
                    self.reporteController.reporte_mas_vendido()
            elif opcion == "4":
                self.usuario_actual = None
                print("Sesión cerrada.")
                break
            else:
                print("Opción no válida.")
                

    def menu_vendedor(self):
    
        while True:
            View.mostrar_menu_vendedor()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                    self.ventaController.registrar_venta()
            elif opcion == "2":
                self.usuario_actual = None
                print("Sesión cerrada.")
                break
            else:
                    print("Opción no válida.")