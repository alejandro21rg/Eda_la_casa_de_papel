import pandas as pd
import matplotlib.pyplot as plt
import os

# Importamos el tsv
df_netflix_country_weekly = pd.read_csv("../data/most-popular_country_weekly.tsv", sep="\t")

# Nos quedamos solo con las series
series = df_netflix_country_weekly[df_netflix_country_weekly["category"].str.contains("TV", na=False)]

#Creamos el top de series españolas
top_espanolas = ["Money Heist", "Elite", "Berlin", "Valeria", "Cable Girls", "Toy Boy",
    "The Snow Girl", "Welcome to Eden", "The Innocent", "Alpha Males"]

# Sacamos el listado de esas series
series_espanolas = series[series["show_title"].isin(top_espanolas)]

# Empezamos a buscar por diferentes paises
# En primer lugar crearemos la lista de cada pais
# Luego lo ordenaremos por tiempo en el top 10 del ranking
# Crearemos el diagrama con barras horizontales 
# Para terminar guardaremos la imagen del diagrama en una carpeta llamada imagenes_diagrama

# Argentina

series_argentina = series_espanolas[ series_espanolas["country_name"] == "Argentina"]

series_argentina_ord = series_argentina.sort_values(by="cumulative_weeks_in_top_10", ascending=False)

# Top 10
top10 = (
    series_argentina
    .groupby("show_title")["cumulative_weeks_in_top_10"]
    .max()
    .sort_values(ascending=False)
    .head(10)
)

plt.style.use("default")

# Figura
plt.figure(figsize=(12,7))

# Barras horizontales
bars = plt.barh(
    top10.index,
    top10.values,
    color="#E50914" 
)

# Invertimos para que el mayor quede arriba
plt.gca().invert_yaxis()

# Títulos
plt.title(
    "Top Series españolas en Argentina",
    fontsize=20,
    fontweight="bold"
)

# Añadir números al final de cada barra
for bar in bars:
    width = bar.get_width()
    
    plt.text(
        width + 0.3,
        bar.get_y() + bar.get_height()/2,
        f"{int(width)}",
        va="center",
        fontsize=11
    )

plt.xlabel(
    "Semanas acumuladas en Top 10",
    fontsize=12
)

# Ajustar diseño
plt.tight_layout()

# Ruta base (subimos desde /código a /Código)
ruta_base = os.path.dirname(os.getcwd())

# Carpeta de imágenes
carpeta = os.path.join(
    ruta_base,
    "imagenes_diagrama"
)

# Crear carpeta si no existe
os.makedirs(carpeta, exist_ok=True)

# Ruta completa de la imagen
ruta_imagen = os.path.join(
    carpeta,
    "top_series_argentina.png"
)

# Guardar imagen
plt.savefig(
    ruta_imagen,
    dpi=300,
    bbox_inches="tight"
)

# Cerrar figura para evitar ventanas
plt.close()

print(f"Imagen guardada en: {ruta_imagen}")

# Francia
series_en_francia = series_espanolas[ series_espanolas["country_name"] == "France"]

series_en_francia_or = series_en_francia.sort_values(by="cumulative_weeks_in_top_10", ascending=False)

# Top 10
top10 = (
    series_en_francia
    .groupby("show_title")["cumulative_weeks_in_top_10"]
    .max()
    .sort_values(ascending=False)
    .head(10)
)

plt.style.use("default")

# Figura
plt.figure(figsize=(12,7))

# Barras horizontales
bars = plt.barh(
    top10.index,
    top10.values,
    color="#E50914" 
)

# Invertimos para que el mayor quede arriba
plt.gca().invert_yaxis()

# Títulos
plt.title(
    "Top Series españolas en Francia",
    fontsize=20,
    fontweight="bold"
)

plt.xlabel(
    "Semanas acumuladas en Top 10",
    fontsize=12
)

# Añadir números al final de cada barra
for bar in bars:
    width = bar.get_width()
    
    plt.text(
        width + 0.3,
        bar.get_y() + bar.get_height()/2,
        f"{int(width)}",
        va="center",
        fontsize=11
    )


