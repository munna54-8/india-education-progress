# India's Education Progress & Gender Gap: 25-Year Trend Analysis

## Problem
How has India's education system actually progressed over the last 25 years, and is the gender gap in literacy closing — or stuck?

## Data source & collection method
7 official World Bank / UNESCO Institute for Statistics indicators for India (2000-2024): literacy by gender, primary and lower-secondary completion rates, school enrollment gender parity, and education spending as % of GDP. Pulled directly from the World Bank's public API — no key or signup required.

## Approach
- Python (requests, Pandas) to pull 7 indicators across 25 years, with retry logic for network timeouts
- Reshaped into a year-by-indicator table for trend analysis
- Calculated the gender literacy gap trend, overall literacy growth, and spending-vs-outcome comparison

## Key findings
- **Gender parity in school enrollment was achieved around 2012** and has held near or above 1.0 since — but the adult literacy gender gap still sits at 15 percentage points, because literacy figures include older generations of women who never had equal access. This is a stock problem (accumulated history), not a current-enrollment problem.
- Overall literacy rose from 61.0% (2001) to 78.2% (2024), a genuine +17.2 percentage point gain
- The gender literacy gap narrowed from 25.6pp to 15.0pp over the same period — real progress, but still substantial
- Education spending as a share of GDP stayed roughly flat (4.32% in 2000 vs. 4.10% in 2022) even as outcomes improved
- Primary completion has been near-universal (94-99%) for most of the last 15 years; lower-secondary completion is where the real remaining growth is happening (55% in 2002 → 87% in 2024)

## Methodology honesty
The apparent literacy jump in 2023 (76.3% → 81.7%) followed by a pullback in 2024 (78.2%) is very likely a survey-methodology revision, not a genuine one-year swing — literacy is measured via infrequent surveys, not continuous tracking, and the 24-year trend is the reliable signal.

## Tools
Python, Pandas, World Bank API, Chart.js

## Dashboard
[paste your GitHub Pages link here once live]