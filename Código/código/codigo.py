import pandas as pd
import matplotlib.pyplot as plt
import os

# Hipotesis 1

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

# Hay un error en el csv ya que aparece la serie con la version Coreana, la vamos a elmininar

series_espanolas = netflix_espanolas[
    ~netflix_espanolas["show_title"].isin([
        "Money Heist: Korea - Joint Economic Area",
    ])
]
# Agrupamos las series y las ordenamos

series_espanolas = (
     series_espanolas.groupby("show_title")["cumulative_weeks_in_top_10"]
    .max()
    .sort_values(ascending=False)
)

# Realizamos el diagrama y guardamos la imagen que se genere

# Top 10 series
top10 = series_espanolas.head(10)

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

print("Gráfico guardado correctamente")

# Vamos a analizar las voloraciones
# Para ello usaremos dos csv de IMDb
# Mediante un merge unifico ambos csv

df_idmb_title_basics = pd.read_csv("../data/title.basics.tsv", sep="\t")
df_idmb_title_ratings = pd.read_csv("../data/title.ratings.tsv", sep="\t")

imdb_completo = pd.merge(df_idmb_title_basics,df_idmb_title_ratings, on="tconst")

series_imdb = imdb_completo[imdb_completo["titleType"] == "tvSeries"]

# Para que se vean titulo, genero, nota y numero de votos

series_final = series_imdb[[
    "primaryTitle",
    "startYear",
    "genres",
    "averageRating",
    "numVotes"
]]

# Ranking global ordenador por votos
ranking_global = (
    series_final.sort_values(
        by="numVotes",
        ascending=False
    )
    .reset_index(drop=True)
)

# Pongo en un diccionario las series españolas

series_espanolas_nombres = [
    "Money Heist",
    "Elite",
    "Berlin",
    "Valeria",
    "Cable Girls",
    "Toy Boy",
    "The Snow Girl",
    "Welcome to Eden",
    "The Innocent",
    "Alpha Males"
]

# Sobre el rankin global, creo un ranking de españolas

ranking_espanolas = ranking_global[
    ranking_global["primaryTitle"].isin(
        series_espanolas_nombres
    )
]

# Diagrama de dispersión mas autoguardado

import matplotlib.pyplot as plt

# Eliminar duplicados por título
ranking_unico = (
    ranking_espanolas
    .sort_values("numVotes", ascending=False)
    .drop_duplicates(subset="primaryTitle")
)

plt.style.use("default")

plt.figure(figsize=(12,8))

# Scatter plot
plt.scatter(
    ranking_unico["numVotes"],
    ranking_unico["averageRating"],
    s=150,
    color="#E50914",
    alpha=0.8
)

# Etiquetas de cada serie
for _, row in ranking_unico.iterrows():

    plt.text(
        row["numVotes"] + 5000,
        row["averageRating"],
        row["primaryTitle"],
        fontsize=10
    )

# Título
plt.title(
    "Popularidad vs valoración de series españolas",
    fontsize=20,
    fontweight="bold"
)

# Etiquetas ejes
plt.xlabel(
    "Número de votos IMDb",
    fontsize=12
)

plt.ylabel(
    "Valoración media IMDb",
    fontsize=12
)

# Cuadrícula suave
plt.grid(
    linestyle="--",
    alpha=0.3
)

# Quitar bordes
ax = plt.gca()

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)


plt.tight_layout()

# Guardar imagen
plt.savefig(
    "../imagenes_diagrama/valoracion_series_espanolas.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Gráfico guardado correctamente")


# Para ver otro gráfico diferente, importamos squarify
import squarify

# Eliminar duplicados por título
ranking_unico = (
    ranking_espanolas
    .sort_values("numVotes", ascending=False)
    .drop_duplicates(subset="primaryTitle")
)

# Top series
ranking_unico = ranking_unico.head(8)

# Tamaños
sizes = ranking_unico["numVotes"]

# Etiquetas
labels = [
    f"{title}\n{votes:,}"
    for title, votes in zip(
        ranking_unico["primaryTitle"],
        ranking_unico["numVotes"]
    )
]

# Paleta más llamativa y moderna
colors = [
    "#E50914",  # Rojo Netflix intenso
    "#FF4D6D",  # Rosa fuerte
    "#F77F00",  # Naranja vibrante
    "#FFD60A",  # Amarillo brillante
    "#06D6A0",  # Verde turquesa
    "#118AB2",  # Azul moderno
    "#8338EC",  # Morado intenso
    "#EF476F"   # Rosa coral
]

