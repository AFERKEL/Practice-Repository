#Import Python Libraries
import pandas as pd #data analysis library
import numpy as np #use for working with numeric/math functions

# Create a blank DataFrame named df_performances
df_performances = pd.DataFrame()

# Load data from the CSV file into the DataFrame
#csv_file = "./Performances_By_Venue_Zip.csv"
csv_file = "./FileNo3.csv"
df_performances = pd.read_csv(csv_file)

#print(df_performances)

#show the shape of the data
df_performances.info()
df_performances.shape
df_performances.columns
df_performances.head()
