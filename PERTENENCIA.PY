import numpy as np
import matplotlib.pyplot as plt

# Función triangular
def triangular(x, a, b, c):
    return np.maximum(np.minimum((x - a)/(b - a), (c - x)/(c - b)), 0)

# Rango de temperatura
x = np.linspace(0, 40, 400)
a, b, c = 15, 25, 35
y = triangular(x, a, b, c)

# Calcular grado de pertenencia para 25°C
temp = 25
grado = triangular(temp, a, b, c)
print(f"Grado de pertenencia para {temp}°C: {grado:.2f}")

# Graficar
plt.plot(x, y, label="Temperatura cálida", color='orange')
plt.axvline(temp, color='gray', linestyle='--')
plt.text(temp + 0.5, grado/2, f"μ({temp}°C) = {grado:.2f}", color='black')
plt.title("Función de pertenencia triangular - Temperatura cálida")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Grado de pertenencia (μ)")
plt.ylim(0, 1.1)
plt.grid(True)
plt.legend()
plt.show()
