import sys
import os
import pandas as pd
import io

print("yahir sifuentes Machine Learning pandas, NC 0142")

# 1. Diccionario con los datos de entrada
datos_farmacias = {
    "Farmacia": ["San Pablo", "Similares", "Del Ahorro", "Guadalajara", "Benavides", "Del Savings"],
    "Productos": [8000, 5000, 6500, 7500, 6000, 5500],
    "Clientes_dia": [1500, 2000, 1800, 1200, 1000, 900]
}

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "yahir sifuentes Machine Learning pandas, NC 0142"
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario a DataFrame
df = pd.DataFrame(datos_farmacias)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de una Columna Numérica (Productos)
registrar("3. Estadísticas Generales de la Columna 'Productos'", df['Productos'].describe())

# 4. Ordenar Ascendente por Productos
df_asc_productos = df.sort_values(by="Productos", ascending=True)
registrar("4. Ordenar Ascendente por Productos", df_asc_productos)

# 5. Ordenar Descendente por Clientes_dia
df_desc_clientes = df.sort_values(by="Clientes_dia", ascending=False)
registrar("5. Ordenar Descendente por Clientes_dia", df_desc_clientes)

# 6. Guardar el archivo resultados-ml-0142.md dentro de resultados-0142
carpeta_resultados = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resultados-0142'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-0142.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("yahir sifuentes Machine Learning pandas, NC 0142")