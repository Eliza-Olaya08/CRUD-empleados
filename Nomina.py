class Nomina:

    def __init__(self):
        self.__empleados = []

    # CREAR
    def agregar_empleado(self, empleado):
        self.__empleados.append(empleado)

    # LEER
    def mostrar_empleados(self):

        for empleado in self.__empleados:
            print(
                "Nombre:", empleado.get_nombre(),
                "| Cargo:", empleado.get_cargo(),
                "| Sueldo:", empleado.get_sueldo(),
                "| Teléfono:", empleado.get_telefono()
            )

    # ACTUALIZAR
    def editar_empleado(self, nombre, nuevo_cargo, nuevo_sueldo):

        for empleado in self.__empleados:

            if empleado.get_nombre() == nombre:

                empleado.set_cargo(nuevo_cargo)
                empleado.set_sueldo(nuevo_sueldo)

                print("Empleado actualizado.")
                return

        print("Empleado no encontrado.")

    # ELIMINAR
    def eliminar_empleado(self, nombre):

        for empleado in self.__empleados:

            if empleado.get_nombre() == nombre:

                self.__empleados.remove(empleado)

                print("Empleado eliminado.")
                return

        print("Empleado no encontrado.")