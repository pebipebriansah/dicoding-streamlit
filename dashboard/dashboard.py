import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.linear_model import LinearRegression
import numpy as np
import os
import statsmodels.api as sm
# Set up page configuration
st.set_page_config(page_title="Air Quality Analysis Dashboard")

# Load dataset
data = pd.read_csv('D:/Project Data Science/data/PRSA_Data_Wanliu_20130301-20170228.csv')

# Title of the dashboard
st.title('Air Quality Analysis Dashboard: Wanshouxigong Station')

# Description
st.write('This dashboard provides an interactive way to explore air quality data, specifically focusing on PM2.5 levels and their relationship with various weather conditions.')

# Sidebar for user input
st.sidebar.header('User Input Features')

# Let users select a year and month to view data
selected_year = st.sidebar.selectbox('Select Year', list(data['year'].unique()))
selected_month = st.sidebar.selectbox('Select Month', list(data['month'].unique()))

# Filter data based on the selected year and month
data_filtered = data[(data['year'] == selected_year) & (data['month'] == selected_month)].copy()

# Displaying data statistics
st.subheader('Data Overview for Selected Period')
st.write(data_filtered.describe())

# Line chart for PM2.5 levels over selected month
st.subheader('Daily PM2.5 Levels')
fig, ax = plt.subplots()
ax.plot(data_filtered['day'], data_filtered['PM2.5'], color='red')
plt.xlabel('Day of the Month')
plt.ylabel('PM2.5 Concentration (µg/m³)')
st.pyplot(fig)

# Correlation heatmap for the selected month
st.subheader('Correlation Heatmap of Air Quality Indicators')
corr = data_filtered[['PM2.5', 'NO2', 'SO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP']].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, ax=ax, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
st.pyplot(fig)

# Seasonal Trend Analysis
st.subheader('Seasonal Trend Analysis')
seasonal_trends = data.groupby('month')['PM2.5'].mean()
fig, ax = plt.subplots()
seasonal_trends.plot(kind='bar', color='skyblue', ax=ax)
plt.title('Average Monthly PM2.5 Levels')
plt.xlabel('Month')
plt.ylabel('Average PM2.5 (µg/m³)')
st.pyplot(fig)

# Time Series Decomposition of PM2.5
st.subheader('Time Series Decomposition of PM2.5')
try:
    data_filtered['PM2.5'].ffill(inplace=True)
    decomposed = seasonal_decompose(data_filtered['PM2.5'], model='additive', period=24) # Adjust period as necessary
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
    decomposed.trend.plot(ax=ax1, title='Trend')
    decomposed.seasonal.plot(ax=ax2, title='Seasonality')
    decomposed.resid.plot(ax=ax3, title='Residuals')
    plt.tight_layout()
    st.pyplot(fig)
except ValueError as e:
    st.error("Unable to perform time series decomposition: " + str(e))

# Linear Regression on PM2.5 and Weather Variables
st.subheader('Regression Analysis: PM2.5 and Weather Variables')
X = data_filtered[['TEMP', 'PRES', 'RAIN']].dropna()
X = sm.add_constant(X)
y = data_filtered['PM2.5'].dropna()

model = sm.OLS(y, X).fit()
st.write(model.summary())

# Visualize the regression coefficients
fig, ax = plt.subplots()
sns.barplot(x=model.params.index, y=model.params.values, ax=ax)
plt.title('Regression Coefficients for PM2.5 Prediction')
plt.ylabel('Coefficient Value')
st.pyplot(fig)

# Rainfall vs. PM2.5 Levels
st.subheader('Rainfall vs. PM2.5 Levels')
fig, ax = plt.subplots()
sns.scatterplot(x='RAIN', y='PM2.5', data=data_filtered, ax=ax, color='green')
sns.regplot(x='RAIN', y='PM2.5', data=data_filtered, scatter=False, color='black')
plt.title('Rainfall vs. PM2.5 Levels')
plt.xlabel('Rainfall (mm)')
plt.ylabel('PM2.5 (µg/m³)')
st.pyplot(fig)

# Conclusion
st.subheader('Conclusion')
st.write("""
- The dashboard provides an in-depth and interactive analysis of air quality data.
- Various visualizations offer insights into PM2.5 levels, their distribution, and factors affecting them.
- Seasonal trends and the impact of different weather conditions and pollutants on air quality are clearly depicted.
- Users can explore the data dynamically to gain a deeper understanding of air quality trends.
""")

# Personal Information Section
st.markdown("""
### About Me
- **Name**: Pebi Pebriansah
- **Email Address**: pebipebriansah160200@gmail.com
- **Dicoding ID**: https://www.dicoding.com/users/pebipebriansah16

### Project Overview
This dashboard presents an analysis of air quality data, particularly focusing on PM2.5 levels, from the Wanshouxigong station. The project aims to uncover trends, seasonal variations, and the impact of different weather conditions on air quality. Insights from this analysis can be valuable for environmental studies and public health monitoring.
""")
