import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import json
import os
import pyarrorw.lib as _lib

st.set_page_config(page_title="PhonePe Transaction Insights", layout="wide")

# --- Download CSV Data ---
@st.cache_data
def load_transaction_data():
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv"
    df = pd.read_csv(url)
    # Rename columns for consistency
    df.rename(columns={"state": "State", "active cases": "Transaction_amount"}, inplace=True)
    return df

# --- Download GeoJSON for India States ---
@st.cache_data
def load_india_geojson():
    geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response = requests.get(geojson_url)
    geojson_data = response.json()
    # Standardize state names for mapping
    for feature in geojson_data["features"]:
        name = feature["properties"].get("ST_NM", "")
        feature["properties"]["State_Name"] = name.lower().strip()
    return geojson_data

# --- Load Data ---
df = load_transaction_data()
geojson_data = load_india_geojson()

# --- Sidebar Filters ---
st.sidebar.header("Filters")
states = sorted(df["State"].unique())
years = sorted(df.get("Year", pd.Series([2020])).unique()) if "Year" in df.columns else [2020]
selected_years = st.sidebar.multiselect("Select Year(s):", years, default=years)
selected_states = st.sidebar.multiselect("Select State(s):", states, default=states)

# Filter by year if column exists
if "Year" in df.columns:
    df_filtered = df[df["State"].isin(selected_states) & df["Year"].isin(selected_years)]
else:
    df_filtered = df[df["State"].isin(selected_states)]

# --- Main Title ---
st.title("PhonePe Transaction Insights Dashboard")
st.markdown("#### India Map Data Visualization")

# --- Metrics ---
total_txn = df_filtered["Transaction_amount"].sum()
avg_txn = df_filtered["Transaction_amount"].mean()
num_states = df_filtered["State"].nunique()
st.metric("Total Transaction Amount", f"{total_txn:,}")
st.metric("Average Transaction Amount per State", f"{avg_txn:,.2f}")
st.metric("Number of States", f"{num_states}")

# --- Choropleth Map ---
df_map = df_filtered.copy()
df_map["State_Name"] = df_map["State"].str.lower().str.strip()

fig = px.choropleth(
    df_map,
    geojson=geojson_data,
    locations="State_Name",
    featureidkey="properties.State_Name",
    color="Transaction_amount",
    color_continuous_scale="Blues",
    hover_name="State",
    hover_data={"Transaction_amount": True},
    title="Transaction Amount by State (India Map)",
    height=700  # Make the map bigger
)

# Custom hover template for state info
fig.update_traces(
    hovertemplate="<b>%{hovertext}</b><br>Transaction Amount: %{z:,}<extra></extra>"
)

fig.update_geos(fitbounds="locations", visible=False)
st.plotly_chart(fig, use_container_width=True)

# --- Bar Chart: State-wise Transaction Amount ---
st.subheader("State-wise Transaction Amount")
fig_bar = px.bar(
    df_filtered.sort_values("Transaction_amount", ascending=False),
    x="State", y="Transaction_amount",
    color="Transaction_amount",
    color_continuous_scale="Blues",
    title="Total Transaction Amount by State"
)
st.plotly_chart(fig_bar, use_container_width=True)

# --- Pie Chart: Transaction Distribution ---
st.subheader("Transaction Distribution by State")
fig_pie = px.pie(
    df_filtered,
    names="State",
    values="Transaction_amount",
    title="Transaction Amount Distribution"
)
st.plotly_chart(fig_pie, use_container_width=True)

# --- Data Table ---
st.subheader("Raw Data Preview")
st.dataframe(df_filtered, use_container_width=True)

