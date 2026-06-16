# 05. Predictive Analysis (Classification)

## Notebook

`05. Predictive Analysis (Classification).ipynb`

## Objective

Build and evaluate multiple classification models to predict Falcon 9 first stage landing success, then identify the best-performing algorithm.

---

## Pipeline

| Step | Detail |
|------|--------|
| Input features (X) | `dataset_part_3.csv` — 83 columns after one-hot encoding |
| Target label (Y) | `Class` column — binary (0 = failure, 1 = success) |
| Standardisation | `StandardScaler` — zero mean, unit variance |
| Train/Test split | 80/20 — 72 training, 18 test samples (`random_state=2`) |
| Tuning method | `GridSearchCV` with `cv=10` (10-fold cross-validation) |

---

## Models & Results

### Logistic Regression
- **Grid:** `C=[0.01, 0.1, 1]`, `penalty=l2`, `solver=lbfgs`
- **Best params:** `C=0.01`
- **CV Accuracy:** 84.6% | **Test Accuracy:** 83.3%

### Support Vector Machine
- **Grid:** `kernel=(linear, rbf, poly, sigmoid)`, `C` & `gamma` over logspace(-3, 3, 5)
- **Best params:** `kernel=sigmoid`, `C=1.0`, `gamma=0.032`
- **CV Accuracy:** 84.8% | **Test Accuracy:** 83.3%

### Decision Tree ✅ Best Model
- **Grid:** `criterion`, `splitter`, `max_depth`, `max_features`, `min_samples_leaf`, `min_samples_split`
- **Best params:** `criterion=entropy`, `max_depth=6`, `max_features=sqrt`, `splitter=random`, `min_samples_split=10`
- **CV Accuracy:** 90.4% | **Test Accuracy:** **94.4%**

### K Nearest Neighbors
- **Grid:** `n_neighbors=1-10`, `algorithm=(auto, ball_tree, kd_tree, brute)`, `p=(1, 2)`
- **CV Accuracy:** 87.7% | **Test Accuracy:** 88.9%

---

## Final Comparison Table

| Algorithm | CV Accuracy | Test Accuracy | Rank |
|-----------|-------------|---------------|------|
| Decision Tree | 90.4% | **94.4%** | #1 |
| K Nearest Neighbors | 87.7% | 88.9% | #2 |
| Support Vector Machine | 84.8% | 83.3% | #3 |
| Logistic Regression | 84.6% | 83.3% | #4 |

**Baseline (always predict success):** 66.7%

All four models outperform the baseline. The **Decision Tree** wins with a 94.4% test accuracy, capturing the non-linear interactions between booster generation, orbit type, payload mass, and flight experience that linear models cannot.
