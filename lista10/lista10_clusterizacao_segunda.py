# -*- coding: utf-8 -*-
"""Lista10_Clusterizacao_Segunda.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QohAeEQ9t2Z45stV-zdAwWovumq4SDa7

# ESCOLA POLITÉCNICA DA UNIVERSIDADE DE SÃO PAULO

## PQI 3403 Análise de Processos da Indústria Química 2021

### Lista de Exercícios 10 - Clusterização - Segunda
"""

# Aluno: Ana Clara Duarte NUSP: 10884260
# Aluno: Lucas Gobatto Bisaio NUSP: 1077006

# Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# Biblioteca para construção do Dendograma
from sklearn.cluster import AgglomerativeClustering, KMeans
import scipy.cluster.hierarchy as sch

# Modelos

""" Questão 1"""

# Abrir o arquivo excel que contém os dados a serem utilizados
uploaded = pd.read_excel('iris.xlsx')
df = uploaded.drop(['especie'], axis=1)
# Variáveis de treino

clustering = AgglomerativeClustering(n_clusters=2)
clustering_class = clustering.fit_predict(df)


# Construção do Dendograma

plt.figure(figsize=(7, 5))
dend = sch.dendrogram(sch.linkage(df, method='ward'))
plt.show()

k = 2
HClustering = AgglomerativeClustering(
    n_clusters=k, affinity="euclidean", linkage="ward")

""" Questão 2"""

# Método Elbow
model = KMeans(n_clusters=5)
model.fit(df)
centers = model.cluster_centers_
labels = model.labels_
sse = []
X = [i for i in range(1, 10)]
for K in X:
    model = KMeans(n_clusters=K)
    model.fit(df)
    sse.append(model.inertia_)

plt.plot(X, sse, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('Metodo do Cotovelo para o diferentes k')
plt.show()
