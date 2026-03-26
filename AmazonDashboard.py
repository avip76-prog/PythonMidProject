import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# 1. הגדרות דף
st.set_page_config(page_title="Amazon Dashboard", layout="wide")

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
        col1, col2, col3 = st.columns(3)
        h = 350

        with col1:
            avg_r = filtered_df['rating'].mean()
            fig1 = go.Figure(go.Indicator(mode="gauge+number", value=avg_r, title={'text': "דירוג איכות"},
                gauge={'axis': {'range': [0, 5]}, 'bar': {'color': "black"},
                       'steps': [{'range': [0, 3.5], 'color': 'red'}, {'range': [3.5, 5], 'color': 'green'}]}))
            st.plotly_chart(fig1.update_layout(height=h), use_container_width=True)

        with col2:
            if 'stock_level' in filtered_df.columns:
                in_stock = len(filtered_df[filtered_df['stock_level'] > filtered_df['restock_threshold']])
                health = (in_stock / len(filtered_df)) * 100
                fig2 = go.Figure(go.Indicator(mode="gauge+number", value=health, number={'suffix': "%"}, title={'text': "בריאות המלאי"},
                    gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "blue"}}))
                st.plotly_chart(fig2.update_layout(height=h), use_container_width=True)

        with col3:
            brand_stats = filtered_df.groupby('product_name').first().reset_index() # חילוץ מותג פשוט
            brand_stats['brand'] = brand_stats['product_name'].str.split().str[0]
            top_b = brand_stats.groupby('brand').size().nlargest(7).reset_index(name='count')
            fig3 = px.pie(top_b, values='count', names='brand', title="פיזור מותגים", hole=0.4)
            st.plotly_chart(fig3.update_layout(height=h), use_container_width=True)

        st.markdown("---")
        # מגמות זמן
        filtered_df['month_year'] = filtered_df['order_date'].dt.to_period('M').astype(str)
        monthly = filtered_df.groupby('month_year').agg({'rating_count': 'sum', 'rating': 'mean'}).reset_index()
        
        fig_trend = make_subplots(specs=[[{"secondary_y": True}]])
        fig_trend.add_trace(go.Bar(x=monthly['month_year'], y=monthly['rating_count'], name="ביקורות"), secondary_y=False)
        fig_trend.add_trace(go.Scatter(x=monthly['month_year'], y=monthly['rating'], name="דירוג", line=dict(color='orange')), secondary_y=True)
        st.plotly_chart(fig_trend.update_layout(height=400), use_container_width=True)

    else:
        st.warning("אין נתונים לקטגוריה זו")

except Exception as e:
    st.error(f"שגיאה: {e}")
