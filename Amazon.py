import pandas as pd
import streamlit as st
import plotly.express as px

# הגדרות דף
st.set_page_config(page_title="Amazon Analysis", layout="wide")
st.title("📊 Amazon Sales Dashboard")

# פונקציית טעינה וניקוי (הקוד המקורי שלך מלוטש)
@st.cache_data
def load_and_clean_data():
    # טעינה - וודא שהקובץ amazon.csv נמצא ב-GitHub באותה תיקייה
    #df = pd.read_csv('amazon.csv')
    df = pd.read_csv('amazon_cleaned.csv')
    
    # הסרת כפילויות
    df = df.drop_duplicates(subset='product_id')
    
    # ניקוי מחירים
    for col in ['discounted_price', 'actual_price']:
        df[col] = df[col].astype(str).str.replace('₹', '').str.replace(',', '').astype(float)
    
    # ניקוי דירוג (טיפול ב-| והמרה למספר)
    df['rating'] = pd.to_numeric(df['rating'].astype(str).str.replace('|', ''), errors='coerce')
    
    # ניקוי כמות דירוגים
    df['rating_count'] = pd.to_numeric(df['rating_count'].astype(str).str.replace(',', ''), errors='coerce')
    
    # יצירת קטגוריה ראשית
    df['main_category'] = df['category'].str.split('|').str[0]
    
    return df

try:
    data = load_and_clean_data()

    # תפריט צד לבחירת קטגוריה
    categories = sorted(data['main_category'].dropna().unique())
    selected_cat = st.sidebar.selectbox("בחר קטגוריה ראשית:", categories)

    if selected_cat:
        filtered_df = data[data['main_category'] == selected_cat]
        
        # הצגת מדדים בראש הדף
        col1, col2, col3 = st.columns(3)
        col1.metric("כמות מוצרים", len(filtered_df))
        col2.metric("דירוג ממוצע", f"{filtered_df['rating'].mean():.2f} ⭐")
        col3.metric("מחיר ממוצע", f"₹{filtered_df['actual_price'].mean():.0f}")

        # גרף התפלגות דירוגים
        fig = px.histogram(filtered_df, x='rating', title=f"התפלגות דירוגים ב-{selected_cat}", 
                           color_discrete_sequence=['#FF9900'])
        st.plotly_chart(fig, use_container_width=True)

        # הצגת הטבלה
        st.write(f"### רשימת מוצרים ב-{selected_cat}")
        st.dataframe(filtered_df[['product_name', 'actual_price', 'rating', 'rating_count']].sort_values(by='rating', ascending=False))

except Exception as e:
    st.error(f"שגיאה: {e}")
    st.info("וודא שקובץ ה-amazon.csv נמצא ב-GitHub")
