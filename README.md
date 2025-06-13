# 🧠 Insightlyzer

**Insightlyzer** is a lightweight and interactive web application built with Streamlit, designed to help you instantly upload, preview, and visualize data from CSV and Excel files. It's perfect for quick data inspections, demos, and exploratory analysis — all in the browser.

---

## 🚀 Features

- 📂 Upload `.csv` or `.xlsx` files via the sidebar
- 📊 Automatic detection of numeric columns
- 📈 Live-rendered line charts from the first two numeric columns
- 🔍 Clean data preview with max-value highlights
- 💡 Simple, responsive, and open-source

---

## 📦 Installation

Make sure you have [uv](https://pypi.org/project/uv/) or `pip` installed. Then:

```bash
# Using uv (recommended)
uv venv
uv pip install streamlit pandas numpy openpyxl
uv run main.py