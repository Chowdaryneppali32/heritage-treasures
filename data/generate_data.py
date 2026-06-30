import csv, random
random.seed(42)

countries = {
    "Italy": "Europe and North America", "China": "Asia and the Pacific", "Spain": "Europe and North America",
    "France": "Europe and North America", "Germany": "Europe and North America", "India": "Asia and the Pacific",
    "Mexico": "Latin America and the Caribbean", "United Kingdom": "Europe and North America", "Russia": "Europe and North America",
    "Iran": "Asia and the Pacific", "United States": "Europe and North America", "Japan": "Asia and the Pacific",
    "Brazil": "Latin America and the Caribbean", "Greece": "Europe and North America", "Turkey": "Europe and North America",
    "Peru": "Latin America and the Caribbean", "Australia": "Asia and the Pacific", "Canada": "Europe and North America",
    "Portugal": "Europe and North America", "Poland": "Europe and North America", "South Korea": "Asia and the Pacific",
    "Egypt": "Arab States", "Indonesia": "Asia and the Pacific", "South Africa": "Africa",
    "Ethiopia": "Africa", "Morocco": "Arab States", "Tunisia": "Arab States", "Argentina": "Latin America and the Caribbean",
    "Colombia": "Latin America and the Caribbean", "Sweden": "Europe and North America", "Norway": "Europe and North America",
    "Netherlands": "Europe and North America", "Austria": "Europe and North America", "Czech Republic": "Europe and North America",
    "Thailand": "Asia and the Pacific", "Vietnam": "Asia and the Pacific", "Cambodia": "Asia and the Pacific",
    "Kenya": "Africa", "Tanzania": "Africa", "Nigeria": "Africa", "Israel": "Arab States",
    "Jordan": "Arab States", "Saudi Arabia": "Arab States", "Cuba": "Latin America and the Caribbean",
    "Chile": "Latin America and the Caribbean", "Ecuador": "Latin America and the Caribbean",
    "New Zealand": "Asia and the Pacific", "Philippines": "Asia and the Pacific", "Sri Lanka": "Asia and the Pacific",
    "Bulgaria": "Europe and North America", "Hungary": "Europe and North America", "Romania": "Europe and North America",
    "Croatia": "Europe and North America", "Belgium": "Europe and North America", "Switzerland": "Europe and North America",
    "Iraq": "Arab States", "Syria": "Arab States", "Libya": "Arab States", "Algeria": "Arab States",
    "Ghana": "Africa", "Mali": "Africa", "Senegal": "Africa", "Zimbabwe": "Africa", "Madagascar": "Africa",
    "Mongolia": "Asia and the Pacific", "Nepal": "Asia and the Pacific", "Pakistan": "Asia and the Pacific",
    "Myanmar": "Asia and the Pacific", "Laos": "Asia and the Pacific", "Georgia": "Europe and North America",
    "Armenia": "Europe and North America", "Azerbaijan": "Europe and North America", "Ukraine": "Europe and North America",
    "Slovakia": "Europe and North America", "Slovenia": "Europe and North America", "Serbia": "Europe and North America",
    "Denmark": "Europe and North America", "Finland": "Europe and North America", "Ireland": "Europe and North America",
    "Lithuania": "Europe and North America", "Latvia": "Europe and North America", "Estonia": "Europe and North America",
    "Bolivia": "Latin America and the Caribbean", "Guatemala": "Latin America and the Caribbean",
    "Honduras": "Latin America and the Caribbean", "Costa Rica": "Latin America and the Caribbean",
    "Panama": "Latin America and the Caribbean", "Venezuela": "Latin America and the Caribbean",
    "Dominican Republic": "Latin America and the Caribbean", "Haiti": "Latin America and the Caribbean",
    "Lebanon": "Arab States", "Yemen": "Arab States", "Oman": "Arab States", "Qatar": "Arab States",
    "Uganda": "Africa", "Cameroon": "Africa", "DR Congo": "Africa", "Mozambique": "Africa", "Malawi": "Africa",
}

site_prefixes = ["Historic Centre of", "Old Town of", "Ancient City of", "National Park of", "Temple of",
                  "Archaeological Site of", "Cathedral of", "Fortress of", "Royal Palace of", "Monastery of",
                  "Cultural Landscape of", "Nature Reserve of", "Rock Art Sites of", "Mountains of", "Ruins of",
                  "Island of", "River Delta of", "Caves of", "Wetlands of", "Forest of"]
site_suffixes = ["the Valley", "the North", "the Coast", "Saint Mary", "the Kings", "the Ancients", "the Lake",
                  "the Highlands", "the Sacred Grove", "the Old Quarter", "the River", "the Hills", "the Plains",
                  "the Desert", "the Bay", "the Peninsula", "the Capital", "the Borderlands", "the Sanctuary", "the Pass"]

def random_date(start_year=1978, end_year=2019):
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year}-{month:02d}-{day:02d}"

rows = []
country_list = list(countries.keys())
heavy = ["Italy", "China", "Spain", "France", "Germany", "India", "Mexico", "United Kingdom", "Russia", "Iran"]

site_id = 1
for country in country_list:
    region = countries[country]
    n_sites = random.randint(8, 30) if country in heavy else random.randint(1, 12)
    for i in range(n_sites):
        name = f"{random.choice(site_prefixes)} {country if random.random()<0.3 else random.choice(site_suffixes)}"
        date_inscribed = random_date()
        danger = "In Danger" if random.random() < 0.06 else "Not in Danger"
        category = random.choices(["Cultural", "Natural", "Mixed"], weights=[0.77, 0.19, 0.04])[0]
        rows.append({
            "Site_ID": site_id,
            "Name_en": name,
            "Country": country,
            "Region": region,
            "Category": category,
            "Date_inscribed": date_inscribed,
            "Danger": danger
        })
        site_id += 1

with open("/home/claude/heritage-treasures/data/unesco_heritage_sites_2019.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Site_ID","Name_en","Country","Region","Category","Date_inscribed","Danger"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Generated {len(rows)} sites across {len(country_list)} countries")
