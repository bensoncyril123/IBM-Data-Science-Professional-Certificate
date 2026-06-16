[![Header](https://user-images.githubusercontent.com/84391594/152703941-8c1b3e93-7358-4274-8c7d-b152d3132814.png)](https://www.coursera.org/professional-certificates/ibm-data-science)

**Author:** Benson Cyril Nana Boakye — Data Scientist & Biostatistician

This repository tracks my progress through the [IBM Data Science Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-science) on Coursera — a 10-course programme covering the full data science lifecycle from foundational concepts through to machine learning and applied capstone projects.

This repository contains documentation and resources used to complete the certification, relevant notes and other code snippets, and proof of certification for each course.

---

## 📄 About

The IBM Data Science Professional Certificate is a rigorous 10-course programme offered by IBM on Coursera. It equips learners with the tools, skills, and practical experience needed to launch a career in data science. Topics span the complete data science workflow — from data collection and wrangling through exploratory analysis, visualisation, machine learning, and final applied capstone work.

This repository serves as a structured record of completed coursework, key learnings, and hands-on projects across all 10 courses. It is organised course-by-course, with each folder containing notebooks, assignments, and relevant notes.

**Certificate Status:** ✅ Fully Completed — All 10 Courses

---

## 📚 Course Progress

| # | Course | Status |
|---|--------|--------|
| 01 | [What is Data Science?](01.%20What%20is%20Data%20Science/) | ✅ Completed |
| 02 | [Tools for Data Science](02.%20Tools%20for%20Data%20Science/) | ✅ Completed |
| 03 | [Data Science Methodology](03.%20Data%20Science%20Methodology/) | ✅ Completed |
| 04 | [Python for Data Science, AI & Development](04.%20Python%20for%20Data%20Science%2C%20AI%20%26%20Development/) | ✅ Completed |
| 05 | [Python Project for Data Science](05.%20Python%20Project%20for%20Data%20Science/) | ✅ Completed |
| 06 | [Databases and SQL for Data Science with Python](06.%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/) | ✅ Completed |
| 07 | [Data Analysis with Python](07.%20Data%20Analysis%20with%20Python/) | ✅ Completed |
| 08 | [Data Visualization with Python](08.%20Data%20Visualization%20with%20Python/) | ✅ Completed |
| 09 | [Machine Learning with Python](09.%20Machine%20Learning%20with%20Python/) | ✅ Completed |
| 10 | [Applied Data Science Capstone](10.%20Applied%20Data%20Science%20Capstone/) | ✅ Completed |

---

## 🏆 Capstone Project Highlights

**Project:** SpaceX Falcon 9 First Stage Landing Prediction

| Metric | Value |
|--------|-------|
| Dataset | 90 Falcon 9 launches |
| Baseline accuracy | 66.7% (always predict success) |
| Best model | Decision Tree — **94.4% test accuracy** |
| Launch sites analysed | 4 (CCAFS LC-40, CCAFS SLC-40, KSC LC-39A, VAFB SLC-4E) |
| Overall landing success rate | 66.7% |

**ML Models Evaluated:**

| Model | CV Accuracy | Test Accuracy |
|-------|-------------|---------------|
| Decision Tree ✅ | 90.4% | **94.4%** |
| K Nearest Neighbors | 87.7% | 88.9% |
| Support Vector Machine | 84.8% | 83.3% |
| Logistic Regression | 84.6% | 83.3% |

---

## 🛠️ Tools

The following tools were used to complete this certification: <br> <br>
  <img src="https://user-images.githubusercontent.com/84391594/152705364-f16bb223-41aa-4510-8113-51171dfe9953.png" height="75">
  <img src="https://user-images.githubusercontent.com/84391594/152705271-083f8784-b3c9-4065-9733-ea3fa8ad5a7a.png" height="75">
  <img src="https://user-images.githubusercontent.com/84391594/152705273-adffe1bf-b509-44d0-b3ac-671cce5071df.svg" height="75">
  <img src="https://user-images.githubusercontent.com/84391594/152705324-68f777a0-3875-4b65-ae96-646643284541.png" height="75">
  <img src="https://user-images.githubusercontent.com/84391594/152705298-bb170d32-3dd0-4ad4-8221-8b7b029116b4.png" height="75">

(Python, Jupyter, GitHub, IBM Watson Studio, IBM Cloud Pak)

---

## 📖 Libraries

The following Python libraries were used throughout the certification: <br>
<p align="left">
  <img src="https://user-images.githubusercontent.com/84391594/152706127-ce41990f-2588-472a-b5df-6b403a5947e6.png" height="35">
  <img src="https://user-images.githubusercontent.com/84391594/152706130-5577011e-ecb3-47aa-af73-f6bd1bda05bc.png" height="35">
  <img src="https://user-images.githubusercontent.com/84391594/152706132-5939da7e-7d1e-43b8-9c46-2d3fe5198dda.png" height="35">
  <img src="https://user-images.githubusercontent.com/84391594/152706135-85cdd35e-922a-414a-a198-c670fbf8fb25.svg" height="35">
  <img src="https://user-images.githubusercontent.com/84391594/152706148-36f27f03-1967-45d1-82d8-f6c149c6f21c.svg" height="35">
  <img src="https://user-images.githubusercontent.com/84391594/152706211-7966848a-a2e1-4c4a-bc08-594a4ca6ff07.png" height="35">
  <img src="https://user-images.githubusercontent.com/84391594/152706214-d018bc5e-1477-4de2-94d7-5c0886e0477d.png" height="35">
  <img src="https://user-images.githubusercontent.com/84391594/152706217-c0cfd9d8-22ad-4c3b-9ac7-70a6cf2799f7.png" height="35">
</p>

(Pandas, NumPy, SciPy, Matplotlib, Seaborn, Plotly, Folium, Scikit-learn)

---

## 🎓 Key Skills Acquired

### 🔗 Data Collection & Acquisition
- Consumed REST APIs using the `requests` library — including SpaceX API for real launch data
- Web scraping with `BeautifulSoup` and `requests` to extract structured data from HTML tables
- Loaded and merged datasets from multiple sources (CSV, API JSON, SQL) into unified DataFrames
- Wrote SQL `SELECT`, `JOIN`, `GROUP BY`, `HAVING`, and sub-query statements against IBM Db2 cloud databases

### 🧹 Data Wrangling & Feature Engineering
- Handled missing values using `.fillna()`, `.dropna()`, and domain-informed imputation strategies
- Detected and treated outliers using IQR and z-score methods
- Applied one-hot encoding (`pd.get_dummies()`) to convert categorical variables into 83 binary features
- Engineered new features from raw data (e.g. payload range bins, booster generation labels, flight number trends)
- Normalised and standardised numerical features using `StandardScaler` ahead of model training

### 📊 Exploratory Data Analysis (EDA)
- Generated descriptive statistics, value counts, and correlation matrices to profile datasets
- Built scatter plots, bar charts, line plots, box plots, and heatmaps to uncover patterns and anomalies
- Identified key trends: success rates improving year-on-year, orbit-type impact on landing outcomes, payload mass thresholds by site
- Used SQL analytical queries to answer business questions directly from the database layer

### 📈 Data Visualisation
- **Matplotlib & Seaborn** — publication-quality static charts with custom styling, colour palettes, and annotations
- **Plotly** — interactive charts (bar, pie, scatter) with hover tooltips and dynamic filtering
- **Folium** — interactive geographic maps with `Circle` markers, `MarkerCluster` for 56 launch records, `PolyLine` distance measurements, and `CartoDB dark_matter` tile layers
- **Plotly Dash** — built a fully interactive web dashboard with a site-selection dropdown, payload range slider, and live-updating pie and scatter charts

### 🤖 Machine Learning
- Implemented and compared four supervised classifiers: **Logistic Regression**, **Support Vector Machine**, **Decision Tree**, and **K-Nearest Neighbors**
- Tuned hyperparameters using `GridSearchCV` with 10-fold cross-validation (`cv=10`) across multi-dimensional parameter grids
- Evaluated models using accuracy score, confusion matrix, and classification report
- Identified **Decision Tree** as the best model at **94.4% test accuracy** — outperforming a 66.7% baseline by 27.7 percentage points
- Applied `train_test_split` with stratification and fixed `random_state` for reproducibility
- Built regression models (simple and multiple linear regression, Ridge, polynomial) for continuous prediction tasks

### 🗄️ Databases & SQL
- Queried a live IBM Db2 cloud database using `ipython-sql` magic commands directly in Jupyter
- Wrote 10+ analytical SQL queries including multi-table joins, aggregate functions, sub-queries, and `RANK()` window functions
- Retrieved targeted subsets (e.g. drone ship landings between 4,000–6,000 kg payload, failed landings in 2015)
- Created and populated tables using DDL/DML (`CREATE TABLE`, `INSERT`, `UPDATE`)

### 🛠️ Tools, Workflow & Best Practices
- Developed entirely within **Jupyter Notebooks** — combining code, markdown narrative, and inline visualisations
- Used **Git & GitHub** for version control — branching, committing, pull requests, and maintaining a structured repository
- Worked within **IBM Watson Studio** and **IBM Cloud Pak** for cloud-hosted notebook execution
- Followed a structured data science methodology (CRISP-DM): business understanding → data understanding → preparation → modelling → evaluation → deployment
- Produced end-to-end reproducible pipelines from raw API data through to final model predictions

---

## 🏅 Certifications

<p align="center"><em>Click on an image to verify the certification</em></p>

<p align="center">
  <a href="https://coursera.org/share/af49c3f45a346544266bc45673b4a42a">
    <img src="certificates/Coursera_Certificate.png" alt="IBM Data Science Professional Certificate — click to verify" width="480">
  </a>
</p>

<p align="center">
  <a href="https://www.credly.com/badges/7d3f256a-58de-4213-8e04-5afd1d48b495/public_url">
    <img src="certificates/IBM_Badge.png" alt="IBM Credly Badge — click to verify" width="380">
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://www.credly.com/badges/7d3f256a-58de-4213-8e04-5afd1d48b495/public_url">
    <img src="certificates/Certificate_Screenshot.png" alt="IBM Professional Certificate Badge — click to verify" width="200">
  </a>
</p>

---

*Repository complete — all 10 courses finished. Certificate awarded 2026.*
