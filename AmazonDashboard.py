import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# 1. הגדרות דף רחב
st.set_page_config(page_title="Amazon Dashboard", layout="wide")

# עיצוב CSS להצמדת התוכן למעלה
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
    # טעינת הנתונים מה-Pipeline
    df = pd.read_csv('amazon_cleaned.csv')
    df.columns = df.columns.str.strip()
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')
    return df

try:
    df = load_data()
    st.title("📊 Amazon Business Insights Dashboard")

    # סרגל צדי לסינון
    categories = sorted(df['main_category'].dropna().unique())
    selected_cat = st.sidebar.selectbox("בחר קטגוריה", categories)
    filtered_df = df[df['main_category'] == selected_cat].copy()

    if not filtered_df.empty:
        upper_charts_height = 350
        col1, col2, col3 = st.columns([1, 1, 1])

        # --- עמודה 1: מדד איכות (Rating) ---
        with col1:
            avg_rating = filtered_df['rating'].mean()
            fig_gauge_rating = go.Figure(go.Indicator(
                mode = "gauge+number", value = avg_rating,
                title = {'text': "מדד איכות ממוצע", 'font': {'size': 18}},
                gauge = {
                    'axis': {'range': [0, 5]},
                    'bar': {'color': "black"},
                    'steps': [
                        {'range': [0, 3.5], 'color': '#FF4B4B'},
                        {'range': [3.5, 4.2], 'color': '#FFD700'},
                        {'range': [4.2, 5], 'color': '#238636'}
                    ]
                }
            ))
            fig_gauge_rating.update_layout(height=upper_charts_height, margin=dict(t=50, b=20))
            st.plotly_chart(fig_gauge_rating, use_container_width=True)

        # --- עמודה 2: בריאות המלאי (Inventory Health) ---
        with col2:
            total_items = len(filtered_df)
            healthy_items = len(filtered_df[filtered_df['rating'] >= 4.0])
            health_score = (healthy_items / total_items) * 100 if total_items > 0 else 0
            
            fig_gauge_inv = go.Figure(go.Indicator(
                mode = "gauge+number", value = health_score, number = {'suffix': "%"},
                title = {'text': "בריאות המלאי (Rating > 4.0)", 'font': {'size': 18}},
                gauge = {
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "black"},
                    'steps': [
                        {'range': [0, 40], 'color': '#FF4B4B'},
                        {'range': [40, 75], 'color': '#FFD700'},
                        {'range': [75, 100], 'color': '#238636'}
                    ]
                }
            ))
            fig_gauge_inv.update_layout(height=upper_charts_height, margin=dict(t=50, b=20))
            st.plotly_chart(fig_gauge_inv, use_container_width=True)

        # --- עמודה 3: דומיננטיות מותגים ---
        with col3:
            filtered_df['brand'] = filtered_df['product_name'].str.split().str[0]
            brand_stats = filtered_df.groupby('brand')['rating_count'].sum().nlargest(7).reset_index()
            fig_pie = px.pie(brand_stats, values='rating_count', names='brand', 
                             title="דומיננטיות מותגים", hole=0.4)
            fig_pie.update_layout(height=upper_charts_height, margin=dict(t=50, b=20))
            st.plotly_chart(fig_pie, use_container_width=True)

        # --- טבלת הסבר למדד הבריאות ---
        st.markdown("### 📋 כיצד חושב מדד בריאות המלאי?")
        poor = filtered_df[filtered_df['rating'] < 3.5]
        fair = filtered_df[(filtered_df['rating'] >= 3.5) & (filtered_df['rating'] < 4.0)]
        good = filtered_df[filtered_df['rating'] >= 4.0]

        explanation_df = pd.DataFrame({
            "קטגוריית איכות": ["🔴 סיכון גבוה (Rating < 3.5)", "🟡 דורש מעקב (3.5 - 4.0)", "🟢 מלאי בריא (Rating >= 4.0)"],
            "כמות מוצרים": [len(poor), len(fair), len(good)],
            "אחוז מהמלאי": [
                f"{(len(poor)/total_items)*100:.1f}%",
                f"{(len(fair)/total_items)*100:.1f}%",
                f"{(len(good)/total_items)*100:.1f}%"
            ],
            "השפעה על המדד": ["לא נספר", "לא נספר", "מהווה את אחוז המדד"]
        })
        st.table(explanation_df)

        st.markdown("---")
        
        # מדדים מספריים (Metrics)
        m_col1, m_col2, m_col3 = st.columns(3)
        m_col1.metric("סה\"כ מכירות (Reviews)", f"{filtered_df['rating_count'].sum():,.0f}")
        m_col2.metric("ממוצע דירוג", f"{avg_rating:.2f} ⭐")
        m_col3.metric("כמות מוצרים", f"{len(filtered_df):,}")

        st.markdown("---")
        
        # גרף מגמות חודשי
        st.subheader(f"📈 מגמות חודשיות: {selected_cat}")
        filtered_df['month_year'] = filtered_df['order_date'].dt.to_period('M').astype(str)
        monthly = filtered_df.groupby('month_year').agg({'rating_count': 'sum', 'rating': 'mean'}).reset_index()
        
        fig_trend = make_subplots(specs=[[{"secondary_y": True}]])
        fig_trend.add_trace(go.Bar(x=monthly['month_year'], y=monthly['rating_count'], name="מכירות"), secondary_y=False)
        fig_trend.add_trace(go.Scatter(x=monthly['month_year'], y=monthly['rating'], name="דירוג", line=dict(color='orange', width=3)), secondary_y=True)
        fig_trend.update_layout(height=450, legend=dict(orientation="h", y=1.1, x=0.5, xanchor="center"))
        st.plotly_chart(fig_trend, use_container_width=True)

    else:
        st.warning(f"לא נמצאו נתונים עבור קטגוריית {selected_cat}")

except Exception as e:
    st.error(f"שגיאה בטעינת הנתונים: {e}")

# סוף הקוד - אין שורות נוספות מעבר לפה
