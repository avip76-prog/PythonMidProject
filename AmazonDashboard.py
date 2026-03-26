import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# --- 1. הגדרות דף ---
st.set_page_config(page_title="Amazon Business Dashboard", layout="wide")

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
    # טעינת הקובץ (הנחה: amazon_cleaned.csv מכיל את נתוני המלאי)
    df = pd.read_csv('amazon_cleaned.csv')
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')
    df['brand'] = df['product_name'].str.split().str[0]
    return df

try:
    df = load_data()
    st.title("📊 Amazon Business & Inventory Insights")

    # --- 2. Sidebar ---
    st.sidebar.header("מסננים")
    categories = sorted(df['main_category'].dropna().unique())
    selected_cat = st.sidebar.selectbox("בחר קטגוריה:", categories)

    filtered_df = df[df['main_category'] == selected_cat].copy()

    if not filtered_df.empty:
        # --- 3. Gauges Section ---
        upper_charts_height = 350
        col1, col2, col3 = st.columns(3)

        with col1:
            avg_rating = filtered_df['rating'].mean()
            fig_rating = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = avg_rating,
                title = {'text': "דירוג איכות", 'font': {'size': 18}},
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
            # בריאות המלאי
            in_stock = len(filtered_df[filtered_df['stock_level'] > filtered_df['restock_threshold']])
            health_score = (in_stock / len(filtered_df)) * 100 if len(filtered_df) > 0 else 0
            fig_inv = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = health_score,
                number = {'suffix': "%"},
                title = {'text': "בריאות המלאי", 'font': {'size': 18}},
                gauge = {
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "#0066CC"},
                    'steps': [{'range': [0, 40], 'color': "#FFCC00"}, {'range': [40, 100], 'color': "#99FF99"}],
                    'threshold': {'line': {'color': "red", 'width': 4}, 'value': 30}
                }
            ))
            fig_inv.update_layout(height=upper_charts_height, margin=dict(t=50, b=0))
            st.plotly_chart(fig_inv, use_container_width=True)

        with col3:
            avg_disc = filtered_df['discount_percentage'].mean() * 100
            fig_disc = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = avg_disc,
                number = {'suffix': "%"},
                title = {'text': "גובה הנחה ממוצע", 'font': {'size': 18}},
                gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "purple"}}
            ))
            fig_disc.update_layout(height=upper_charts_height, margin=dict(t=50, b=0))
            st.plotly_chart(fig_disc, use_container_width=True)

        # --- 4. Metrics & Brands ---
        st.markdown("---")
        m_col1, m_col2 = st.columns([1, 2])
        with m_col1:
            st.metric("סה\"כ מוצרים", f"{len(filtered_df):,}")
            low_stock = len(filtered_df[filtered_df['stock_level'] <= filtered_df['restock_threshold']])
            if low_stock > 0:
                st.error(f"⚠️ {low_stock} מוצרים מתחת לסף!")
            else:
                st.success("✅ מלאי תקין")

        with m_col2:
            brand_data = filtered_df.groupby('brand')['rating_count'].sum().nlargest(7).reset_index()
            fig_pie = px.pie(brand_data, values='rating_count', names='brand', title="נתח שוק לפי מותג", hole=0.4)
            st.plotly_chart(fig_pie, use_container_width=True)

        # --- 5. Trends ---
        st.markdown("---")
        filtered_df['month_year'] = filtered_df['order_date'].dt.to_period('M').astype(str)
        monthly = filtered_df.groupby('month_year').agg({'rating_count': 'sum', 'rating': 'mean'}).reset_index()
        fig_trend = make_subplots(specs=[[{"secondary_y": True}]])
        fig_trend.add_trace(go.Bar(x=monthly['month_year'], y=monthly['rating_count'], name="ביקורות"), secondary_y=False)
        fig_trend.add_trace(go.Scatter(x=monthly['month_year'], y=monthly['rating'], name="דירוג", line=dict(color='orange')), secondary_y=True)
        st.plotly_chart(fig_trend, use_container_width=True)

except Exception as e:
    st.error(f"שגיאה: {e}")
