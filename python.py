import plotly.figure_factory as ff 
import csv
import statistics
import pandas as pd 
import random

df = pd.read_csv('data.csv')
data = df["Avg Rating"].tolist()
population_mean = statistics.mean(data)

fig = ff.create_distplot([data], ["Avg Rating"], show_hist = False)
fig.show()





