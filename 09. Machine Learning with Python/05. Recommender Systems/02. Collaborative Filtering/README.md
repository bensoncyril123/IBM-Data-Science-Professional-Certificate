# Collaborative Filtering

Recommends items based on the preferences of similar users.

**Dataset used:** MovieLens ratings dataset

**Steps:**
1. Build a user-item ratings matrix
2. Compute similarity between users (Pearson / cosine)
3. Predict missing ratings using weighted average of similar users' ratings
4. Return top-N highest predicted-rating items

**Memory-based vs Model-based:**
- Memory-based: direct similarity computation (k-NN style)
- Model-based: matrix factorisation (SVD, NMF) learns latent factors

**Key library:** `scikit-learn`, `scipy`, `surprise`
