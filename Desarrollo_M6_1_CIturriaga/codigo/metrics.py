"""
    metric.py: Implementar las funciones de métricas de evaluación del modelo
"""
##from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.metrics import r2_score, mean_squared_error, mean_squared_log_error, mean_absolute_percentage_error, mean_absolute_error
from math import sqrt

## rms = sqrt(mean_squared_error(y_actual, y_predicted))

def metrica_r2(y_true, y_pred):
    """Métrica de clasificación R squared"""
    return r2_score(y_true, y_pred)
######

def metrica_f1score(y_verdad, y_preds, avg='micro'):
    """Métrica de clasificación F1-score"""
    return f1_score(y_verdad, y_preds, average=avg)


def matriz_confusion(y_verdad, y_preds):
    """Obtener matriz de confusion"""
    return confusion_matrix(y_verdad, y_preds)