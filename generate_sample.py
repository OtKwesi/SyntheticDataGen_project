from syntheticgen import generate_synthetic_data

# Path to your YAML schema
schema_file = "schemas/example.yaml"

# Generate 50 rows and save to CSV
df = generate_synthetic_data(schema_file, n_rows=50, save_csv=True, filename="synthetic_sample.csv")

# Display first 5 rows in console
print(df.head())
print("[INFO] Sample dataset saved to synthetic_sample.csv")
