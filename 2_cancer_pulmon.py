# Creacion del DF a partir del CSV descargado previamente
# El codigo PYTHON se maneja separado del procedimiento de descarga
import pandas as pd
df = pd.read_csv("Cancer_Pulmon.csv")
df.info()
