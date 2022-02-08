### Introduction to Clustering

#### What is clustering?

Clustering means finding clusters in a dataset, unsupervised. <br />

Cluster is a group of objects that are similar to other objects in the cluster, and dissimilar to data points in other clusters.

#### Clustering vs Classification

Classification is a supervised learning where each training data instance belongs to a particular class. <br />

In clustering, the data is unlabeled and the process is unsupervised.

#### Clustering applications

- RETAIL/MARKETING:
  - Identifying buying patterns of customers
  - Recommending new books or movies to new customers

- BANKING:
  - Fraud detection in credit card use
  - Identifying clusters of customers

- INSURANCE:
  - Fraud detection in claims analysis
  - Insurance risk of customers

- PUBLICATION:
  - Auto-categorizing news based on their content
  - Recommending similar news articles

- MEDICINE:
  - Characterizing patient behavior

- BIOLOGY:
  - Clustering general remarks to identify family ties

#### Why clustering?

- Exploratory data analysis
- Summary generation
- Outlier detection
- Finding duplicates
- Pre-processing step

#### Clustering algorithms

- Partitioned-based Clustering
  - Relatively efficient
  - E.g. k-Means, k-Median, Fuzzy c-Means
- Hierarchical Clustering
  - Produces trees of clusters
  - E.g. Agglomerative, Divisive
- Density-based Clustering
  - Produces arbitrary shaped clusters
  - E.g. DBSCAN

### Intro to k-Means

#### k-Means algorithm

- Partitioning Clustering
- k-Means divides the data into k non-overlapping subsets (clusters) without any cluster-internal structure
- Examples within a cluster are very similar
- Examples across different clusters are very different

#### Determine the similarity or dissimilarity

k-Means tries to minimize the intra-cluster distances and maximize the inter-cluster distances. <br />

Euclidean distance: <br /> ![render.png](https://2.pik.vn/20226e030c0d-59c9-4237-88bb-8e8ab29bc8e6.png)

#### How does k-Means clustering work?

1. Initalize k centroids randomly
2. Distance calculation
3. Assign each point to the closest centroid
4. Compute the new centroids for each cluster <br /> Each cluster center will be updated to be the mean for datapoints in its cluster
5. Repeat until there are no more changes

### More on k-Means

#### k-Means cluster algorithm

1. Randomly placing k centroids, one for each cluster
2. Calculate the distance of each point from each centroid
3. Assign each data point (object) to its closest centroid, creating a cluster
4. Recalculate the position of the k centroids.
5. Repeat the steps 2-4, until the centroids no longer move

#### k-Means accuracy

- External approach
  - Compare the clusters with the ground truth, if it is available
- Internal approach
  - Average the distance between data points within a cluster

#### Choosing k

- Elbow method
- The elbow point is determined where the rate of decrease sharply shifts. It is the right K for clustering.

#### k-Means recap

- Med and Large sized databases
- Produces sphere-like clusters
- Needs number for clusters (k)

### Intro to Hierarchical Clustering

#### Hierarchical clustering

Hierarchical clustering algorithms build a hierarchy of clusters where a node is a cluster consists of the clusters of its daughter nodes.

#### Agglomerative clustering

1. Create n clusters, one for each data points
2. Compute the Proximity Matrix
3. Repeat
  1. Merge the two closest clusters
  2. Update the proximity matrix
4. Until only a single cluster remains

#### Distance between clusters

- Single-Linkage Clustering
  - Minimum distance between clusters

- Complete-Linkage Clustering
  - Maximum distance between clusters

- Avarage Linkage Clustering
  - Average distance between clusters

- Centroid Linkage Clustering
  - Distance between clusters centroids

#### Advantages vs Disadvantages

- Advantages:
  - Doesn't required number of clusters to be specified
  - Easy to implement
  - Produces a dendrogram, which helps with understanding the data

- Disadvantages:
  - Can never undo any previous steps throughout the algorithm
  - Generally has long runtimes
  - Sometimes difficult to identify the number of clusters by the dendrogram

#### k-Means vs Hierarchical clustering

- k-Means:
  - Much more efficient
  - Requires the number of clusters to be specified
  - Give only one partitioning of the data based on the predefined number of clusters
  - Potentially returns different clusters each time it is run due to random initialization of centroids

- Hierarchical clustering:
  - Can be slow for large datasets
  - Does not require the number of clusters to run
  - Give more than one partitioning depending on the resolution
  - Always generates the same clusters

### DBSCAN

#### What is DBSCAN

- DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
  - Is one of the most common clustering algorithms
  - Works based on density of objects

- R (Radius of neighborhood)
  - Radius (R) that if includes enough number of points within, we call it a dense area

- M (Min number of neighbors)
  - The minimum number of data points that we want in a neighborhood to define a cluster

#### How DBSCAN works?

- Core point: A data point is a core point if within our neighborhood of the point there are at least M points

- Border point: A data point is a border point if its neighbourhood contains less than M data points or it is reachable from some core point.

- Outlier: An outlier is a point that is not a core point and also is not close enough to be reachable from a core point

#### Advantages of DBSCAN

- Arbitrarily shaped clusters
- Robust to outliers
- Does not require specification of the number of clusters
