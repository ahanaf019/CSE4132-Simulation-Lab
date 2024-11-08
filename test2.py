import pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure()

df = pd.read_csv('./cpm_data.csv')

pd.plotting.autocorrelation_plot(df['duration'])
plt.show()