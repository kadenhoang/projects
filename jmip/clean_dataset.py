import pandas as pd

df = pd.read_csv("Uncleaned_DS_jobs.csv")
pd.options.display.max_columns= 16
print(df.info())
print(df.head(10))