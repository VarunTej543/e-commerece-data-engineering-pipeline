import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine("postgresql://postgres:Earthly009#@localhost:5432/ecommerce_db")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

events_path = os.path.join(BASE_DIR, "data", "events.csv")

events = pd.read_csv(events_path)

events.to_sql(
    "events",
    engine,
    if_exists="replace",
    index=False
)

print("Events data loaded successfully")