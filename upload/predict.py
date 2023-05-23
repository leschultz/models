from joblib import load
import pandas as pd

df = pd.read_csv('/mnt/test.csv').values
model = load('model.joblib')
y_pred = model.predict(df)
df = pd.DataFrame()
df['y_pred'] = y_pred
df.to_csv('/mnt/prediction.csv', index=False)
