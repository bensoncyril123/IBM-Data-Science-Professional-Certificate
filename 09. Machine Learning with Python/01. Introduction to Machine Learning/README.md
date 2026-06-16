# 01. Introduction to Machine Learning

## Overview

Machine Learning is a subfield of artificial intelligence that gives computers the ability to learn without being explicitly programmed. It involves developing algorithms that improve through experience and exposure to data.

## Types of Machine Learning

### Supervised Learning
The algorithm is trained on labelled data — each training example includes an input and a correct output.
- **Regression** — predicting a continuous value (e.g. house price)
- **Classification** — predicting a discrete category (e.g. spam or not spam)

### Unsupervised Learning
The algorithm finds patterns in unlabelled data without any predefined correct answers.
- **Clustering** — grouping similar data points together
- **Dimensionality Reduction** — simplifying data while preserving structure

### Reinforcement Learning
An agent learns by interacting with an environment, receiving rewards for correct actions.

## Python Libraries for ML

| Library | Purpose |
|---------|---------|
| `scikit-learn` | Core ML algorithms, preprocessing, model evaluation |
| `numpy` | Numerical computing and array operations |
| `pandas` | Data manipulation and analysis |
| `matplotlib` / `seaborn` | Data visualization |

## Key Concepts

- **Training set** — data used to fit the model
- **Test set** — data used to evaluate the model
- **Features (X)** — input variables
- **Target (y)** — output variable to predict
- **Overfitting** — model learns training data too well, performs poorly on new data
- **Underfitting** — model is too simple to capture the underlying pattern
