import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import plotly 
import plotly.figure_factory as ff 
from datetime import timedelta

df = pd.read_csv('../downloads/covid19dataexport.csv',
	names=['number', 'Start', 'zone', 'gender', 'age', 'Task', 'confirmed'], skiprows=1, parse_dates=['Start'])

df['Finish'] = df['Start'] + timedelta(days=14)

fig = ff.create_gantt(df.sort_values(by='Start', ascending='True'), bar_width=.3, height=6000, index_col='Task')



fig.update_layout(
    yaxis = {
        'autorange': 'reversed',
    }
)

fig.show()
