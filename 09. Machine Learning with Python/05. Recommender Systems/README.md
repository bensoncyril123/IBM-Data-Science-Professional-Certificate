# 05. Recommender Systems

Recommender systems suggest relevant items (products, movies, articles) to users based on past behaviour or item characteristics. This module covers the two primary approaches.

## Sub-modules

| Folder | Method |
|--------|--------|
| `01. Content-based/` | Recommends items similar to what the user has liked before |
| `02. Collaborative Filtering/` | Recommends items liked by users with similar tastes |

## Content-Based Filtering

**How it works:**
- Builds a profile for each item based on its attributes (genre, cast, keywords, etc.)
- Builds a profile for each user based on items they have liked
- Recommends items whose profiles are most similar to the user's profile
- Similarity measured using **cosine similarity** or **Pearson correlation**

**Pros:** No cold-start problem for items; transparent recommendations  
**Cons:** Limited discovery (only recommends similar to what user already knows); requires good item metadata

## Collaborative Filtering

**How it works:**
- Finds users (or items) with similar interaction patterns
- Predicts ratings/preferences based on what similar users liked

**Two approaches:**
1. **User-based CF** — finds similar users and recommends what they liked
2. **Item-based CF** — finds items that co-occur with items the user liked

**Matrix Factorisation (SVD):**
- Decomposes the user-item rating matrix into latent factor matrices
- Captures hidden relationships between users and items

**Pros:** Discovers unexpected items; no item metadata needed  
**Cons:** Cold-start problem for new users/items; sparsity issue with large catalogues

## Evaluation Metrics

| Metric | Description |
|--------|-------------|
| RMSE | Root mean squared error of predicted vs actual ratings |
| MAE | Mean absolute error of ratings |
| Precision@K | Fraction of top-K recommendations that are relevant |
| Recall@K | Fraction of relevant items appearing in top-K |
