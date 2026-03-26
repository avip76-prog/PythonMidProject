import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# --- 1. הגדרות דף ---
st.set_page_config(page_title="Amazon Business Dashboard", layout="wide")

# CSS לצמצום רווחים מיותרים בראש הדף
st.markdown("""
    <style>
           .block-container {
                padding-top: 1rem;
                padding-bottom: 0rem;
            }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data
def load_data():
    # טעינת הקובץ (הנחה: הקובץ כבר מכיל את עמודות המלאי לאחר ה-Join)
    df = pd.read_csv('amazon_cleaned.csv')
    
    # המרת תאריך לפורמט זמן
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')
    
    # חילוץ שם המותג (המילה הראשונה בשם המוצר)
    df['brand'] = df['product_name'].str.split().str[0]
    
    return df

try:
    df = load_data()
    
    st.title("📊 Amazon Business & Inventory Insights")

    # --- 2. סרגל צד (Sidebar) לבחירת קטגוריה ---
    st.sidebar.header("מסננים")
    categories = sorted(df['main_category'].dropna().unique())
    selected_cat = st.sidebar.selectbox("בחר קטגוריה:", categories)

    # סינון הנתונים לפי הקטגוריה שנבחרה
    filtered_df = df[df['main_category'] == selected_cat].copy()

    if not filtered_df.empty:
        
        # --- 3. חלק עליון: שלושה מחווני Gauge ---
        upper_charts_height = 350
        col1, col2, col3 = st.columns(3)

        with col1:
            # מחוון 1: דירוג איכות ממוצע
            avg_rating = filtered_df['rating'].mean()
            fig_rating = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = avg_rating,
                title = {'text': "דירוג איכות ממוצע", 'font': {'size': 18}},
                gauge = {
                    'axis': {'range': [0, 5]},
                    'bar': {'color': "black"},
                    'steps': [
                        {'range': [0, 3.8], 'color': "#FF4B4B"},
                        {'range': [3.8, 4.2], 'color': "#FFA500"},
                        {'range': [4.2, 5], 'color': "#238636"}
                    ]
                }
            ))
            fig_rating.update_layout(height=upper_charts_height, margin=dict(t=50, b=0))
            st.plotly_chart(fig_rating, use_container_width=True)

        with col2:
            # מחוון 2: בריאות המלאי (% מוצרים שמעל סף ההזמנה)
            in_stock_count = len(filtered_df[filtered_df['stock_level'] > filtered_df['restock_threshold']])
            health_score = (in_stock_count / len(filtered_df)) * 100 if len(filtered_df) > 0 else 0

            fig_inventory = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = health_
