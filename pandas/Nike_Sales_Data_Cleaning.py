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

#the Order_Date is 'str' type and has mixed format -> change it to datetime with matching format
df["Order_Date"] = pd.to_datetime(df["Order_Date"],dayfirst=True, errors = "coerce") #date has mixed format
#double check
print(df.info())
print(df.head(50))
print()

#Cleaning:

# - Size column:

#The products are shoes but there are clothing sizes in 'Size'
#check for all the sizes
print(df["Size"].unique())
#create a column to show all the rows that missing data
df["missing_size"] = df["Size"].isna().astype(bool)
#Since there is no numeric kids size, I decide to keep it as NaN
df.loc[df["Gender_Category"] == "Kids", "Size"] = None
#Remove sizes in letter
df["Size"] = pd.to_numeric(df["Size"], errors= "coerce") 
#fill the empty size of each group with median value of each group
df["Size"] = df.groupby("Gender_Category")["Size"].transform(
    lambda x: x.fillna(x.median())
)


#df["return_flag"] = (df["Units_Sold"] < 0).astype(int) #flag if a product is returned (negative)
#df["sale_flag"] = (df["Units_Sold"] > 0).astype(int) # flag if a product is sold
#df["unsold_flag"] = df["Units_Sold"].isna().astype(int)
#df["revenue"] = 
print(df["Size"].head(50))