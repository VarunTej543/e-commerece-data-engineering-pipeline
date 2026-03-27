import os

print("Starting pipeline...")

os.system("python init_db.py")
os.system("python load_data.py")
os.system("python build_star_schema.py")
os.system("python load_events.py")

print("Pipeline completed successfully")