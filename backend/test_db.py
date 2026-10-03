import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
db_url = os.getenv("DATABASE_URL")
print(f"Connecting to {db_url}")
engine = create_engine(db_url, connect_args={"connect_timeout": 5})
try:
    with engine.connect() as conn:
        print("Successfully connected!")
except Exception as e:
    print(f"Error: {e}")
