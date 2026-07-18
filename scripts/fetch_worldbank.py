import requests
import pandas as pd
import time

INDICATORS = {
    "SE.ADT.LITR.ZS": "literacy_total",
    "SE.ADT.LITR.FE.ZS": "literacy_female",
    "SE.ADT.LITR.MA.ZS": "literacy_male",
    "SE.PRM.CMPT.ZS": "primary_completion_rate",
    "SE.SEC.CMPT.LO.ZS": "lower_secondary_completion_rate",
    "SE.XPD.TOTL.GD.ZS": "education_spend_pct_gdp",
    "SE.ENR.PRSC.FM.ZS": "gender_parity_enrollment",
}

def fetch_indicator(code, name, max_attempts=3):
    url = f"https://api.worldbank.org/v2/country/IND/indicator/{code}"
    params = {"format": "json", "date": "2000:2024", "per_page": 100}

    for attempt in range(1, max_attempts + 1):
        try:
            response = requests.get(url, params=params, timeout=30)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"  {name}: attempt {attempt}/{max_attempts} failed ({type(e).__name__}), retrying...")
            time.sleep(3)
    print(f"  {name}: all attempts failed, skipping")
    return None

all_data = []

for code, name in INDICATORS.items():
    data = fetch_indicator(code, name)
    if data is None:
        continue

    if len(data) < 2 or not data[1]:
        print(f"{name}: NO DATA returned")
        continue

    records = data[1]
    count = 0
    for r in records:
        if r["value"] is not None:
            all_data.append({"indicator": name, "year": int(r["date"]), "value": r["value"]})
            count += 1
    print(f"{name}: {count} yearly values collected")
    time.sleep(1)

df = pd.DataFrame(all_data)
df.to_csv("data/raw/education_indicators.csv", index=False)
print(f"\nTotal records: {len(df)}")
print(f"Indicators successfully collected: {df['indicator'].nunique() if len(df) > 0 else 0} of {len(INDICATORS)}")