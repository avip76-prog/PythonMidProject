import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# 1. הגדרות דף
st.set_page_config(page_title="Amazon Dashboard", layout="wide")

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
    df = pd.read_csv('amazon_cleaned.csv')
    df.columns = df.columns.str.strip()
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')
    return df

try:
    df = load_data()
    st.title("📊 Amazon Business Insights Dashboard")

    categories = sorted(df['main_category'].dropna().unique())
    selected_cat = st.sidebar.selectbox("בחר קטגוריה:", categories)
    filtered_df = df[df['main_category'] == selected_cat].copy()

    if not filtered_df.empty:
        upper_charts_height = 350
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            avg_rating = filtered_df['rating'].mean()
            fig_gauge_rating = go.Figure(go.Indicator(
                mode = "gauge+number", value = avg_rating,
                title = {'text': "מדד איכות", 'font': {'size': 18}},
                gauge = {'axis': {'range': [0, 5]}, 'bar': {'color': "black"},
                         'steps': [{'range': [0, 3.5], 'color': '#FF4B4B'},
                                   {'range': [3.5, 4.2], 'color': '#FFA500'},
                                   {'range': [4.2, 5], 'color': '#238636'}]}
            ))
            fig_gauge_rating.update_layout(height=upper_charts_height, margin=dict(t=50, b=20))
            st.plotly_chart(fig_gauge_rating, use_container_width=True)

        with col2:
            if 'stock_level' in filtered_df.columns:
                in_stock = len(filtered_df[filtered_df['stock_level'] > filtered_df['restock_threshold']])
                health = (in_stock / len(filtered_df)) * 100
                fig_gauge_inv = go.Figure(go.Indicator(
                    mode = "gauge+number", value = health, number = {'suffix': "%"},
                    title = {'text': "בריאות המלאי", 'font': {'size': 18}},
                    gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "#0066CC"},
                             'steps': [{'range': [0, 40], 'color': '#FFCC00'},
                                       {'range': [40, 100], 'color': '#99FF99'}]}
                ))
                fig_gauge_inv.update_layout(height=upper_charts_height, margin=dict(t=50, b=20))
                st.plotly_chart(fig_gauge_inv, use_container_width=True)

        with col3:
            filtered_df['brand'] = filtered_df['product_name'].str.split().str[0]
            brand_stats = filtered_df.groupby('brand')['rating_count'].sum().nlargest(7).reset_index()
            fig_pie = px.pie(brand_stats, values='rating_count', names='brand', 
                             title="דומיננטיות מותגים", hole=0.4)
            fig_pie.update_layout(height=upper_charts_height, margin=dict(t=50, b=20))
            st.plotly_chart(fig_pie, use_container_width=True)

        st.markdown("---")
        m_col1, m_col2, m_col3 = st.columns(3)
        m_col1.metric("סה\"כ מכירות (Reviews)", f"{filtered_df['rating_count'].sum():,.0f}")
        m_col2.metric("ממוצע דירוג", f"{avg_rating:.2f} ⭐")
        m_col3.metric("כמות מוצרים", f"{len(filtered_df):,}")

        st.markdown("---")
        st.subheader(f"מגמות חודשיות: {selected_cat}")
        filtered_df['month_year'] = filtered_df['order_date'].dt.to_period('M').astype(str)
        monthly = filtered_df.groupby('month_year').agg({'rating_count': 'sum', 'rating': 'mean'}).reset_index()
        
        fig_trend = make_subplots(specs=[[{"secondary_y": True}]])
        fig_trend.add_trace(go.Bar(x=monthly['month_year'], y=monthly['rating_count'], name="מכירות"), secondary_y=False)
