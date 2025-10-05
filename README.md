# Synthetic_Data_Generation

SyntheticGen is a plug-and-play **synthetic data generator** for machine learning engineers, data scientists, and analysts. It allows you to **define your dataset schema in YAML** and generate realistic synthetic datasets in CSV or Pandas DataFrame format.

The goal is to provide an **open-source alternative to Kaggle datasets** by letting you generate your own customisable data.

## ✨ Features

- Define datasets via simple **YAML schemas**.
- Generate **CSV files** or directly return **Pandas DataFrames**.
- **Command-line interface (CLI)** and **Python API**.
- Flexible: works for *any* project domain (ML, data analytics, data science).
- MIT Licensed — free to use, modify, and share.
- CI/CD ready with GitHub Actions and unit tests.

## 📦 Installation - Quickstart (30 seconds)

```bash
# Step 1: Clone the repository
git clone https://github.com/<your-username>/syntheticgen.git
cd syntheticgen

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Install the package locally
pip install .
```

## 📝 Defining a Schema

Datasets are defined in YAML schema files (placed in the `schemas/` folder). Below is an example schema (`schemas/example.yaml`):

```yaml
columns:
  - name: user_id
    type: integer
    min: 1
    max: 10000
  - name: signup_date
    type: date
    start: 2020-01-01
    end: 2023-12-31
  - name: country
    type: category
    values: ["US", "UK", "GH", "IN"]
  - name: purchase_amount
    type: float
    min: 10.0
    max: 500.0
```

## 🐍 Usage (Python API)

```python
from syntheticgen import generate_synthetic_data

# Generate 1000 rows of synthetic data and save to CSV
df = generate_synthetic_data(
    "schemas/example.yaml",  # Path to YAML schema
    n_rows=1000,            # Number of rows
    save_csv=True,          # Save to CSV
    filename="output.csv"   # Output filename
)

# Preview the first 5 rows
print(df.head())
```

## 💻 Usage (CLI)

```bash
# Generate 10,000 rows and save to output.csv
syntheticgen --schema schemas/example.yaml --rows 10000 --out output.csv

# Generate 100 rows and preview in terminal without saving
syntheticgen --schema schemas/example.yaml --rows 100 --no-save
```

## 📂 Project Structure

```syntheticgen_project/
├─ syntheticgen/         # Core Python package
│   ├─ __init__.py
│   ├─ generator.py
│   ├─ cli.py
│   └─ utils.py
├─ schemas/              # Example schemas
│   └─ example.yaml
├─ tests/                # Unit tests
│   └─ test_generator.py
├─ .github/workflows/    # CI/CD workflows
│   └─ ci.yml
├─ requirements.txt      # Python dependencies
├─ setup.py              # Package setup
├─ README.md             # This file
├─ LICENSE               # MIT License
└─ .gitignore
```

## 🧪 Running Unit Tests

```bash
# Run all unit tests using pytest
pytest
```

## ⚙️ Continuous Integration (CI)

This repository uses GitHub Actions for CI/CD.0
Every push triggers:

- Installation of dependencies
- Execution of unit tests

Check the Actions tab on GitHub to see test results.

## 📜 License

This project is licensed under the MIT License — free to use, modify, and distribute. See LICENSE for details.

## 🚀 Contributing

Contributions are welcome! Feel free to fork the repo, open issues, or submit pull requests.
