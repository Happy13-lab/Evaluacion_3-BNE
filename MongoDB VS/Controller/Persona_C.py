from Config.db_config import MongoConfing
from Model.Persona_M import usuarioModel 

class UsuarioController:
    def __init__(self, usuarioModel):
        
        self.usuarioModel = usuarioModel
        self.usuario_actual = None 

    def iniciar_sesion(self):
        
        print("\n--- INICIO DE SESIÓN ---")
        nombre = input("Nombre de usuario: ").strip()
        contraseña = input("Contraseña: ").strip()

        usuario = self.usuarioModel.verificar_usuario(nombre, contraseña)

        if usuario:
            self.usuario_actual = usuario
            print(f"\nAcceso concedido. Bienvenido, {usuario['nombre']}.")
            
            # Redirección según el rol
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
            print("\n--- MENÚ ADMINISTRADOR ---")
            print("1. Actualizar salmones (Stock y Precios)")
            print("2. Ver historial de ventas")
            print("3. Ver reporte: Coste-Ganancia")
            print("4. Ver reporte: Salmón más vendido")
            print("5. Cerrar Sesión")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print("Funcionalidad de actualización en desarrollo...")
            elif opcion == "5":
                self.usuario_actual = None
                print("Sesión cerrada.")
                break
            else:
                print("Opción no válida.")

    def menu_vendedor(self):
    
        while True:
            print("\n--- MENÚ VENDEDOR ---")
            print("1. Realizar pedido de salmón")
            print("2. Cerrar Sesión")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print("Iniciando proceso de venta...")
            elif opcion == "2":
                self.usuario_actual = None
                print("Sesión cerrada.")
                break
            else:
                print("Opción no válida.")