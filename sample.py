import ijson
import streamlit as st

# Stream JSON data from a large file
def stream_large_json(file_path):
    schedule_list = []
    with open(file_path, 'r') as f:
        parser = ijson.items(f, 'item')  # Assuming JSON is an array of objects
        for schedule in parser:
            schedule_list.append(schedule)
            if len(schedule_list) >= 1000:  # Process in batches, e.g., every 1000 records
                break  # Adjust this logic to suit your needs
    return schedule_list

# Load large JSON file (streaming)
file_path = 'schedules.json'
try:
    schedule_data = stream_large_json(file_path)
    st.write(f"Loaded {len(schedule_data)} schedule entries")
except Exception as e:
    st.error(f"Error streaming large JSON file: {e}")
