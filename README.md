# 📊 Trader Sentiment Analysis

This project analyzes how market sentiment (Fear vs Greed) influences trader behavior and performance using Hyperliquid trading data.

# 🔹 Objective

To understand how trader performance and behavior change under different market sentiment conditions and derive actionable trading strategies.


# 🔹 Methodology

- Cleaned and preprocessed both datasets
- Converted timestamps and aligned data on daily level
- Merged trader data with sentiment data using Date

- Created key metrics:
  - Closed PnL
  - Win rate
  - Trade frequency
  - Average trade size
  - Long/Short ratio

- Segmented traders:
  - Frequent vs Infrequent
  - Winners vs Losers
  - High vs Low trade size

# 🔹 Key Insights

1. **Highest profitability occurs during Extreme Greed**
   - Average PnL peaks during these periods.

2. **Risk-taking increases in Greed markets**
   - Trade size is significantly higher compared to Fear periods.

3. **Strong short bias during Extreme Greed (~70% SHORT)**
   - Indicates profit booking or counter-trend strategies.

4. **Frequent traders perform more consistently**
   - Suggests experience improves stability.

# 🔹 Strategy Recommendations

- During Fear periods:
  - Reduce leverage and trade size to minimize losses

- During Greed periods:
  - Increase activity but manage risk carefully
  - Avoid excessive shorting despite market optimism

# 🔹 Bonus Work

Predictive Model

Used Random Forest to predict trade profitability using sentiment and behavior features.

Clustering

Identified trader groups based on activity, trade size, and profitability.

Streamlit Dashboard

A Streamlit app is included to interactively explore:
- PnL distribution
- Trade frequency
- Risk behavior
- Long/Short bias

Run using:

streamlit run app/taskapp.py



# Dataset

Due to GitHub file size limits, the full dataset is not included.

You can download it here:
- Historical Trader Data: [https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=sharing]
- Sentiment Freed Data: [https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=sharing]




# 🔷  Requirements
## Requirements

pip install -r task-requirements.txt
