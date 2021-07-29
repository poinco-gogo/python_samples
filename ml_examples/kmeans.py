import sys
import MDAnalysis as mda
import numpy as np
from sklearn.cluster import KMeans

pdb=mda.Universe(sys.argv[1])

sel=pdb.select_atoms("protein")

X = np.zeros( (len(sel), 3) )

for i in range( len(sel) ):
	X[i] = sel[i].position

kmeans = KMeans(n_clusters=10).fit(X)

print(kmeans.cluster_centers_)
print(kmeans.labels_)
