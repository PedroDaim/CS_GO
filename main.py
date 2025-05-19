#Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Import players and teams data and tranform the CSV files into pandas dataframes
df_players = pd.read_csv('player_stats.csv')
df_teams = pd.read_csv('team_stats.csv')

#Display the first few rows of the dataframe df_players
print("First Few Rows Of the Dataframe.")
print(df_players.head())
print("\n" + "="*50 + "\n")

#Display the total rows and columns of the dataframe df_players
print("Rows and Columns Total.")
print(df_players.shape)   
print("\n" + "="*50 + "\n")

#Display the columns of the dataframe df_players
print("Columns of the Dataframe.")  
print(df_players.columns)
print("\n" + "="*50 + "\n")

#Display data types, null counts, memory usage.
print("Data Types, Null Counts, Memory Usage.")
print(df_players.info)   
print("\n" + "="*50 + "\n")


#Display descriptive statistics of the dataframe df_players
print("Descriptive Statistics of the Dataframe.")       
print(df_players.describe())
print("\n" + "="*50 + "\n")

#Check for missing values in the dataframe df_players
print("Missing Values in the Dataframe.")   
print(df_players.isnull().sum())
print("\n" + "="*50 + "\n")

# Get the top 10 players by rating
top10_rated_players = df_players.sort_values(by='rating', ascending=False).head(10)

# Display the top 10 players by rating
print("Top 10 Players by Rating.")
print(top10_rated_players[['name', 'country', 'rating']])
print("\n" + "="*50 + "\n")

# Get the top 10 players by KD Ratio
top10_kd_players = df_players.sort_values(by='kd', ascending=False).head(10)

# Display the top 10 players by KD Ratio
print("Top 10 Players by KD Ratio.")    
print(top10_kd_players[['name', 'country', 'kd']])
print("\n" + "="*50 + "\n")

