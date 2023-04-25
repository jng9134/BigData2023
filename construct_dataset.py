import pandas as pd
import numpy as np
import os
import copy

filepath  = "cps_data_2019_2023"

months = ["jan", "feb", "march", "april", "may", "june", "jul", "aug", "sep", "oct", "nov", "dec"]
years = [i for i in range (19,24,1)]


boroughs = { 1 : "The Bronx",
             2 : "Brooklyn", 
             3 : "Manhattan",
             4 : "Queens",
             5 : "Staten Island"
            }

sectors = {
            0 : "No Category",
            1: "Management", 
            2: "Business/Finance",
            3: "Computer/Math/Science",
            4: "Architecture/Engineering", 
            5: "Life/Physical/Social",
            6: "Community",
            7: "Legal", 
            8: "Education/Training/Library",
            9: "Arts/Design/Entertainment/Sports/Media", 
            10: "Healthcare Practioner",
            11: "Healthcare Support",
            12: "Protective Services",
            13: "Food Preparation/Serving",
            14: "Building Cleaning/Maitenance",
            15: "Personal Care",
            16: "Sales",
            17: "Officee and Administrative",
            18: "Farming/Fishing/Forestry",
            19: "Construction", 
            20: "Installation/Maitenance/Repair",
            21: "Production",
            22: "Transportation",
            23: "Armed Forces"
          }
          
initialized = False
pd.options.mode.chained_assignment = None
for year in years:
    for month in months:

        path = filepath + "/" + month + str(year) + ".csv"

        if (os.path.exists(path)):

            df = pd.read_csv(path, skiprows=[i for i in range(4)])
            
            

            df["Year"] = year
            df["Month"] = month
            df["Borough"] = None
            df["Sector"] =  None

            borough_ranges = range(2, 3250, 649)
            sector_ranges =  range(3, 3250, 27)
            for i in range(len(borough_ranges) - 1):
                df['Borough'].iloc[borough_ranges[i]:borough_ranges[i+1] - 1] = boroughs[i+1]

            for i in range(len(sector_ranges) - 1):
                df['Sector'].iloc[sector_ranges[i]:sector_ranges[i+1] - 1] = sectors[i % 24]

            if not initialized:
                res = copy.deepcopy(df)
                initialized = True

            else:
                res = pd.concat([res, df], axis=0)



print(res["Demographics- race of respondent (PTDTRACE)"].unique())
#do we want to look at different sectors?
#spark -> add column for borough, add column for sector?
res.to_csv('concat.csv')

