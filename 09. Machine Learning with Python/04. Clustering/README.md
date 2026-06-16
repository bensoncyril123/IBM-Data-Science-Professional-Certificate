# 04. Clustering

Clustering is an **unsupervised learning** technique that groups similar data points together without predefined labels. This module covers three foundational clustering algorithms.

## Notebooks

| Notebook | Description |
|----------|-------------|
| `01. k-Means.ipynb` | Partitions data into k clusters by minimising intra-cluster variance |
| `02. Agglomerative Clustering.ipynb` | Builds a hierarchy of clusters from the bottom up |
| `03. Density-based Clustering.ipynb` | Groups points by density; identifies noise/outliers (DBSCAN) |

## Key Concepts

### k-Means Clustering
1. Choose k cluster centroids randomly
2. Assign each point to the nearest centroid
3. Recompute centroids as cluster means
4. Repeat until convergence

**Choosing k:** Use the Elbow Method — plot inertia (within-cluster sum of squares) against k and look for the "elbow" where improvement slows.

**Use case:** Customer segmentation, image compression, document clustering

### Agglomerative (Hierarchical) Clustering
- Starts with each point as its own cluster
- Iteratively merges the two closest clusters
- Produces a **dendrogram** — a tree diagram showing all merge decisions
- No need to specify k in advance; cut the dendrogram at any level

**Linkage methods:** Single, Complete, Average, Ward

### DBSCAN (Density-Based Spatial Clustering)
- Groups points in high-density regions; marks low-density points as **noise**
- Key parameters: `eps` (neighbourhood radius) and `min_samples`
- Can discover clusters of arbitrary shape
- Robust to outliers — unlike k-Means

## Evaluation

Since clustering is unsupervised, evaluation is less straightforward:
- **Silhouette Score** — measures how similar a point is to its own cluster vs other clusters (range: -1 to 1)
- **Davies-Bouldin Index** — lower is better
- **Inertia (k-Means)** — within-cluster sum of squared distances
