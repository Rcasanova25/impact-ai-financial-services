import streamlit as st



import pandas as pd
import plotly.express as px
import os




data_path = os.path.join("data", "final_tfp_merged_cleaned.csv")

if not os.path.exists(data_path):
	print(f"Warning: File not found: {data_path}. Trying absolute path fallback.")
	data_path = r"C:\Users\Robert Casanova\OneDrive\Documents\Impact_AI_Financial_Services\data\final_tfp_merged_cleaned.csv"
	if not os.path.exists(data_path):
		raise FileNotFoundError(f"File not found at both relative and absolute paths: {data_path}")
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





