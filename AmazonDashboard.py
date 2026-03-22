import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# הגדרות דף
st.set_page_config(page_title="Amazon Business Dashboard", layout="wide")

@st.cache_data
def load_clean_data():
    # טעינת הקובץ הנקי
    df = pd.read_csv('amazon_cleaned.csv')
    # המרת תאריך
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['month_year'] = df['order_date'].dt.to_period('M').astype(str)
    return df

try:
    df = load_clean_data()
    
    st.title("📊 Amazon Category Analysis Dashboard")
    
    # בחירת קטגוריה בסרגל הצד
    categories = sorted(df['main_category'].dropna().unique())
    selected_cat = st.sidebar.selectbox("בחר קטגוריה לניתוח:", categories)
    
    filtered_df = df[df['main_category'] == selected_cat]

    # --- 1. מד אוץ (Gauge Chart) ---
    avg_rating = filtered_df['rating'].mean()
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = avg_rating,
        title = {'text': f"מדד איכות: {selected_cat}"},
        gauge = {
            'axis': {'range': [0, 5]},
            'steps': [
                {'range': [0, 3.5], 'color': 'red'},
                {'range': [3.5, 4.2], 'color': 'orange'},
                {'range': [4.2, 5], 'color': 'green'}
            ],
            'threshold': {'line': {'color': "black", 'width': 4}, 'value': 4.0}
        }
    ))
    st.plotly_chart(fig_gauge, use_container_width=True)

    # --- 2. מדדי KPI ---
    c1, c2, c3 = st.columns(3)
    c1.metric("סה\"כ מוצרים", len(filtered_df))
    c2.metric("הנחה ממוצעת", f"{filtered_df['discount_percentage'].mean()*100:.1f}%")
    c3.metric("דירוג ממוצע", f"{avg_rating:.2f} ⭐")

    # --- 3. גרף מגמות חודשיות ---
    st.subheader("מגמת דירוגים (Engagement) לאורך זמן")
    trend = filtered_df.groupby('month_year')['rating_count'].sum().reset_index()
    fig_line = px.line(trend, x='month_year', y='rating_count', markers=True)
    st.plotly_chart(fig_line, use_container_width=True)

    # --- 4. התפלגות מחירים מול הנחות ---
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("התפלגות מחירי מכירה")
        fig_hist = px.histogram(filtered_df, x='discounted_price', color_discrete_sequence=['skyblue'])
        st.plotly_chart(fig_hist, use_container_width=True)
    with col_b:
        st.subheader("קשר בין הנחה לדירוג")
        fig_scatter = px.scatter(filtered_df, x='discount_percentage', y='rating', size='rating_count', hover_name='product_name')
        st.plotly_chart(fig_scatter, use_container_width=True)

except Exception as e:
    st.error(f"שגיאה בטעינת הקובץ הנקי: {e}")
    st.info("וודא שהקובץ amazon_cleaned.csv נמצא ב-GitHub באותה תיקייה.")
