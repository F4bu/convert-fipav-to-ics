# FIPAV CSV to iCalendar Converter

This Python script converts a CSV file of events into an iCalendar (.ics) file. The CSV file can be exported from the FIPAV site: https://www.sol.milano.federvolley.it/sol/webRisultati/Calendari.aspx

## Requirements

- Python 3.6 or higher
- pandas
- ics
- pytz

You can install the required Python packages using pip:

```bash
pip install pandas ics pytz
```

## Usage

```bash
python generate_ical_from_fipav_csv.py <path_to_csv_file>
```

Replace `<path_to_csv_file>` with the path to your CSV file.

## CSV File Format

The CSV file generated from FIPAV is semicolon-separated (;) and contain among others the following columns:

- OSPITANTE: The home team
- OSPITE: The visiting team
- CAMPO: The location of the event
- COMUNE: The city where the event is taking place
- VIA: The street where the event is taking place
- DATA: The date of the event, in the format dd/mm/yyyy
- ORA: The time of the event, in the format "HH:MM"

## Output

The script will create an iCalendar file named 'events.ics'. Each event in the CSV file will be converted into an iCalendar event and added to the 'events.ics' file. The events are set to last 2 hours by default.

## Timezone

The script uses the 'Europe/Rome' timezone by default. You can change this by modifying the 'timezone' variable in the script.
