import os
import pandas as pd
import pytest
from syntheticgen.generator import generate_synthetic_data

# Test parameters
SCHEMA_FILE = "schemas/example.yaml"
TEST_CSV = "tests/test_output.csv"

def test_generate_dataframe():
    """Test that the generator returns a DataFrame with the correct number of rows."""
    df = generate_synthetic_data(SCHEMA_FILE, n_rows=10, save_csv=False)
    assert isinstance(df, pd.DataFrame), "Output should be a Pandas DataFrame"
    assert len(df) == 10, "DataFrame should have 10 rows"
    assert all(col in df.columns for col in ["id", "amount", "date", "category", "notes"]), "All schema columns should exist"

def test_save_csv():
    """Test that the generator saves a CSV file correctly."""
    if os.path.exists(TEST_CSV):
        os.remove(TEST_CSV)
    
    df = generate_synthetic_data(SCHEMA_FILE, n_rows=5, save_csv=True, filename=TEST_CSV)
    assert os.path.exists(TEST_CSV), "CSV file should be created"
    
    # Clean up
    os.remove(TEST_CSV)

if __name__ == "__main__":
    pytest.main([__file__])
