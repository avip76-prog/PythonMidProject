{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e1dca867-7475-4865-a721-58d7d63497b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Starting ETL Pipeline...\n",
      "✅ Files loaded successfully!\n",
      "🎉 Success! Processed 1043 rows and saved to amazon_cleaned.csv\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "# רשימת הקבצים הנדרשים להרצה\n",
    "required_files = ['amazon.csv', 'inventory.csv']\n",
    "\n",
    "# 1. בדיקה האם הקבצים קיימים במערכת לפני שמתחילים\n",
    "missing_files = [f for f in required_files if not os.path.exists(f)]\n",
    "\n",
    "if missing_files:\n",
    "    print(f\"❌ שגיאה: חסרים קבצים קריטיים להרצה: {', '.join(missing_files)}\")\n",
    "    print(\"התהליך נעצר.\")\n",
    "else:\n",
    "    try:\n",
    "        print(\"Starting ETL Pipeline...\")\n",
    "        \n",
    "        # Load files\n",
    "        df = pd.read_csv('amazon.csv')\n",
    "        inventory_df = pd.read_csv('inventory.csv')\n",
    "        print(\"✅ Files loaded successfully!\")\n",
    "\n",
    "        #### Data Cleaning ####\n",
    "        df = df.drop_duplicates(subset='product_id')\n",
    "\n",
    "        # ניקוי עמודות מחיר ודירוג\n",
    "        df['discounted_price'] = df['discounted_price'].str.replace('₹', '').str.replace(',', '').astype(float)\n",
    "        df['actual_price'] = df['actual_price'].str.replace('₹', '').str.replace(',', '').astype(float)\n",
    "        df['rating'] = pd.to_numeric(df['rating'].astype(str).str.replace('|', ''), errors='coerce')\n",
    "        df['rating_count'] = pd.to_numeric(df['rating_count'].astype(str).str.replace(',', ''), errors='coerce')\n",
    "        df['discount_percentage'] = df['discount_percentage'].str.replace('%', '').astype(float)/100\n",
    "        df['main_category'] = df['category'].str.split('|').str[0]\n",
    "\n",
    "        #### Data Filter ####\n",
    "        # סינון מוצרי פרימיום\n",
    "        df = df[df['actual_price'] < 5000]\n",
    "\n",
    "        # 2. בדיקת איכות: האם נשארו נתונים אחרי הסינון?\n",
    "        if df.empty:\n",
    "            print(\"⚠️ אזהרה: לאחר סינון מוצרי פרימיום, לא נותרו מוצרים ב-DataFrame.\")\n",
    "        \n",
    "        # Merge Amazon clean file with Inventory file\n",
    "        df_enriched = pd.merge(df, inventory_df, on='product_id', how='left')\n",
    "\n",
    "        # 3. בדיקת איכות: האם המיזוג הצליח? (בדיקה אם יש מוצרים ללא נתוני מלאי)\n",
    "        missing_inventory = df_enriched['inventory_status'].isna().sum() if 'inventory_status' in df_enriched else 0\n",
    "        if missing_inventory > 0:\n",
    "            print(f\"⚠️ שים לב: נמצאו {missing_inventory} מוצרים ללא התאמה בקובץ ה-Inventory.\")\n",
    "\n",
    "        # Save the results\n",
    "        df_enriched.to_csv('amazon_cleaned.csv', index=False)\n",
    "        print(f\"🎉 Success! Processed {len(df_enriched)} rows and saved to amazon_cleaned.csv\")\n",
    "\n",
    "    except Exception as e:\n",
    "        print(f\"❌ התרחשה שגיאה בלתי צפויה במהלך ה-Pipeline: {e}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0622953d-bad5-47f2-9b25-0836080ffbf6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45f769bc-2aba-4491-966f-9eabb629d670",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04e82fb1-0d24-4f9d-99f4-9d9560217b42",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-ai-2025.12-py312",
   "language": "python",
   "name": "conda-env-anaconda-ai-2025.12-py312-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
