class Vendedor:
    def __init__(self, nombre, rut, telefono):
        self.nombre = nombre
        self.rut = rut
        self.telefono = telefono

    def mostrar_datos(self):
        print("--- Datos ---")
        print(f"Nombre del vendedor: {self.nombre}, RUT: {self.rut}, Telefono: {self.telefono}")

    def calcular_comision(self, monto_venta):
        pass      