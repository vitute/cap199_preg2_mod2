import numpy as np
import matplotlib.pyplot as plt

# 1) Creando array para la funcion SENO (desde -0.5 a 2π aprox.)
x = np.linspace(-0.5, 2*np.pi, 1200)
y = np.sin(x)

# 2) Definir Lista con Puntos para tangentes y color de lineas
#    (x0 (punto inicial), texto en leyenda, color de recta tangente, 
#      half_width (semiancho de la recta tangente) )
points = [
    (0,            "Tangente en x=0",       "red",      0.8),
    (np.pi/4,      "Tangente en x=π/4",     "green",    1.0),
    (np.pi/2,      "Tangente en x=π/2",     "blue",     0.9),
    (np.pi,        "Tangente en x=π",       "magenta",  1.1),
    (3*np.pi/2,    "Tangente en x=3π/2",    "c",        1.0),
]

plt.figure(figsize=(12, 4.6))

# 3) Ploteo de la curva SENO (gris/negro y más gruesa)
plt.plot(x, y, color="0.3", linewidth=2.5, label="f(x) = sin(x)")

# 4) Dibujar rectas tangentes SOLO como segmento alrededor de x0
for x0, label, color, half_width in points:  # Recorrer lista anterior
    y0 = np.sin(x0) # Calculo de la altura
    m = np.cos(x0)  # pendiente de la tangente = f'(x0)
    # Construir datos de recta tangente en x0
    x_seg = np.linspace(x0 - half_width, x0 + half_width, 200)
    y_seg = y0 + m * (x_seg - x0)
    # Ploteo de la recta tangente
    plt.plot(x_seg, y_seg, color=color, linewidth=2, label=label)
    # Ploteo de puntos "x0" aislados con area=80 y arriba de las otras lineas
    plt.scatter([x0], [y0], color=color, s=80, zorder=5)

# 5) Ejes, grilla y límites
# Dibujar ejes X e Y, color gris, ancho normal, visibilidad 0.7
plt.axhline(0, color="0.6", linewidth=1, alpha=0.7)
plt.axvline(0, color="0.6", linewidth=1, alpha=0.7)
# Activar la cuadricula con visibilidad suave
plt.grid(True, alpha=0.2)
# Definir limites visibles del eje X y eje Y
plt.xlim(-0.5, 2*np.pi)
plt.ylim(-1.1, 1.55)

plt.title("Rectas tangentes a f(x) = sin(x)", fontweight="bold")
plt.xlabel("x")
plt.ylabel("f(x)")
# Colocar todos los LABELS en la esquina superior derecha
plt.legend(loc="upper right", frameon=True)
plt.show()

