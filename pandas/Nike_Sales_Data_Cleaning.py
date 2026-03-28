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

pd.options.display.max_columns=17


dfc = pd.DataFrame(df)
#Cleaning:

# - Order_Date Column

#the Order_Date is 'str' type and has mixed format -> change it to datetime with matching format
dfc["Order_Date"] = pd.to_datetime(dfc["Order_Date"],dayfirst=True, errors = "coerce") #date has mixed format
#double check
print(dfc.info())

print()


# - Size column:

#The products are shoes but there are clothing sizes in 'Size'
#check for all the sizes
print(dfc["Size"].unique())
#create a column to show all the rows that missing data
dfc["missing_size"] = dfc["Size"].isna().astype(int)
#Since there is no numeric kids size, I decide to keep it as NaN
dfc.loc[dfc["Gender_Category"] == "Kids", "Size"] = None
#Remove sizes in letter
dfc["Size"] = pd.to_numeric(dfc["Size"], errors= "coerce") 
#fill the empty size of each group with median value of each group
dfc["Size"] = dfc.groupby("Gender_Category")["Size"].transform(
    lambda x: x.fillna(x.median())
)


#df["return_flag"] = (df["Units_Sold"] < 0).astype(int) #flag if a product is returned (negative)
#df["sale_flag"] = (df["Units_Sold"] > 0).astype(int) # flag if a product is sold


# - Unit_Sold - MRP - Revenue

#flag unsold product
dfc["unsold_flag"] = dfc["Units_Sold"].isna().astype(int)
#fill the NaN with 0
dfc["Units_Sold"] = dfc["Units_Sold"].fillna(0)


#check for how many rows that has sale but no MRP or Discount
mask = dfc[(dfc["Units_Sold"] > 0) & (dfc["MRP"].isna() | dfc["Discount_Applied"].isna())]
print(mask)


#change MRP and Discount_Applied
dfc["MRP"] = dfc.groupby("Product_Line")["MRP"].transform(
    lambda x: x.fillna(x.median())
)
dfc["Discount_Applied"] = dfc.groupby("Gender_Category")["Discount_Applied"].transform(
    lambda x: x.fillna(x.median())
)
#calculate the Revenue
dfc["final_price"] = dfc["MRP"] * ( 1 - dfc["Discount_Applied"])
dfc["Revenue"] = dfc["final_price"] * dfc["Units_Sold"]

print(dfc.head(30))