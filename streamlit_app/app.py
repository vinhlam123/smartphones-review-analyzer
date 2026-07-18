import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Beyond Star Ratings", page_icon="📱", layout="wide")

@st.cache_data
def load_data():
    BASE = "data/processed/"
    brand = pd.read_csv(BASE + "summary_brand.csv")
    brand_topic = pd.read_csv(BASE + "summary_brand_topic.csv")
    brand_price = pd.read_csv(BASE + "summary_brand_price.csv")
    features = pd.read_csv(BASE + "summary_features.csv")
    return brand, brand_topic, brand_price, features

df_brand, df_brand_topic, df_brand_price, df_features = load_data()

st.title("📱 Beyond Star Ratings")
st.subheader("How Brand Loyalty and Price Shape Smartphone Sentiment")
st.divider()

st.sidebar.header("Filters")
selected_brands = st.sidebar.multiselect("Select Brands", options=sorted(df_brand["brand"].unique()), default=["Apple","Samsung","Google","OnePlus","Xiaomi","Huawei"])

brand_filtered = df_brand[df_brand["brand"].isin(selected_brands)].copy()

st.header("1. Brand Sentiment Overview")
col1, col2 = st.columns(2)
with col1:
    fig1 = px.bar(brand_filtered.sort_values("avg_vader", ascending=True), x="avg_vader", y="brand", orientation="h", color="avg_vader", color_continuous_scale="RdYlGn", color_continuous_midpoint=0, title="Average Sentiment by Brand")
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    fig2 = px.scatter(brand_filtered, x="five_star_rate", y="avg_vader", size="total_reviews", color="brand", hover_name="brand", title="Brand Loyalty vs Sentiment")
    st.plotly_chart(fig2, use_container_width=True)

st.divider()
st.header("2. Topic Sentiment Heatmap")
topic_filtered = df_brand_topic[df_brand_topic["brand"].isin(selected_brands)]
pivot = topic_filtered.pivot_table(values="avg_vader", index="brand", columns="topic_label", aggfunc="mean")
fig3 = px.imshow(pivot, color_continuous_scale="RdYlGn", color_continuous_midpoint=0, zmin=-0.3, zmax=0.6, title="Sentiment Heatmap: Brand x Topic", aspect="auto")
st.plotly_chart(fig3, use_container_width=True)

st.divider()
st.header("3. Price Tier vs Sentiment")
price_filtered = df_brand_price[df_brand_price["brand"].isin(selected_brands)]
TIER_ORDER = ["Budget (<$100)", "Mid-Range ($100-$250)", "Upper-Mid ($250-$500)", "Premium ($500+)"]
price_filtered = price_filtered[price_filtered["price_tier"].isin(TIER_ORDER)]
fig4 = px.bar(price_filtered, x="brand", y="avg_vader", color="price_tier", barmode="group", category_orders={"price_tier": TIER_ORDER}, title="Sentiment by Brand and Price Tier")
st.plotly_chart(fig4, use_container_width=True)

st.divider()
st.header("4. AI Feature Sentiment Impact")
df_features["sentiment_lift"] = df_features["avg_vader_with"] - df_features["avg_vader_without"]
fig5 = px.bar(df_features.sort_values("sentiment_lift", ascending=True), x="sentiment_lift", y="feature", orientation="h", color="sentiment_lift", color_continuous_scale="RdYlGn", title="Sentiment Lift by Feature")
st.plotly_chart(fig5, use_container_width=True)

st.divider()
st.markdown("""**Data:** 124,000+ Amazon reviews across 9 brands | **Tableau:** [View Dashboard](https://public.tableau.com/app/profile/vinh.lam3565/viz/Book1_17838755321340/SmartphoneSentimentDashboard) | **GitHub:** [vinhlam123/smartphones-review-analyzer](https://github.com/vinhlam123/smartphones-review-analyzer)""")
