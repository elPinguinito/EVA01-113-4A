class Vehiculo:
    def __init__(self, patente, marca, modelo, año, precio):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def mostrarInfo(self):
        # aplicamos el format, para printear toda la informacion del vehiculo
        print("--- INFORMACION ---")
        print(f"patente: {self.patente}, marca: {self.marca}, modelo: {self.modelo}, año: {self.año}, precio: {self.precio}")

    def calcularAñosUso(self):
        return f"El vehiculo tiene: {2026 - self.año} años."