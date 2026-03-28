import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# 1. הגדרות דף רחב
st.set_page_config(page_title="Amazon Dashboard", layout="wide")

# עיצוב CSS להפחתת רווחים מיותרים למעלה
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
    # טעינת הקובץ המנקה (זה שנוצר לאחר ה-Merge עם ה-Inventory)
    df = pd.read_csv('amazon_cleaned.csv')
    df.columns = df.columns.str.strip()
    # המרת תאריך לפורמט פייתון
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')
    return df

try:
    df = load_data()
    st.title("📊 Amazon Business Insights Dashboard")

    # סרגל צדי לבחירת קטגוריה
    categories = sorted(df['main_category'].dropna().unique())
    selected_cat = st.sidebar.selectbox("בחר קטגוריה", categories)
    
    # סינון הנתונים לפי הבחירה
    filtered_df = df[df['main_category'] == selected_cat].copy()

    if not filtered_df.empty:
        upper_charts_height = 350
        col1, col2, col3 = st.columns([1, 1, 1])

        # --- עמודה 1: מדד איכות מוצרים (Rating) ---
        with col1:
            avg_rating = filtered_df['rating'].mean()
            fig_gauge_rating = go.Figure(go.Indicator(
                mode = "gauge+number", 
                value = avg_rating,
                title = {'text': "דירוג איכות ממוצע", 'font': {'size': 18}},
                gauge = {
                    'axis': {'range': [0, 5], 'tickwidth': 1},
                    'bar': {'color': "black"}, # מחוון שחור בולט
                    'steps': [
                        {'range': [0, 3.5], 'color': '#FF4B4B'},   # אדום
                        {'range': [3.5, 4.2], 'color': '#FFD700'},  # צהוב
                        {'range': [4.2, 5], 'color': '#238636'}    # ירוק
                    ]
                }
            ))
            fig_gauge_rating.update_layout(height=upper_charts_height, margin=dict(t=50, b=20))
            st.plotly_chart(fig_gauge_rating, use_container_width=True)

        # --- עמודה 2: מדד בריאות המלאי (Inventory Health) ---
        with col2:
            # חישוב אחוז המוצרים האיכותיים (מעל 4.0) כאינדיקטור לבריאות המלאי
            total_cat = len(filtered_df)
            healthy_count = len(filtered_df[filtered_df['rating'] >= 4.0])
            health_pct = (healthy_count / total_cat) * 100 if total_cat > 0 else 0
            
            fig_gauge_inv = go.Figure(go.Indicator(
                mode = "gauge+number", 
                value = health_pct, 
                number = {'suffix': "%"},
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
            # חילוץ מותג מהשם (מילה ראשונה)
            filtered_df['brand'] = filtered_df['product_name'].str.split().str[0]
            brand_stats = filtered_df.groupby('brand')['rating_count'].sum().nlargest(7).reset_index()
            fig_pie = px.pie(brand_stats, values='rating_count', names='brand', 
                             title="דומיננטיות מותגים (לפי Reviews)", hole=0.4)
            fig_pie.update_layout(height=upper_charts_height, margin=dict(t=50, b=20))
            st.plotly_chart(fig_pie, use_container_width=True)

        # --- טבלת הסבר כמויות למדד הבריאות ---
        st.markdown("### פירוט התפלגות איכות המלאי")
        poor_df = filtered_df[filtered_df['rating'] < 3.5]
        fair_df = filtered_df[(filtered_df['rating'] >= 3.5) & (filtered_df['rating'] < 4.0)]
        good_df = filtered_df[filtered_df['rating'] >= 4.0]

        summary_data = {
            "סטטוס איכות": ["🔴 דורש החלפה (מתחת ל-3.5)", "🟡 דורש שיפור (3.5-4.0)", "🟢 איכות גבוהה (4.0+)"],
            "כמות מוצרים": [len(poor_df), len(fair_df), len(good_df)],
            "אחוז מהקטגוריה": [
                f"{(len(poor_df)/total_cat)*100:.1f}%",
                f"{(len(fair_df)/total_cat)*100:.1f}%",
                f"{(len(good_df)/total_cat)*100:.1f}%"
            ]
        }
        st.table(pd.DataFrame(summary_data))

        # --- רשימת מוצרים פסולים לטיפול מיידי ---
        if not poor_df.empty:
            with st.expander("⚠️ רשימת מוצרים שמומלץ להסיר מהמלאי (Rating < 3.5)"):
                st.write(f"נמצאו {len(poor_df)} מוצרים בסיכון גבוה בקטגוריית {selected_cat}:")
                cols_to_show = ['product_id', 'product_name', 'actual_price', 'rating']
                st.dataframe(poor_df[cols_to_show].sort_values(by='rating'))
                
                # כפתור הורדה ל-CSV
                csv = poor_df[cols_to_show].to_csv(index=False).encode('utf-8')
                st.download_button("📥 הורד רשימת מוצרים פסולים", data=csv, 
                                   file_name='low_quality_items.csv', mime='text/csv')

        st.markdown("---")
        
        # מדדים מרכזיים (Metrics)
        m_col1, m_col2, m_col3 = st.columns(3)
        m_col1.metric("סה\"כ מכירות (Reviews)", f"{filtered_df['rating_count'].sum():,.0f}")
        m_col2.metric("ממוצע דירוג קטגוריה", f"{avg_rating:.2f} ⭐")
        m_col3.metric("כמות מוצרים פעילים", f"{len(filtered_df):,}")

        st.markdown("---")
        
        # גרף מגמות חודשי משולב
        st.subheader(f"📈 מגמות חודשיות: {selected_cat}")
        filtered_df['month_year'] = filtered_df['order_date'].dt.to_period('M').astype(str)
        monthly = filtered_df.groupby('month_year').agg({'rating_count': 'sum', 'rating': 'mean'}).reset_index()
        
        fig_trend = make_subplots(specs=[[{"secondary_y": True}]])
        # עמודות מכירות
        fig_trend.add_trace(go.Bar(x=monthly['month_year'], y=monthly['rating_count'], name="מכירות (Reviews)"), secondary_y=False)
        # קו דירוג
        fig_trend.add_trace(go.Scatter(x=monthly['month_year'], y=monthly['rating'], name="דירוג ממוצע", 
                                      line=dict(color='orange', width=3)), secondary_y=True)
        
        fig_trend.update_layout(height=450, legend=dict(orientation="h", y=1.1, x=0.5, xanchor="center"))
        st.plotly_chart(fig_trend, use_container_width=True)

    else:
        st.warning(f"לא נמצאו נתונים עבור קטגוריית {selected_cat}")

except Exception as e:
    st.error(f"התרחשה שגיאה: {e}")
