
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
import os
from scipy.stats import spearmanr
import Funciones as f
sns.set_theme(style="whitegrid")   # Fondo oscuro con cuadrícula

print("Empezando a crear gráficos")

#Cargar datos
df = pd.read_csv(r"C:\Users\Iker\Documents\Bootcamp\EDA_Iker_OK\EDA_Iker\ClassicHit.csv")
df = df[df["Year"] > 1970]
df = df[df["Year"] < 2015]

df["Yearcat"] = pd.cut(
    df["Year"],
    bins=[1969,1979, 1990, 1999, 2015],
    labels=["1970-1979", "1980-1990", "1991-2000", "2000-2015"]
)

df["Genre2"] = np.select(
    [
        df["Genre"] == "Metal",
        df["Genre"].isin(["Pop", "Today"]),        
    ],
    [
        "Metal",
        "Pop/Today",
    ],
    default="Resto de géneros"
)
df["Duration"] = (df["Duration"]/1000) /60


df["Valence"] = df["Valence"] *100
df["Energy"] = df["Energy"] *100
df["Danceability"] = df["Danceability"] *100
df["Speechiness"] = df["Speechiness"] *100
df["Acousticness"] = df["Acousticness"] *100
df["Instrumentalness"] = df["Instrumentalness"] *100
df["Liveness"] = df["Liveness"] *100



medianas1 = df.groupby("Genre")[["Valence","Energy","Danceability","Speechiness","Acousticness","Instrumentalness","Liveness","Popularity"]].median()
medianas2 = df.groupby("Key")[["Valence","Energy","Danceability","Speechiness","Acousticness","Instrumentalness","Liveness","Popularity"]].median()
medianas3 = df.groupby("Time_Signature")[["Valence","Energy","Danceability","Speechiness","Acousticness","Instrumentalness","Liveness","Popularity"]].median()
medianas4 = df.groupby("Genre")[["Mode"]].mean()

variablesmat = ["Year","Loudness","Valence","Energy","Acousticness","Danceability","Tempo","Instrumentalness","Speechiness","Popularity"]
corr = df[variablesmat].corr("spearman")

df["Genre3"] = np.select(
    [
        df["Genre"] == "Country"


    
    ],
    [
        "Country"
      

    ],
    default="Resto de géneros"
)



