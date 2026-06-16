# 02. Data Wrangling

## Notebook

`02. Data Wrangling.ipynb`

## Objective

Transform the raw API dataset into a clean, ML-ready format with a binary landing outcome label.

---

## Steps

### 1. Landing Outcome Analysis

Examined the 8 distinct values in the `Outcome` column:

| Outcome | Count | Class |
|---------|-------|-------|
| True ASDS | 41 | 1 — Success |
| None None | 19 | 0 — Failure / No attempt |
| True RTLS | 14 | 1 — Success |
| False ASDS | 6 | 0 — Failure |
| True Ocean | 5 | 1 — Success |
| None ASDS | 2 | 0 — No attempt |
| False Ocean | 2 | 0 — Failure |
| False RTLS | 1 | 0 — Failure |

### 2. Binary Label Creation

```python
bad_outcomes = {'False ASDS', 'False Ocean', 'False RTLS', 'None ASDS', 'None None'}
df['Class'] = df['Outcome'].apply(lambda x: 0 if x in bad_outcomes else 1)
```

**Overall success rate:** `df['Class'].mean()` = **0.6667** (66.67%)

### 3. Dataset Summary

| Feature | Value |
|---------|-------|
| Total rows | 90 |
| Successful landings (Class=1) | 60 |
| Unsuccessful (Class=0) | 30 |

**Top launch sites:**
- CCAFS SLC 40: 55 launches
- KSC LC 39A: 22 launches
- VAFB SLC 4E: 13 launches

**Top orbits:** GTO (27), ISS (21), VLEO (14), PO (9), LEO (7)

### 4. Output

`dataset_part_2.csv` — 90 rows × 18 columns (includes `Class` label)
