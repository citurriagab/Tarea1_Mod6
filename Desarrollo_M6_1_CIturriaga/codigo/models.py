"""
    model.py: modulo donde se especifica el modelo
"""
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

def reg_lineal(X, y):
    reg = LinearRegression()
    return reg.fit(X, y)

def reg_KNN(X, y, num_vecinos=5):
    reg = KNeighborsRegressor(n_neighbors=num_vecinos)
    return reg.fit(X, y)