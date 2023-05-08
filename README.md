# BigData2023

Code Repository for Big Data Final Project

# Data
The data used in this repository is taken from various sources and is stored in the ```/data/``` folder

Cleaned data is stored in ```/cleaned_data/``` folder.
# How to Run
Python 3.10 or above required

To install requirements:

```
pip install -r requirements.txt
```

Run the notebooks under data cleaning to process raw data, then run the analysis notebooks to get results
## Data Cleaning

```General_Cleaning``` and ```PPP_Cleaning``` are notebooks used to clean raw data from the ```/data/``` directory, results are stored in ```/cleaned_data/```

## Analysis


There are four notebooks used for analysis of processed data:
1. ```PPP_Analysis ``` - Analysis of Paycheck Protection Program
2. ```QCEW_Analysis``` - Analysis of Quarterly Census of Employment and Wages
3. ```Pedestrians_Analysis``` - Analysis of Pedestrian Volume over Time
4. ```General_Analysis``` - Analysis of Savings, COVID-19 Numbers, Licenses, and Interest Rates

Tables and graphs are stored in ```/output/``` with subdirectory results organized by notebook.
