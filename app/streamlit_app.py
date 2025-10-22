import os
from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Strava Fitness Dashboard", layout="wide")

# Resolve data directory relative to this file
THIS_DIR = Path(__file__).resolve().parent
DATA_DIR = (THIS_DIR.parent / "Data Files" / "mturkfitbit_export_4.12.16-5.12.16" / "Fitabase Data 4.12.16-5.12.16").resolve()

st.sidebar.title("Data Sources")
if not DATA_DIR.exists():
    st.error(f"Data directory not found: {DATA_DIR}")
    st.stop()

# Map friendly names to files
DATASETS = {
    "Daily Activity": "dailyActivity_merged.csv",
    "Daily Calories": "dailyCalories_merged.csv",
    "Daily Intensities": "dailyIntensities_merged.csv",
    "Daily Steps": "dailySteps_merged.csv",
    "Hourly Calories": "hourlyCalories_merged.csv",
    "Hourly Intensities": "hourlyIntensities_merged.csv",
    "Hourly Steps": "hourlySteps_merged.csv",
    "Sleep (Daily)": "sleepDay_merged.csv",
    "Weight Log": "weightLogInfo_merged.csv",
    # Heavy minute-level datasets (sampled by default)
    "Heartrate (seconds) [sampled]": "heartrate_seconds_merged.csv",
    "Minute Calories (Narrow) [sampled]": "minuteCaloriesNarrow_merged.csv",
    "Minute Intensities (Narrow) [sampled]": "minuteIntensitiesNarrow_merged.csv",
    "Minute Steps (Narrow) [sampled]": "minuteStepsNarrow_merged.csv",
}

selection = st.sidebar.selectbox("Choose a dataset", list(DATASETS.keys()))
file_name = DATASETS[selection]
file_path = DATA_DIR / file_name

st.sidebar.caption(str(file_path))

@st.cache_data(show_spinner=False)
def load_csv(path: Path, parse_dates=True, nrows=None):
    kwargs = {}
    if parse_dates:
        # Try to infer date columns by common names
        date_cols = [c for c in ["ActivityDate", "Date", "ActivityDay", "SleepDay", "Time", "date", "Datetime", "DateTime"] if c]
        try:
            df_head = pd.read_csv(path, nrows=5)
            infer = [c for c in df_head.columns if any(dc.lower() == c.lower() for dc in date_cols)]
            if infer:
                kwargs["parse_dates"] = infer
        except Exception:
            pass
    return pd.read_csv(path, nrows=nrows, **kwargs)

st.title("Strava Fitness Dashboard")
st.write("Interactive exploration of Fitbit/Strava CSV exports.")

# Load data with sampling strategy for very large files
MAX_ROWS = st.sidebar.number_input("Max rows to load (0 = all)", min_value=0, value=250000, step=50000)

def smart_load(path: Path):
    size_mb = path.stat().st_size / (1024 * 1024)
    if size_mb > 50 and MAX_ROWS != 0:
        return load_csv(path, nrows=MAX_ROWS)
    return load_csv(path, nrows=None if MAX_ROWS == 0 else MAX_ROWS)

with st.spinner("Loading data..."):
    df = smart_load(file_path)

st.subheader(f"Preview: {selection}")
st.dataframe(df.head(50), use_container_width=True)

st.markdown("---")

# Basic profiling
st.subheader("Summary")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Rows", f"{len(df):,}")
with col2:
    st.metric("Columns", f"{len(df.columns):,}")
with col3:
    st.metric("File Size", f"{file_path.stat().st_size / (1024*1024):.1f} MB")

# Try to detect time and value columns for plotting
def guess_time_col(columns):
    candidates = [
        "Datetime", "DateTime", "Time", "date", "Date", "ActivityDate", "ActivityDay", "SleepDay"
    ]
    for c in columns:
        for cand in candidates:
            if c.lower() == cand.lower():
                return c
    # fallback: first column that looks like a date
    for c in columns:
        if any(k in c.lower() for k in ["date", "time", "datetime"]):
            return c
    return None

numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
time_col = guess_time_col(df.columns)

with st.expander("Columns"):
    st.write({"time_col": time_col, "numeric_cols": numeric_cols[:10]})

st.subheader("Visualizations")
if time_col and numeric_cols:
    y_col = st.selectbox("Metric", numeric_cols, index=0)
    # Parse datetime if not already
    try:
        df_plot = df.copy()
        if not pd.api.types.is_datetime64_any_dtype(df_plot[time_col]):
            df_plot[time_col] = pd.to_datetime(df_plot[time_col], errors="coerce")
        df_plot = df_plot.dropna(subset=[time_col])
        # Downsample for very large datasets
        if len(df_plot) > 200000:
            df_plot = df_plot.iloc[::int(len(df_plot)/200000)+1, :]
        fig = px.line(df_plot, x=time_col, y=y_col, title=f"{y_col} over time")
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.warning(f"Could not render time series: {e}")

if numeric_cols:
    x_col = st.selectbox("X (numeric)", numeric_cols, key="x")
    y_col2 = st.selectbox("Y (numeric)", numeric_cols, key="y")
    try:
        fig2 = px.scatter(df, x=x_col, y=y_col2, opacity=0.5, title=f"{y_col2} vs {x_col}")
        st.plotly_chart(fig2, use_container_width=True)
    except Exception as e:
        st.warning(f"Could not render scatter: {e}")

st.markdown("---")

st.subheader("Raw Data")
st.dataframe(df, use_container_width=True, height=400)

st.caption("Tip: Adjust 'Max rows to load' in the sidebar for performance.")
