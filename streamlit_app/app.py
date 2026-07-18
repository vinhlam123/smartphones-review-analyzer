import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Beyond Star Ratings",
    page_icon="📱",
    layout="wide"
)

@st.cache_data
def load_data():
    BASE = "/Users/vinhlam/PycharmProjects/smartphones-review-analyzer/data/processed/"
    brand = pd.read_csv(BASE + "summary_brand.csv")
    brand_topic = pd.read_csv(BASE + "summary_brand_topic.csv")
    brand_price = pd.read_csv(BASE + "summary_brand_price.csv")
    features = pd.read_csv(BASE + "summary_features.csv")
    return brand, brand_topic, brand_price, features

df_brand, df_brand_topic, df_brand_price, df_features = load_data()

st.title("📱 Beyond Star Ratings")
st.subheader("How Brand Loyalty and Price Shape Smartphone Sentiment — with AI Feature Analysis")
st.markdown("*Analyzing 124,000+ Amazon reviews across 9 smartphone brands using VADER sentiment analysis and LDA topic modeling.*")
st.divider()

st.sidebar.header("Filters")
selected_brands = st.sidebar.multiselect(
    "Select Brands",
    options=sorted(df_brand['brand'].unique()),
    default=sorted(df_brand['brand'].unique())
)

brand_filtered = df_brand[df_brand['brand'].isin(selected_brands)].copy()

st.header("1. Brand Sentiment Overview")
col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(
        brand_filtered.sort_values('avg_vader', ascending=True),
        x='avg_vader', y='brand', orientation='h',
        color='avg_vader', color_continuous_scale='RdYlGn',
        color_continuous_midpoint=0,
        labels={'avg_vader': 'Avg Sentiment Score', 'brand': 'Brand'},
        title='Average VADER Sentiment by Brand'
    )
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.scatter(
        brand_filtered,
        x='five_star_rate', y='avg_vader',
        size='total_reviews', color='brand',
        hover_name='brand',
        labels={'five_star_rate': '5-Star Rate (%) — Loyalty Proxy',
                'avg_vader': 'Avg Sentiment Score'},
        title='Brand Loyalty vs Sentiment Score'
    )
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.header("2. What Topics Drive Sentiment?")
topic_filtered = df_brand_topic[df_brand_topic['brand'].isin(selected_brands)]
pivot = topic_filtered.pivot_table(
    values='avg_vader', index='brand', columns='topic_label', aggfunc='mean'
)
fig3 = px.imshow(
    pivot,
    color_continuous_scale='RdYlGn',
    color_continuous_midpoint=0,
    zmin=-0.3, zmax=0.6,
    labels={'color': 'Avg Sentiment'},
    title='Sentiment Heatmap: Brand × Topic',
    aspect='auto'
)
st.plotly_chart(fig3, use_container_width=True)

st.divider()

st.header("3. Does Price Matter?")
price_filtered = df_brand_price[df_brand_price['brand'].isin(selected_brands)]
TIER_ORDER = ['Budget (<$100)', 'Mid-Range ($100-$250)', 'Upper-Mid ($250-$500)', 'Premium ($500+)']
price_filtered = price_filtered[price_filtered['price_tier'].isin(TIER_ORDER)]
fig4 = px.bar(
    price_filtered,
    x='brand', y='avg_vader',
    color='price_tier',
    barmode='group',
    category_orders={'price_tier': TIER_ORDER},
    labels={'avg_vader': 'Avg Sentiment Score', 'brand': 'Brand'},
    title='Sentiment Score by Brand and Price Tier'
)
st.plotly_chart(fig4, use_container_width=True)

st.divider()

st.header("4. AI & Hardware Feature Impact")
df_features['sentiment_lift'] = df_features['avg_vader_with'] - df_features['avg_vader_without']
fig5 = px.bar(
    df_features.sort_values('sentiment_lift', ascending=True),
    x='sentiment_lift', y='feature', orientation='h',
    color='sentiment_lift', color_continuous_scale='RdYlGn',
    labels={'sentiment_lift': 'Sentiment Lift', 'feature': 'Feature'},
    title='Sentiment Lift When Feature is Mentioned'
)
st.plotly_chart(fig5, use_container_width=True)

st.divider()
st.markdown("""
**Data:** Amazon Unlocked Mobile + scraped 2019 reviews (124,000+ reviews, 9 brands)  
**Methods:** VADER Sentiment · LDA Topic Modeling · SQLite · Tableau · Streamlit  
**Tableau Dashboard:** [View Live](https://public.tableau.com/app/profile/vinh.lam3565/viz/Book1_17838755321340/SmartphoneSentimentDashboard)  
**GitHub:** [vinhlam123/smartphones-review-analyzer](https://github.com/vinhlam123/smartphones-review-analyzer)
""")
BASE = "/Users/vinhlam/PycharmProjects/smartphones-review-analyzer/data/processed/"
BASE = "data/processed/"