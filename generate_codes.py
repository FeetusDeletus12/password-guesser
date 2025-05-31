import json
import random
from datetime import datetime

def generate_code():
    return str(random.randint(1000, 9999))

codes = {
    "level1": generate_code(),
    "level2": generate_code(),
    "last_updated": datetime.now().strftime("%Y-%m-%d")
}

with open("codes.json", "w") as f:
    json.dump(codes, f, indent=2)
