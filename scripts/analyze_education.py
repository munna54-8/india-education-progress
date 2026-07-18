import pandas as pd

df = pd.read_csv("data/raw/education_indicators.csv")
wide = df.pivot(index="year", columns="indicator", values="value").sort_index()
wide.to_csv("data/clean/education_wide.csv")

print("=== FULL DATA, BY YEAR ===")
print(wide.to_string())

# Gender gap trend
if "literacy_male" in wide.columns and "literacy_female" in wide.columns:
    wide["gender_gap_pp"] = wide["literacy_male"] - wide["literacy_female"]
    valid_gap = wide["gender_gap_pp"].dropna()
    if len(valid_gap) >= 2:
        first_year, last_year = valid_gap.index[0], valid_gap.index[-1]
        print(f"\n=== GENDER LITERACY GAP ===")
        print(f"{first_year}: {valid_gap.iloc[0]:.1f} percentage points")
        print(f"{last_year}: {valid_gap.iloc[-1]:.1f} percentage points")
        change = valid_gap.iloc[-1] - valid_gap.iloc[0]
        print(f"Change: {change:+.1f} pp ({'narrowing' if change < 0 else 'widening'})")

# Literacy growth
if "literacy_total" in wide.columns:
    valid_lit = wide["literacy_total"].dropna()
    if len(valid_lit) >= 2:
        print(f"\n=== OVERALL LITERACY GROWTH ===")
        print(f"{valid_lit.index[0]}: {valid_lit.iloc[0]:.1f}%")
        print(f"{valid_lit.index[-1]}: {valid_lit.iloc[-1]:.1f}%")
        print(f"Change: {valid_lit.iloc[-1] - valid_lit.iloc[0]:+.1f} percentage points")

# Education spending trend
if "education_spend_pct_gdp" in wide.columns:
    valid_spend = wide["education_spend_pct_gdp"].dropna()
    if len(valid_spend) >= 2:
        print(f"\n=== EDUCATION SPENDING (% of GDP) ===")
        print(f"{valid_spend.index[0]}: {valid_spend.iloc[0]:.2f}%")
        print(f"{valid_spend.index[-1]}: {valid_spend.iloc[-1]:.2f}%")