# Ajustar diseño
plt.tight_layout()

# Ruta base (subimos desde /código a /Código)
ruta_base = os.path.dirname(os.getcwd())

# Carpeta de imágenes
carpeta = os.path.join(
    ruta_base,
    "imagenes_diagrama"
)

# Crear carpeta si no existe
os.makedirs(carpeta, exist_ok=True)

# Ruta completa de la imagen
ruta_imagen = os.path.join(
    carpeta,
    "top_series_francia.png"
)

# Guardar imagen
plt.savefig(
    ruta_imagen,
    dpi=300,
    bbox_inches="tight"
)

# Cerrar figura para evitar ventanas
plt.close()

print(f"Imagen guardada en: {ruta_imagen}")

# EE.UU
series_en_eeuu = series_espanolas[ series_espanolas["country_name"] == "United States"]

series_en_eeuu_ord = series_en_eeuu.sort_values(by="cumulative_weeks_in_top_10", ascending=False)

# Top 10
top10 = (
    series_en_eeuu
    .groupby("show_title")["cumulative_weeks_in_top_10"]
    .max()
    .sort_values(ascending=False)
    .head(10)
)

plt.style.use("default")

# Figura
plt.figure(figsize=(12,7))

# Barras horizontales
bars = plt.barh(
    top10.index,
    top10.values,
    color="#E50914" 
)

# Invertimos para que el mayor quede arriba
plt.gca().invert_yaxis()

# Títulos
plt.title(
    "Top Series españolas en EE.UU",
    fontsize=20,
    fontweight="bold"
)

plt.xlabel(
    "Semanas acumuladas en Top 10",
    fontsize=12
)

# Añadir números al final de cada barra
for bar in bars:
    width = bar.get_width()
    
    plt.text(
        width + 0.3,
        bar.get_y() + bar.get_height()/2,
        f"{int(width)}",
        va="center",
        fontsize=11
    )



# Ajustar diseño
plt.tight_layout()

# Ruta base (subimos desde /código a /Código)
ruta_base = os.path.dirname(os.getcwd())

# Carpeta de imágenes
carpeta = os.path.join(
    ruta_base,
    "imagenes_diagrama"
)

# Crear carpeta si no existe
os.makedirs(carpeta, exist_ok=True)

# Ruta completa de la imagen
ruta_imagen = os.path.join(
    carpeta,
    "top_series_eeuu.png"
)

# Guardar imagen
plt.savefig(
    ruta_imagen,
    dpi=300,
    bbox_inches="tight"
)

# Cerrar figura para evitar ventanas
plt.close()

print(f"Imagen guardada en: {ruta_imagen}")

# UAE
series_en_uae = series_espanolas[ series_espanolas["country_name"] == "United Arab Emirates"]

series_en_uae_ord = series_en_uae.sort_values(by="cumulative_weeks_in_top_10", ascending=False)

# Top 10
top10 = (
    series_en_uae
    .groupby("show_title")["cumulative_weeks_in_top_10"]
    .max()
    .sort_values(ascending=False)
    .head(10)
)

plt.style.use("default")

# Figura
plt.figure(figsize=(12,7))

# Barras horizontales
bars = plt.barh(
    top10.index,
    top10.values,
    color="#E50914" 
)

# Invertimos para que el mayor quede arriba
plt.gca().invert_yaxis()

# Títulos
plt.title(
    "Top Series españolas en United Arab Emirates ",
    fontsize=20,
    fontweight="bold"
)

plt.xlabel(
    "Semanas acumuladas en Top 10",
    fontsize=12
)

# Añadir números al final de cada barra
for bar in bars:
    width = bar.get_width()
    
    plt.text(
        width + 0.3,
        bar.get_y() + bar.get_height()/2,
        f"{int(width)}",
        va="center",
        fontsize=11
    )

# Ajustar diseño
plt.tight_layout()

# Ruta base (subimos desde /código a /Código)
ruta_base = os.path.dirname(os.getcwd())

