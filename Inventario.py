class Inventario:

    def __init__(self):
        self.__productos = []

    # CREAR
    def agregar_producto(self, producto):
        self.__productos.append(producto)

    # LEER
    def mostrar_productos(self):
        for producto in self.__productos:
            print(
                "Nombre:", producto.get_nombre(),
                "| Categoría:", producto.get_categoria(),
                "| Precio:", producto.get_precio(),
                "| Cantidad:", producto.get_cantidad()
            )

    # ACTUALIZAR
    def editar_producto(self, nombre, nuevo_precio, nueva_cantidad):

        for producto in self.__productos:

            if producto.get_nombre() == nombre:
                producto.set_precio(nuevo_precio)
                producto.set_cantidad(nueva_cantidad)

                print("Producto actualizado.")
                return

        print("Producto no encontrado.")

    # ELIMINAR
    def eliminar_producto(self, nombre):

        for producto in self.__productos:

            if producto.get_nombre() == nombre:
                self.__productos.remove(producto)

                print("Producto eliminado.")
                return

        print("Producto no encontrado.")