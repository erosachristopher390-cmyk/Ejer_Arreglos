import random

meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
]

departamentos = [
    "Ropa",
    "Deportes",
    "Jugueteria"
]

ventas = [[0 for _ in range(len(departamentos))] for _ in range(12)]


def generar_ventas():
    for i in range(12):
        for j in range(len(departamentos)):
            ventas[i][j] = random.randint(1000, 50000)


def agregar_departamento():
    nombre = input("\nIngresa el nombre del nuevo departamento: ")

    if nombre.strip() == "":
        print("\nEl nombre no puede estar vacio.")
        return

    if nombre in departamentos:
        print("\nEse departamento ya existe.")
        return

    departamentos.append(nombre)

    for i in range(12):
        ventas[i].append(random.randint(1000, 50000))

    print(f"\nDepartamento '{nombre}' agregado correctamente.")


def insertar_venta(mes, departamento, cantidad):
    ventas[mes][departamento] = cantidad

    print("\nVenta insertada correctamente.")
    print("Mes:", meses[mes])
    print("Departamento:", departamentos[departamento])
    print(f"Venta: ${cantidad:,.2f}")


def buscar_venta(mes, departamento):
    venta = ventas[mes][departamento]

    print("\n========== VENTA ENCONTRADA ==========")
    print("Mes:", meses[mes])
    print("Departamento:", departamentos[departamento])
    print(f"Venta: ${venta:,.2f}")


def eliminar_venta(mes, departamento):
    ventas[mes][departamento] = 0

    print("\nVenta eliminada correctamente.")
    print("Mes:", meses[mes])
    print("Departamento:", departamentos[departamento])


def mostrar_ventas():
    print("\n" + "=" * (15 + len(departamentos) * 16))
    print("VENTAS MENSUALES")
    print("=" * (15 + len(departamentos) * 16))

    print(f"{'Mes':<15}", end="")

    for departamento in departamentos:
        print(f"{departamento:<16}", end="")

    print()

    print("-" * (15 + len(departamentos) * 16))

    for i in range(12):
        print(f"{meses[i]:<15}", end="")

        for j in range(len(departamentos)):
            print(f"${ventas[i][j]:<15,.2f}", end="")

        print()

    print("=" * (15 + len(departamentos) * 16))


def mostrar_meses():
    print("\n========== MESES ==========")

    for i in range(len(meses)):
        print(f"{i + 1}. {meses[i]}")


def mostrar_departamentos():
    print("\n========== DEPARTAMENTOS ==========")

    for i in range(len(departamentos)):
        print(f"{i + 1}. {departamentos[i]}")


generar_ventas()

while True:

    print("\n")
    print("==========================================")
    print("       SISTEMA DE VENTAS MENSUALES")
    print("==========================================")
    print("1. Insertar venta")
    print("2. Buscar venta")
    print("3. Eliminar venta")
    print("4. Mostrar todas las ventas")
    print("5. Agregar departamento")
    print("6. Regenerar ventas aleatorias")
    print("7. Salir")
    print("==========================================")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":

        mostrar_meses()

        try:
            mes = int(input("Selecciona el mes: "))

            mostrar_departamentos()

            departamento = int(
                input("Selecciona el departamento: ")
            )

            cantidad = float(
                input("Ingresa la cantidad de venta: $")
            )

            if (
                1 <= mes <= 12
                and 1 <= departamento <= len(departamentos)
                and cantidad >= 0
            ):
                insertar_venta(
                    mes - 1,
                    departamento - 1,
                    cantidad
                )
            else:
                print("\nDatos invalidos.")

        except ValueError:
            print("\nDebes ingresar valores numericos.")

    elif opcion == "2":

        mostrar_meses()

        try:
            mes = int(input("Selecciona el mes: "))

            mostrar_departamentos()

            departamento = int(
                input("Selecciona el departamento: ")
            )

            if (
                1 <= mes <= 12
                and 1 <= departamento <= len(departamentos)
            ):
                buscar_venta(
                    mes - 1,
                    departamento - 1
                )
            else:
                print("\nDatos invalidos.")

        except ValueError:
            print("\nDebes ingresar valores numericos.")

    elif opcion == "3":

        mostrar_meses()

        try:
            mes = int(input("Selecciona el mes: "))

            mostrar_departamentos()

            departamento = int(
                input("Selecciona el departamento: ")
            )

            if (
                1 <= mes <= 12
                and 1 <= departamento <= len(departamentos)
            ):
                eliminar_venta(
                    mes - 1,
                    departamento - 1
                )
            else:
                print("\nDatos invalidos.")

        except ValueError:
            print("\nDebes ingresar valores numericos.")

    elif opcion == "4":

        mostrar_ventas()

    elif opcion == "5":

        agregar_departamento()

    elif opcion == "6":

        generar_ventas()
        print("\nSe generaron nuevas ventas aleatorias.")

    elif opcion == "7":

        print("\nPrograma finalizado.")
        break

    else:

        print("\nOpcion no valida.")
