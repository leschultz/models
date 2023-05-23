from sklearn.linear_model import LinearRegression
from joblib import dump
import pandas as pd

df = pd.read_csv('train.csv')
y = df['y'].values
X = df.drop('y', axis=1).values
reg = LinearRegression().fit(X, y)
dump(reg, 'model.joblib')
