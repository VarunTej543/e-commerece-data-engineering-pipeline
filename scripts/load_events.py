import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:Earthly009#@localhost:5432/ecommerce_db")

events = pd.read_csv("../data/events.csv")

events.to_sql("events", engine, if_exists="replace", index=False)

print("Events loaded successfully")