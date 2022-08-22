import pandas as pd

DATA = "RESULTADO_2019_2020.csv"
COLUMN_NAMES = ["FECHA","LOTE","UNIDAD","TIPO","MARCA","MODELO","ANHO","TRACC","COMB","GTIA. MEC","MAG","KILOMETRAJE","ADJUDIC."]


def load_result(data='RESULTADO_2019_2020.csv'):
    """Va a buscar los resultados entre 2019 y 2020 de las adjudicaciones de vehículos en remates de la compania. Retorna "X / input" o variables dependientes (características del vehículo) e "y / output" correspondiente al precio de venta.'."""
    print("Datos cargados con éxito")
    df = pd.read_csv(data, sep=';', encoding='latin')
    X, y = df.iloc[:, 0:12], df.iloc[:, [12]]
    y = y.replace({"PRECIO_VENTA"}).squeeze()
    return {"dataset": (X, y)}