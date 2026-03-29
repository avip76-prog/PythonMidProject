import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# 1. הגדרות דף רחב
st.set_page_config(page_title="Amazon Dashboard", layout="wide")

# עיצוב CSS ליישור לימין, התאמת טבלאות וצמצום רווחים
st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
    }
    .main, .stMarkdown {
        direction: rtl;
        text-align: right;
    }
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        direction: rtl;
        text-align: right;
        margin-bottom: 20px;
    }
    .custom-table th, .custom-table td {
        padding: 12px;
        border-bottom: 1px solid #ddd;
        text-align: right;
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
    st.markdown("<h1 style='text-align: right;'>📊 Amazon Business Insights Dashboard</h1>", unsafe_allow_html=True)

    # סינון לפי קטגוריה
    categories = sorted(df['main_category'].dropna().unique())
    selected_cat = st.sidebar.selectbox("בחר קטגוריה", categories)
    filtered_df = df[df['main_category'] == selected_cat].copy()

    if not filtered_df.empty:
        charts_height = 400 
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            avg_rating = filtered_df['rating'].mean()
            fig_gauge_rating = go.Figure(go.Indicator(
                mode = "gauge+number", value = avg_rating,
                title = {'text': "מדד איכות ממוצע", 'font': {'size': 20}},
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
            fig_gauge_rating.update_layout(height=charts_height, margin=dict(t=80, b=20, l=30, r=30))
            st.plotly_chart(fig_gauge_rating, use_container_width=True)

        with col2:
            total_items = len(filtered_df)
            healthy_items = len(filtered_df[filtered_df['rating'] >= 4.0])
            health_score = (healthy_items / total_items) * 100 if total_items > 0 else 0
            
            fig_gauge_inv = go.Figure(go.Indicator(
                mode = "gauge+number", value = health_score, number = {'suffix': "%"},
                title = {'text': "בריאות המלאי (Rating > 4.0)", 'font': {'size': 20}},
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
            fig_gauge_inv.update_layout(height=charts_height, margin=dict(t=80, b=20, l=30, r=30))
            st.plotly_chart(fig_gauge_inv, use_container_width=True)

        with col3:
            filtered_df['brand'] = filtered_df['product_name'].str.split().str[0]
            brand_stats = filtered_df.groupby('brand')['rating_count'].sum().nlargest(7).reset_index()
            fig_pie = px.pie(brand_stats, values='rating_count', names='brand', 
                             title="דומיננטיות מותגים (Reviews)")
            fig_pie.update_layout(
                height=charts_height, 
                margin=dict(t=80, b=80, l=10, r=10),
                legend=dict(orientation="h", yanchor="top", y=-0.1, xanchor="center", x=0.5)
            )
            st.plotly_chart(fig_pie, use_container_width=True)

        st.markdown("---")
        st.markdown("<h3 style='text-align: right;'>📋 נתונים כלליים לקטגוריה</h3>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <table class="custom-table">
            <tr>
                <th>כמות דירוגים</th>
                <th>כמות מוצרים</th>
                <th>דירוג ממוצע</th>
            </tr>
            <tr>
                <td>{filtered_df['rating_count'].sum():,.0f}</td>
                <td>{len(filtered_df):,}</td>
                <td>{avg_rating:.2f} ⭐</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("<h3 style='text-align: right;'>💡 כיצד חושב מדד בריאות המלאי?</h3>", unsafe_allow_html=True)
        poor = filtered_df[filtered_df['rating'] < 3.5]
        fair = filtered_df[(filtered_df['rating'] >= 3.5) & (filtered_df['rating'] < 4.0)]
        good = filtered_df[filtered_df['rating'] >= 4.0]

        st.markdown(f"""
        <table class="custom-table">
            <tr>
                <th>קטגוריית איכות</th>
                <th>כמות מוצרים</th>
                <th>אחוז מהמלאי</th>
                <th>השפעה על המדד</th>
            </tr>
            <tr>
                <td>🔴 סיכון גבוה (Rating < 3.5)</td>
                <td>{len(poor)}</td>
                <td>{(len(poor)/total_items)*100:.1f}%</td>
                <td>לא נספר במדד</td>
            </tr>
            <tr>
                <td>🟡 דורש מעקב (3.5 - 4.0)</td>
                <td>{len(fair)}</td>
                <td>{(len(fair)/total_items)*100:.1f}%</td>
                <td>לא נספר במדד</td>
            </tr>
            <tr>
                <td>🟢 מלאי בריא (Rating >= 4.0)</td>
                <td>{len(good)}</td>
                <td>{(len(good)/total_items)*100:.1f}%</td>
                <td>מהווה את אחוז המדד</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)
        
        st.info(f"חישוב המדד: {len(good)} מוצרים בריאים מתוך {total_items} סך הכל = **{health_score:.1f}%**")

        st.markdown("---")
        st.markdown(f"<h3 style='text-align: right;'>📈 מגמות חודשיות: {selected_cat}</h3>", unsafe_allow_html=True)
        filtered_df['month_year'] = filtered_df['order_date'].dt.to_period('M').astype(str)
        monthly = filtered_df.groupby('month_year').agg({'rating_count': 'sum', 'rating': 'mean'}).reset_index()
        
        fig_trend = make_subplots(specs=[[{"secondary_y": True}]])
        fig_trend.add_trace(go.Bar(x=monthly['month_year'], y=monthly['rating_count'], name="דירוגים"), secondary_y=False)
        fig_trend.add_trace(go.Scatter(x=monthly['month_year'], y=monthly['rating'], name="דירוג ממוצע", line=dict(color='orange', width=3)), secondary_y=True)
        fig_trend.update_layout(height=450, legend=dict(orientation="h", y=1.1, x=0.5, xanchor="center"))
        st.plotly_chart(fig_trend, use_container_width=True)

except Exception as e:
    st.error(f"שגיאה: {e}")
