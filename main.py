from auto import Auto
from motocicleta import Motocicleta
from vendedor import Vendedor
from automotora import Automotora


def main():

    # Crear automotora
    automotora_1 = Automotora("Bruno Fritsch")

    # Crear 2 automóviles
    auto_1 = Auto("jklo23", "nissan", "sentra", 2005, 2300000, 4, "Bencina")
    auto_2 = Auto("poxd89", "mazda", "cx-5", 2023, 22500000, 5, "Diesel")
    auto_1.mostrarInfo()
    print(auto_1.calcularAñosUso())
    print()
    auto_2.mostrarInfo()
    print()
    print(auto_2.calcularAñosUso())




    # Crear motocicleta
    moto_1 = Motocicleta("cx65", "kawasaki", "800", 1996, 1200000, 330, "chopper" )
    moto_1.mostrarInfo()
    print()




    # Agregar vehículos a la automotora
    #automotora_1.agregarVehiculo()
    


    # Mostrar vehículos
    print("===== VEHÍCULOS DE LA AUTOMOTORA =====")
    automotora_1.mostrarVehiculos()
    


    # Probar métodos de un Auto
    print("\n===== AUTO =====")
    auto_1.abrirMaletero()
    print(auto_1.tieneAireAcondicionado())



    # Calcular años de uso del auto


    # Probar métodos de Motocicleta
    print("\n===== MOTOCICLETA =====")
    moto_1.encenderMotor()
    print(moto_1.esDeAltaCilindrada())


    # Calcular años de uso de la motocicleta


    # Crear vendedor
    # vendedor1 = Vendedor(
    #     "Juan Pérez",
    #     "12.345.678-9",
    #     "987654321"
    # )
    vendedor_1 = Vendedor("Elias", "12.345.678-9", "956781234")

    print("\n===== VENDEDOR =====")
    vendedor_1.mostrar_datos()
    #print(vendedor_1.calcular_comision())




    

if __name__ == "__main__":
    main()

# link github: https://github.com/elPinguinito/EVA01-113-4A.git