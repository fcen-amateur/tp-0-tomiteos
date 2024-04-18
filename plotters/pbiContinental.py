import seaborn.objects as so
from gapminder import gapminder
import numpy as np

gdpmean = gapminder.groupby(["year","continent"])["gdpPercap"]
gdpmean = gdpmean.agg(np.mean)
gdpmean = gdpmean.reset_index()

def plot():
    figura = (
        (
            so.Plot(gdpmean, x="year",y="gdpPercap",color="continent") 
            .add(so.Line())
            .label(title="Pbi per capita por continente a lo largo del tiempo",x="Año",y="Pbi Per Capita",color="continente")
        )
    )
    return dict(
        descripcion="Pbi per capita continental lo largo del tiempo",
        autor="Tomas Mateos",
        figura=figura,
    )
