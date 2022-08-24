"""
    metric.py: Implementar las funciones de métrica y evaluación
"""
from sklearn.metrics import r2_score, mean_squared_error, mean_squared_log_error, mean_absolute_percentage_error, mean_absolute_error
from math import sqrt

def met_r2(y_real, y_preds):
    """Coeficiente de Determinación r2"""
    return r2_score(y_real, y_preds)

def met_mse(y_real, y_preds):
    """Error cuadrático medio"""
    return mean_squared_error(y_real, y_preds)

def met_rmse(y_real, y_preds):
    """Raíz del error cuadrático medio"""
    return sqrt(mean_squared_error(y_real, y_preds))

def met_mae(y_real, y_preds):
    """Error medio absoluto"""
    return mean_absolute_error(y_real, y_preds)

def met_msle(y_real, y_preds):
    """Error logarítmico cuadrático medio"""
    return mean_squared_log_error(y_real, y_preds)

def met_mape(y_real, y_preds):
    """Error absoluto medio porcentual"""
    return mean_absolute_percentage_error(y_real, y_preds)