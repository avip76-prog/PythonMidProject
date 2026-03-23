import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# 1. הגדרות דף רחב וצמצום רווחים
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
    # טעינת הקובץ הנקי
    df = pd.read_csv('amazon_cleaned.csv')
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')
    return df

try:
    df = load_data()
    st.title("📊 Amazon Business Insights Dashboard")

    # סרגל צד לבחירת קטגוריה
    categories = sorted(df['main_category'].dropna().unique())
    selected_cat = st.sidebar.selectbox("בחר קטגוריה:", categories)

    filtered_df = df[df['main_category'] == selected_cat].copy()

    if not filtered_df.empty:
        # גובה אחיד לגרפים העליונים
        upper_charts_height = 400
        col1, col2 = st.columns([1, 1])

        with col1:
            # א. גרף המד-אוץ
            avg_rating = filtered_df['rating'].mean()
            fig_gauge = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = avg_rating,
                title = {'text': f"מדד איכות: {selected_cat}", 'font': {'size': 20}},
                gauge = {
                    'axis': {'range': [0, 5]},
                    'bar': {'color': "black"},
                    'steps': [
                        {'range': [0, 3.5], 'color': '#FF4B4B'},
                        {'range': [3.5, 4.2], 'color': '#FFA500'},
                        {'range': [4.2, 5], 'color': '#238636'}
                    ],
                    'threshold': {'line': {'color': "white", 'width': 4}, 'value': 4.0}
                }
            ))
            fig_gauge.update_layout(height=upper_charts_height, margin=dict(t=80, b=20))
            st.plotly_chart(fig_gauge, use_container_width=True)

            # ב. טבלת מדדים
            st.markdown("### סיכום מדדי קטגוריה")
            metrics_table = pd.DataFrame({
                "מדד": ["כמות מכירות (Reviews)", "ממוצע דירוג", "כמות מוצרים"],
                "ערך": [
                    f"{filtered_df['rating_count'].sum():,.0f}",
                    f"{avg_rating:.2f} ⭐",
                    f"{len(filtered_df):,}"
                ]
            })
            st.table(metrics_table)

        with col2:
            # ג. גרף פאי - מותגים
            filtered_df['brand'] = filtered_df['product_name'].str.split().str[0]
            brand_stats = filtered_df.groupby('brand')['rating_count'].sum().reset_index()
            top_brands = brand_stats.nlargest(7, 'rating_count')
            others_sum = brand_stats.sort_values('rating_count', ascending=False)[7:]['rating_count'].sum()
            if others_sum > 0:
                top_brands = pd.concat([top_brands, pd.DataFrame({'brand':['Other'], 'rating_count':[others_sum]})])

            fig_pie = px.pie(top_brands, values='rating_count', names='brand', 
                             title="דומיננטיות מותגים (נתח שוק)",
                             hole=0.4,
                             color_discrete_sequence=px.colors.qualitative.Pastel)
            fig_pie.update_layout(height=upper_charts_height, margin=dict(t=80, b=20))
            st.plotly_chart(fig_pie, use_container_width=True)

        st.markdown("---")

        # ד. גרף מגמות חודשיות
        st.subheader(f"מגמות מכירות ודירוג: {selected_cat}")
        filtered_df['month_year'] = filtered_df['order_date'].dt.to_period('M').astype(str)
        monthly_data = filtered_df.groupby('month_year').agg({'rating_count': 'sum', 'rating': 'mean'}).reset_index().sort_values('month_year')

        fig_combined = make_subplots(specs=[[{"secondary_y": True}]])
        fig_combined.add_trace(go.Bar(x=monthly_data['month_year'], y=monthly_data['rating_count'], name="סך מכירות"), secondary_y=False)
        fig_combined.add_trace(go.Scatter(x=monthly_data['month_year'], y=monthly_data['rating'], name="דירוג ⭐", mode='lines+markers', line=dict(color='orange')), secondary_y=True)

        fig_combined.update_layout(height=500, legend=dict(orientation="h", y=1.1))
        st.plotly_chart(fig_combined, use_container_width=True)

    else:
        st.warning("אין נתונים לקטגוריה זו.")

except Exception as e:
    st.error(f"שגיאה: {e}")
