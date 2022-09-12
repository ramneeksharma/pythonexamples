import pandas as pd
import matplotlib.pyplot as plt

# Read the Cloud Seeding data 
df = pd.read_csv('CloudSeedingData.csv')

# Prepare the boxplot
fig, main_ax = plt.subplots()

# Label the various parts of the plot labels / axis / title
main_ax.boxplot(df, labels=df.columns)
main_ax.set_xlabel('Cloud (Control / Seeded)')
main_ax.set_ylabel('Rainfall (acre - feet)')
main_ax.set_title('Cloud Seeding Experiment')

# Render the plot on the screen
plt.show()