
## https://raw.githubusercontent.com/citurriagab/Data_Hist_Resultados/main/RESULTADO_2019_2020.csv

"""
    dataset.py: modulo donde se especifica la descarga de la base de datos
"""
import pandas as pd

DATA_SOURCE = "https://raw.githubusercontent.com/citurriagab/Data_Hist_Resultados/main/RESULTADO_2019_2020.csv"
LOCAL_PATH = "./data/resultados"

def load_result(URL=DATA_SOURCE):
    """Va a buscar los resultados entre 2019 y 2020 de las adjudicaciones de vehículos en remates de la compania. Retorna "X / input" o variables dependientes (características del vehículo) e "y / output" correspondiente al precio de venta.'."""
    print("Datos cargados con éxito")
    df = pd.read_csv(URL, sep=';', encoding='latin')
    X, y = df.iloc[:, 0:12], df.iloc[:, [12]]
    y = y.replace({"PRECIO_VENTA"}).squeeze()
    return {"dataset": (X, y)}

def load_result_local(PATH=LOCAL_PATH):
    """Cargar el dataset desde una ruta en disco local. Específicamente un archivo guardado en la carpeta ./data"""
    print("Datos cargados con éxito")
    return pd.read_csv(PATH, sep=';', encoding='latin')