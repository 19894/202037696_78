temperatura = 100
sistema_activo = True

for ciclo in range(20):

    if temperatura > 130:
        print("ALERTA CRÍTICA: Parada de emergencia")
        sistema_activo = False
        break

    elif temperatura < 115:
        print("Estado: Calentando autoclave")
        temperatura += 2

    elif temperatura >= 115 and temperatura <= 121:
        print("Estado: Fase estable de esterilización")
        temperatura = temperatura

    else:
        print("Estado: Enfriamiento activo")
        temperatura -= 3

    print("Temperatura actual:", temperatura)