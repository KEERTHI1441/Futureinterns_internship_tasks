import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("ENCRYPTION_KEY")

if key:
    print(f"ENCRYPTION_KEY found: {key}")
else:
    print("ENCRYPTION_KEY not found!")
