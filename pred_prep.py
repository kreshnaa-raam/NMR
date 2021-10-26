import pandas as pd


preds = pd.read_csv("11Oct/result.csv")

preds.head()

preds2 = preds[['id','target_PREDICTION']]

preds2 = preds2.rename({"id": "id", "target_PREDICTION": "prediction"}, axis='columns')
preds2.to_csv("results_p.csv",index = False)