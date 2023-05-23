class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.stock = 0
        def __str__(self):
            return f"{self.nombre} - {self.precio}"

class Tienda:
    def __init__(self):
        self.productos = []

    def ver_productos(self):
        if not self.productos:
            print("No hay productos en la Tienda.")
            return
        print("Productos en la tienda:")
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Stock: {producto.stock}")

    def vender_producto(self, nom_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nom_producto:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    print(f"Se vendieron {cantidad} unidades de {nom_producto}.")
                else:
                    print("No hay suficiente stock para vender.")
                return
        print("El producto no existe en la tienda.")

    def abastecer_producto(self, nom_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nom_producto:
                producto.stock += cantidad
                print(f"Se abastecieron {cantidad} unidades de {nom_producto}.")
                return
        print("El producto no existe en la tienda.")

    def trasladar_producto(self, nom_producto, nuevo_nombre, nuevo_precio):
        for producto in self.productos:
            if producto.nombre == nom_producto:
                producto.nombre = nuevo_nombre
                producto.precio = nuevo_precio
                print(f"El producto {nom_producto} se cambió por {nuevo_nombre} con precio {nuevo_precio}.")
                return
        print("El producto no existe en la tienda.")

    def medir_estadisticas_ventas(self):
        if not self.productos:
            print("No hay productos en la tienda.")
            return
        total_dinero = 0
        total_unidades = 0
        ventas_por_producto = {}

        for producto in self.productos:
            ventas_por_producto[producto.nombre] = 0

        for producto in self.productos:
            total_dinero += producto.stock * producto.precio
            total_unidades += producto.stock
            ventas_por_producto[producto.nombre] += producto.stock

        producto_mayor_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
        cantidad_mas_vendida = ventas_por_producto[producto_mayor_vendido]
        producto_menos_vendido = min(ventas_por_producto, key=ventas_por_producto.get)
        cantidad_menos_vendida = ventas_por_producto[producto_menos_vendido]

        promedio_por_unidad = total_dinero / total_unidades if total_unidades > 0 else 0

        print(f"El producto mayor vendido fue {producto_mayor_vendido} con {cantidad_mas_vendida} unidades vendidas.")
        print(f"El producto menos vendido es {producto_menos_vendido} con {cantidad_menos_vendida} unidades vendidas.")
        print(f"La cantidad total de dinero obtenido por las ventas de la tienda es: {total_dinero}")
        print(f"La cantidad de dinero promedio obtenido por unidad de producto vendida es: {promedio_por_unidad}")

tienda = Tienda()

tienda.productos.append(Producto("Galletas", 9))
tienda.productos.append(Producto("Sporade", 10))
tienda.productos.append(Producto("Yogurt", 21))
tienda.productos.append(Producto("Chocolate", 13))
tienda.ver_productos()

tienda.abastecer_producto("Galletas", 4)
tienda.abastecer_producto("Sporade", 9)
tienda.ver_productos()

tienda.vender_producto("Galletas", 5)
tienda.vender_producto("Sporade", 7)
tienda.ver_productos()

tienda.trasladar_producto("Yogurt", "chicles", 20)
tienda.ver_productos()

tienda.medir_estadisticas_ventas()
