import numpy as np
from sklearn.cluster import KMeans

# Sample data
X = np.array([[1,2], [1,4], [1,0],
              [10,2], [10,4], [10,0]])

# Create model
kmeans = KMeans(n_clusters=2)

# Fit model
kmeans.fit(X)

# Cluster labels
print("Labels:", kmeans.labels_)

# Centroids
print("Centroids:", kmeans.cluster_centers_)
