temperaturas_caldera = [110.5, 112.3, 115.8, 111.2, 118.4] * 2000
def filtrar_ruido_termico():
temperaturas_filtradas = []
suma_acumulada = 0 # Acumulador iniciado antes del ciclo
for i in range(len(temperaturas_caldera)):
# 1. Actualizamos la suma con el dato actual
suma_acumulada = suma_acumulada + temperaturas_caldera[i]
# 2. Calculamos el promedio
promedio = suma_acumulada / (i + 1)
# 3. Guardamos el promedio en la lista 
temperaturas_filtradas.append(promedio)
return temperaturas_filtradas