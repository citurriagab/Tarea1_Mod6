import pandas as pd

DATA_SOURCE = "RESULTADO_POR_LOTE.csv"
COLUMN_NAMES = ["FECHA","LOTE","UNIDAD","PLACA","TIPO","MARCA","MODELO","ANHO","TRACC","COMB","GTIA. MEC","MAG","KILOMETRAJE","ADJUDIC."]



def load_result(data=DATA_SOURCE):
    """Descarga desde el repositorio UCI el dataset iris y retorna un diccionario con el 'dataset', una tupla que
    contiene X (input) e y (output), además de las 'etiquetas'."""
    print("Datos cargados con éxito")
    df = pd.read_csv(data, names=COLUMN_NAMES, header=None)
    X, y = df.iloc[:, 0:14], df.iloc[:, [14]]
    y = y.replace({"PRECIO_VENTA"}).squeeze()
    return {"dataset": (X, y)}
