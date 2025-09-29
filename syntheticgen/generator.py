import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta
import yaml

fake = Faker()

class SyntheticDataGenerator:
    """
    Generic Synthetic Data Generator for any ML or analytics project.
    Features:
        - Column types: id, numeric, categorical, datetime, text
        - Schema-driven: easy plug-and-play
        - Produces Pandas DataFrame or CSV
    """

    def __init__(self, schema: list, n_rows: int = 1000, seed: int = None):
        """
        Initialize generator.
        Args:
            schema (list): Column definitions
            n_rows (int): Number of rows to generate
            seed (int): Optional random seed for reproducibility
        """
        self.schema = schema
        self.n_rows = n_rows
        if seed:
            np.random.seed(seed)
            random.seed(seed)
            Faker.seed(seed)

    def _generate_column(self, col_config: dict, index: int):
        """Generate data for a single column based on its type."""
        col_type = col_config["type"]
        
        if col_type == "id":
            prefix = col_config.get("prefix", "")
            return f"{prefix}{str(index+1).zfill(5)}"
        
        elif col_type == "numeric":
            min_val, max_val = col_config.get("range", (0, 100))
            return round(random.uniform(min_val, max_val), 2)
        
        elif col_type == "categorical":
            categories = col_config.get("categories", ["A", "B"])
            return random.choice(categories)
        
        elif col_type == "datetime":
            start = datetime.fromisoformat(col_config.get("start_date", "2020-01-01"))
            end = datetime.fromisoformat(col_config.get("end_date", "2021-01-01"))
            delta = (end - start).days
            return start + timedelta(days=random.randint(0, delta),
                                     hours=random.randint(0,23),
                                     minutes=random.randint(0,59))
        
        elif col_type == "text":
            faker_func = getattr(fake, col_config.get("faker", "word"))
            return faker_func()
        
        else:
            raise ValueError(f"Unsupported column type: {col_type}")

    def generate(self, save_csv: bool = False, filename: str = "synthetic_data.csv"):
        """
        Generate the full dataset.
        Args:
            save_csv (bool): Save DataFrame to CSV
            filename (str): File name if saving
        Returns:
            pd.DataFrame: Generated dataset
        """
        data = {}
        for col in self.schema:
            col_name = col["name"]
            data[col_name] = [self._generate_column(col, i) for i in range(self.n_rows)]
        
        df = pd.DataFrame(data)
        
        if save_csv:
            df.to_csv(filename, index=False)
            print(f"[INFO] Dataset saved to {filename}")
        
        return df

def generate_synthetic_data(schema_file: str, n_rows: int = 1000, save_csv: bool = True, filename: str = "synthetic_data.csv"):
    """
    Load YAML schema and generate synthetic dataset.
    """
    with open(schema_file, "r") as f:
        schema = yaml.safe_load(f)
    
    generator = SyntheticDataGenerator(schema, n_rows)
    return generator.generate(save_csv=save_csv, filename=filename)
