import pandas as pd
import plotly.express as plot

df = pd.read_csv('data.csv')
graph = plot.scatter(df, x = 'date', y = 'cases', color = 'country')

graph.show()