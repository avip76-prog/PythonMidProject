import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# הגדרת דף רחב - מכין תשתית להוספת גרפים נוספים בהמשך
st.set_page_config(page_title="Amazon Business Dashboard", layout="wide")

# פונקציה לטעינת הנתונים מהקובץ הנקי
@st.cache_data
def load_data():
    # הקוד פונה ישירות לקובץ הנקי שיצרת
    df = pd.read_csv('amazon_cleaned.csv')
    return df

try:
    df = load_data()
    
    st.title("📊 Amazon Category Insights")
    st.markdown("---")

    # 1. סרגל צד לבחירת קטגוריה
    st.sidebar.header("מסננים")
    categories = sorted(df['main_category'].dropna().unique())
    selected_cat = st.sidebar.selectbox("בחר קטגוריה ראשית:", categories)

    # 2. סינון הנתונים לפי הבחירה
    filtered_df = df[df['main_category'] == selected_cat]

    if not filtered_df.empty:
        # חישוב הנתון למד-אוץ
        avg_rating = filtered_df['rating'].mean()

        # 3. יצירת גרף המד-אוץ (Gauge Chart)
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = avg_rating,
            title = {'text': f"חווית לקוח: {selected_cat}", 'font': {'size': 24}},
            gauge = {
                'axis': {'range': [0, 5], 'tickwidth': 1},
                'bar': {'color': "black"},
                'steps': [
                    {'range': [0, 3.5], 'color': "#FF4B4B"}, # אדום
                    {'range': [3.5, 4.2], 'color': "#FFA500"}, # כתום
                    {'range': [4.2, 5], 'color': "#238636"}    # ירוק
                ],
                'threshold': {
                    'line': {'color': "white", 'width': 4},
                    'thickness': 0.75,
                    'value': 4.0 # יעד מינימלי
                }
            }
        ))

        fig_gauge.update_layout(height=450)

        # הצגת הגרף ב-Streamlit
        st.plotly_chart(fig_gauge, use_container_width=True)
        
        # --- כאן תוכל להוסיף פונקציות לגרפים נוספים בעתיד ---
        st.info(f"מציג נתונים עבור {len(filtered_df)} מוצרים בקטגוריית {selected_cat}")

    else:
        st.warning("לא נמצאו נתונים לקטגוריה הנבחרת.")

except Exception as e:
    st.error(f"שגיאה קריטית: {e}")
    st.info("וודא שקובץ ה-amazon_cleaned.csv נמצא באותה תיקייה ב-GitHub.")
