# import streamlit as st
# import json
# import pandas as pd
# # Load datasets
# with open('trains.json') as f:
#     trains_data = json.load(f)['features']  # assuming 'features' contains train data

# with open('schedules.json') as f:
#     schedule_data = json.load(f)  # directly loading schedule data (no 'features')

# with open('stations.json') as f:
#     stations_data = json.load(f)['features']  # assuming 'features' contains station data

# # Function to get train information
# def get_train_info(train_number):
#     for train in trains_data:
#         train_props = train.get('properties', {})
#         if train_props.get('number') == train_number:
#             return {
#                 'Train Name': train_props.get('name', 'N/A'),
#                 'From Station': train_props.get('from_station_name', 'N/A'),
#                 'To Station': train_props.get('to_station_name', 'N/A'),
#                 'Departure': train_props.get('departure', 'N/A'),
#                 'Arrival': train_props.get('arrival', 'N/A'),
#                 'Duration (hours)': train_props.get('duration_h', 'N/A'),
#                 'Duration (minutes)': train_props.get('duration_m', 'N/A'),
#                 'Distance (km)': train_props.get('distance', 'N/A'),
#                 'Train Type': train_props.get('type', 'N/A')
#             }
#     return "Train not found."

# # Function to get schedule information
# def get_schedule_info(station_code):
#     schedule_list = []
#     for schedule in schedule_data:
#         if schedule.get('station_code') == station_code:
#             schedule_list.append({
#                 'Train Number': schedule.get('train_number', 'N/A'),
#                 'Train Name': schedule.get('train_name', 'N/A'),
#                 'Station Name': schedule.get('station_name', 'N/A'),
#                 'Departure': schedule.get('departure', 'N/A'),
#                 'Arrival': schedule.get('arrival', 'N/A'),
#                 'Day': schedule.get('day', 'N/A')
#             })
#     if schedule_list:
#         df=pd.DataFrame(schedule_list)
#         return df
#     return "No schedules found for this station."

# # Function to get station information
# def get_station_info(station_code):
#     for station in stations_data:
#         station_props = station.get('properties', {})
#         if station_props.get('code') == station_code:
#             return {
#                 'Station Name': station_props.get('name', 'N/A'),
#                 'State': station_props.get('state', 'N/A'),
#                 'Zone': station_props.get('zone', 'N/A'),
#                 'Address': station_props.get('address', 'N/A'),
#                 'Coordinates': station.get('geometry', {}).get('coordinates', 'N/A')
#             }
#     return "Station not found."

# # Query handler function
# def respond_to_query(query):
#     if "train" in query.lower():
#         # Extract train number from query
#         train_number = query.split()[-1]  # Assuming train number is the last word
#         return get_train_info(train_number)
#     elif "schedule" in query.lower():
#         # Extract station code from query
#         station_code = query.split()[-1]  # Assuming station code is the last word
#         return get_schedule_info(station_code)
#     elif "station" in query.lower():
#         # Extract station code from query
#         station_code = query.split()[-1]  # Assuming station code is the last word
#         return get_station_info(station_code)
#     else:
#         return "Sorry, I don't understand the question."

# # Streamlit app
# st.title("Train & Station Information Chatbot")

# # Create a text input for the user to type their message
# user_input = st.text_input("Ask about trains, schedules, or stations: ", "")

# if user_input:
#     # Get response from the chatbot
#     reply = respond_to_query(user_input)
    
#     # Display the chatbot's response
#     if isinstance(reply, list):
#         for item in reply:
#             st.write(item)
#     else:
#         st.text_area("Chatbot Response: ", str(reply), height=200)










# import streamlit as st
# import json
# import pandas as pd

# # Load datasets
# with open('trains.json') as f:
#     trains_data = json.load(f)['features']  # assuming 'features' contains train data

# with open('schedules.json') as f:
#     schedule_data = json.load(f)  # directly loading schedule data

# with open('stations.json') as f:
#     stations_data = json.load(f)['features']  # assuming 'features' contains station data

# # Function to get train information
# def get_train_info(train_number):
#     for train in trains_data:
#         train_props = train.get('properties', {})
#         if train_props.get('number') == train_number:
#             return {
#                 'Train Name': train_props.get('name', 'N/A'),
#                 'From Station': train_props.get('from_station_name', 'N/A'),
#                 'To Station': train_props.get('to_station_name', 'N/A'),
#                 'Departure': train_props.get('departure', 'N/A'),
#                 'Arrival': train_props.get('arrival', 'N/A'),
#                 'Duration (hours)': train_props.get('duration_h', 'N/A'),
#                 'Duration (minutes)': train_props.get('duration_m', 'N/A'),
#                 'Distance (km)': train_props.get('distance', 'N/A'),
#                 'Train Type': train_props.get('type', 'N/A')
#             }
#     return "Train not found."

