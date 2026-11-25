import streamlit as st
import pandas as pd
import json
from pdf_generator import create_pdf

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Aviation Safety Report Analyzer",
    page_icon="✈",
    layout="wide"
)

# ---------------- LOAD DATA ---------------- #
@st.cache_data
def load_data():
    df = pd.read_parquet("clustered_aviation_reports.parquet")

    with open("hazard_reports.json","r") as f:
        hazard_reports = json.load(f)

    return df, hazard_reports

df, hazard_reports = load_data()

# ---------------- SIDEBAR ---------------- #

st.sidebar.image(
    "https://img.icons8.com/color/96/airplane-take-off.png",
    width=80
)

st.sidebar.title("Aviation Safety Analyzer")

st.sidebar.markdown("---")

st.sidebar.write("LLM Analytics")

st.sidebar.write("Semantic Clustering")

st.sidebar.write("Hazard Detection")

st.sidebar.markdown("---")

cluster_list = sorted(df[df["cluster"]!=-1]["cluster"].unique())

selected_cluster = st.sidebar.selectbox(
    "Select Cluster",
    cluster_list
)

# ---------------- HEADER ---------------- #

st.title("✈ Aviation Safety Report Analyzer")

col1,col2,col3,col4=st.columns(4)

col1.metric("Total Reports",len(df))
col2.metric("Clusters",len(cluster_list))
col3.metric("Noise Reports",(df["cluster"]==-1).sum())
col4.metric("Current Cluster",selected_cluster)

st.divider()

# ---------------- CLUSTER REPORT ---------------- #

risk="Unknown"

if str(selected_cluster) in hazard_reports:

    text = hazard_reports[str(selected_cluster)].lower()

    if "high" in text:
        risk="🔴 HIGH"

    elif "medium" in text:
        risk="🟠 MEDIUM"

    elif "low" in text:
        risk="🟢 LOW"

st.subheader("Risk Level")

st.info(risk)

st.subheader(f"Cluster {selected_cluster}")

cluster_key=str(selected_cluster)

if cluster_key in hazard_reports:

    with st.expander("📑 View Hazard Review", expanded=True):
        st.markdown(hazard_reports[cluster_key])

else:

    st.warning("Hazard summary not generated for this cluster.")

st.divider()

if cluster_key in hazard_reports:

    pdf_file = create_pdf(
        selected_cluster,
        hazard_reports[cluster_key]
    )

    with open(pdf_file, "rb") as pdf:

        st.download_button(
            "📄 Download Hazard Report PDF",
            pdf,
            file_name=pdf_file,
            mime="application/pdf"
        )


import plotly.express as px

st.subheader("📊 Cluster Distribution")

cluster_counts = (
    df[df["cluster"] != -1]
    .groupby("cluster")
    .size()
    .reset_index(name="Reports")
)

fig = px.bar(
    cluster_counts,
    x="cluster",
    y="Reports",
    title="Reports per Cluster"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("🛠 Primary Problem Distribution")

problem_counts = (
    df[df["cluster"] == selected_cluster]["primary_problem"]
    .value_counts()
    .reset_index()
)

problem_counts.columns = ["Primary Problem", "Count"]

fig2 = px.pie(
    problem_counts,
    names="Primary Problem",
    values="Count",
    title="Primary Problem"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("⚠ Top Anomalies")

anomaly_counts = (
    df[df["cluster"] == selected_cluster]["anomaly"]
    .value_counts()
    .head(10)
    .reset_index()
)

anomaly_counts.columns = ["Anomaly", "Count"]

fig4 = px.bar(
    anomaly_counts,
    x="Count",
    y="Anomaly",
    orientation="h",
    title="Top 10 Anomalies"
)

st.plotly_chart(fig4, use_container_width=True)



# ---------------- SAMPLE REPORTS ---------------- #

st.divider()

st.subheader("🔍 Search Safety Reports")

keyword = st.text_input("Enter keyword (Example: bird, altitude, weather, runway)")

if keyword:

    results = df[
        df["narrative"].str.contains(keyword, case=False, na=False)
    ][[
        "cluster",
        "primary_problem",
        "flight_phase",
        "narrative"
    ]]

    st.write(f"Found {len(results)} reports")

    st.dataframe(results.head(20), use_container_width=True)

st.divider()

st.subheader("📈 Dataset Statistics")

c1,c2,c3 = st.columns(3)

c1.metric(
    "Average Cluster Size",
    round(cluster_counts["Reports"].mean())
)

c2.metric(
    "Largest Cluster",
    cluster_counts["Reports"].max()
)

c3.metric(
    "Smallest Cluster",
    cluster_counts["Reports"].min()
)

st.divider()

st.subheader("⬇ Download Cluster Reports")

cluster_df = df[df["cluster"]==selected_cluster]

csv = cluster_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Cluster CSV",
    data=csv,
    file_name=f"cluster_{selected_cluster}.csv",
    mime="text/csv"
)

st.subheader("Sample Incident Reports")

sample=df[df["cluster"]==selected_cluster][
    [
        "primary_problem",
        "flight_phase",
        "anomaly",
        "narrative"
    ]
].head(10)

st.dataframe(sample,use_container_width=True)