import numpy as np

data = np.array([[2,3],[3,4],[5,6],[8,8],[9,10]])

k = 2
centroids = data[:k]

for _ in range(5):
    clusters = [[] for i in range(k)]

    for point in data:
        distances = [np.sum(abs(point-centroid)) for centroid in centroids]
        index = distances.index(min(distances))
        clusters[index].append(point)

    new_centroids = []
    for cluster in clusters:
        new_centroids.append(np.median(cluster, axis=0))

    centroids = new_centroids

print("Final centroids:", centroids)
