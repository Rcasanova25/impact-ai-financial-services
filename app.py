import streamlit as st



import pandas as pd
import plotly.express as px
import os




data_path = "data/final_tfp_merged_cleaned.csv"

df = pd.read_csv(data_path)

df.head()




fig = px.line(
    df,
    x="Year",
    y="TFP_norm",
    color="Country",
    line_dash="Source",
    markers=True,
    title="Interactive Total Factor Productivity (2015 = 100)",
    labels={"TFP_norm": "TFP Index"}
)

fig.update_layout(
    legend_title_text="Country / Source",
    template="plotly_white",
    height=600,
    width=1000
)

fig.show()




