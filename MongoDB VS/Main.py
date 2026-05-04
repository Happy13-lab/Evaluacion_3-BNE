from Config.db_config import db_config
from Model.Persona_M import usuarioModel
from Model.Objeto_M import stockModel, ventaModel, registroVentaModel
from Controller.Persona_C import UsuarioController
from Controller.Objeto_C import  stockController, ventaController, reporteController
import pymongo as pm


mongo = db_config()

def main():
    db = mongo
    user_model = usuarioModel(db)
    user_model.crear_usuario() 

    usuario_ctrl = UsuarioController(user_model)

    # Bucle principal
    while True:
        print("\n=== SISTEMA DE VENTAS DE SALMÓN ===")
        if not usuario_ctrl.iniciar_sesion():
            opcion = input("¿Desea intentar nuevamente? (s/n): ").lower()
            if opcion != "s":
                print("Saliendo del sistema...")
                break
        else:
            # Cuando el usuario inicia sesión, se queda en su menú
            # Los menús ya están definidos en UsuarioController
            pass

if __name__ == "__main__":
    main()


