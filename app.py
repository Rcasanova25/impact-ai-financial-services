import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI & Productivity: TFP Viewer", layout="wide")

st.title("Total Factor Productivity Visualization")
st.markdown("""
This prototype explores trends in total factor productivity (TFP) across countries or regions as a foundation 
for broader analysis of how AI adoption may impact labor and productivity in the global economy.
""")
data_path = "final_tfp_merged_cleaned.csv"

try:
    df = pd.read_csv(data_path)

    # Basic structure: expect columns like ['Country', 'Year', 'TFP']
    if "Country" in df.columns and "Year" in df.columns and "TFP" in df.columns:
        countries = df["Country"].unique()
        selected_countries = st.multiselect("Select countries to visualize", countries, default=list(countries[:3]))

        filtered_df = df[df["Country"].isin(selected_countries)]

        fig = px.line(
            filtered_df,
            x="Year",
            y="TFP",
            color="Country",
            title="TFP Over Time by Country"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("CSV file must include 'Country', 'Year', and 'TFP' columns.")
except FileNotFoundError:
    st.error(f"Data file not found at: {data_path}. Please ensure it's in the repo root.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")
