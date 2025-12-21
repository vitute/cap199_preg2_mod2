# Paso 4: Utilizando el mismo dataset cargado en "df" en el Paso 2,
#   se pide generar un BOXPLOT para las variables:
#   "age", "bmi" y "cholesterol_level"

# Importando librerias
import pandas as pd
import matplotlib.pyplot as plt

# Cargando el mismo dataset del Paso 2
df = pd.read_csv("Cancer_Pulmon.csv")

# Asegurando que las columnas solicitadas sean numéricas
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["bmi"] = pd.to_numeric(df["bmi"], errors="coerce")
df["cholesterol_level"] = pd.to_numeric(df["cholesterol_level"], errors="coerce")

# Creando el marco general para colocar las 3 BOTPLOX de forma horizontal
fig, axes = plt.subplots(
    nrows=1,
    ncols=3,
    figsize=(14, 7)   # ancho x altura
)

fig.suptitle(
    "Distribucion de variables clinicas",
    fontsize=16,
    fontweight="bold"
)

# Creación del 1er BOXPLOT para la variable "age"
axes[0].boxplot(
    df["age"].dropna(),
    vert=True,
    patch_artist=True,
    boxprops=dict(facecolor="skyblue"),
    medianprops=dict(color="black")
)

axes[0].set_title("Age")
axes[0].set_ylabel("Edad")
axes[0].grid(True, axis="y", alpha=0.2)

# Creación del 2do BOXPLOT para la variable "bmi"
axes[1].boxplot(
    df["bmi"].dropna(),
    vert=True,
    patch_artist=True,
    boxprops=dict(facecolor="lightgreen"),
    medianprops=dict(color="black")
)

axes[1].set_title("BMI")
axes[1].set_ylabel("Indice de Masa Corporal")
axes[1].grid(True, axis="y", alpha=0.2)

# Creación del 3er BOXPLOT para la variable "cholesterol_level"
axes[2].boxplot(
    df["cholesterol_level"].dropna(),
    vert=True,
    patch_artist=True,
    boxprops=dict(facecolor="lightcoral"),
    medianprops=dict(color="black")
)

axes[2].set_title("Cholesterol Level")
axes[2].set_ylabel("Nivel de colesterol")
axes[2].grid(True, axis="y", alpha=0.2)

# Ajustes finales para acomodar las figuras
plt.subplots_adjust(
    wspace=0.25,   # espacio horizontal (menor = más juntos)
    top=0.85
)

plt.show()
