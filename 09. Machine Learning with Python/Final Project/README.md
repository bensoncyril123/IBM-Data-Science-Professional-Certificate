# Final Project — The Best Classifier

## Objective

Apply multiple classification algorithms to a real-world loan dataset and determine which classifier performs best.

## Dataset

**Loan dataset** — historical records of loans with features including:
- `loan_status` — target variable: PAIDOFF or COLLECTION
- `Principal` — loan amount
- `terms` — repayment term (7, 15, or 30 days)
- `effective_date` — loan issue date
- `due_date` — repayment due date
- `age`, `education`, `Gender` — borrower demographics

## Algorithms Compared

| Algorithm | Best Parameters | Jaccard | F1 | Log Loss |
|-----------|----------------|---------|-----|----------|
| KNN | k=7 | — | — | — |
| Decision Tree | max_depth=4 | — | — | — |
| SVM | kernel=rbf | — | — | — |
| Logistic Regression | C=0.01, solver=liblinear | — | — | — |

*(Results filled in from notebook output)*

## Evaluation Metrics

- **Jaccard Index** — intersection over union of predicted and actual labels
- **F1 Score** — harmonic mean of precision and recall
- **Log Loss** — only for probabilistic classifiers (LR); penalises confident wrong predictions

## Key Steps

1. Load and explore the loan dataset
2. Feature engineering: extract day-of-week from date, encode categoricals
3. Normalise features with `StandardScaler`
4. Train each classifier with `GridSearchCV` (or manual tuning)
5. Evaluate on test set using all three metrics
6. Produce a comparison report table
