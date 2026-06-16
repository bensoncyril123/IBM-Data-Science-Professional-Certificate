# Content-Based Filtering

Recommends items by comparing item attributes to a user's preference profile.

**Dataset used:** Movie metadata (genres, cast, director, keywords)

**Steps:**
1. Represent each item as a feature vector
2. Compute the user profile as a weighted average of liked item vectors
3. Rank unrated items by cosine similarity to the user profile
4. Return top-N recommendations

**Key library:** `scikit-learn` TF-IDF vectoriser + cosine similarity
