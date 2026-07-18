import requests
import pandas as pd
import time

MISSING = {
    "SE.ADT.LITR.MA.ZS": "literacy_male",
    "SE.SEC.CMPT.LO.ZS": "lower_secondary_completion_rate",
    "SE.XPD.TOTL.GD.ZS": "education_spend_pct_gdp",
}

def fetch_indicator(code, name, max_attempts=5):
    url = f"https://api.worldbank.org/v2/country/IND/indicator/{code}"
    params = {"format": "json", "date": "2000:2024", "per_page": 100}
    for attempt in range(1, max_attempts + 1):
        try:
            response = requests.get(url, params=params, timeout=45)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"  {name}: attempt {attempt}/{max_attempts} failed ({type(e).__name__}), waiting 5s...")
            time.sleep(5)
    print(f"  {name}: all attempts failed, skipping")
    return None

new_rows = []
for code, name in MISSING.items():
    data = fetch_indicator(code, name)
    if data and len(data) >= 2 and data[1]:
        count = 0
        for r in data[1]:
            if r["value"] is not None:
                new_rows.append({"indicator": name, "year": int(r["date"]), "value": r["value"]})
                count += 1
        print(f"{name}: {count} yearly values collected")
    time.sleep(1)

existing = pd.read_csv("data/raw/education_indicators.csv")
combined = pd.concat([existing, pd.DataFrame(new_rows)], ignore_index=True).drop_duplicates(subset=["indicator", "year"])
combined.to_csv("data/raw/education_indicators.csv", index=False)

print(f"\nTotal indicators now in dataset: {combined['indicator'].nunique()} of 7")