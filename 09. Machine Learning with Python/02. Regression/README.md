# 02. Regression

Regression algorithms predict a continuous numerical value based on input features. This module covers four regression techniques from simple to complex.

## Notebooks

| Notebook | Description |
|----------|-------------|
| `01. Simple Linear Regression.ipynb` | One independent variable predicts one continuous outcome |
| `02. Multiple Linear Regression.ipynb` | Multiple independent variables used simultaneously |
| `03. Polynomial Regression.ipynb` | Models non-linear relationships using polynomial features |
| `04. Non-Linear Regression.ipynb` | Fits complex curves using exponential/logistic/sigmoidal functions |

## Key Concepts

### Simple Linear Regression
Models the linear relationship between one predictor and one response:

```
y = b0 + b1 * x
```

Coefficients estimated by minimising Mean Squared Error (MSE).

### Multiple Linear Regression
Extends simple linear regression to multiple predictors:

```
y = b0 + b1*x1 + b2*x2 + ... + bn*xn
```

### Polynomial Regression
Transforms features into polynomial terms to fit curves:

```
y = b0 + b1*x + b2*x² + b3*x³ ...
```

### Non-Linear Regression
Uses non-linear functions (e.g. sigmoid, exponential) fitted via `scipy.optimize.curve_fit`.

## Evaluation Metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| MAE | mean(|y - ŷ|) | Average absolute error |
| MSE | mean((y - ŷ)²) | Penalises large errors more |
| RMSE | √MSE | Same units as target variable |
| R² | 1 - SS_res/SS_tot | Proportion of variance explained (0–1) |
