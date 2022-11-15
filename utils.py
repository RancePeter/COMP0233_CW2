from cities import City, CityCollection
import csv
from pathlib import Path

file_path = Path("attendee_locations.csv")


def read_attendees_file(filepath: Path) -> CityCollection:
    # (csv) the argument of read_attendees_file  is Path object from module
    # file can be anywhere
    csv_data = csv.reader(open(filepath))
    headers = next(csv_data)  # read the first line
    list_of_cities = []
    list_of_distance = []
    list_of_city_collection = []
    for row in csv_data:
        city = City(row[3], row[1], int(row[0]), float(row[4]), float(row[5]))
        # city is cities.City object has properties in constructor
        list_of_cities.append(city)

    city_collection = CityCollection(list_of_cities)
    # print(list_of_cities)
    # print(city_collection.cities == list_of_cities)
    # print(city_collection.cities)
    return city_collection


def find_city(key):
    for i in range(0, len(city_collections.cities)):
        if city_collections.cities[i].city_name == str(key):
            return city_collections.cities[i]


city_collections = read_attendees_file(file_path)  # city_collections is list
print(city_collections.plot_top_emitters(find_city('Zurich'), 10, False))
# By default, n should be 10 and save should be False.
print(city_collections.sorted_by_emissions())
# print(city_collections.total_co2(find_city('Zurich')))