# Carpeta de imágenes
carpeta = os.path.join(
    ruta_base,
    "imagenes_diagrama"
)

# Crear carpeta si no existe
os.makedirs(carpeta, exist_ok=True)

# Ruta completa de la imagen
ruta_imagen = os.path.join(
    carpeta,
    "top_series_uae.png"
)

# Guardar imagen
plt.savefig(
    ruta_imagen,
    dpi=300,
    bbox_inches="tight"
)

# Cerrar figura para evitar ventanas
plt.close()

print(f"Imagen guardada en: {ruta_imagen}")

# Turquía
series_en_turquia = series_espanolas[ series_espanolas["country_name"] == "Turkey"]

series_en_turquia_ord = series_en_turquia.sort_values(by="cumulative_weeks_in_top_10", ascending=False)

# Top 10
top10 = (
    series_en_turquia
    .groupby("show_title")["cumulative_weeks_in_top_10"]
    .max()
    .sort_values(ascending=False)
    .head(10)
)

plt.style.use("default")

# Figura
plt.figure(figsize=(12,7))

# Barras horizontales
bars = plt.barh(
    top10.index,
    top10.values,
    color="#E50914" 
)

# Invertimos para que el mayor quede arriba
plt.gca().invert_yaxis()

# Títulos
plt.title(
    "Top Series españolas en Turquía ",
    fontsize=20,
    fontweight="bold"
)

plt.xlabel(
    "Semanas acumuladas en Top 10",
    fontsize=12
)

# Añadir números al final de cada barra
for bar in bars:
    width = bar.get_width()
    
    plt.text(
        width + 0.3,
        bar.get_y() + bar.get_height()/2,
        f"{int(width)}",
        va="center",
        fontsize=11
    )



# Ajustar diseño
plt.tight_layout()

# Ruta base (subimos desde /código a /Código)
ruta_base = os.path.dirname(os.getcwd())

# Carpeta de imágenes
carpeta = os.path.join(
    ruta_base,
    "imagenes_diagrama"
)

# Crear carpeta si no existe
os.makedirs(carpeta, exist_ok=True)

# Ruta completa de la imagen
ruta_imagen = os.path.join(
    carpeta,
    "top_series_turquia.png"
)

# Guardar imagen
plt.savefig(
    ruta_imagen,
    dpi=300,
    bbox_inches="tight"
)

# Cerrar figura para evitar ventanas
plt.close()

print(f"Imagen guardada en: {ruta_imagen}")


# Vamos a ver ahora las series españolas a nivel global

# Importamos el csv
netflix_espanolas = pd.read_csv("../data/series_espanolas_netflix_global.csv")

# Agrupamos las series y las ordenamos

netflix_espanolas = (
     netflix_espanolas.groupby("show_title")["cumulative_weeks_in_top_10"]
    .max()
    .sort_values(ascending=False)
)

# Realizamos el diagrama y guardamos la imagen que se genere

# Top 10 series
top10 = netflix_espanolas.head(10)

# Estilo claro
plt.style.use("default")

# Figura
plt.figure(figsize=(12,7))

# Barras
bars = plt.barh(
    top10.index,
    top10.values,
    color="#E50914"
)

# Mayor arriba
plt.gca().invert_yaxis()

# Título
plt.title(
    "Series españolas más vistas en Netflix",
    fontsize=20,
    fontweight="bold"
)

# Eje X
plt.xlabel(
    "Semanas acumuladas en Top 10",
    fontsize=12
)

# Etiquetas numéricas
for bar in bars:
    width = bar.get_width()

    plt.text(
        width + 0.3,
        bar.get_y() + bar.get_height()/2,
        f"{int(width)}",
        va="center",
        fontsize=11
    )

# Cuadrícula suave
plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.3
)

# Ajuste
plt.tight_layout()

# Guardar imagen
plt.savefig(
    "../imagenes_diagrama/top_series_espanolas.png",
    dpi=300,
    bbox_inches="tight"
)

# Cerrar figura
plt.close()

print("Diagrama guardado correctamente")