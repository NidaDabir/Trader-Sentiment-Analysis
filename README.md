## 📊 Trader Performance vs Market Sentiment

🔹 Objective

This project analyzes how market sentiment (Fear vs Greed) influences trader performance and behavior using Hyperliquid trading data.

Dataset

Due to GitHub file size limits, the full dataset is not included.

You can download it here:
- Historical Trader Data: [https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=sharing]
- Sentiment Freed Data: [https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=sharing]

🔹 Methodology
Cleaned and merged sentiment and trading datasets on a daily level
Created key metrics:
PnL (profit/loss)
Win rate
Trade size (risk proxy)
Trade frequency
Long/Short ratio
Performed sentiment-based analysis and trader segmentation
Built a simple predictive model and clustering approach
Developed an interactive Streamlit dashboard

🔹 Key Insights
Higher profitability during Extreme Greed
Traders achieve the highest average PnL during Extreme Greed periods.
Behavior changes with sentiment
Traders take larger positions and higher risks during Greed, while being more cautious during Fear.
Strong short bias in Extreme Greed (~70%)
Indicates profit-taking or counter-trend strategies.
Frequent traders perform more consistently
Suggesting experience and activity improve outcomes.

🔹 Strategy Recommendations
Risk control during Fear
Reduce trade size and exposure due to lower profitability and higher uncertainty.
Increase activity during Greed (for experienced traders)
Frequent traders can capitalize on higher momentum and better performance.

🔹 Bonus Work
Predictive Model
Used Random Forest to predict trade profitability using sentiment and behavior features.
Clustering
Identified trader groups based on activity, trade size, and profitability.
Streamlit Dashboard
Built an interactive dashboard to explore performance and behavior dynamically.
🔹 How to Run
pip install -r requirements.txt
streamlit run app/taskapp.py
