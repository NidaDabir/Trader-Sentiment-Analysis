import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Trader Sentiment Dashboard", layout="wide")
st.title("📊 Trader Performance vs Market Sentiment")

# Load data
@st.cache_data
def load_data():
    sentiment = pd.read_csv("data/fear_greed_index.csv")
    trades = pd.read_csv("data/historical_data.csv")
    

    sentiment['date'] = pd.to_datetime(sentiment['date'])
    trades['Timestamp IST'] = pd.to_datetime(trades['Timestamp IST'], errors='coerce')

    sentiment['Date'] = sentiment['date'].dt.date
    trades['Date'] = trades['Timestamp IST'].dt.date

    df = pd.merge(trades, sentiment[['Date','classification']], on='Date', how='inner')

    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    df['side'] = df['side'].str.strip().str.upper()
    df['side'] = df['side'].replace({'BUY':'LONG','SELL':'SHORT'})

    df['win'] = df['closed_pnl'] > 0

    return df

df = load_data()

# Sidebar filter
st.sidebar.header("Filters")
sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    options=df['classification'].unique(),
    default=df['classification'].unique()
)

filtered_df = df[df['classification'].isin(sentiment_filter)]

# =========================
# METRICS
# =========================
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Avg PnL", round(filtered_df['closed_pnl'].mean(), 2))
col2.metric("Win Rate", f"{round(filtered_df['win'].mean()*100, 2)}%")
col3.metric("Avg Trade Size", round(filtered_df['size_usd'].mean(), 2))

# =========================
# PnL Distribution
# =========================
st.subheader("PnL Distribution")

fig, ax = plt.subplots()
order = ['Extreme Fear','Fear','Neutral','Greed','Extreme Greed']

sns.boxplot(x='classification', y='closed_pnl', data=filtered_df, order=order, ax=ax)
ax.set_xlabel("Market Sentiment")
ax.set_ylabel("Closed PnL")
ax.set_title("PnL Distribution by Sentiment")
plt.xticks(rotation=45)
st.pyplot(fig)

# =========================
# Trade Size by Sentiment
# =========================
st.subheader("Average Trade Size by Sentiment")

size_data = filtered_df.groupby('classification')['size_usd'].mean()

st.bar_chart(size_data)

# =========================
# Trade Frequency Chart
# =========================
st.subheader("Trade Frequency")

freq = filtered_df['classification'].value_counts()
st.bar_chart(freq)
# =========================
# Long/Short Bias
# =========================
st.subheader("Long vs Short Bias")

bias = pd.crosstab(filtered_df['classification'], filtered_df['side'], normalize='index')

st.dataframe(bias)


st.sidebar.write("### Insights")
st.sidebar.write("• Highest profitability during Extreme Greed")
st.sidebar.write("• Traders increase risk in Greed periods")
st.sidebar.write("• Strong short bias in Extreme Greed (~70%)")
