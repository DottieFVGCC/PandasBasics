#Based on parts of tutorials: using Pandas and Python to explore your dataset
#https://realpython.com/pandas-python-explore-dataset/
#And Getting Started with Pandas Sort Methods
#https://realpython.com/pandas-sort-python/#getting-started-with-pandas-sort-methods

#before running this main.py file, run the get...Data.py file to populate the dataset
#HINT: you can change which file runs when the Run button is clicked - edit the .replit file

import pandas as pd  #convention is to use pd as alias for pandas 

# Read data from csv into a variable; the result is a Dataframe
#df = pd.read_csv("nba_all_elo.csv")  #NBA data

df = pd.read_csv("chicago_vac_by_zip.csv")  #Chicago vaccination data

print(type(df))  #display the type of the df variable - it is a DataFrame!
print(len(df))  #number of records in the dataset
print(df.shape)  #Dimensionality: rows and columns

pd.set_option("display.max.columns", None)  #show all columns
pd.set_option("display.precision", 2)  #decimal places

#head() and tail() functions get rows from the beginning and end of the dataset; they default
# to 5 rows but can take a parameter for number of rows wanted
print(df.head()) #the first 5 rows
#print(df.head(10)) #the first 10 rows
print(df.tail()) #the last 5 rows

print("Dataframe Info:")
print(df.info()) #describes the columns

print("Dataframe Describe")
print(df.describe()) #some basic statistics

print("Dataframe Describe: Include Objects")
print(df.describe(include=object)) #some basic statistics for objects

dfSorted= df.sort_values("Total Doses - Daily")
print(dfSorted.head())

#convert the dataframe to HTML and save to a file
# in a future phase of this development we may create a Flask Web site and write to a template within the project
html_table = dfSorted.to_html()
html_file = open("index.html", "w")
html_file.write(html_table)
html_file.close()




