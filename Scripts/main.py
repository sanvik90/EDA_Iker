
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
import os
from scipy.stats import spearmanr
import Funciones as f
import variables  as v
from matplotlib.animation import FuncAnimation, PillowWriter




print("Comienza progrma")
df = v.df
print("Datos Cargados")



#Historgramas solos
f.cajsol(df,"Loudness")
f.cajsol(df,"Energy")
f.cajsol(df, "Valence")
f.cajsol(df,"Danceability")
print("Graficos monovariable creados")


#Medianas y medias.


f.medianas(v.medianas1,"medianas_genero","Medianas de los principales atiributos por género")
f.medianas(v.medianas2,"medianas_clave","Medianas de los principales atiributos por clave")
f.medianas(v.medianas3,"medianas_timesig","Medianas de los principales atiributos por compás")
f.mediasmodo(v.medianas4)

#Matiz correlaciones

f.matcorr(v.corr)

print("Heatmaps creados")

#Gráficos de linea
f.graflin(df,"Loudness","Evolución del volumen percivido a lo largo del tiempo")
f.graflin(df,"Valence","Evolución la postividad  a lo largo del tiempo")
f.graflin(df,"Energy","Evolución de la energía a lo largo del tiempo")
f.graflin(df,"Acousticness","Evolución d la acusticidad lo largo del tiempo")
f.graflin(df,"Danceability","Evolución de la bailabilidad  a lo largo del tiempo")
f.graflin(df,"Instrumentalness","Evolución la instrumentalidad largo del tiempo")
f.graflin(df,"Speechiness","Evolución de la verbalidad a lo largo del tiempo")
f.graflin2(df)
print("gráficos de linea creados")

# Gráficos de caja
f.cajatemp(df, "Loudness" ,"Evolución de la distribucion del volumen percicivdo")
f.cajatemp(df, "Valence", "Evolución de la distribucion la positividad")
f.cajatemp(df, "Energy", "Evolución de la distribucion la energía")
f.cajatemp(df, "Acousticness", "Evolución de la distribucion la acusticidad")
f.cajatemp(df, "Instrumentalness", "Evolución de la distribucion la instrumentalida")
f.cajatemp(df, "Speechiness", "Evolución de la distribucion la Verbalidad")
print("gráficos de caja creados")


#Gráficos de Denidad

f.densi(df,"Loudness","Evolución de la densidad del Loudness a lo largo de los años")
f.densi(df,"Valence","Evolución de la densidad del Valence a lo largo de los años")
f.densi(df,"Energy","Evolución de la densidad del Energy a lo largo de los años")
f.densi(df,"Acousticness","Evolución de la densidad del Acousticness a lo largo de los años")
f.densi(df,"Danceability","Evolución de la densidad del Danceability a lo largo de los años")
f.densi(df,"Speechiness","Evolución de la densidad del Speechiness a lo largo de los años")
f.densi(df,"Instrumentalness","Evolución de la densidad del Instrumentalness a lo largo de los años")
f.densi(df,"Popularity","Evolución de la densidad del Popularidad según el año")

print("gráficos de densidad creados")

#Popularidad y género

f.popugen(df,"Year")
f.popugen(df,"Loudness")
f.popugen(df,"Valence")
f.popugen(df,"Energy")
f.popugen(df,"Acousticness")
f.popugen(df,"Danceability")
f.popugen(df,"Speechiness")
f.popugen(df,"Instrumentalness")
f.popugen(df,"Tempo")
f.popugen(df,"Mode")



f.densi_gif(df,"Valence")
f.densi_gif(df,"Loudness")
f.densi_gif(df,"Energy")


print("Gráficos creados ^_^ ")
