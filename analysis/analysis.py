from matplotlib import pyplot as plt
import pandas as pd
data = pd.read_csv('only_road_accidents_data_month2.csv', usecols=['STATE/UT', 'TOTAL', 'YEAR'])
d = data.groupby('STATE/UT', as_index=False).mean()
fig = plt.figure(figsize=(5, 20))
ax = fig.add_subplot(111)
ax.scatter(d['TOTAL'], d['STATE/UT'], s=50)
plt.xlabel('Mean of Road accidents from 2001-2014')
plt.ylabel('States/UT of India')
ax.plot(d['TOTAL'], d['STATE/UT'])
plt.title('Mean of Road Accidents in various states of India from 2001-2014')
plt.savefig('graph1', dpi=400)
plt.show()

# p = data[data['TOTAL'] > 5000]
# data.groupby('STATE/UT', as_index=False).sum()
# tamil = data[data['STATE/UT'] == 'Tamil Nadu']
