import os
from config import BASE_DIR

def ensure_name_data_exists():
    data_dir = BASE_DIR / "data"
    data_dir.mkdir(exist_ok=True)
    
    # Check if files exist, if not create dummy ones for the demo to run
    if not (data_dir / "first_names.csv").exists():
        with open(data_dir / "first_names.csv", "w") as f:
            f.write("name\nJohn\nJane\nAlice\nBob\nCharlie\nDavid\nEva\nFrank")
            
    if not (data_dir / "last_names.csv").exists():
        with open(data_dir / "last_names.csv", "w") as f:
            f.write("name\nSmith\nDoe\nJohnson\nBrown\nWilson\nTaylor\nAnderson")