# Figura
plt.figure(figsize=(16,8))

# Treemap
squarify.plot(
    sizes=sizes,
    label=labels,
    color=colors,
    alpha=0.95,
    text_kwargs={
        'fontsize':13,
        'weight':'bold',
        'color':'white'
    }
)

# Quitar ejes
plt.axis("off")

# Título
plt.title(
    "Popularidad de series españolas en IMDb",
    fontsize=24,
    fontweight="bold",
    pad=20
)

plt.tight_layout()

# Guardar imagen
plt.savefig(
    "../imagenes_diagrama/valoracion_series_espanolas_2.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Gráfico guardado correctamente")

# Hipotesis 2

# Analisis con otras series de no habla inglesa
# Importamos el csv

df_netflix_alltime = pd.read_csv("../data/most-popular_global_alltime.tsv", sep="\t")

# Nos quedamos con las tv que no son de habla inglesa, que es la parte que nos interesa

tv_non_english = df_netflix_alltime[df_netflix_alltime["category"] == "TV (Non-English)"]

# Creamos el gáfico e importamos seaborn

import seaborn as sns

plt.figure(figsize=(12,6))

ax = sns.barplot(
    data=tv_non_english,
    x="show_title",
    y="views_first_91_days",
    hue="show_title",   # evita el warning
    palette=["#7AE22F", "#F30313", "#CA4850", "#E6E6C3", "#8B1C1C"],
    errorbar=None,
    legend=False
)

# Añadir etiquetas
for p in ax.patches:
    height = p.get_height()

    ax.text(
        p.get_x() + p.get_width()/2,
        height + 3000000,  # separación vertical
        f'{height/1_000_000:.1f}M',
        ha="center",
        fontsize=10,
        fontweight="bold"
    )

plt.xticks(rotation=45)

