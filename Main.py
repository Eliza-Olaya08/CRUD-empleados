from Producto import Producto
from Empleado import Empleado
from Inventario import Inventario
from Nomina import Nomina


inventario = Inventario()
nomina = Nomina()

# MENÚ PRINCIPAL

def menu_principal():

    while True:

        print("\n===== SISTEMA DE LA EMPRESA =====")
        print("1. Gestionar inventario")
        print("2. Gestionar nómina")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_inventario()

        elif opcion == "2":
            menu_nomina()

        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")

# MENÚ INVENTARIO

def menu_inventario():

    while True:

        print("\n===== MENÚ INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Editar producto")
        print("4. Eliminar producto")
        print("5. Regresar")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            nombre = input("Nombre del producto: ")
            categoria = input("Categoría: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))

            producto = Producto(
                nombre,
                categoria,
                precio,
                cantidad
            )

            inventario.agregar_producto(producto)

            print("Producto agregado.")

        elif opcion == "2":

            print("\n===== PRODUCTOS =====")
            inventario.mostrar_productos()

        elif opcion == "3":

            nombre = input("Nombre del producto a editar: ")
            precio = float(input("Nuevo precio: "))
            cantidad = int(input("Nueva cantidad: "))

            inventario.editar_producto(
                nombre,
                precio,
                cantidad
            )

        elif opcion == "4":

            nombre = input("Nombre del producto a eliminar: ")

            inventario.eliminar_producto(nombre)

        elif opcion == "5":

            break

        else:

            print("Opción no válida.")

# MENÚ NÓMINA

def menu_nomina():

    while True:

        print("\n===== MENÚ NÓMINA =====")
        print("1. Agregar empleado")
        print("2. Mostrar empleados")
        print("3. Editar empleado")
        print("4. Eliminar empleado")
        print("5. Regresar")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            nombre = input("Nombre del empleado: ")
            cargo = input("Cargo: ")
            sueldo = float(input("Sueldo: "))
            telefono = input("Teléfono: ")

            empleado = Empleado(
                nombre,
                cargo,
                sueldo,
                telefono
            )

            nomina.agregar_empleado(empleado)

            print("Empleado agregado.")

        elif opcion == "2":

            print("\n===== EMPLEADOS =====")
            nomina.mostrar_empleados()

        elif opcion == "3":

            nombre = input("Nombre del empleado a editar: ")
            cargo = input("Nuevo cargo: ")
            sueldo = float(input("Nuevo sueldo: "))

            nomina.editar_empleado(
                nombre,
                cargo,
                sueldo
            )

        elif opcion == "4":

            nombre = input("Nombre del empleado a eliminar: ")

            nomina.eliminar_empleado(nombre)

        elif opcion == "5":

            break

        else:

            print("Opción no válida.")

# INICIAR PROGRAMA

menu_principal()