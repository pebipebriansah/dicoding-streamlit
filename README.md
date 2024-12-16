# Air Quality Analysis Project: Wanshouxigong Station

## Live Dashboard


## Project Overview
This project, submitted for the "Learn Data Analysis with Python" course from Dicoding, focuses on analyzing air quality data, particularly PM2.5 levels, from the Wanliu station. The objective is to uncover trends, seasonal variations, and the impact of different weather conditions on air quality. The dataset used includes air quality measurements with a focus on PM2.5, NO2, SO2, CO, O3, temperature, pressure, humidity, and rainfall, spanning several years from 2013 to 2017.

## Course Submission
This analysis serves as a course submission for "Learn Data Analysis with Python" offered by Dicoding. It demonstrates the application of data analysis techniques and visualization skills learned in the course.

## Table of Contents
- [Air Quality Analysis Project: Wanshouxigong Station](#air-quality-analysis-project-wanshouxigong-station)
  - [Live Dashboard](#live-dashboard)
  - [Project Overview](#project-overview)
  - [Course Submission](#course-submission)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Data Source](#data-source)
  - [Libraries Used](#libraries-used)
  - [Key Insights](#key-insights)
  - [How to Run the Dashboard](#how-to-run-the-dashboard)
    - [Setup Environment](#setup-environment)
    - [Run the Streamlit App](#run-the-streamlit-app)
    - [Additional Files](#additional-files)
    - [P.S.](#ps)
  - [About Me](#about-me)

## Introduction
The goal of this project is to analyze air quality data, specifically PM2.5 pollutant levels, and understand their relationship with various environmental factors. The analysis includes identifying trends, seasonal patterns, and correlations with weather conditions.

## Data Source
The dataset used in this project includes air quality measurements from the Wanshouxigong station, with a focus on PM2.5 levels and other related environmental data.

## Libraries Used
- altair==5.5.0
- attrs==24.2.0
- blinker==1.9.0
- cachetools==5.5.0
- certifi==2024.12.14
- charset-normalizer==3.4.0
- click==8.1.7
- colorama==0.4.6
- contourpy==1.3.1
- cycler==0.12.1
- fonttools==4.55.3
- gitdb==4.0.11
- GitPython==3.1.43
- idna==3.10
- Jinja2==3.1.4
- joblib==1.4.2
- jsonschema==4.23.0
- jsonschema-specifications==2024.10.1
- kiwisolver==1.4.7
- markdown-it-py==3.0.0
- MarkupSafe==3.0.2
- matplotlib==3.10.0
- mdurl==0.1.2
- narwhals==1.18.4
- numpy==2.2.0
- packaging==24.2
- pandas==2.2.3
- patsy==1.0.1
- pillow==11.0.0
- protobuf==5.29.1
- pyarrow==18.1.0
- pydeck==0.9.1
- Pygments==2.18.0
- pyparsing==3.2.0
- python-dateutil==2.9.0.post0
- pytz==2024.2
- referencing==0.35.1
- requests==2.32.3
- rich==13.9.4
- rpds-py==0.22.3
- scikit-learn==1.6.0
- scipy==1.14.1
- seaborn==0.13.2
- six==1.17.0
- smmap==5.0.1
- statsmodels==0.14.4
- streamlit==1.41.1
- tenacity==9.0.0
- threadpoolctl==3.5.0
- toml==0.10.2
- tornado==6.4.2
- typing_extensions==4.12.2
- tzdata==2024.2
- urllib3==2.2.3
- watchdog==6.0.0
  
## Key Insights
- Seasonal Variation in PM2.5 Levels: Higher concentrations of PM2.5 are observed during colder months, indicating seasonal variations in air quality.
- Correlation Between PM2.5 and Weather Conditions: A correlation is found between PM2.5 levels and weather factors like temperature and humidity, where higher temperature tends to correlate with lower PM2.5, and higher humidity with increased PM2.5 levels.
- Trends and Patterns from Time Series Analysis: Time series analysis reveals consistent trends and seasonal patterns in PM2.5 levels, with clear seasonal fluctuations and residual components that provide deeper insights into air quality changes over time.

## How to Run the Dashboard

To run the Air Quality Analysis Dashboard, follow these steps:

### Setup Environment

1. **Create and Activate a Python Environment**:
   - If using Conda (ensure [Conda](https://docs.conda.io/en/latest/) is installed):
     ```
     conda create --name airquality-ds python=3.9
     conda activate airquality-ds
     ```
   - If using venv (standard Python environment tool):
     ```
     python -m venv airquality-ds
     source airquality-ds/bin/activate  # On Windows use `airquality-ds\Scripts\activate`
     ```

2. **Install Required Packages**:
   - The following packages are necessary for running the analysis and the dashboard:
     ```
     pip install altair==5.5.0 attrs==24.2.0 blinker==1.9.0 cachetools==5.5.0 certifi==2024.12.14 charset-normalizer==3.4.0 click==8.1.7 colorama==0.4.6 contourpy==1.3.1 cycler==0.12.1 fonttools==4.55.3 gitdb==4.0.11 GitPython==3.1.43 idna==3.10 Jinja2==3.1.4 joblib==1.4.2 jsonschema==4.23.0 jsonschema-specifications==2024.10.1 kiwisolver==1.4.7 markdown-it-py==3.0.0 MarkupSafe==3.0.2 matplotlib==3.10.0 mdurl==0.1.2 narwhals==1.18.4 numpy==2.2.0 packaging==24.2 pandas==2.2.3 patsy==1.0.1 pillow==11.0.0 protobuf==5.29.1 pyarrow==18.1.0 pydeck==0.9.1 Pygments==2.18.0 pyparsing==3.2.0 python-dateutil==2.9.0.post0 pytz==2024.2 referencing==0.35.1 requests==2.32.3 rich==13.9.4 rpds-py==0.22.3 scikit-learn==1.6.0 scipy==1.14.1 seaborn==0.13.2 six==1.17.0 smmap==5.0.1 statsmodels==0.14.4 streamlit==1.41.1 tenacity==9.0.0 threadpoolctl==3.5.0 toml==0.10.2 tornado==6.4.2 typing_extensions==4.12.2 tzdata==2024.2 urllib3==2.2.3 watchdog==6.0.0
     ```

     or you can do
     ```
     pip install -r requirements.txt
     ```
### Run the Streamlit App

1. **Navigate to the Project Directory** where `dashboard.py` is located.

2. **Run the Streamlit App**:
    ```
    streamlit run dashboard.py
    ```

### Additional Files

- The dataset used for this analysis is included in the project repository.
- A detailed Python notebook (`Proyek_Analisis_Data.ipynb`) containing the data analysis and visualizations is also provided.
---
### P.S.

Since Dicoding recommended creating the good and tidy folder structures, as `dashboard.py` in `dashboard` folder, then the deployment for Streamlit App affected.

That was why I put the `requirements.txt` in the `dashboard` folder as well.  

---

## About Me
- **Name**: Pebi Pebriansah
- **Email Address**: pebipebriansah160200@gmail.com
- **Dicoding ID**: https://www.dicoding.com/users/pebipebriansah16

---