# # Function to get schedule information
# def get_schedule_info(station_code):
#     schedule_list = []
#     for schedule in schedule_data:
#         if schedule.get('station_code') == station_code:
#             schedule_list.append({
#                 'Train Number': schedule.get('train_number', 'N/A'),
#                 'Train Name': schedule.get('train_name', 'N/A'),
#                 'Station Name': schedule.get('station_name', 'N/A'),
#                 'Departure': schedule.get('departure', 'N/A'),
#                 'Arrival': schedule.get('arrival', 'N/A'),
#                 'Day': schedule.get('day', 'N/A')
#             })
#     if schedule_list:
#         df = pd.DataFrame(schedule_list)
#         return df
#     return "No schedules found for this station."

# # Function to get station information
# def get_station_info(station_code):
#     for station in stations_data:
#         station_props = station.get('properties', {})
#         if station_props.get('code') == station_code:
#             return {
#                 'Station Name': station_props.get('name', 'N/A'),
#                 'State': station_props.get('state', 'N/A'),
#                 'Zone': station_props.get('zone', 'N/A'),
#                 'Address': station_props.get('address', 'N/A'),
#                 'Coordinates': station.get('geometry', {}).get('coordinates', 'N/A')
#             }
#     return "Station not found."

# # Query handler function
# def respond_to_query(query):
#     if "train" in query.lower():
#         # Extract train number from query
#         train_number = query.split()[-1]  # Assuming train number is the last word
#         return get_train_info(train_number)
#     elif "schedule" in query.lower():
#         # Extract station code from query
#         station_code = query.split()[-1]  # Assuming station code is the last word
#         return get_schedule_info(station_code)
#     elif "station" in query.lower():
#         # Extract station code from query
#         station_code = query.split()[-1]  # Assuming station code is the last word
#         return get_station_info(station_code)
#     else:
#         return "Sorry, I don't understand the question."

# # Streamlit app
# def main():
#     # Greeting and task list
#     st.title("Welcome to the Train Information Assistant!")

#     st.write("""
#     Hello! I am here to assist you with the following tasks:
#     - 🚆 **Train Details**: Get detailed information about trains.
#     - 🕒 **Train Schedules**: Check schedules at a specific station.
#     - 🗺️ **Station Information**: Get details about railway stations.
#     """)

#     # Create a text input for the user to type their message
#     user_input = st.text_input("Ask about trains, schedules, or stations:", "")

#     if user_input:
#         # Get response from the chatbot
#         reply = respond_to_query(user_input)

#         # Display the chatbot's response
#         if isinstance(reply, pd.DataFrame):
#             st.write(reply)
#         else:
#             st.text_area("Chatbot Response:", str(reply), height=200)

# if __name__ == "__main__":
#     main()


import streamlit as st
import json
import pandas as pd

# Load datasets
with open('trains.json') as f:
    trains_data = json.load(f)['features']  # assuming 'features' contains train data

with open('schedules.json') as f:
    schedule_data = json.load(f)  # directly loading schedule data

with open('stations.json') as f:
    stations_data = json.load(f)['features']  # assuming 'features' contains station data

# Functions for train, schedule, and station information
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
        df = pd.DataFrame(schedule_list)
        return schedule_list
    return "No schedules found for this station."

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
        train_number = query.split()[-1]  # Assuming train number is the last word
        return get_train_info(train_number)
    elif "schedule" in query.lower():
        station_code = query.split()[-1]  # Assuming station code is the last word
        return get_schedule_info(station_code)
    elif "station" in query.lower():
        station_code = query.split()[-1]  # Assuming station code is the last word
        return get_station_info(station_code)
    else:
        return "Sorry, I don't understand the question."

# Streamlit Chatbot Interface
st.title("Train Assistant")

# Initialize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message["content"])

# Check if it's the first message to send the greeting and task list
if len(st.session_state.messages) == 0:
    greeting ='''Hello! I am here to assist you with the following tasks:\n
    - 🚆 Train Details: Get detailed information about trains.\n
    - 🕒 Train Schedules: Check schedules at a specific station.\n
    - 🗺️ Station Information: Get details about railway stations.'''
    
    # Display bot's initial greeting and task list
    with st.chat_message("assistant"):
        st.markdown(greeting)
    
    # Add the greeting to the session history
    st.session_state.messages.append({"role": "assistant", "content": greeting})

# Prompt for user input
prompt = st.chat_input("Ask about trains, schedules, or stations:")

if prompt:
    # Display user's input in chat history
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to the session history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get assistant's response
    response = respond_to_query(prompt)

    # Display assistant's response in chat history
    with st.chat_message("assistant"):
        st.markdown(response)

    # Add assistant's response to session history
    st.session_state.messages.append({"role": "assistant", "content": response})