plt.title(
    "Series TV No Inglesas más vistas en Netflix",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout()

# Guardar imagen
plt.savefig(
    "../imagenes_diagrama/series_habla_no_inglesa.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Gráfico guardado correctamente")

# Hipotesis 3
# Usamos el csv anterior 

tv_general = df_netflix_alltime[df_netflix_alltime["category"].isin(["TV (English)","TV (Non-English)" ])]

# Ordenamos por visualizaciones
orden_visualizaciones = tv_general.sort_values(by="views_first_91_days", ascending=False)

# Agrupamos por nombre, para ver las visualizaciones totales de cada serie

df_series = (
    orden_visualizaciones
    .groupby("show_title", as_index=False)["views_first_91_days"]
    .sum()
    .sort_values(by="views_first_91_days", ascending=False)
)

df_series.head(10)

# Creamo el gráfico 

plt.figure(figsize=(12,7))

# Ordenar top 10
top10 = df_series.head(10).sort_values("views_first_91_days")

# Colores personalizados
colors = [
    "#E50914", "#B20710", "#D81F26", "#F40612", "#831010",
    "#564D4D", "#221F1F", "#C1351D", "#FF6B6B", "#9B111E"
]

# Líneas
for i, (value, color) in enumerate(zip(top10["views_first_91_days"], colors)):
    plt.hlines(
        y=i,
        xmin=0,
        xmax=value,
        color=color,
        linewidth=4
    )

# Puntos
plt.scatter(
    top10["views_first_91_days"],
    range(len(top10)),
    color=colors,
    s=150
)

# Etiquetas eje Y
plt.yticks(range(len(top10)), top10["show_title"])

# Más espacio a la derecha para que no se corte Squid Game
max_value = top10["views_first_91_days"].max()
plt.xlim(0, max_value * 1.20)

# Valores separados de la línea
for i, value in enumerate(top10["views_first_91_days"]):
    plt.text(
        value + max_value * 0.03,
        i,
        f'{value/1_000_000:.1f}M',
        va='center',
        fontsize=10,
        fontweight='bold'
    )

# Título
plt.title(
    "Top Series Netflix por Visualizaciones Acumuladas",
    fontsize=20,
    fontweight="bold"
)

plt.xlabel("Visualizaciones")
plt.ylabel("Serie")

sns.despine()

plt.tight_layout()

# Guardar imagen
plt.savefig(
    "../imagenes_diagrama/series_general.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Gráfico guardado correctamente")


# Volvemos a usar los csv de IMBd
# Esta vez vamos a comparar la casa de papel con la series no solo con la pltaforma Netflix
# Se valorara, el número de votos o nota que tiene
# La intentción es mostra que está en la lista con grandes series

series_imdb = imdb_completo[imdb_completo["titleType"] == "tvSeries"]

# Para que se vean titulos, genero, nota y numero de votos

series_final = series_imdb[[
    "primaryTitle",
    "startYear",
    "genres",
    "averageRating",
    "numVotes"
]]

# Top 25 

top_25_rating = series_final.sort_values(
    by="numVotes",
    ascending=False
).head(25)

top_25_rating

# Gráfico

top_votes = top_25_rating.head(25)

plt.style.use("default")

# Figura
fig, ax = plt.subplots(figsize=(14,8))

# Líneas horizontales
ax.hlines(
    y=top_votes["primaryTitle"],
    xmin=0,
    xmax=top_votes["numVotes"],
    color="#D1D5DB",
    linewidth=3
)

# Puntos finales
colors = []

for title in top_votes["primaryTitle"]:
    
    if title == "Money Heist":
        colors.append("#E50914")  # Rojo Netflix
    else:
        colors.append("#1D3557")  # Azul elegante

ax.scatter(
    top_votes["numVotes"],
    top_votes["primaryTitle"],
    color=colors,
    s=250
)

# Valores + nota IMDb
for i, (_, row) in enumerate(top_votes.iterrows()):

    ax.text(
        row["numVotes"] + 60000,
        i,
        f'{row["numVotes"]:,} | IMDb: {row["averageRating"]}',
        va='center',
        fontsize=9
    )

# Título
ax.set_title(
    "Series con mayor número de votos en IMDb",
    fontsize=22,
    fontweight="bold",
    pad=20
)

# Etiquetas
ax.set_xlabel(
    "Número de votos",
    fontsize=13
)

ax.set_ylabel("")

# Grid suave
ax.grid(
    axis='x',
    linestyle='--',
    alpha=0.25
)

# Limpiar bordes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.tight_layout()

# Guardar imagen
plt.savefig(
    "../imagenes_diagrama/series_general_imbd.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Gráfico guardado correctamente")

# Hipotesis 4
# Influyo La Casa de Papel en la valoración de las series españolas

# Separamos por años antes de 2017 y después

antes_2017 = [
    "Gran Hotel",
    "Isabel",
    "Velvet",
    "The Ministry of Time",
    "Mar de Plastico",
    "Locked Up",
    "Física o química",
    "Aquí no hay quien viva",
    "La que se avecina",
]

despues_2017 = [
    "Money Heist",
    "Elite",
    "Cable Girls",
    "Valeria",
    "Berlin",
    "Toy Boy",
    "The Snow Girl",
    "Welcome to Eden",
    "Alpha Males",
    "Muted"
]

antes = series_imdb[
    (
        series_imdb["primaryTitle"].isin(antes_2017)
    )
    |
    (
        series_imdb["originalTitle"].isin(antes_2017)
    )
]

despues = series_imdb[
    (
        series_imdb["primaryTitle"].isin(despues_2017)
    )
    |
    (
        series_imdb["originalTitle"].isin(despues_2017)
    )
]

ranking_antes_orde = (
    antes.sort_values(
        by="numVotes",
        ascending=False
    )
    .reset_index(drop=True)
)

ranking_despues_orde = (
    despues.sort_values(
        by="numVotes",
        ascending=False
    )
    .reset_index(drop=True)
)

# Top 8 antes de 2017
antes_top = (
    ranking_antes_orde
    .head(8)
    .copy()
)

# Top 8 después de 2017
despues_top = (
    ranking_despues_orde
    .head(8)
    .copy()
)

import matplotlib.pyplot as plt

# Top 8 antes de 2017
antes_top = (
    ranking_antes_orde
    .sort_values("numVotes", ascending=False)
    .head(8)
    .sort_values("numVotes")
)

plt.style.use("default")

plt.figure(figsize=(13,7))

# Barras
plt.barh(
    antes_top["primaryTitle"],
    antes_top["numVotes"],
    color="#6C757D"
)

# Texto votos + rating
for i, (_, row) in enumerate(antes_top.iterrows()):

    plt.text(
        row["numVotes"] + 500,
        i,
        f'{row["numVotes"]:,} | IMDb {row["averageRating"]}',
        va='center',
        fontsize=9
    )

# Título
plt.title(
    "Series españolas más populares antes de 2017",
    fontsize=20,
    fontweight="bold"
)

plt.xlabel("Número de votos IMDb")

# Grid
plt.grid(axis='x', alpha=0.25)

# Limpiar bordes
ax = plt.gca()

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()

# Guardar imagen
plt.savefig(
    "../imagenes_diagrama/valoracion_antes_2017.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Gráfico guardado correctamente")


# Top 8 desde 2017
despues_top = (
    ranking_despues_orde
    .sort_values("numVotes", ascending=False)
    .head(8)
    .sort_values("numVotes")
)

plt.figure(figsize=(13,7))

# Barras
plt.barh(
    despues_top["primaryTitle"],
    despues_top["numVotes"],
    color="#E50914"
)

# Texto votos + rating
for i, (_, row) in enumerate(despues_top.iterrows()):

    plt.text(
        row["numVotes"] + 5000,
        i,
        f'{row["numVotes"]:,} | IMDb {row["averageRating"]}',
        va='center',
        fontsize=9
    )

# Título
plt.title(
    "Series españolas más populares desde 2017",
    fontsize=20,
    fontweight="bold"
)

plt.xlabel("Número de votos IMDb")

# Grid
plt.grid(axis='x', alpha=0.25)

# Limpiar bordes
ax = plt.gca()

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()

# Guardar imagen
plt.savefig(
    "../imagenes_diagrama/valoracion_2017.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Gráfico guardado correctamente")

# Añadir categoría temporal
antes_top["Periodo"] = "Antes de 2017"
despues_top["Periodo"] = "Desde 2017"

# Unir
comparacion = pd.concat([
    antes_top,
    despues_top
])

# Ordenar
comparacion = comparacion.sort_values("numVotes")

# Colores
colors = []

for periodo in comparacion["Periodo"]:

    if periodo == "Antes de 2017":
        colors.append("#6C757D")
    else:
        colors.append("#E50914")

# Figura
plt.figure(figsize=(15,9))

# Barras
plt.barh(
    comparacion["primaryTitle"],
    comparacion["numVotes"],
    color=colors
)

# Texto votos + IMDb
for i, (_, row) in enumerate(comparacion.iterrows()):

    plt.text(
        row["numVotes"] + 5000,
        i,
        f'{row["numVotes"]:,} | IMDb {row["averageRating"]}',
        va='center',
        fontsize=9
    )

# Título
plt.title(
    "Impacto internacional de las series españolas tras La Casa de Papel",
    fontsize=22,
    fontweight="bold"
)

plt.xlabel("Número de votos IMDb")

# Leyenda manual
from matplotlib.patches import Patch

legend_elements = [
    Patch(facecolor="#6C757D", label="Antes de 2017"),
    Patch(facecolor="#E50914", label="Desde 2017")
]

plt.legend(handles=legend_elements)

# Grid
plt.grid(axis='x', alpha=0.25)

# Limpiar bordes
ax = plt.gca()

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()

# Guardar imagen
plt.savefig(
    "../imagenes_diagrama/valoracion_conjunta.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Gráfico guardado correctamente")


# Demostración de que no es producto de la digitalización
# Sino del impacto de La Casa de Papel

# Top 25 series más votadas
top_votes = (
    top_25_rating
    .sort_values("numVotes")
)

plt.style.use("default")

# Figura
fig, ax = plt.subplots(figsize=(16,12))

# Líneas horizontales
ax.hlines(
    y=top_votes["primaryTitle"],
    xmin=0,
    xmax=top_votes["numVotes"],
    color="#C7CCD4",
    linewidth=3
)

# Colores
colors = []

for title in top_votes["primaryTitle"]:

    if title == "Money Heist":
        colors.append("#E50914")  # Rojo Netflix
    else:
        colors.append("#1D3557")  # Azul elegante

# Puntos
ax.scatter(
    top_votes["numVotes"],
    top_votes["primaryTitle"],
    color=colors,
    s=260
)

# Texto -> votos + año
for i, (_, row) in enumerate(top_votes.iterrows()):

    ax.text(
        row["numVotes"] + 35000,
        i,
        f'{row["numVotes"]:,} | Año: {row["startYear"]}',
        va='center',
        fontsize=10
    )

# Título
ax.set_title(
    "Series con mayor número de votos en IMDb y año de estreno",
    fontsize=24,
    fontweight="bold",
    pad=20
)

# Ejes
ax.set_xlabel(
    "Número de votos IMDb",
    fontsize=14
)

ax.set_ylabel("")

# Grid suave
ax.grid(
    axis='x',
    linestyle='--',
    alpha=0.2
)

# Limpiar bordes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.tight_layout()

# Guardar imagen
plt.savefig(
    "../imagenes_diagrama/top25_con_año.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Gráfico guardado correctamente")

# Hipotesis 5

# Influyó La Casa de Papel en el aumento de series españolas en Netflix
# Veremos las que habia antes de estar y despues
# Además la compararemos con otros paises Europeos
# Importamos el csv 

crecimiento_esp = pd.read_csv("../data/titles.csv")

netflix_esp = crecimiento_esp[
    ["title", "release_year", "production_countries"]
]

spain_only = netflix_esp[
    netflix_esp["production_countries"] == "['ES']"
]

# Solo producciones exclusivamente españolas
spain_only = netflix_esp[
    netflix_esp["production_countries"] == "['ES']"
]

# Contar producciones por año
growth = spain_only.groupby("release_year").size()

# Filtrar años relevantes
growth = growth[(growth.index >= 2014) & (growth.index <= 2021)]

# Colores de barras
colors = []

for year in growth.index:
    if year < 2017:
        colors.append("#9CA3AF")   # Gris suave
    else:
        colors.append("#E50914")   # Rojo Netflix

# Crear gráfica
plt.figure(figsize=(14,7))

# Barras
plt.bar(
    growth.index,
    growth.values,
    color=colors,
    edgecolor="black",
    linewidth=1.2
)


# Fondo suave posterior a 2017
plt.axvspan(
    2017,
    2021.5,
    color="#FDECEC",
    alpha=0.3
)

# Títulos
plt.title(
    "Producciones españolas en Netflix antes y después de La Casa de Papel",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel(
    "Año",
    fontsize=13
)

plt.ylabel(
    "Número de producciones",
    fontsize=13
)

plt.xticks(
    growth.index,
    fontsize=11
)

plt.yticks(fontsize=11)

# Grid elegante
plt.grid(
    axis='y',
    linestyle='--',
    alpha=0.3
)

# Quitar bordes superiores y derechos
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Guardar imagen
plt.savefig(
    "../imagenes_diagrama/produciones_esp.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Gráfico guardado correctamente")

# Comparación con otros paises Europeos

# Función para contar producciones por país
def country_growth(code):
    
    country = crecimiento_esp[
        crecimiento_esp["production_countries"] == f"['{code}']"
    ]

    growth = country.groupby("release_year").size()

    growth = growth[
        (growth.index >= 2014) &
        (growth.index <= 2021)
    ]

    return growth

# Datos países
spain = country_growth("ES")
france = country_growth("FR")
germany = country_growth("DE")
italy = country_growth("IT")
uk = country_growth("GB")

# Figura
plt.figure(figsize=(15,8))

# España destacada
plt.plot(
    spain.index,
    spain.values,
    linewidth=4,
    marker="o",
    label="España"
)

# Otros países
plt.plot(
    france.index,
    france.values,
    linewidth=2.5,
    marker="o",
    label="Francia"
)

plt.plot(
    germany.index,
    germany.values,
    linewidth=2.5,
    marker="o",
    label="Alemania"
)

plt.plot(
    italy.index,
    italy.values,
    linewidth=2.5,
    marker="o",
    label="Italia"
)

plt.plot(
    uk.index,
    uk.values,
    linewidth=2.5,
    marker="o",
    color="#1D3557",   # Color Reino Unido
    label="Reino Unido"
)

# Línea vertical La Casa de Papel
plt.axvline(
    x=2017,
    color="red",
    linestyle="--",
    linewidth=2
)


# Títulos
plt.title(
    "Evolución de producciones europeas en Netflix",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel("Año", fontsize=12)
plt.ylabel("Número de producciones", fontsize=12)

plt.legend()

plt.grid(alpha=0.3)

# Guardar imagen
plt.savefig(
    "../imagenes_diagrama/comparacion_otros_paises.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Gráfico guardado correctamente")
