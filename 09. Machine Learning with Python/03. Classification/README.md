# 03. Classification

Classification algorithms predict which category a data point belongs to. This module covers four widely-used classifiers applied to real datasets.

## Notebooks

| Notebook | Description |
|----------|-------------|
| `01. K Nearest Neighbours (KNN).ipynb` | Classifies based on majority class among k nearest neighbours |
| `02. Decision Trees.ipynb` | Tree-structured model splitting data on feature thresholds |
| `03. Logistic Regression.ipynb` | Probabilistic linear classifier for binary/multi-class problems |
| `04. Support Vector Machines (SVM).ipynb` | Finds optimal hyperplane maximising class margin |

## Key Concepts

### K Nearest Neighbours (KNN)
- Non-parametric, instance-based learning
- Prediction = majority class among k nearest training points (using Euclidean distance)
- Key hyperparameter: `k` — higher k = smoother boundary, lower k = more flexible

### Decision Trees
- Splits data recursively on the feature providing the highest information gain (entropy) or lowest Gini impurity
- Produces interpretable, human-readable rules
- Prone to overfitting; controlled via `max_depth`, `min_samples_split`

### Logistic Regression
- Models the probability of class membership using the sigmoid function
- Despite the name, it is a **classification** algorithm
- Output: probability between 0 and 1, thresholded at 0.5 by default

### Support Vector Machine (SVM)
- Finds a hyperplane that maximises the margin between classes
- Kernel trick (linear, RBF, polynomial, sigmoid) maps data to higher dimensions
- Effective in high-dimensional spaces; robust to outliers

## Evaluation Metrics

| Metric | Description |
|--------|-------------|
| Accuracy | (TP + TN) / Total |
| Precision | TP / (TP + FP) |
| Recall | TP / (TP + FN) |
| F1 Score | Harmonic mean of precision and recall |
| Jaccard Index | TP / (TP + FP + FN) |
| Log Loss | Penalises confident wrong predictions |
