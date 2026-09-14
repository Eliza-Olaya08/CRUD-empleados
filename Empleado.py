class Empleado:

    def __init__(self, nombre, cargo, sueldo, telefono):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__sueldo = sueldo
        self.__telefono = telefono

    # GET
    def get_nombre(self):
        return self.__nombre

    def get_cargo(self):
        return self.__cargo

    def get_sueldo(self):
        return self.__sueldo

    def get_telefono(self):
        return self.__telefono

    # SET
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def set_sueldo(self, sueldo):
        self.__sueldo = sueldo

    def set_telefono(self, telefono):
        self.__telefono = telefono