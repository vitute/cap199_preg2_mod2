# Esta es una 1ra actualizacion del archivo PY anterior
# Importando librerias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carga del dataset (descargado en celda anterior)
df = pd.read_csv("Cancer_Pulmon.csv")

# Limpieza mínima (evita espacios y asegura tipos)
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["gender"] = df["gender"].astype(str).str.strip()
df["country"] = df["country"].astype(str).str.strip()
df["cancer_stage"] = df["cancer_stage"].astype(str).str.strip()

# Crear marco para Dashboard con 4 figuras (2 x 2)
fig, axes = plt.subplots(2, 2, figsize=(20, 12))
fig.suptitle("Cancer", fontsize=16, fontweight="bold")

# Figura 1: Histograma de la columna/variable "age"
ax = axes[0, 0]
# Definimos 3 bins para que salgan 3 barras:
#   [25-45], [45-65], [65-85]
bins_age = [25, 45, 65, 85]

ax.hist(
    df["age"].dropna(),
    bins=bins_age,
    color="skyblue",
    edgecolor="black",
    alpha=0.6
)

ax.set_title("Distribucion de la edad")
ax.set_xlabel("Edad")
ax.set_ylabel("Frecuencia")

# Definiendo limites segun gráfico de referencia.
ax.set_xlim(0, 110)
ax.set_ylim(0, 650000)

ax.grid(True, alpha=0.2)

# Figura 2: Diagrama tipo PIE con la columna/variable "gender"
ax = axes[0, 1]
gender_counts = df["gender"].value_counts()

ax.pie(
    gender_counts.values,
    labels=gender_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
ax.set_title("Distribucion del genero")
ax.axis("equal")

# Figura 3: Distribución de Paises (Barras) con variable "country"
ax = axes[1, 0]
country_counts = df["country"].value_counts()

ax.bar(
    country_counts.index,
    country_counts.values,
    color="lightcoral",   # rosado ligeramente oscuro
    alpha=0.9,
    edgecolor="white"
)

ax.set_title("Pacientes por pais")
ax.set_ylabel("Numero de pacientes")
ax.tick_params(axis="x", rotation=90)
ax.grid(True, axis="y", alpha=0.2)

# Figura 4: Distribución de etapas del cancer (Barras) con variable "cancer_stage"
ax = axes[1, 1]
stage_counts = df["cancer_stage"].value_counts()

ax.bar(
    stage_counts.index,
    stage_counts.values,
    color="lightgreen",   # verde claro
    alpha=0.9,
    edgecolor="white"
)

ax.set_title("Distribucion de la etapa del cancer")
ax.set_ylabel("Numero de observaciones")
ax.grid(True, axis="y", alpha=0.2)

# Ajuste final y mostrar el DASHBOARD
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

