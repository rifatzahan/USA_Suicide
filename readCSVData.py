import pandas as pd

# Define the file path
csv_file_path = r"C:\Users\......\VS23MORT.csv"

# Read the CSV file as strings
df = pd.read_csv(csv_file_path, dtype=str, low_memory=False)

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Confirm column names
print("Columns in dataset:", df.columns.tolist())

# Clean icd_10 column
df['icd_10'] = df['icd_10'].str.strip().str.upper()

# Explore ICD-10 unique values (optional but good for debugging)
print("\nICD-10 Unique Codes (sample):")
print(df['icd_10'].value_counts().head(20))  # Print top 20 codes for verification

# Filter rows where icd_10 contains 

# X60 to X84
# X72 to X74
# X83
# Y87.0

pattern = r"^(X6[0-9](\.\d+)?|X7[0-9](\.\d+)?|X8[0-4](\.\d+)?|Y87\.0)$"
suicide_deaths = df[df['icd_10'].str.match(pattern, na=False)]


# Check number of rows found
print(f"\nNumber of suicide-related deaths (X60): {suicide_deaths.shape[0]}")

# Define output file path
output_csv_path = r"C:\...........\SuicideDeaths.csv"

# Save the filtered dataset
suicide_deaths.to_csv(output_csv_path, index=False, encoding="utf-8")

print(f"Filtered suicide-related deaths saved to: {output_csv_path}")


