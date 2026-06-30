# Heritage Treasures: An In-Depth Analysis of UNESCO World Heritage Sites (2019)

A comprehensive project exploring the UNESCO World Heritage Sites dataset, visualizing
distribution, risk status, and inscription trends to support preservation decision-making.

## What's in this package

```
heritage-treasures/
├── data/
│   ├── unesco_heritage_sites_2019.csv   # Source dataset (755 sites, 99 countries, 5 regions)
│   └── generate_data.py                  # Script used to build the dataset
├── dashboard/
│   ├── index.html                        # Standalone interactive web dashboard
│   └── data.json                         # Dataset embedded for the dashboard
├── tableau/
│   └── TABLEAU_BUILD_GUIDE.md            # Step-by-step guide to recreate all 3 scenarios in Tableau Desktop
└── README.md
```

## Dataset schema

| Column          | Description                                      |
|-----------------|---------------------------------------------------|
| Site_ID         | Unique identifier                                 |
| Name_en         | Site name (English)                               |
| Country         | Country where the site is located                 |
| Region          | UNESCO region grouping                            |
| Category        | Cultural / Natural / Mixed                         |
| Date_inscribed  | Date the site was added to the World Heritage List |
| Danger          | "In Danger" or "Not in Danger"                    |

## Scenarios covered

**Scenario 1 — Heritage Sites by Country.** A treemap where each block represents a
country, sized by number of heritage sites, filterable by region.

**Scenario 2 — Heritage Sites at Risk.** A donut chart segmenting sites into "In Danger"
and "Not in Danger," with a scrollable list of every endangered site.

**Scenario 3 — Regional Inscription Trends.** A cumulative line chart of new site
inscriptions by year, segmented and toggleable by region (1978–2019).

## Running the web dashboard

No build step required — it's a static page.

```
cd dashboard
python3 -m http.server 8000
```

Then open `http://localhost:8000` in a browser. (Opening `index.html` directly via
`file://` may block the `fetch('data.json')` call in some browsers due to CORS —
use a local server as shown above.)

## Building it in Tableau Desktop

See `tableau/TABLEAU_BUILD_GUIDE.md` for a full walkthrough: connecting the CSV,
building each of the three visualizations, and assembling the dashboard + story.

## Note on the dataset

The original Kaggle "UNESCO World Heritage Sites 2019" dataset could not be
downloaded directly into this environment (no network access to Kaggle). This
package instead ships a synthetically generated dataset with the same schema
(Country, Name_en, Region, Date_inscribed, Danger) and realistic distributions
(e.g. Italy, China, and Spain holding the most sites; ~6% of sites in danger;
inscriptions spanning 1978–2019). Swap in the real CSV from Kaggle and the
dashboard/Tableau workbook will work unchanged, provided column names match.
