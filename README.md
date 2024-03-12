# get-fipav-ics

This script retrieves data from the FIPAV website and converts it into an iCalendar file (.ics). The script takes command line arguments for the season, series, phase, group, and team. It then sends a GET request to the FIPAV website to retrieve the data. The data is in CSV format and is parsed using the pandas library. Each row of the CSV represents an event, which is then converted into an iCalendar event. The iCalendar events are added to a calendar and serialized into an iCalendar file. The resulting iCalendar file is written to stdout.

## Requirements

- Python 3
- pandas
- pytz
- ics
- requests

## Usage

```bash
python3 get-fipav-ics.py <stagione> <serie> <fase> <girone> <squadra>
```

Replace `<stagione>`, `<serie>`, `<fase>`, `<girone>`, and `<squadra>` with your desired values.

## Arguments

- `stagione`: The season for which you want to retrieve data.
- `serie`: The series for which you want to retrieve data.
- `fase`: The phase for which you want to retrieve data.
- `girone`: The group for which you want to retrieve data.
- `squadra`: The team for which you want to retrieve data.

## Output

The script writes the resulting iCalendar file to stdout. You can redirect this to a file if you wish:

```bash
python3 get-fipav-ics.py <stagione> <serie> <fase> <girone> <squadra> > output.ics
```

This README provides a brief description of the script, lists the requirements, explains how to use the script, describes the command line arguments, and explains the output.