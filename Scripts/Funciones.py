import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
import os
from scipy.stats import spearmanr
from matplotlib.animation import FuncAnimation, PillowWriter

#### Histogramas solos


def cajsol(df,x):
    plt.figure(figsize=(6, 1))
    sns.boxplot(data=df, x=x, fill=False)
    ruta = os.path.join("EDA_Iker", "Gráficas", f"cajasol{x}.png")
    plt.savefig(ruta, dpi=300, bbox_inches="tight")    

    return

def medianas(medianas,nombre,titulo):
    plt.figure(figsize=(13, 6))  # (ancho, alto) en pulgadas
    sns.heatmap(
        medianas,
        annot=True,
        cmap= "rocket_r",
        fmt='.2f',
        linewidths=0,
        vmin= 0,
        vmax=100,
        center=50
)
    plt.title(titulo)
    plt.tight_layout()
    ruta = os.path.join("EDA_Iker", "Gráficas", f"medianas_{nombre}.png")
    plt.savefig(ruta, dpi=300, bbox_inches="tight")  

    return 


def mediasmodo(medianas):
    plt.figure(figsize=(13, 6))  # (ancho, alto) en pulgadas
    sns.heatmap(
        medianas,
        annot=True,
        cmap= "rocket_r",
        fmt='.2f',
        linewidths=0,
        vmin= 0,
        vmax=1,
        center=0.5
)
    plt.title("Medias de modo según género")
    plt.tight_layout()
    ruta = os.path.join("EDA_Iker", "Gráficas", f"medias_modo.png")
    plt.savefig(ruta, dpi=300, bbox_inches="tight")  

    return 

def matcorr(corr):
    

    plt.figure(figsize=(12, 5))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        center=0,
        vmin =-1
    )

    plt.title("Matriz de correlaciones (Spearman) - Principales variables numéricas")
    plt.tight_layout()
    ruta = os.path.join("EDA_Iker", "Gráficas", "Matrizcorr.png")
    plt.savefig(ruta, dpi=300, bbox_inches="tight")
    return 

def graflin(df,y,titulo):
    plt.figure(figsize=(12,5))
    sns.lineplot(data = df, x = "Year" , y = y , hue = "Genre2", palette = "colorblind", estimator="mean", errorbar=("ci", 90))
    plt.title(titulo)
    plt.tight_layout()
    ruta = os.path.join("EDA_Iker", "Gráficas", f"Lin_{y}.png")
    plt.savefig(ruta, dpi=300, bbox_inches="tight")
    return


def graflin2(df):
    plt.figure(figsize=(12,5))

    sns.lineplot(
        data=df,
        x="Year",
        y="Valence",
        hue="Genre3",
        palette="colorblind",
        estimator="mean",
        errorbar=("ci", 90)
    )

    plt.xlim(1996, 2010)

    plt.title(
        "Evolución de Valence a lo largo de los años. "
        "Ciclo de guerra de Irak: Country vs resto de géneros"
    )

    plt.axvline(x=2001, color="red", linestyle="--", linewidth=0.5)
    plt.axhline(y=35, color="black", linestyle="--", linewidth=0.6)
    plt.axhline(y=76, color="black", linestyle="--", linewidth=0.6)

    plt.tight_layout()

    ruta = os.path.join("EDA_Iker", "Gráficas", "Grafilin_country.png")
    plt.savefig(ruta, dpi=300, bbox_inches="tight")



def cajatemp(df, x,titulo):
    plt.figure(figsize=(9,3))

    sns.boxplot(data = df, x = x, y= "Genre2" , fill = True   ,hue = "Yearcat",showmeans=True,  meanprops={
            "marker": "o",
            "markerfacecolor": "black",
            "markeredgecolor": "black",
            "markersize": 7,
            "alpha": 0.6
        }
    )
    plt.title(titulo)
    plt.legend(
        title="Rango temporal",
        bbox_to_anchor=(1.02, 1),
        loc="upper left",
        borderaxespad=0
        )
    ruta = os.path.join("EDA_Iker", "Gráficas", f"Cajat_{x}.png")
    plt.savefig(ruta, dpi=300, bbox_inches="tight")
    return


def densi(df,x,titulo):
    #plt.style.use("dark_background")

    plt.figure(figsize=(9,3))

    sns.kdeplot(data= df,x = x, hue="Year", palette=  "viridis", legend=False, common_norm=False,alpha = 0.6)
    plt.title(titulo)
    ruta = os.path.join("EDA_Iker", "Gráficas", f"densi_{x}.png")
    plt.savefig(ruta, dpi=300, bbox_inches="tight")
    return
    


def popugen(df, x):

    resultados = []

    for genero, subset in df.groupby("Genre"):
        r, p = spearmanr(subset[x], subset["Popularity"])

        if p < 0.01:
            resultados.append((genero, r, p))

    corr_df = pd.DataFrame(resultados, columns=["Género", "R", "p-value"])
    corr_df = corr_df.sort_values("R", ascending=False)

    plt.figure(figsize=(15, 8))

    sns.barplot(
        data=corr_df,
        x="R",
        y="Género",
        hue="R",
        palette="RdYlGn",
        hue_norm=(-1, 1),
        dodge=False,
        legend=False
    )

    plt.axvline(0, color="black", linewidth=0.8)
    plt.xlim(-1, 1)
    plt.title(f"Correlación entre  popularidad y {x}  por género (p < 0.01)")
    plt.tight_layout()
    plt.xlabel("Correlación Spearman")
    plt.savefig(f"EDA_Iker/Gráficas/Popugen_{x}.png")
    return


def densi_gif(df, x):

    years = sorted(df["Year"].dropna().unique())

    # Un color por año
    palette = sns.color_palette("viridis", n_colors=len(years))
    colors = dict(zip(years, palette))

    # Límites globales del eje X
    xmin = df[x].min()
    xmax = df[x].max()

    # Calcular el límite máximo de densidad entre todos los años
    ymax = 0

    for year in years:
        data_year = df[df["Year"] == year]

        kde = sns.kdeplot(
            data=data_year,
            x=x
        )

        ymax = max(ymax, kde.get_lines()[-1].get_ydata().max())

        plt.close()

    fig, ax = plt.subplots(figsize=(9, 3))

    def update(year):
        ax.clear()

        data_year = df[df["Year"] == year]

        sns.kdeplot(
            data=data_year,
            x=x,
            color=colors[year],
            fill=False,
            ax=ax
        )

        ax.set_title(f"{x} | Year: {year}")
        ax.set_xlabel(x)
        ax.set_ylabel("Density")

        # Escalas X e Y constantes
        ax.set_xlim(xmin, xmax)
        ax.set_ylim(0, ymax * 1.05)

    anim = FuncAnimation(
        fig,
        update,
        frames=years,
        repeat=True,
        interval=800
    )

    ruta = os.path.join("EDA_Iker", "Gráficas", f"densi_{x}.gif")

    anim.save(
        ruta,
        writer=PillowWriter(fps=3),
        dpi=150
    )

    plt.close(fig)

    return