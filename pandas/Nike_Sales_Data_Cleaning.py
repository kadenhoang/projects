import pandas as pd

df = pd.read_csv("Nike_Sales_Uncleaned.csv")

#inspect
print(df.head(10))
print()
print(df.info())
print()
print(df.describe())
print("\nNaN rows in each column")
print(df.isna().sum())
print("\nDuplicated rows")
print(df.duplicated().sum())

pd.options.display.max_columns=17

dfc = pd.DataFrame(df)

print("\nCleaning process begin: \n")
#Cleaning:

# - Order_Date Column

#the Order_Date is 'str' type and has mixed format -> change it to datetime with matching format
dfc["Order_Date"] = pd.to_datetime(dfc["Order_Date"],format="mixed", dayfirst=True, errors = "coerce") #date has mixed format
#double check
print("Change the format of the Order_Date column \n")
print(dfc.info())
print()

#################################################################################################

# - Size column:

#The products are shoes but there are clothing sizes in 'Size'
#check for all the sizes
print("sizes in the dataset:")
print(dfc["Size"].unique())
print()

#Since there is no numeric kids size, I decide to keep it as NaN
dfc.loc[dfc["Gender_Category"] == "Kids", "Size"] = None
#Remove sizes in letter
dfc["Size"] = pd.to_numeric(dfc["Size"], errors= "coerce") 
#fill the empty size of each group with median value of each group
dfc["Size"] = dfc.groupby("Gender_Category")["Size"].transform(
    lambda x: x.fillna(x.median())
)
#create a column to show all the rows that missing size
dfc["missing_size"] = dfc["Size"].isna().astype(int)

print("Dataset after cleaning size: \n")
print(dfc.head())
print()

#################################################################################################

# Unit_Sold - MRP - Revenue columns

#flag unsold product
dfc["unsold_flag"] = dfc["Units_Sold"].isna().astype(int)
#fill the NaN with 0
dfc["Units_Sold"] = dfc["Units_Sold"].fillna(0)


#check for how many rows that has sale but no MRP or Discount
print("Rows that has sale but no MRP or Discount:")
mask = dfc[(dfc["Units_Sold"] > 0) & (dfc["MRP"].isna() | dfc["Discount_Applied"].isna())]
print(mask)
print()


#change MRP and Discount_Applied
#fill the empty MRP of each group with median price base on the product line
dfc["MRP"] = dfc.groupby("Product_Line")["MRP"].transform(
    lambda x: x.fillna(x.median())
)
#fill the empty discount of each group with the median discount base on gender 
dfc["Discount_Applied"] = dfc.groupby("Gender_Category")["Discount_Applied"].transform(
    lambda x: x.fillna(x.median())
)
# re-calculate the Revenue
dfc["final_price"] = dfc["MRP"] * ( 1 - dfc["Discount_Applied"])
dfc["Revenue"] = dfc["final_price"] * dfc["Units_Sold"]

#create a column to show all the rows that missing data
dfc["missing_size"] = dfc["Size"].isna().astype(int)
print("Dataset after cleaning MRP, Discount and Revenue:")
print(dfc.head())
print()

#################################################################################################

# Profit column

# no sale but has negative profit
print("\nrows that has no sale but negative profit:")
mask = (dfc["Profit"] < 0) & (dfc["Units_Sold"] == 0)
print(mask.sum())
print()
print("Add Sale Lost Flag column to show the rows that has no sale but negative profit:" )
dfc["Salelost_flag"] = ((dfc["Profit"] < 0) & (dfc["Units_Sold"] == 0)).astype(int)
print(dfc.head())