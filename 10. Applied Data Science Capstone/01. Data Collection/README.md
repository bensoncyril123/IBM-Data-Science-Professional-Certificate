# 01. Data Collection

Two methods were used to collect SpaceX Falcon 9 launch data.

## Notebooks

| Notebook | Method | Output |
|----------|--------|--------|
| `01. Data Collection - API.ipynb` | SpaceX REST API | `dataset_part_1.csv` |
| `01. Data Collection - Web Scraping.ipynb` | Wikipedia (BeautifulSoup) | `spacex_web_scraped.csv` |

---

## Method 1: SpaceX REST API

**Endpoint:** `https://api.spacexdata.com/v4/launches/past`

- Queried all past launches and filtered to Falcon 9 only (removed Falcon 1)
- Reset `FlightNumber` sequentially (1–90)
- Made nested API calls to `/cores`, `/launchpads`, and `/payloads` to enrich each record
- Filled 5 missing `PayloadMass` values with the column mean
- Retained 26 missing `LandingPad` values as NaN

**Helper Functions:** `getBoosterVersion()`, `getLaunchSite()`, `getPayloadData()`, `getCoreData()`

**Result:** 90 rows × 17 columns → `dataset_part_1.csv`

---

## Method 2: Web Scraping (Wikipedia)

**Source:** Wikipedia — Falcon 9 and Falcon Heavy launch records (snapshot: June 9, 2021)

- Used `BeautifulSoup` to parse HTML `wikitable` elements
- Extracted all column headers from `<th>` tags
- Iterated rows and cells, handling rowspan attributes
- Applied helper functions to clean dates, masses, and landing outcomes

**Helper Functions:** `date_time()`, `booster_version()`, `landing_status()`, `get_mass()`, `extract_column_from_header()`

**Result:** `spacex_web_scraped.csv`
