import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# הגדרות דף
st.set_page_config(page_title="Amazon Business Dashboard", layout="wide")

@st.cache_data
def load_data():
    # טעינת הקובץ הנקי
    df = pd.read_csv('amazon_cleaned.csv')
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    return df

try:
    df = load_data()
    
    st.title("📊 Amazon Business Insights Dashboard")

    # סרגל צד לבחירת קטגוריה
    categories = sorted(df['main_category'].dropna().unique())
    selected_cat = st.sidebar.selectbox("בחר קטגוריה לניתוח:", categories)

    # סינון הנתונים לפי בחירה
    filtered_df = df[df['main_category'] == selected_cat].copy()

    if not filtered_df.empty:
        # --- חלק 1: מד אוץ (Gauge Chart) ---
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
        fig_gauge.update_layout(height=350)
        st.plotly_chart(fig_gauge, use_container_width=True)

        st.markdown("---")

        # --- חלק 2: גרף משולב (Bar + Line) למגמות חודשיות ---
        st.subheader(f"מגמות מכירות ודירוג: {selected_cat}")
        
        # הכנת נתונים חודשיים
        filtered_df['month_year'] = filtered_df['order_date'].dt.to_period('M').astype(str)
        monthly_stats = filtered_df.groupby('month_year').agg({
            'rating_count': 'sum',
            'rating': 'mean'
        }).reset_index().sort_values('month_year')

        # יצירת גרף עם ציר Y כפול
        fig_combo = make_subplots(specs=[[{"secondary_y": True}]])

        # הוספת עמודות (מכירות)
        fig_combo.add_trace(
            go.Bar(x=monthly_stats['month_year'], y=monthly_stats['rating_count'], 
                   name="סך מכירות (Reviews)", marker_color='skyblue', opacity=0.7),
            secondary_y=False,
        )

        # הוספת קו (דירוג)
        fig_combo.add_trace(
            go.Scatter(x=monthly_stats['month_year'], y=monthly_stats['rating'], 
                       name="דירוג ממוצע ⭐", mode='lines+markers', line=dict(color='orange', width=3)),
            secondary_y=True,
        )

        fig_combo.update_layout(xaxis_title="חודש", height=500, legend=dict(orientation="h", y=1.1, x=0.5))
        fig_combo.update_yaxes(title_text="סך מכירות", secondary_y=False)
        fig_combo.update_yaxes(title_text="דירוג ממוצע", range=[0, 5], secondary_y=True)

        st.plotly_chart(fig_combo, use_container_width=True)

    else:
        st.warning("אין נתונים לקטגוריה זו.")

except Exception as e:
    st.error(f"שגיאה: {e}")
