import pandas as pd
import numpy as np
order = pd.read_table("http://bit.ly/chiporders")
order.head()

#looking at an example of a data frame with no specific separator
#we have to tell pandas the separator used in the dataframe

movie_user = pd.read_table("http://bit.ly/movieusers")
movie_user.head()

movie_user = pd.read_table("http://bit.ly/movieusers", sep ="|")
movie_user.head()

#notice the header of the columns are not what it should be
#hence we tell pandas this as well
column_names = ["user_id", "gender", "occupation","zip_code"]
movie_user = pd.read_table("http://bit.ly/movieusers", sep="|", header = None, names=column_names)
movie_user.head()
print(movie_user)


ufo = pd.read_table("http://bit.ly/uforeports", sep=",")
ufo.head()

ufo= pd.read_csv("http://bit.ly/uforeports")
ufo

#the following code is to ensure the dataframe is completely displayed
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 15000)
ufo
pd.set_option('display.notebook_repr_html', True)
ufo
ufo["City"]
#or you can write line above as ufo.City
ufo.City
pd.set_option("display.width", 15000)
movies = pd.read_csv("http://bit.ly/imdbratings")
movies
movies.describe()
movies.columns
#to replace all or some of the columns in a data frame.
#you can use a dictionary to specify changes to one or more column names using key would be the old column name while value will be the new column name
#you can create a new list variable to replace the total columns
movies.rename(columns={"duration": "length"}, inplace=True)
movies.columns

#renaming the columns for the ufo dataset
ufo.columns
ufo_cols = ["city", "colors", "shape", "state", "time"]
ufo.columns = ufo_cols
ufo.head()

#you can also replace specific characters in a column
ufo=pd.read_csv("http://bit.ly/uforeports")
ufo.columns
#here, we are replacing the space with _
ufo.columns = ufo.columns.str.replace(" ","_")
ufo.columns
#checking if there is a keyword in a particular column
ufo.columns
ufo.City
ufo.City.str.contains("nigeria")

#While cleaning data, you might need to remove(drop) some columns or rows
movie_user
movie_user.shape #just to check the number of rows and columns
movie_user.drop("zip_code", axis=1)
#you have to specify the axis if it is abou the column
#also, it would not reflect on the real dataframe until inplace is true
movie_user.drop("gender", axis=1, inplace=True)
movie_user
movie_user.shape

movies
movies.columns
movies.drop(["title","actors_list"], axis=1, inplace=True)
movies.head()
movies.drop([0,1,3,5], axis= 0, inplace =True)
movies.head()
movies.shape
#sorting the movies according to length
movies.length.sort_values()
#could also be written as 
movies["length"].sort_values()
#pandas automatically sort in ascending order, to do the reverse, specify
movies.length.sort_values(ascending = False) #this wont affect the original dataframe as usual because inplace was not set
movies.sort_values(["length"], ascending =True, inplace=True)
movies.columns
movies.head()
movies.iloc[0,2]# for row 0 in column 2
movies.iloc[:, 0:2]# all rows from column 0 till 2
movies.head
movies.loc[movies["genre"]=="Drama"]
# all rows from column 0 till 2// 
# the last part is the condition to parse//

booleans =[]
for length in movies.length:
    if length >= 195:
        booleans.append(True)
    else:
         booleans.append(False)

#we could also do
boolea = movies.length >= 195
boolea.head
()

booleans[1:7]
movie_length = pd.Series(booleans)#creating a new dataframe series
movie_length.head()
movie_length
movies["movie_length"] = movie_length
movies

#using just 2 columns when reading in a dataframe
orders = pd.read_table("http://bit.ly/chiporders", usecols=["item_name", "quantity"])
orders.head()

#you can also read in cols using the index numbers
chiporder = pd.read_table("http://bit.ly/chiporders", usecols=[2,4])

chiporder.head()