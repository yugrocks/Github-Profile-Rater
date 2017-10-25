import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pickle

data = pd.read_csv("profiles.csv")
X = data.iloc[:, (0,1,2,3,5,6)].values
scoring_weights = np.array([1.2, 0.5, 1.02, 1, 1.9, 2.5])
clustering_weights = scoring_weights**0.5

X = X * clustering_weights
# Now to check what number of clusters gives the optimal result
number_clusters = 200


# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = number_clusters, init = 'k-means++') # With 200 clusters to level from 1 to 200
y_kmeans = kmeans.fit(X)


def givescores(x):
    return np.dot(x, np.array([1,1,1,1,1,1]).T)

# Now to sort the clusters on a criteria
scores = givescores(kmeans.cluster_centers_)
sorted_clusters = [x for (y, x) in sorted(zip(scores, kmeans.cluster_centers_))]
# Now pickle cluster centers
with open('cluster_centers.pkl', 'wb') as file:
    pickle.dump(sorted_clusters, file)
    