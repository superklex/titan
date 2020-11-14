
import pandas as pd
import numpy as np

#dropping non-numeric columns from a dataframe
drinks = pd.read_csv("http://bit.ly/drinksbycountry")
drinks.head()
drinks.select_dtypes(include=[np.number]).dtypes
drinks.head()
drinks.drop("continent", axis = 1).head()
drinks.drop("continent", axis = 1)
drinks.head()
drinks["cap_count"] = drinks.country.str.upper()
drinks.cap_count
drinks.columns
drinks.drop("cap_count", axis =1, inplace = True)
drinks.columns
yes = drinks.country.str.contains("Nigeria","nigeria")
drinks[yes]

order = pd.read_table("http://bit.ly/chiporders")
order.head()
order.columns
order["item_price"] = order.item_price.str.replace("$", "")
order["item_price"] = order["item_price"].astype(float)

