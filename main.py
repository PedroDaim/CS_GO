#Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_players = pd.read_csv('player_stats.csv')

#Display the first few rows of the dataframe
print("First Few Rows Of the Dataframe.")
print(df_players.head())
print("\n" + "="*50 + "\n")

#Display the total rows and columns of the dataframe
print("Rows and Columns Total.")
print(df_players.shape)   
print("\n" + "="*50 + "\n")

#Display the columns of the dataframe
print("Columns of the Dataframe.")  
print(df_players.columns)
print("\n" + "="*50 + "\n")




