#Escenario 3
modbus_tuf = {
    "0x01": {
        "unit": "m3/h",
        "multiplier": 0.1,
        "modbus_type": "Holding"
    },

    "0x03": {
        "unit": "m/s",
        "multiplier": 0.01,
        "modbus_type": "Input"
    },

    "0x09": {
        "unit": "m3",
        "multiplier": 1.0,
        "modbus_type": "Holding"
    }
}

max_consultas = 3
consulta = 0
while consulta < max_consultas:

    direccion = input(
        "\nIngrese la dirección hexadecimal del registro "
        "(0x01, 0x03 o 0x09): "
    ).strip().lower()

    registro = modbus_tuf.get(direccion)

    if registro is not None:
        print("\n--- REGISTRO ENCONTRADO ---")
        print(f"Dirección: {direccion}")
        print(f"Unidad: {registro.get('unit')}")
        print(f"Multiplicador: {registro.get('multiplier')}")
        print(f"Tipo Modbus: {registro.get('modbus_type')}")

    else:
        print("\nRegistro no encontrado.")
        print("Verifique la dirección ingresada.")

    consulta += 1

print("\nFin de las consultas.")