# -*- coding: utf-8 -*-
"""Lista9_Regressao_Segunda.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w0X8i_cApGh1OzGIIDeIsjXEU3JmFoyC

# ESCOLA POLITÉCNICA DA UNIVERSIDADE DE SÃO PAULO

## PQI 3403 Análise de Processos da Indústria Química 2021

### Lista de Exercícios 9 - Regressão
"""

# Aluno: Ana Clara Duarte NUSP: 10884260;
# Aluno: Lucas Gobatto Bisaio NUSP: 10771006;

# Bibliotecas

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Modelos
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression

# Separação do conjunto de dados
from sklearn.model_selection import train_test_split

# Métricas
from sklearn.metrics import r2_score, mean_squared_error

"""#### Questão 1"""

# Dataset Questão 1

rng = np.random.RandomState(1)
X1 = np.sort(5 * rng.rand(80, 1), axis=0)
y1 = np.sin(X1).ravel()
y1[::5] += 3 * (0.5 - rng.rand(16))

# Gráfico do Dataset

plt.figure(figsize = (14,8))
plt.scatter(X1, y1, s=20, edgecolor="black", c="darkorange", label="data")
plt.xlabel("data")
plt.ylabel("target")
plt.title("Dados")
plt.legend()
plt.show()

# Divisão dos dados amostrais
X_train, X_test, y_train, y_test = train_test_split(X1, y1, test_size=0.2, random_state=0)

# Modelos de Regressão e Ajuste (fit)
#regressor = LinearRegression()
#regressor = DecisionTreeRegressor(max_depth=5)
regressor = KNeighborsRegressor(n_neighbors=2, weights='distance')
regressor.fit(X_train, y_train)

# Conjunto de teste - Valores de 0 a 5, com variação de 0.01

X1_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y1_test = np.sin(X1_test)

# Previsão do modelo de regressão
y_pred = regressor.predict(X1_test)

# Gráfico dos resultados
plt.figure(figsize=(20,10))
plt.scatter(X1, y1, s=20, edgecolor="black", c="darkorange", label="data")
plt.plot(X1_test, y_pred, color='red', linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Dados")
plt.show()

# Calculando o coeficiente de determinação R2 para o modelo
r2_score(y1_test, y_pred)