## Análisis del impacto nacional e internacional de *La Casa de Papel*

##  Descripción del proyecto

Este proyecto analiza el impacto nacional e internacional de la serie española **La Casa de Papel** utilizando datos procedentes de plataformas como Netflix, IMDb y Kaggle.

El objetivo principal es estudiar cómo esta producción española consiguió convertirse en un fenómeno global y evaluar si su éxito influyó en la visibilidad y valoración posterior de otras series españolas dentro del mercado internacional del streaming.

El análisis se desarrolla mediante técnicas de limpieza de datos, análisis exploratorio (EDA) y visualización de información utilizando Python y herramientas de ciencia de datos.

---

#  Objetivos

## Objetivo principal

Analizar el impacto internacional de *La Casa de Papel* dentro del catálogo de Netflix y estudiar su relevancia en comparación con otras producciones españolas.

## Objetivos específicos

- Comparar el rendimiento de la serie con otras series españolas.
- Analizar su alcance internacional.
- Evaluar su reconocimiento en IMDb.
- Estudiar si el éxito de la serie incrementó la visibilidad de producciones españolas posteriores.

---

# 🧠 Hipótesis

Se estudiará si La Casa de Papel logró:

Convertirse en la serie española más vista en distintos países.

Mantenerse durante más tiempo dentro del Top 10 global de Netflix respecto a otras producciones españolas.

Mejor serie española valorada en IMDb.

Alcanzar posiciones destacadas dentro de los rankings internacionales de contenido no angloparlante.

Competir con producciones internacionales de gran relevancia dentro de la plataforma.

Alcanzó posiciones destacadas dentro de rankings internacionales en IMDb.

El éxito internacional de La Casa de Papel favoreció un aumento de la valoración global de las producciones españolas a partir de 2017.

Influir con en su impacto en el incremento de producciones españolas dentro de la plataforma Netflix.

---

# Fuentes de datos

Los datos utilizados proceden de distintas fuentes:

## Netflix
Información relacionada con títulos disponibles en la plataforma.

## IMDb
Valoraciones, puntuaciones y métricas de popularidad.

## Kaggle
Datasets públicos relacionados con catálogos de streaming y métricas audiovisuales.

---

#  Metodología

El proyecto sigue las siguientes fases:

##  Obtención y carga de datos

- Importación de datasets CSV.
- Revisión inicial de estructuras y tipos de datos.

## Limpieza y preparación

Procesos realizados:

- Eliminación de valores nulos.
- Conversión de formatos.
- Normalización de variables.
- Filtrado de registros relevantes.

## Integración de datasets

- Unión de información procedente de diferentes fuentes.
- Homogeneización de variables.

## Análisis exploratorio de datos (EDA)

Aspectos analizados:

- Distribución de  series.
- Evolución temporal de producciones.
- Valoraciones IMDb.
- Comparación entre producciones españolas e internacionales.

## Visualización de resultados

Se utilizan gráficos para representar:

- Rankings.
- Evolución temporal.
- Comparativas de puntuaciones.
- Popularidad.

---

# Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Squarify

---

# Estructura del proyecto

```bash
Eda_la_casa_de_papel/
│
├── Código/
│   ├── código/
│   │   └── codigo.py
│   │
│   ├── data/
│   │   ├── most-popular_country_weekly.tsv
│   │   ├── most-popular_global_weekly.tsv
│   │   ├── series_espanolas_netflix_global.csv
│   │   ├── title.basics.tsv
│   │   ├── title.ratings.tsv
│   │   └── titles.csv
│   │
│   ├── imagenes_diagrama/
│         
│
├── imagenes/
│
├── memoria.ipynb
├── Presentacion.ipynb
└── README.md