import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid")

# Load the dataset
file_path = "C:\\Users\\raush\\Downloads\\WDFW_-_Creel_Summary_Counts_20250412.csv"
df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip()

# Rename for simplicity
df.rename(columns={
    'survey_date': 'Date',
    'species_name': 'Species',
    'water_body': 'Location'
}, inplace=True)

# Create total count of harvested fish
df['Count'] = df[['wild_harvest', 'hatchery_harvest', 'other_harvest']].sum(axis=1)

# Convert date
df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%y', errors='coerce')

# Create Month column
df['Month'] = df['Date'].dt.to_period('M').astype(str)

# ============================
# 1. Line Plot - Monthly Count
# ============================
monthly_counts = df.groupby('Month')['Count'].sum().reset_index()

plt.figure(figsize=(12, 5))
location_counts = df['Location'].value_counts()
sns.lineplot(x=location_counts.index, y=location_counts.values)
plt.xticks(rotation=90)
plt.title('Monthly Total Fish Count')
plt.xlabel('Month')
plt.ylabel('Total Count')
plt.tight_layout()
plt.show()

# ============================
# 2. Donut Chart - Species Distribution
# ============================
species_counts = df.groupby('Species')['Count'].sum().sort_values(ascending=False)
species_counts = species_counts[species_counts > 0]

plt.figure(figsize=(8, 8))
plt.pie(species_counts, labels=species_counts.index, startangle=90, autopct='%1.1f%%',
        wedgeprops={'width': 0.4})
plt.title('Species Distribution (Donut Chart)')
plt.show()

# ============================
# 3. Bar Plot - Top 10 Locations
# ============================
location_counts = df.groupby('Location')['Count'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=location_counts.values, y=location_counts.index, hue=location_counts.index, palette='viridis', legend=False)

plt.title('Top 10 Locations by Fish Count')
plt.xlabel('Total Count')
plt.ylabel('Location')
plt.tight_layout()
plt.show()

# ============================
# 4. Heatmap - Monthly Count per Species
# ============================
heatmap_data = df.pivot_table(index='Species', columns='Month', values='Count', aggfunc='sum', fill_value=0)

plt.figure(figsize=(14, 8))
sns.heatmap(heatmap_data, cmap='YlGnBu', linewidths=0.5)
plt.title('Monthly Fish Count per Species (Heatmap)')
plt.xlabel('Month')
plt.ylabel('Species')
plt.tight_layout()
plt.show()

# ============================
# 5. Box Plot - Count Distribution per Top Species
# ============================
top_species = df['Species'].value_counts().head(6).index
filtered_df = df[df['Species'].isin(top_species)]

plt.figure(figsize=(12, 6))
sns.boxplot(data=filtered_df, x='Species', y='Count')
plt.title('Fish Count Distribution per Top 6 Species')
plt.ylabel('Count')
plt.xlabel('Species')
plt.tight_layout()
plt.show()
