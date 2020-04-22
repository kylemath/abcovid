import pandas as pd
import plotly 
import plotly.figure_factory as ff 
from datetime import timedelta
import matplotlib.pyplot as plt 


df = pd.read_csv('../downloads/covid19dataexport.csv',
	names=['number', 'Start', 'zone', 'gender', 'age', 'Task', 'confirmed'], skiprows=1, parse_dates=['Start'])

df['Finish'] = df['Start'] + timedelta(days=14)

# fig = ff.create_gantt(df.sort_values(by='Start', ascending='True'), bar_width=.3, height=6000, index_col='Task')

# fig.update_layout(
#     yaxis = {'autorange': 'reversed'}
# )

# fig.show()
zones = ['Edmonton Zone', 'Calgary Zone', 'North Zone', 'Central Zone', 'South Zone']

for zone in zones: 
	df[df['zone'] == zone].groupby('Start').count().confirmed.plot()

plt.legend(zones)
plt.ylabel('New daily cases')
plt.show()