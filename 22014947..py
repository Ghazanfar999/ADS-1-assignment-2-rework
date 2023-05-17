# -*- coding: utf-8 -*-
"""Copy of Untitled17.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XjdEiKqZUFzOGywsvQqyyn6I2UG4UJ5B
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy
import scipy

def read_data(filename):
    """
    Read data from a CSV file and perform necessary data manipulation.

    Args:
        filename (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The processed dataframe.
    """
    df = pd.read_csv(filename)

    df = df.dropna()  # Remove rows with missing values

    df = df.set_index('Country Name')  # Set 'Country Name' column as the index
    
    df = df.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])  # Remove unnecessary columns
    df = df.transpose()  # Transpose the dataframe
    df.index = pd.to_datetime(df.index)  # Convert index to datetime format
    return df

def explore_statistics(dataframe):
    """
    Explore the statistical properties of indicators.

    Args:
        dataframe (pd.DataFrame): The dataframe containing the indicator data.

    Returns:
        pd.DataFrame: Summary statistics of the indicators.
    """
    if dataframe.empty:
        return pd.DataFrame()  # Return an empty DataFrame if no columns are present
    summary_stats = dataframe.describe()
    
    # Add additional statistical methods here if desired
    return summary_stats

def explore_correlations(dataframe1, dataframe2):
    """
    Explore the correlations between indicators.

    Args:
        dataframe1 (pd.DataFrame): The first dataframe containing indicator data.

        dataframe2 (pd.DataFrame): The second dataframe containing indicator data.

    Returns:
    
        pd.DataFrame: Correlation matrix between the indicators.
    """
    correlations = dataframe1.corrwith(dataframe2)

    # Add additional correlation analyses here if desired
    return correlations

# Read the CO2 emissions dataset from the local file
co2_emissions_filename = '/co2_emission.csv'  # Replace with the actual file path
co2_emissions_df = read_data(co2_emissions_filename)

# Read the total greenhouse gas emissions dataset from the local file
ghg_emissions_filename = '/green.csv'  # Replace with the actual file path
ghg_emissions_df = read_data(ghg_emissions_filename)

# Explore statistical properties of CO2 emissions

co2_stats = explore_statistics(co2_emissions_df)

# Explore statistical properties of total greenhouse gas emissions

ghg_stats = explore_statistics(ghg_emissions_df)

# Explore correlations between CO2 emissions and total greenhouse gas emissions

correlations = explore_correlations(co2_emissions_df, ghg_emissions_df)

def explore_correlations(dataframe1, dataframe2):
    """
    Explore the correlations between indicators.

    Args:
        dataframe1 (pd.DataFrame): The first dataframe containing indicator data.

        dataframe2 (pd.DataFrame): The second dataframe containing indicator data.

    Returns:
    
        pd.DataFrame: Correlation matrix between the indicators.
    """
    correlations = dataframe1.corrwith(dataframe2)

    # Add additional correlation analyses here if desired
    return correlations

# Print the summary statistics and correlations
print("CO2 Emissions Statistics:")

print(co2_stats)
print("\nGreenhouse Gas Emissions Statistics:")

print(ghg_stats)

print("\nCorrelations:")

print(correlations)

# Calculate the total CO2 emissions and total greenhouse gas emissions
co2_total = co2_emissions_df.mean(axis=1).sum().sum()%100

ghg_total = ghg_emissions_df.mean(axis=1).sum().sum()%100
print(co2_total)
print(ghg_total)
# Create a pie chart
labels = ['CO2 Emissions', 'Total Greenhouse Gas Emissions']
sizes = [co2_total, ghg_total]

colors = ['#FF0000', '#00FF00']  # Red for CO2 emissions, green for total greenhouse gas emissions

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title('CO2 Emissions vs Total Greenhouse Gas Emissions')

plt.show()

# Plot CO2 emissions vs total greenhouse gas emissions


fig, ax1 = plt.subplots(figsize=(8, 8))
ax2 = ax1.twinx()
COLOR_PRICE = "##FF0000"

ax1.plot(co2_emissions_df.index, co2_emissions_df.mean(axis=1), label='CO2 emissions',color='red')
ax2.plot(ghg_emissions_df.index, ghg_emissions_df.mean(axis=1), label='Total greenhouse gas emissions')
plt.xlabel('Year')

plt.ylabel('Emissions (kt)')
plt.title('CO2 Emissions vs Total Greenhouse Gas Emissions')
plt.legend()
plt.show()

# Read the Fossil fuel energy consumption (% of total) dataset from the local file
eu_emissions_filename = '/FS.csv'  # Replace with the actual file path
eu_emissions_df = read_data(co2_emissions_filename)


# Read the Electricity production from oil sources (% of total) dataset from the local file

ep_emissions_filename = '/EP.csv'  # Replace with the actual file path
ep_emissions_df = read_data(ep_emissions_filename)

# Explore statistical properties 
eu_stats = explore_statistics(eu_emissions_df)

# Explore statistical properties 

ep_stats = explore_statistics(ep_emissions_df)

# Explore correlations between Energy use and Electricity production

correlations = explore_correlations(eu_emissions_df, ep_emissions_df)

# Print the summary statistics and correlations
print("Electricity production from oil sources -% of total Statistics:")
print(ep_stats)

print("\nFossil fuel energy consumption -% of total:")

print(eu_stats)
print("\nCorrelations:")
print(correlations)

# Plot bar graph
plt.figure(figsize=(10, 9))

plt.bar(eu_emissions_df.index, eu_emissions_df.mean(axis=1), label='Fossil fuel energy consumption (% of total)')
plt.bar(ep_emissions_df.index, ep_emissions_df.mean(axis=1), label='Electricity Production from Oil Sources (% of total)')

plt.xlabel('Year')

plt.ylabel('Value')
plt.title('Fossil fuel energy consumption (% of total) vs Electricity Production from Oil Sources')

plt.legend()
plt.xticks(rotation=45)

plt.show()