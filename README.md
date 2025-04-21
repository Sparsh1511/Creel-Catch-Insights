# Creel-Catch-Insights
A data analysis project focused on summarizing and exploring recreational fishing activity through creel survey data. The dataset includes detailed records on angler participation, fishing effort, species caught and released, and distinctions between wild, hatchery, and other fish types across various Washington water bodies.

# Creel Catch Insights

## Overview

Creel Catch Insights is a data analysis project using cleaned creel survey data collected from recreational fisheries. This dataset helps to understand angler behavior, fishing effort, species-specific trends, and hatchery vs. wild fish interactions over time.

## Dataset

The dataset `Creel_Summary_Cleaned.csv` contains 10,450 rows and 15 columns, with the following key fields:

- `survey_date`: Date of the survey
- `project_name`, `fishery_name`: Identification of the monitoring project
- `water_body`, `catch_area_code`: Location details
- `species_name`: Type of fish observed
- `wild_released`, `wild_harvest`: Counts for wild fish
- `hatchery_released`, `hatchery_harvest`: Counts for hatchery fish
- `other_released`, `other_harvest`: Miscellaneous fish counts
- `anglers`, `boatanglers`: Number of total and boat anglers
- `hours_fished`: Total fishing hours

## Objectives

- Analyze angler effort across different water bodies and time periods
- Compare harvest and release rates by species and fish type
- Visualize trends in hatchery vs. wild fish captures
- Provide insights for fisheries management and sustainability

## Usage

1. Load the dataset using `pandas`
2. Clean or preprocess if necessary
3. Use matplotlib, seaborn, or plotly for visualizations
4. Perform analysis on:
   - Catch per unit effort (CPUE)
   - Species composition over time
   - Location-based fishing activity

## Example

```python
import pandas as pd

df = pd.read_csv("Creel_Summary_Cleaned.csv")
df['survey_date'] = pd.to_datetime(df['survey_date'])
df.groupby('species_name')['wild_harvest'].sum().sort_values(ascending=False).plot(kind='bar')
