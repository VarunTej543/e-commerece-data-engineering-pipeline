import subprocess
import logging
import os

# Get current script directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Log file path
log_file = os.path.join(BASE_DIR, "..", "logs", "pipeline.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_script(script_name):
    script_path = os.path.join(BASE_DIR, script_name)

    try:
        logging.info(f"Starting {script_name}")
        subprocess.run(["python", script_path], check=True)
        logging.info(f"Finished {script_name}")
    except subprocess.CalledProcessError:
        logging.error(f"Error running {script_name}")

def main():
    logging.info("Pipeline started")

    scripts = [
        "load_data.py",
        "build_star_schema.py",
        "load_events.py"
    ]

    for script in scripts:
        run_script(script)

    logging.info("Pipeline completed")

if __name__ == "__main__":
    main()