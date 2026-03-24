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
      "Amazon File loaded successfully!\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "\n",
    "# Load the file directly from the current working directory\n",
    "df = pd.read_csv('amazon.csv')\n",
    "\n",
    "print(\"Amazon File loaded successfully!\")\n",
    "\n",
    "#### Data Cleaning ####\n",
    "# Remove duplicates\n",
    "df = df.drop_duplicates(subset='product_id')\n",
    "total_rows = len(df)\n",
    "\n",
    "# Cleaning discounted_price Column: remove Rupee currency , remove comma and convert to float\n",
    "df['discounted_price'] = df['discounted_price'].str.replace('₹', '').str.replace(',', '').astype(float)\n",
    "# Cleaning actual_price Column: remove Rupee currency , remove comma and convert to float\n",
    "df['actual_price'] = df['actual_price'].str.replace('₹', '').str.replace(',', '').astype(float)\n",
    "# Cleaning rating Column: remove \"|\" char and convert to numeric\n",
    "df['rating'] = pd.to_numeric(df['rating'].astype(str).str.replace('|', ''), errors='coerce')\n",
    "# Cleaning rating_count Column:  remove comma chars and convert to numeric\n",
    "df['rating_count'] = pd.to_numeric(df['rating_count'].astype(str).str.replace(',', ''), errors='coerce')\n",
    "# Cleaning discount_percentage Column:  remove % chars and convert to numeric\n",
    "df['discount_percentage'] = df['discount_percentage'].str.replace('%', '').astype(float)/100\n",
    "# Create a new Category\n",
    "df['main_category'] = df['category'].str.split('|').str[0]\n",
    "\n",
    "####  Data Filter ####\n",
    "#remove Premium product  \n",
    "df = df[df['actual_price'] < 5000]\n",
    "#save the results to new csv\n",
    "df.to_csv('amazon_cleaned.csv', index=False)\n",
    "\n"
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
