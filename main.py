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

# Get the names of the top 10 rated players
top_rated_names = set(top10_rated_players['name'])

# Get the names of the top 10 KD players
top_kd_names = set(top10_kd_players['name'])

# Get the intersection of the two sets
common_players = top_rated_names.intersection(top_kd_names) 
print("Common Players in Top 10 Rated and Top 10 KD Players.")
print(common_players)       
print("\n" + "="*50 + "\n")

# Find players unique to the top 10 rating list
unique_to_rating = top_rated_names.difference(top_kd_names)
print("Players in the Top 10 for Rating but not KD:")
print(unique_to_rating)
print("\n" + "="*50 + "\n")

# Find players unique to the top 10 KD list
unique_to_kd = top_kd_names.difference(top_rated_names)
print("Players in the Top 10 for KD but not Rating:")
print(unique_to_kd)
