from pathlib import Path
import json

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "expenses.json"

def load_expenses():
    # check if notebook exists
    if DATA_FILE.exists():
        # if yes, open and read it
        with open(DATA_FILE, "r") as f:
            content = f.read()
            if content.strip():
                return json.loads(content)
    # if no, return empty list
    return []

def save_expenses(data):
    # make sure the folder exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    # open and write the data
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)       