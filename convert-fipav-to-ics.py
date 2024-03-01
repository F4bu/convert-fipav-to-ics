# Import necessary modules
import argparse
import pandas as pd
from ics import Calendar, Event
from datetime import datetime, timedelta
import pytz

# Define the timezone
timezone = 'Europe/Rome'

# Create an argument parser
parser = argparse.ArgumentParser()

# Add an argument for the file path
parser.add_argument('file_path', help='The path to the CSV file')

# Parse the arguments
args = parser.parse_args()

# Read the CSV file
# The file path is obtained from the command line arguments
df = pd.read_csv(args.file_path, sep=';')

# Create a new calendar
cal = Calendar()

# Iterate over the rows of the DataFrame
# Each row represents an event
for _, row in df.iterrows():
    # Create an event
    event = Event()

    # Set the event details
    # The details are obtained from the current row of the DataFrame
    event.name = f"{row['OSPITANTE']} vs {row['OSPITE']}"
    event.location = f"{row['CAMPO']}, {row['COMUNE']}, {row['VIA']}"

    # Combine date and time into a datetime object
    dt = datetime.strptime(f"{row['DATA']} {row['ORA']}", '%d/%m/%Y ="%H:%M"')

    # Localize the datetime object to the defined timezone
    dt = pytz.timezone(timezone).localize(dt)

    # Set the start and end times of the event
    event.begin = dt
    event.end = dt + timedelta(hours=2)

    # Add the event to the calendar
    cal.events.add(event)

# Get the iCalendar representation of the calendar
# The serialize method returns a string that represents the calendar in the iCalendar format
ics_str = cal.serialize()

# Write the iCalendar representation to an iCal file
# The file is named 'events.ics'
with open('events.ics', 'w') as f:
    f.write(ics_str)
