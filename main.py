import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Data Explorer",
    page_icon="line-chart.png",
    layout="wide"
)
st.title("📊 Data Explorer")

st.sidebar.header("Upload File")
uploaded_file = st.sidebar.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

# Process uploaded file
if uploaded_file is not None:
    try:
        # Show uploaded file name
        st.markdown(f"**📁 File:** `{uploaded_file.name}`")

        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("✅ File Uploaded Successfully!")
        st.markdown(f"**📏 Shape:** `{df.shape[0]} rows × {df.shape[1]} columns`")

        st.subheader("📄 Uploaded Data")
        st.dataframe(df.style.highlight_max(axis=0))

        # Show line chart if numeric columns exist
        numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
        if len(numeric_cols) >= 2:
            st.subheader("📈 Line Chart (first 2 numeric columns)")
            st.line_chart(df[numeric_cols[:2]])
        elif len(numeric_cols) == 1:
            st.subheader("📈 Line Chart (only 1 numeric column)")
            st.line_chart(df[numeric_cols])
        else:
            st.warning("⚠️ No numeric columns found to generate chart.")

    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
else:
    st.info("📂 Please upload a CSV or Excel file to begin.")

# --- Footer ---
st.markdown("""
<hr style="margin-top:50px;">

<div style="text-align: center;">
    <small>Made with ❤️ by <strong>Ch. Abdul Wahab</strong> — Open Source Project</small>
</div>
""", unsafe_allow_html=True)
