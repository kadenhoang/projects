import pandas as pd

df = pd.read_csv("Nike_Sales_Uncleaned.csv")

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

pd.options.display.max_columns=14
df["Order_Date"] = pd.to_datetime(df["Order_Date"],dayfirst=True, errors = "coerce") #date has mixed format
#double check
print(df.info())
print(df.head())
print()

df["return_flag"] = (df["Units_Sold"] < 0).astype(int) #flag if a product is returned (negative)
df["sale_flag"] = (df["Units_Sold"] > 0).astype(int) # flag if a product is sold
df["unsold_flag"] = df["Units_Sold"].isna().astype(int)
#df["revenue"] = 
print(df.head(30))