# NÚCLEO DE LA APLICACIÓN

# Siempre se importan los módulos al inicio del código.
import almacenamiento
import operaciones

print("\n=============== GESTOR FINANCIERO ================\n")

# Sincronización inicial: Cargamos el disco duro a la memoria RAM
operaciones.transaction_history = almacenamiento.load_data()

while True:
    print(
        "---------------------- Menú ----------------------\n",
        "1. Nueva transacción.\n",
        "2. Balance general.\n",
        "3. Salir."
    )

    option = input("\nDigite el número de la opción deseada: ").strip()

    match option:
        case "1":
            try:
                # El try captura el error si el usuario tipea letras en lugar de números.
                print("\n--- Transacción ---\n")
                amount = float(input("Ingrese el monto $0.0: "))
                description = input("Describa la transacción: ").strip()
                transaction_type = input("Mencione el tipo de operación (Ingreso o Egreso): ").strip().capitalize()
                
                # Si todo está bien, guardamos la transacción.
                operaciones.add_transaction(amount, description, transaction_type)
                print("\n¡Transacción registrada con éxito!\n")

            except ValueError:
                print(f"\nError detectado: Ingrese una opción válida.\n")

        case "2":
            print("\n--- Balance General ---\n")
            # Envolvemos el cálculo en un print para verlo en consola.
            current_balance = operaciones.get_balance()
            print(f"Su saldo actual es de: \t${current_balance}\n")
            
        case "3":
            print("\n--- Guardando Información ---\n")
            # Sincronización final: Guardamos la RAM en el disco duro antes de salir.
            # Esto es posible por save_data() nos devuelve una respuesta booleana.
            success = almacenamiento.save_data(operaciones.transaction_history)
            
            if success:
                print("Datos guardados exitosamente ¡Hasta pronto!")
                break
            else:
                print("Error detectado: No se pudo guardar el archivo.\n")
                
        case _:
            print("\n¡Lo sentimos! Opción no reconocida, vuelve a intentarlo por favor.\n")

print("\n=============== CERRANDO APLICACIÓN ===============")