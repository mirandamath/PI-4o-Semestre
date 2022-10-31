import math
from sklearn import linear_model
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np

import os

colunas = ['carat', 'depth', 'price']
dataFrame = pd.read_csv("csv/diamonds.csv", header = 0, usecols= colunas, index_col=False)

amostra = dataFrame.sample(frac=1)
treino = amostra[:math.floor(len(amostra)*0.80)]
teste = amostra[:math.floor(len(amostra)*0.20)]

reta = linear_model.LinearRegression()
reta.fit(treino[["carat", "depth"]], treino[["price"]])

predict = reta.predict(teste[["carat", "depth"]]);
r2= r2_score(predict, teste["price"])

print(r2)
