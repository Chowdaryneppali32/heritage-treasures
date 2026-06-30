# Tableau Build Guide — Heritage Treasures

This guide recreates the three scenarios in Tableau Desktop using
`data/unesco_heritage_sites_2019.csv`.

## 1. Connect the data

1. Open Tableau Desktop → **Connect → Text File** → select
   `unesco_heritage_sites_2019.csv`.
2. Confirm field types: `Date_inscribed` should auto-detect as Date; if not,
   right-click the field in the Data pane → **Change Data Type → Date**.
3. Go to **Sheet 1** to begin building.

## 2. Scenario 1 — Heritage Sites by Country (Treemap)

1. New worksheet, rename it **"Sites by Country"**.
2. Drag **Country** to the **Color** shelf and to **Detail**.
3. Drag **Name_en** to the **Marks → Size** shelf, set the aggregation to
   **Count Distinct** (right-click the pill → Measure → Count (Distinct)).
4. Change the Marks type dropdown to **Square** (Tableau will switch
   automatically when you also drop Size and Color this way, but verify it's
   on "Square"/Treemap behavior).
5. Drag **Country** to **Label** as well, so block labels show the country
   name.
6. Optional: add **Region** to **Filters** as a quick filter so a mentor or
   user can isolate one region at a time.
7. Sort descending by the Count Distinct of Name_en for a cleaner reading
   order (right-click axis/legend → Sort → Descending).

## 3. Scenario 2 — Heritage Sites at Risk (Pie Chart)

1. New worksheet, rename it **"Sites at Risk"**.
2. Drag **Danger** to **Color**.
3. Drag **Name_en** to **Angle** (Count Distinct).
4. Change Marks type to **Pie**.
5. Drag **Name_en** (Count Distinct) to **Label** too, and add a Quick Table
   Calculation → **Percent of Total** on a duplicate copy of the measure on
   the Label shelf, so each slice shows both count and percentage.
6. Set colors: right-click the Danger color legend → Edit Colors → assign a
   warm red to "In Danger" and a muted green to "Not in Danger" for clarity.
7. Optional: build a companion text table listing site names for In Danger
   only, using a filter (Danger = "In Danger") on a separate sheet, then
   place both on the same dashboard.

## 4. Scenario 3 — Regional Inscription Trends (Line Chart)

1. New worksheet, rename it **"Regional Inscription Trends"**.
2. Drag **Date_inscribed** to **Columns**; right-click the resulting pill →
   set to **Year** (continuous, green pill) rather than the default discrete
   date hierarchy.
3. Drag **Name_en** to **Rows**, aggregation **Count Distinct**, this gives
   inscriptions per year.
4. To get a *cumulative* trend (running total) rather than per-year counts:
   right-click the Count Distinct(Name_en) pill on Rows → **Add Table
   Calculation** → **Running Total**, computed using **Date_inscribed**.
5. Drag **Region** to **Color** to segment the lines.
6. Change Marks type to **Line**.
7. Optional: add a discrete **Region** filter / highlight action so users can
   isolate a single region's trend line.

## 5. Assemble the Dashboard

1. Create a new Dashboard, name it **"Heritage Treasures Overview"**.
2. Set size to **Automatic** (or a fixed 1300×900 for consistent export).
3. Drag in all three sheets, arranging Scenario 1 across the top (it benefits
   from width) and Scenarios 2 and 3 side-by-side below.
4. Add a **Text** object at the top with the dashboard title and a one-line
   summary.
5. Add **filter actions**: clicking a region block in the treemap (Scenario
   1) can filter the line chart (Scenario 3) — set this up via **Dashboard →
   Actions → Add Action → Filter**, source sheet = Sites by Country, target
   sheet = Regional Inscription Trends, run on **Select**.

## 6. Build the Story

1. **Story → New Story**, name it **"Heritage Treasures: A World Heritage
   Story"**.
2. Story point 1: the Dashboard overview, captioned "755 sites across 99
   countries, 1978–2019."
3. Story point 2: duplicate, filter to top 10 countries, captioned "A handful
   of countries hold a disproportionate share of the world's heritage."
4. Story point 3: duplicate, focus on Scenario 2, captioned "A small but
   meaningful fraction of sites are formally at risk."
5. Story point 4: duplicate, focus on Scenario 3, captioned "Some regions
   have accelerated their conservation efforts far faster than others."

## 7. Publish / Export

- **Tableau Public** or **Tableau Server**: Server → Publish Workbook.
- For local sharing: **File → Export Packaged Workbook (.twbx)** so the data
  is bundled with the workbook in a single file.
