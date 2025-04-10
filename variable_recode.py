import pandas as pd
import numpy as np


# Load your dataset (adjust file path as needed)
df = pd.read_csv(r"C:\Users\rzahan\OneDrive - Loyola University Chicago\Research\Abhijna Research\US suicide and Occupation\SuicideDeaths.csv")

# Convert all column names to lowercase and strip whitespace for consistency
df.columns = df.columns.str.strip().str.lower()

# Recode EDUCATION (from locations 63-64 in documentation)
education_map = {
    1: "8th grade or less",
    2: "9-12th grade, no diploma",
    3: "High school graduate or GED",
    4: "Some college credit, no degree",
    5: "Associate degree",
    6: "Bachelor's degree",
    7: "Master's degree",
    8: "Doctorate or professional degree",
    9: "Unknown"
}
df['education_recode'] = df['education'].map(education_map)

# Recode SEX (from location 69)
sex_map = {
    'M': "Male",
    'F': "Female"
}
df['sex_recode'] = df['sex'].map(sex_map)

# Recode MARITAL STATUS (from location 84)
marital_status_map = {
    'S': "Never Married",
    'M': "Married",
    'W': "Widowed",
    'D': "Divorced",
    'U': "Unknown"
}
df['marital_status_recode'] = df['marital_status'].map(marital_status_map)

# Convert 'age_key' and 'age_value' to string to ensure proper processing
df['age_key'] = df['age_key'].astype(str).str.strip()
df['Age_Value'] = df['Age_Value'].astype(str).str.strip()

# Convert 'age_value' to numeric, handling missing values
df['age_value_num'] = pd.to_numeric(df['Age_Value'], errors='coerce')

# Function to convert age to years
def calculate_age_in_years(row):
    key = row['age_key']
    val = row['age_value_num']
    
    if pd.isna(val):
        return np.nan
    
    if key == '1':  # Years
        return val
    elif key == '2':  # Months
        return val / 12
    elif key == '4':  # Days
        return val / 365.25
    elif key == '5':  # Hours
        return val / (365.25 * 24)
    elif key == '6':  # Minutes
        return val / (365.25 * 24 * 60)
    elif key == '9':  # Age not stated
        return np.nan
    else:
        return np.nan

# Apply the conversion function
df['age_in_years'] = df.apply(calculate_age_in_years, axis=1)

# View the result
print(df[['age_key', 'Age_Value', 'age_in_years']].head(10))

# View a few rows to confirm
print(df[['education', 'education_recode', 'sex', 'sex_recode', 'marital_status', 'marital_status_recode', 'manner_of_death', 'manner_of_death_recode']].head())

# Export to CSV if needed
output_path = r"C:\Users\rzahan\OneDrive - Loyola University Chicago\Research\Eniola Heat related deaths\mort2023us\SuicideDeaths_Recoded.csv"
df.to_csv(output_path, index=False, encoding='utf-8')

print(f"Recoded data exported to: {output_path}")
