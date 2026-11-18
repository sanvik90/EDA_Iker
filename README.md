🎵 EDA Iker: la evolución de la música a través de los datos de Spotify

Análisis exploratorio de datos (EDA) sobre un dataset de ~15.000 hits con los indicadores de audio que calcula Spotify. El objetivo es estudiar cómo ha cambiado la música popular entre los años 70 y 2015 combinando ciencia de datos y estudios culturales: ¿suena hoy más fuerte? ¿es más enérgica? ¿más triste? ¿qué hace que una canción sea popular?

📌 Contexto

Spotify estima los atributos de cada canción mediante modelos computacionales de análisis de audio (ritmo, intensidad, tempo, estructura sonora, propiedades espectrales). No proceden de votaciones ni de valoraciones subjetivas de los usuarios. La mayoría se normalizan entre 0 y 1; en el notebook se multiplican por 100 para facilitar su lectura.

Variable	Rango habitual	Significado
Danceability	0 – 1	Facilidad para bailar
Energy	0 – 1	Intensidad y actividad
Loudness	-60 – 0 dB aprox.	Volumen percibido de la grabación
Speechiness	0 – 1	Presencia de palabras habladas
Acousticness	0 – 1	Probabilidad de que sea acústica
Instrumentalness	0 – 1	Probabilidad de que no tenga voces
Liveness	0 – 1	Probabilidad de que sea en directo
Valence	0 – 1	Positividad emocional percibida
Tempo	BPM	Velocidad de la canción
Duration	ms (convertida a minutos)	Duración
🗂️ Contenido del repositorio
EDA_Iker/
├── EDA_NOTEBOOK_LIMPIO.ipynb   # Notebook principal con todo el análisis
├── ClassicHit.csv              # Dataset original
└── README.md
🧹 Tratamiento de los datos
Filtro temporal: se eliminan las canciones fuera del periodo de estudio (el dataset original arranca en 1923). Quedan 10.104 registros y 21 variables, sin valores ausentes.
Yearcat: nueva variable categórica con los intervalos 1970-1979, 1980-1989, 1990-1999 y 2000-2015.
Genre2: agrupa Pop y Today en Pop/Today (Today empieza en 2002 y se interpreta como continuación del Pop), mantiene Metal aparte y junta el resto en Resto de géneros.
Genre3: aísla Country frente al resto, para su análisis específico.
Reescalado: los atributos de Spotify (0–1) pasan a escala 0–100 y Duration se convierte a minutos.
Estadísticos robustos: al haber outliers, se trabaja principalmente con medianas. El modo (binario) se resume con su media, que equivale a la proporción de canciones en modo mayor.
🔬 Hipótesis planteadas
	Hipótesis
H1	La tonalidad y el modo no afectan significativamente a los atributos musicales.
H2	El compás influye ligeramente en los atributos musicales.
H3	Ha aumentado el volumen percibido (loudness).
H4	Ha disminuido la positividad percibida (valence).
H5	Ha aumentado la energía (energy).
H6	Estos cambios son más intensos en el género Metal.
H7	Algunos géneros tienen evoluciones propias contextualizables socio-históricamente.
H8	Los factores que determinan la popularidad varían según el género.
📈 Principales resultados
Tonalidad y modo: apenas aportan información discriminativa. El compás 4/4 sí se asocia con valores más altos de valence, energy y danceability.
Volumen: pasa de poco más de −12 dB en 1970 a cerca de −6 dB en 2015. El salto se concentra entre 1990 y mediados de los 2000, y afecta incluso a las canciones más "suaves".
Positividad: descenso general a lo largo del periodo. La caída es especialmente marcada en el Metal.
Energía: crece en todos los grupos; el Metal supera de media los 90 puntos en el siglo XXI.
El caso del Country (1996–2010): valence mínimo en 2001 (~35) y máximo en 2005 (~75), un repunte que contrasta con la tendencia general y abre una línea de investigación sociohistórica (ciclo de la guerra de Irak). Los datos no permiten afirmar causalidad; haría falta contrastarlo con fuentes históricas y sociológicas.
Popularidad: las correlaciones (Spearman, p < 0,01) son débiles y cambian según el género. Por ejemplo, el valence se correlaciona positivamente con la popularidad en EDM, Metal y Punk, y negativamente en Rock alternativo y Gospel.
🛠️ Tecnologías
Python 3
pandas, numpy
matplotlib, seaborn
scipy (correlaciones de Pearson y Spearman)

