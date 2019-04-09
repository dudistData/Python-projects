# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:48:29 2019

@author: wilki
"""

import seaborn as sn
import pandas as pd
import numpy as npy
import plotly as plty
import matplotlib.pyplot as plt
import plotly.tools as tls
import plotly.offline as py
from plotly.offline import init_notebook_mode, iplot, plot
import plotly.graph_objs as go
init_notebook_mode(connected=True)
import warnings

df_features = pd.read_csv(r"C:\Users\wilki\Documents\realEstatedata.csv", encoding='ISO-8859-1', index_col='UID')
percentual_types = round(df_features["type"].value_counts(), 2)

print("Type Count Values: ")
print(percentual_types)

types = round(df_features["type"].value_counts() / len(df_features["type"]) * 100,2)

labels = list(types.index)
values = list(types.values)

trace1 = go.Pie(labels=labels, values=values, marker=dict(colors=['red']))

layout = go.Layout(title='Distribuition of Types', legend=dict(orientation="h"));

fig = go.Figure(data=[trace1], layout=layout)
iplot(fig)
