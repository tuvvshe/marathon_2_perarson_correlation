import pandas as pd

movies = pd.read_csv("MoviesOnStreamingPlatforms_updated.csv")
movies['Rotten Tomatoes'] = movies["Rotten Tomatoes"].str.replace("%", "").astype(float)
movies.drop("Type", inplace=True, axis=1)
correlations = movies.corr(method='pearson')

print(correlations)

print(correlations["Year"])

import seaborn as sns

import matplotlib.pyplot as plt

sns.heatmap(correlations)
plt.show()
