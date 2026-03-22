import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# הגדרות דף רחב
st.set_page_config(page_title="Amazon Business Dashboard", layout="wide")

@st.cache_data
def load_data():
    # טעינת הקובץ הנקי
    df = pd.read_csv('amazon_cleaned.csv')
    # המרת תאריך לפורמט זמן
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')
    return df

try:
    df = load_data()
    
    st.title("📊 Amazon Business Insights Dashboard")
    st.markdown("---")

    # 1. סרגל צד לבחירת קטגוריה
    st.sidebar.header("מסננים")
    categories = sorted(df['main_category'].dropna().unique())
    selected_cat = st.sidebar.selectbox("בחר קטגוריה לניתוח:", categories)

    # סינון הנתונים לפי הבחירה
    filtered_df = df[df['main_category'] == selected_cat].copy()

    if not filtered_df.empty:
        
        # יצירת שתי עמודות לחלק העליון (מד-אוץ ופאי)
        col_top_left, col_top_right = st.columns([1, 1])

        with col_top_left:
            # --- תובנה 1: מדד איכות (Gauge Chart) ---
            avg_rating = filtered_df['rating'].mean()
            fig_gauge = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = avg_rating,
                title = {'text': f"חווית לקוח: {selected_cat}", 'font': {'size': 20}},
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
            fig_gauge.update_layout(height=350, margin=dict(l=20, r=20, t=50, b=20))
            st.plotly_chart(fig_gauge, use_container_width=True)

        with col_top_right:
            # --- תובנה 2: תמהיל מותגים (Pie/Donut Chart) ---
            # חילוץ מותג (מילה ראשונה משם המוצר)
            filtered_df['brand'] = filtered_df['product_name'].str.split().str[0]
            brand_stats = filtered_df.groupby('brand')['rating_count'].sum().reset_index()
            
            # לקיחת 7 הגדולים והשאר כ-"Other"
            top_brands = brand_stats.nlargest(7, 'rating_count')
            others_sum = brand_stats.sort_values('rating_count', ascending=False)[7:]['rating_count'].sum()
            if others_sum > 0:
                top_brands = pd.concat([top_brands, pd.DataFrame({'brand':['Other'], 'rating_count':[others_sum]})])

            fig_pie = px.pie(top_brands, values='rating_count', names='brand', 
                             title=f"דומיננטיות מותגים (לפי Reviews)",
                             hole=0.4,
                             color_discrete_sequence=px.colors.qualitative.Pastel)
            fig_pie.update_layout(height=350, margin=dict(l=20, r=20, t=50, b=20))
            st.plotly_chart(fig_pie, use_container_width=True)

        st.markdown("---")

        # --- תובנה 3: מגמות חודשיות (Combined Bar & Line) ---
        st.subheader(f"מגמות מכירות ודירוג לאורך זמן: {selected_cat}")
        
        filtered_df['month_year'] = filtered_df['order_date'].dt.to_period('M').astype(str)
        monthly_stats = filtered_df.groupby('month_year').agg({'rating_count': 'sum', 'rating': 'mean'}).reset_index().sort_values('month_year')

        fig_combo = make_subplots(specs=[[{"secondary_y": True}]])
        
        # עמודות מכירות
        fig_combo.add_trace(
            go.Bar(x=monthly_stats['month_year'], y=monthly_stats['rating_count'], 
                   name="סך מכירות (Reviews)", marker_color='skyblue', opacity=0.7),
            secondary_y=False,
        )
        
        # קו דירוג
        fig_combo.add_trace(
            go.Scatter(x=monthly_stats['month_year'], y=monthly_stats['rating'], 
                       name="דירוג ממוצע ⭐", mode='lines+markers', line=dict(color='orange', width=3)),
            secondary_y=True,
        )

        fig_combo.update_layout(height=500, legend=dict(orientation="h", y=1.1, x=0.5))
        fig_combo.update_yaxes(title_text="סך מכירות", secondary_y=False)
        fig_combo.update_yaxes(title_text="דירוג ממוצע", range=[0, 5], secondary_y=True)

        st.plotly_chart(fig_combo, use_container_width=True)

    else:
        st.warning(f"לא נמצאו נתונים לקטגוריה: {selected_cat}")

except Exception as e:
    st.error(f"שגיאה בטעינת הקוד: {e}")
