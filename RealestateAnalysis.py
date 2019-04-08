# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:04:54 2019

@author: wilki
"""
import seaborn as sn
import pandas as pd
import numpy as npy
import plotly as plty
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\wilki\Documents\realEstatedata.csv", encoding='ISO-8859-1', index_col='UID')
print(df[:2])
df['pop_density'] = df['pop'].values/ df['ALand'].values# calculate population density
# calculate average median age
t_male_yrs       = df.male_age_median.values*df.male_pop.values
t_female_yrs     = df.female_age_median.values*df.female_pop.values 
df['age_median'] = (t_male_yrs + t_female_yrs)/(df.male_pop.values + df.female_pop.values)

df.describe()
df.columns.values.tolist()

df.describe(include='all')
df.married.describe()
df.ALand.describe()
