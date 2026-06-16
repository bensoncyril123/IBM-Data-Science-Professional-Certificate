# 04. Interactive Visual Analytics

## Notebooks / Scripts

| File | Tool | Purpose |
|------|------|---------|
| `04. Interactive Visual Analytics - Folium.ipynb` | Folium | Geographic launch site analysis |
| `spacex_dash_app.py` | Plotly Dash | Interactive web dashboard |
| `spacex_launch_geo.csv` | Data | Launch coordinates dataset |

---

## Folium — Geographic Analysis

### Task 1: Mark All Launch Sites
- Created a `folium.Map` centred on NASA Johnson Space Center
- Added `folium.Circle` markers (orange, radius=50m) for each of the 4 launch sites with popup labels

**Launch Site Coordinates:**

| Site | Lat | Long |
|------|-----|------|
| CCAFS LC-40 | 28.562°N | 80.577°W |
| CCAFS SLC-40 | 28.563°N | 80.577°W |
| KSC LC-39A | 28.573°N | 80.647°W |
| VAFB SLC-4E | 34.633°N | 120.611°W |

### Task 2: Success/Failure Launch Markers
- Used `MarkerCluster` to group the 56 individual launch records by site
- Green markers = Class 1 (success), Red markers = Class 0 (failure)

### Task 3: Proximity Analysis (from CCAFS SLC-40)

| Feature | Distance |
|---------|---------|
| Coastline | 0.87 km |
| Highway (US-1) | 0.57 km |
| Railway | 0.72 km |
| Nearest city (Titusville) | ~27.5 km |

**Geographic insights:** All sites are within 10 km of the coast (enabling ocean drone ship recovery), close to transport infrastructure, and far enough from cities for public safety.

---

## Plotly Dash — Interactive Dashboard

### Features
- **Dropdown** — select individual launch site or all sites
- **Pie chart** — success vs failure proportion for selected site
- **Range slider** — filter by payload mass (0–15,600 kg)
- **Scatter plot** — payload vs success class, colour-coded by booster serial

### Key Dashboard Findings
- KSC LC-39A has the highest success rate (~77%)
- VAFB SLC-4E has no launches with payload > 10,000 kg
- Block 5 (B5) boosters significantly outperform earlier blocks
