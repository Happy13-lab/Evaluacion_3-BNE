from Config.db_config import db_config
from Model.Persona_M import usuarioModel
from Controller.Persona_C import UsuarioController
from Controller.Objeto_C import stockController

def main():
    try:
        db = db_config()
    except Exception as e:
        print(f"Error al conectar a la base de datos. {e}")
        return
    usuario_model = usuarioModel(db)
    usuario_model.crear_usuario()
    usuario_contro = UsuarioController(usuario_model)
    stockController().insertar_stock()

    while True:
        print("\n--- ACME ---")
        print("1. Iniciar sesión")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            if usuario_contro.iniciar_sesion():
                continue
        elif opcion == "2":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()


