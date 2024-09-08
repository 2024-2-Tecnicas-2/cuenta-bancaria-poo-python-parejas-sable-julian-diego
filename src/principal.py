from cuenta_bancaria import CuentaBancaria

def buscar_cuenta(cuentas, numero_cuenta):
    for cuenta in cuentas:
        if cuenta.get_numero_cuenta() == numero_cuenta:
            return cuenta
    return None

def main():
    cuentas = []

    # Agregar una cuenta inicial
    cuentas.append(CuentaBancaria("Juan Pérez", "123456789", 1000.0))

    continuar = True
    while continuar:
        print("\nMenú:")
        print("1. Mostrar información de todas las cuentas")
        print("2. Ingresar una cantidad en una cuenta")
        print("3. Retirar una cantidad de una cuenta")
        print("4. Calcular el interés de una cuenta")
        print("5. Cambiar el tipo de interés de una cuenta")
        print("6. Agregar una nueva cuenta")
        print("7. Salir")
        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            for cuenta in cuentas:
                print("\nInformación de la cuenta:")
                print(f"Titular: {cuenta.get_titular()}")
                print(f"Número de cuenta: {cuenta.get_numero_cuenta()}")
                print(f"Saldo: {cuenta.get_saldo()}")
                print(f"Tipo de interés: {cuenta.calcular_interes()}")

        elif opcion == 2:
            numero_cuenta_ingreso = input("Ingrese el número de cuenta para el depósito: ")
            cuenta_ingreso = buscar_cuenta(cuentas, numero_cuenta_ingreso)
            if cuenta_ingreso:
                cantidad_ingreso = float(input("Ingrese la cantidad a depositar: "))
                cuenta_ingreso.ingresar(cantidad_ingreso)
                print(f"Nuevo saldo después del ingreso: {cuenta_ingreso.get_saldo()}")
            else:
                print("Número de cuenta no encontrado.")

        elif opcion == 3:
            numero_cuenta_retiro = input("Ingrese el número de cuenta para el retiro: ")
            cuenta_retiro = buscar_cuenta(cuentas, numero_cuenta_retiro)
            if cuenta_retiro:
                cantidad_retiro = float(input("Ingrese la cantidad a retirar: "))
                cuenta_retiro.retirar(cantidad_retiro)
                print(f"Nuevo saldo después del retiro: {cuenta_retiro.get_saldo()}")
            else:
                print("Número de cuenta no encontrado.")

        elif opcion == 4:
            numero_cuenta_interes = input("Ingrese el número de cuenta para calcular el interés: ")
            cuenta_interes = buscar_cuenta(cuentas, numero_cuenta_interes)
            if cuenta_interes:
                saldo_con_interes = cuenta_interes.calcular_interes()
                print(f"Saldo con interés aplicado: {saldo_con_interes}")
            else:
                print("Número de cuenta no encontrado.")

        elif opcion == 5:
            numero_cuenta_tipo_interes = input("Ingrese el número de cuenta para cambiar el tipo de interés: ")
            cuenta_tipo_interes = buscar_cuenta(cuentas, numero_cuenta_tipo_interes)
            if cuenta_tipo_interes:
                nuevo_tipo_interes = float(input("Ingrese el nuevo tipo de interés (entre 0% y 10%): "))
                cuenta_tipo_interes.set_tipo_interes(nuevo_tipo_interes)
                print(f"Nuevo tipo de interés: {nuevo_tipo_interes}")
                print(f"Saldo con el nuevo tipo de interés aplicado: {cuenta_tipo_interes.calcular_interes()}")
            else:
                print("Número de cuenta no encontrado.")

        elif opcion == 6:
            nuevo_titular = input("Ingrese el nombre del titular de la nueva cuenta: ")
            nuevo_numero_cuenta = input("Ingrese el número de cuenta: ")
            nuevo_saldo = float(input("Ingrese el saldo inicial: "))
            cuentas.append(CuentaBancaria(nuevo_titular, nuevo_numero_cuenta, nuevo_saldo))
            print("Nueva cuenta añadida.")

        elif opcion == 7:
            continuar = False
            print("Saliendo del programa.")

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
