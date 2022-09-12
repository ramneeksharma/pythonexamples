import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('MRT.csv')

# print(df.to_string()) 
# df.plot(kind = 'scatter', x = 'Group', y = 'Change')
# plt.show()

# Mean change in MRT
print(df["Change"][0:17].mean())
print(df["Change"][17:34].mean())