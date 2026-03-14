import numpy as np
from sklearn.cluster import KMeans

X = np.array([[1,2], [1,4], [1,0],
              [10,2], [10,4], [10,0]])

# Start with one cluster and divide
kmeans = KMeans(n_clusters=2)

labels = kmeans.fit_predict(X)

print("Cluster labels after division:", labels)
