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
movies.rows

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