import numpy as np
import matplotlib.pyplot as plt

# Función para realizar la aproximación discreta por mínimos cuadrados
def minimos_cuadrados(x, y):
    # Cálculo de los coeficientes de la recta (pendiente y ordenada al origen)
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    return m, c

# Entrada de datos por parte del usuario
x = list(map(float, input("Ingresa los valores de x separados por espacios: ").split()))
y = list(map(float, input("Ingresa los valores de y separados por espacios: ").split()))

# Convertir las listas a arrays de numpy
x = np.array(x)
y = np.array(y)

# Verificar que las longitudes de x e y coincidan
if len(x) != len(y):
    print("Error: Los arrays x e y deben tener la misma longitud.")
else:
    # Realizar la aproximación
    m, c = minimos_cuadrados(x, y)

    # Mostrar resultados
    print(f"Pendiente: {m:.2f}")
    print(f"Ordenada al origen: {c:.2f}")

    # Gráfica de los datos y la recta de ajuste
    plt.scatter(x, y, color='red', label='Datos')
    plt.plot(x, m*x + c, color='blue', label='Recta de ajuste')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Ajuste por mínimos cuadrados')
    plt.show()
