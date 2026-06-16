# 03. Exploratory Data Analysis

## Notebooks

| Notebook | Tool | Focus |
|----------|------|-------|
| `03. Exploratory Data Analysis - Data Visualization.ipynb` | Seaborn / Matplotlib | Visual patterns in launch features |
| `03. Exploratory Data Analysis - SQL.ipynb` | IBM Db2 + ipython-sql | Analytical SQL queries |

---

## Data Visualization — Key Charts & Findings

| Chart | Finding |
|-------|---------|
| FlightNumber vs PayloadMass | Later flights (higher number) have higher success rates; heavier payloads tend to fail |
| FlightNumber vs LaunchSite | CCAFS SLC-40 dominates early; KSC LC-39A appears from ~flight 40 with very high success |
| PayloadMass vs LaunchSite | VAFB SLC-4E has no launches with payload > 10,000 kg |
| Success Rate by Orbit | ES-L1, GEO, HEO, SSO = 100%; GTO ≈ 50% (hardest) |
| FlightNumber vs Orbit | LEO success improves with experience; GTO shows no time trend |
| PayloadMass vs Orbit | ISS/LEO/PO land successfully even with heavy payloads |
| Yearly Success Trend | Success grew from 0% (2010) to 85%+ (2020) — continuous engineering improvement |

**Feature engineering output:** `dataset_part_3.csv` — 80 one-hot encoded features (from `pd.get_dummies()`)

---

## SQL Analysis — 10 Queries

| Task | Query Focus | Key Result |
|------|-------------|------------|
| 1 | Unique launch sites | 4 distinct sites |
| 2 | Sites starting with 'CCA' | CCAFS LC-40, CCAFS SLC-40 |
| 3 | NASA CRS total payload | 45,596 kg |
| 4 | F9 v1.1 avg payload | 2,928 kg |
| 5 | First successful ground landing | December 22, 2015 |
| 6 | Drone ship boosters, payload 4k-6k kg | F9 FT B1022, B1026, B1021.2, B1031.2 |
| 7 | Mission outcome totals | Success: 99, Failure (in flight): 1 |
| 8 | Max payload boosters (subquery) | 12 F9 B5 boosters at 15,400 kg |
| 9 | Failed drone ship landings, 2015 | F9 v1.1 B1012 & B1015 at CCAFS LC-40 |
| 10 | Landing outcome ranking 2010-2017 | No attempt (10), Failure/Success drone ship (5 each) |

**Database:** IBM Db2 cloud — table `SPACEXTBL`
