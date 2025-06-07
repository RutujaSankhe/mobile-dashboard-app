import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load data
df = pd.read_csv("Flipkart_Mobiles.csv")

# Preprocessing
df.columns = df.columns.str.strip()
df.dropna(subset=["Brand", "Model", "Memory", "Storage", "Selling Price"], inplace=True)
df["Memory"] = df["Memory"].str.extract("(\d+)").astype(int)
df["Storage"] = df["Storage"].str.extract("(\d+)").astype(int)

def price_segment(price):
    if price < 10000:
        return "Low Range"
    elif 10000 <= price < 20000:
        return "Mid Range"
    else:
        return "Premium"

df["Price Segment"] = df["Selling Price"].apply(price_segment)

# Streamlit Dashboard
st.title("📱 Indian Mobile Market Analysis Dashboard")

st.sidebar.header("Filters")
selected_brand = st.sidebar.multiselect("Select Brand(s):", options=df["Brand"].unique(), default=df["Brand"].unique())
filtered_df = df[df["Brand"].isin(selected_brand)]

# Price Segment Distribution
st.subheader("Price Segment Distribution")
fig1 = px.histogram(filtered_df, x="Price Segment", color="Price Segment", category_orders={"Price Segment": ["Low Range", "Mid Range", "Premium"]})
st.plotly_chart(fig1)

# Top Brands by Product Count
st.subheader("Top Brands by Product Offerings")
top_brands = filtered_df["Brand"].value_counts().nlargest(10)
fig2 = px.bar(top_brands, x=top_brands.values, y=top_brands.index, orientation='h', labels={'x': 'Number of Products', 'index': 'Brand'})
st.plotly_chart(fig2)

# Memory vs Storage Scatter
st.subheader("Memory vs Storage Distribution")
fig3 = px.scatter(filtered_df, x="Memory", y="Storage", color="Brand", size="Selling Price", hover_data=["Model"])
st.plotly_chart(fig3)

# Ratings Distribution
st.subheader("Ratings Distribution")
fig4 = px.histogram(filtered_df.dropna(subset=["Rating"]), x="Rating", nbins=20)
st.plotly_chart(fig4)

# Brand Coverage Across Segments
st.subheader("Brand Coverage Across Price Segments")
cross_tab = pd.crosstab(filtered_df['Brand'], filtered_df['Price Segment'])
fig5 = px.imshow(cross_tab, labels=dict(x="Price Segment", y="Brand", color="Count"))
st.plotly_chart(fig5)

st.markdown("---")
st.markdown("**Built with ❤️ using Streamlit & Plotly**")
