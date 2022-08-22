{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "DATA_SOURCE = \"https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data\"\n",
    "LOCAL_PATH = \"./data/iris.data\"\n",
    "COLUMN_NAMES = [\"sepal_length\", \"sepal_width\", \"petal_length\", \"petal_width\", \"species\"]\n",
    "\n",
    "\n",
    "def load_iris_web(URL=DATA_SOURCE):\n",
    "    \"\"\"Descarga desde el repositorio UCI el dataset iris y retorna un diccionario con el 'dataset', una tupla que\n",
    "    contiene X (input) e y (output), además de las 'etiquetas'.\"\"\"\n",
    "    print(\"Datos cargados con éxito\")\n",
    "    df = pd.read_csv(URL, names=COLUMN_NAMES, header=None)\n",
    "    X, y = df.iloc[:, 0:4], df.iloc[:, [4]]\n",
    "    labels = {key: id for key, id in zip(y.species.unique(), [x for x in range(3)])}\n",
    "    y = y.replace({\"species\": labels}).squeeze()\n",
    "    return {\"dataset\": (X, y),\n",
    "            \"labels\": labels}\n",
    "\n",
    "\n",
    "def load_iris_local(PATH=LOCAL_PATH):\n",
    "    \"\"\"Cargar el dataset desde una ruta en disco local. Específicamente un archivo guardado en la carpeta ./data\"\"\"\n",
    "    print(\"Datos cargados con éxito\")\n",
    "    return pd.read_csv(PATH, names=COLUMN_NAMES, header=None)"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
