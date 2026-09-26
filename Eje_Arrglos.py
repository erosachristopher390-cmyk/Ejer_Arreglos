
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


ventas = [[0 for _ in range(3)] for _ in range(12)]


def generar_ventas():

    for i in range(12):

        for j in range(3):

           
            ventas[i][j] = random.randint(1000, 50000)



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

    print("\n==============================================================")
    print("                    VENTAS MENSUALES")
    print("==============================================================")

    print(
        f"{'Mes':<15}"
        f"{'Ropa':<15}"
        f"{'Deportes':<15}"
        f"{'Jugueteria':<15}"
    )

    print("--------------------------------------------------------------")

    for i in range(len(ventas)):

        print(
            f"{meses[i]:<15}"
            f"${ventas[i][0]:<14,.2f}"
            f"${ventas[i][1]:<14,.2f}"
            f"${ventas[i][2]:<14,.2f}"
        )

    print("==============================================================")



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
    print("5. Regenerar ventas aleatorias")
    print("6. Salir")
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
                and 1 <= departamento <= 3
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
                and 1 <= departamento <= 3
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
                and 1 <= departamento <= 3
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

        generar_ventas()

        print("\nSe generaron nuevas ventas aleatorias.")


    elif opcion == "6":

        print("\nPrograma finalizado.")
        break

    else:

        print("\nOpcion no valida.")
