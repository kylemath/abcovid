import pandas as pd
import plotly 
import plotly.figure_factory as ff 
from datetime import timedelta
import matplotlib
matplotlib.use('tkAgg')

import matplotlib.pyplot as plt 


try:
    from urllib.request import Request, urlopen  # Python 3
except ImportError:
    from urllib2 import Request, urlopen  # Python 2

req = Request('https://www.alberta.ca/data/stats/covid-19-alberta-statistics-data.csv')
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0')
content = urlopen(req)


df = pd.read_csv(content,
	names=['Rownum', 'Start', 'zone', 'gender', 'age', 'Task', 'confirmed'], skiprows=1, parse_dates=['Start'])
print(df)
# df['Finish'] = df['Start'] + timedelta(days=14)

# fig = ff.create_gantt(df.sort_values(by='Start', ascending='True'), bar_width=.3, height=6000, index_col='Task')

# fig.update_layout(
#     yaxis = {'autorange': 'reversed'}
# )

# fig.show()
zones = ['Edmonton Zone', 'Calgary Zone', 'North Zone', 'Central Zone', 'South Zone']


print(df.head(1))
for zone in zones: 
	print(df['gender'] == 'Female')
	df_zone = df[df['zone'] == zone].groupby('Start').count().confirmed
	# df_zone.drop(df_zone.tail(1).index, inplace=True)
	df_zone.plot()


plt.legend(zones)
plt.ylabel('New daily cases')
plt.show()



populations = {'Edmonton Zone': 1424837, 'Calgary Zone': 1696765, 'North Zone': 484941, 'Central Zone': 482349, 'South Zone': 308924 }
print(df.head(1))
for zone in zones: 
	print(df['gender'] == 'Female')
	df_zone = df[df['zone'] == zone].groupby('Start').count().confirmed
	# df_zone.drop(df_zone.tail(1).index, inplace=True)
	df_zone = df_zone.divide(populations[zone]).multiply(1000)
	df_zone.plot()


plt.legend(zones)
plt.ylabel('Cases per 100,000')
plt.show()
