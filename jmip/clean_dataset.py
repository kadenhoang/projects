import pandas as pd

df = pd.read_csv("data/Uncleaned_DS_jobs.csv")
pd.options.display.max_columns= 16
pd.set_option("display.expand_frame_repr", False)
pd.set_option("display.width", 200)
#inspect
print(df.head())
print()
print(df.info())
print()
print(df.describe())
print()
print(df.isna().sum())
print()
print(df.duplicated().sum())

#drop the unecessary columns
df_cleaned = df.drop(["index", "Headquarters", "Founded", "Type of ownership", "Sector", "Revenue", "Competitors", "Size"], axis=1)

#clean the unecessary letters
df_cleaned["Company Name"] = df_cleaned["Company Name"].str.replace(r'[^a-zA-Z]','',regex=True)

#inspect
print(df_cleaned.head())
print()
print(df_cleaned.info())

df_cleaned.to_csv("data/Cleaned_DS_jobs.csv",index=False)
print("Dataset cleaned and exported")

