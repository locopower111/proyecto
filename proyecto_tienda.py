class Producto:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

class item_carrito:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

class tienda_en_linea:
    def __init__(self):
        self.productos = []
        self.carrito = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_catalogo(self):
        print("Catalogo:")
        for i, producto in enumerate(self.productos, 1):
            print(f"{i}. {producto.nombre} - Precio: ${producto.precio}")

    def mostrar_detalle_producto(self, indice_producto):
        if 0 < indice_producto <= len(self.productos):
            producto = self.productos[indice_producto - 1]
            print(f"Detalle del Producto:")
            print(f"Nombre: {producto.nombre}")
            print(f"Descripción: {producto.descripcion}")
            print(f"Precio: ${producto.precio}")
        else:
            print("Producto no encontrado.")

    def agregar_al_carrito(self, indice_producto, cantidad):
        if 0 < indice_producto <= len(self.productos):
            producto = self.productos[indice_producto - 1]
            item = item_carrito(producto, cantidad)
            self.carrito.append(item)
            print(f"{cantidad} {producto.nombre}(s) agregado(s) al carrito.")
        else:
            print("Producto no encontrado.")

    def mostrar_carrito(self):
        if self.carrito:
            total = 0
            print("Carrito de Compras:")
            for i, item in enumerate(self.carrito, 1):
                subtotal = item.producto.precio * item.cantidad
                print(f"{i}. {item.producto.nombre} - Cantidad: {item.cantidad} - Subtotal: ${subtotal}")
                total += subtotal
            print(f"Total a pagar: ${total}")
        else:
            print("El carrito de compras está vacío.")

    def realizar_pedido(self, informacion_envio, informacion_pago):
        if self.carrito:
            print("Pedido realizado con éxito!")
            print("Información de envío:")
            for key, value in informacion_envio.items():
                print(f"{key}: {value}")
            print("\nInformación de pago:")
            for key, value in informacion_pago.items():
                print(f"{key}: {value}")
            print("\nProductos del pedido:")
            for item in self.carrito:
                print(f"{item.cantidad} {item.producto.nombre} - ${item.producto.precio} c/u")
            total = sum(item.producto.precio * item.cantidad for item in self.carrito)
            print(f"Total a pagar: ${total}")
            self.carrito.clear()
        else:
            print("No hay productos en el carrito para realizar un pedido.")


tienda = tienda_en_linea()


tienda.agregar_producto(Producto("Xbox", 200, "Consola gamer."))
tienda.agregar_producto(Producto("Play Station 4", 200, "Consola gamer."))
tienda.agregar_producto(Producto("Pc gamer", 150, "Computador que sirve para cuaqluier tipo de trabajo."))
tienda.agregar_producto (Producto("Nintendo Switch", 125,"Consola gamer."))
tienda.agregar_producto (Producto("Juegos para xbox", 20,"Con estos juegos podrás divertirte."))
tienda.agregar_producto (Producto("Juegos para Play", 25,"Con estos juegos podrás divertirte."))
tienda.agregar_producto (Producto("Accesorios xbox/play", 15,"Podras personalizar tus consolas como quieras."))
tienda.agregar_producto (Producto("Mantenimientos xbox / play", 70,"Si tu consola esta fallando, aca podremos arreglarla."))
tienda.agregar_producto (Producto("Mantenimientos pc", 70,"Si tu pc esta fallando, traelo y podremos solucionarlo."))
tienda.agregar_producto (Producto("Clases de mantenimiento para pc o consolas", 50,"Si quieres aprender a arreglar tus dispositivos, ven y aprenderás."))


tienda.mostrar_catalogo()


indice_producto = int(input("Ingrese el número del producto para agregar al carrito: "))
cantidad = int(input("Ingrese la cantidad deseada: "))
tienda.agregar_al_carrito(indice_producto, cantidad)


tienda.mostrar_carrito()


if tienda.carrito:
    print("\nPor favor, complete la información de envío:")
    informacion_envio = {
        "Nombre": input("Nombre: "),
        "Dirección": input("Dirección: "),
        "Ciudad": input("Ciudad: "),
        "País": input("País: ")
    }

    print("\nPor favor, complete la información de pago:")
    informacion_pago = {
        "Número de tarjeta": input("Número de tarjeta: "),
        "Fecha de vencimiento": input("Fecha de vencimiento (MM/YY): "),
        "CVV": input("CVV: "),
    }

    tienda.realizar_pedido(informacion_envio, informacion_pago)