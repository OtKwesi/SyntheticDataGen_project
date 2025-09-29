import argparse
from .generator import generate_synthetic_data

def main():
    parser = argparse.ArgumentParser(description="Generate synthetic datasets from schema YAML.")
    parser.add_argument("--schema", type=str, required=True, help="Path to YAML schema file")
    parser.add_argument("--rows", type=int, default=1000, help="Number of rows to generate")
    parser.add_argument("--out", type=str, default="synthetic_data.csv", help="Output CSV file name")
    parser.add_argument("--no-save", action="store_true", help="Do not save CSV, just print preview")
    
    args = parser.parse_args()
    
    save_csv = not args.no_save
    df = generate_synthetic_data(schema_file=args.schema, n_rows=args.rows, save_csv=save_csv, filename=args.out)
    
    print("[INFO] Preview of generated data:")
    print(df.head())

if __name__ == "__main__":
    main()
