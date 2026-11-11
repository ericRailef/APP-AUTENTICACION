from autenticacion import Autenticacion



def mostrar_menu():

    print("\n ==========================")
    print("   SISTEMA DE AUTENTICACION  ")
    print("=============================")
    print("1. Registrar Usuario")
    print("2. Iniciar Sesion")
    print("3 Mostrar Datos del usuario")
    print("4. Cambiar Constraseña")
    print("5 Cerrar Sesion")
    print("6 Salir")


def main():


    sistema = Autenticacion()

    usuario_actual = None

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion:  ").strip()


        if opcion == "1":
            print("--- REGISTRO ---")
            nombre = input("Nombre: ").strip()
            correo = input("Correo: ").strip()
            password = input("Contraseña (minimo de 8 caracteres)")

            sistema.registrar_usuario(nombre, correo, password)

        elif opcion=="2":
            
            if usuario_actual is not None:
                print("ya existe una sesion activa")
                continue
            print("---Iniciar Sesion---")
            correo = input("Correo: ").strip()
            password = input("Contraseña:")

            usuario_actual = sistema.iniciar_sesion(correo, password)

        elif opcion == "3":
            if usuario_actual is not None:
                usuario_actual.mostrar_datos()
            else:
                print("Debes ingresar sesion primero.")

        elif opcion == "4":
            if usuario_actual is None:
                print("Debes iniciar sesion primero")
                continue

            print("--Cambiar Contraseña---")
            actual = input("Contraseña actual:  ")
            nueva = input ("Nueva contraseña (minimo 8 caracteres): ")

            sistema.cambiar_password(usuario_actual, actual, nueva)

        elif opcion == "5":
            if usuario_actual is not None:
                usuario_actual = None
                print("Sesion cerrada correctamente")
            else:
                print("No existe una sesion activa")

        elif opcion == "6":
            print("Saliendo del sistema")
            break

        else:
            print("Opcion inválida. Intente nuevamente")









if __name__ == "__main__":
    main()