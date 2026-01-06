import pandas as pd
import random
from config import BASE_DIR

class NameGenerator:
    def __init__(self):
        self.first_names = []
        self.last_names = []
        self._load_data()

    def _load_data(self):
        # Load from CSVs in /data directory
        try:
            df_first = pd.read_csv(BASE_DIR / "data" / "first_names.csv")
            df_last = pd.read_csv(BASE_DIR / "data" / "last_names.csv")
            self.first_names = df_first['name'].tolist()
            self.last_names = df_last['name'].tolist()
        except Exception:
            # Fallback if files missing
            self.first_names = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer"]
            self.last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia"]

    def generate_full_name(self):
        return f"{random.choice(self.first_names)} {random.choice(self.last_names)}"