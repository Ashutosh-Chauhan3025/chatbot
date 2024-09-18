import streamlit as st
import json
import pandas as pd
# Load datasets
with open('trains.json') as f:
    trains_data = json.load(f)['features']  # assuming 'features' contains train data

with open('schedules.json') as f:
    schedule_data = json.load(f)  # directly loading schedule data (no 'features')

with open('stations.json') as f:
    stations_data = json.load(f)['features']  # assuming 'features' contains station data

# Function to get train information
def get_train_info(train_number):
    for train in trains_data:
        train_props = train.get('properties', {})
        if train_props.get('number') == train_number:
            return {
                'Train Name': train_props.get('name', 'N/A'),
                'From Station': train_props.get('from_station_name', 'N/A'),
                'To Station': train_props.get('to_station_name', 'N/A'),
                'Departure': train_props.get('departure', 'N/A'),
                'Arrival': train_props.get('arrival', 'N/A'),
                'Duration (hours)': train_props.get('duration_h', 'N/A'),
                'Duration (minutes)': train_props.get('duration_m', 'N/A'),
                'Distance (km)': train_props.get('distance', 'N/A'),
                'Train Type': train_props.get('type', 'N/A')
            }
    return "Train not found."

# Function to get schedule information
def get_schedule_info(station_code):
    schedule_list = []
    for schedule in schedule_data:
        if schedule.get('station_code') == station_code:
            schedule_list.append({
                'Train Number': schedule.get('train_number', 'N/A'),
                'Train Name': schedule.get('train_name', 'N/A'),
                'Station Name': schedule.get('station_name', 'N/A'),
                'Departure': schedule.get('departure', 'N/A'),
                'Arrival': schedule.get('arrival', 'N/A'),
                'Day': schedule.get('day', 'N/A')
            })
    if schedule_list:
        df=pd.DataFrame(schedule_list)
        return df
    return "No schedules found for this station."

# Function to get station information
def get_station_info(station_code):
    for station in stations_data:
        station_props = station.get('properties', {})
        if station_props.get('code') == station_code:
            return {
                'Station Name': station_props.get('name', 'N/A'),
                'State': station_props.get('state', 'N/A'),
                'Zone': station_props.get('zone', 'N/A'),
                'Address': station_props.get('address', 'N/A'),
                'Coordinates': station.get('geometry', {}).get('coordinates', 'N/A')
            }
    return "Station not found."

# Query handler function
def respond_to_query(query):
    if "train" in query.lower():
        # Extract train number from query
        train_number = query.split()[-1]  # Assuming train number is the last word
        return get_train_info(train_number)
    elif "schedule" in query.lower():
        # Extract station code from query
        station_code = query.split()[-1]  # Assuming station code is the last word
        return get_schedule_info(station_code)
    elif "station" in query.lower():
        # Extract station code from query
        station_code = query.split()[-1]  # Assuming station code is the last word
        return get_station_info(station_code)
    else:
        return "Sorry, I don't understand the question."

# Streamlit app
st.title("Train & Station Information Chatbot")

# Create a text input for the user to type their message
user_input = st.text_input("Ask about trains, schedules, or stations: ", "")

if user_input:
    # Get response from the chatbot
    reply = respond_to_query(user_input)
    
    # Display the chatbot's response
    if isinstance(reply, list):
        for item in reply:
            st.write(item)
    else:
        st.text_area("Chatbot Response: ", str(reply), height=200)

