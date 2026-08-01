import os
import json

def save_jobs(record):
    
    filename = "jobs.json"
    # Load existing data
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Append new record
    data.append(record)
    
    # Save
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("================== Job Saved =====================")

