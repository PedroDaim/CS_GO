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

#Display descriptive statistics of the dataframe
print("Descriptive Statistics of the Dataframe.")       
print(df_players.describe())
print("\n" + "="*50 + "\n")

#Display top 10 countries with the highest KD ratio
top_10_countries = (
    df_players.groupby('country')['kd']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("Top 10 countries with the highest KD ratio:")
print(top_10_countries)
print("\n" + "="*50 + "\n")

# Convert the pandas Series to a DataFrame for seaborn
top_10_df = top_10_countries.reset_index(name='average_kd')

# Create the bar plot for the top_10_countries function using seaborn
plt.figure(figsize=(12, 8))
sns.barplot(x='average_kd', y='country', data=top_10_df, palette='viridis')
plt.title('Top 10 Countries with Highest Average KD Ratio')
plt.xlabel('Average Kill/Death Ratio')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

