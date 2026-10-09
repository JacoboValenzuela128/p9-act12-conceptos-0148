## Arath Valenzuela 
## NC:0148

import pandas as pd

# 1. Crear el dataset utilizando datos28
datos28 = {
    'distancia_km': [1.3, 4.1, 5.9, 2.6, 3.5],
    'trafico_nivel': [1, 2, 3, 1, 3],
    'edad_repartidor': [22, 37, 43, 29, 25],
    'tiempo_entrega_min': [10, 30, 55, 18, 33]
}

df = pd.DataFrame(datos28)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                 # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))

print("Arath Valenzuela")
print("NC:0148")