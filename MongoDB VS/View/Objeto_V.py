class View:
    @staticmethod
    def mostrar_menu_admin():
        print("\n--- Menú Administrador ---")
        print("1. Actualizar stock/precios")
        print("2. Ver historial de ventas")
        print("3. Reportes")
        print("4. Salir")

    @staticmethod
    def mostrar_menu_vendedor():
        print("\n--- Menú Vendedor ---")
        print("1. Registrar venta")
        print("2. Salir")

    @staticmethod
    def mostrar_mensaje(msg):
        print(msg)
