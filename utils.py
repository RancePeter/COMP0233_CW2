from cities import City, CityCollection
import csv
from pathlib import Path
file_path = Path("attendee_location.csv")

def read_attendees_file(filepath: Path) -> CityCollection:
    csv_data = csv.reader(open(filepath))
    headers = next(csv_data)  #to read the first row
    
