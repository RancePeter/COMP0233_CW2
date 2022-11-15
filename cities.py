import math
from typing import Dict, List, Tuple
from math import *
import matplotlib.pyplot as plt


class City:
    # to represent a single city, this class would be created City object and
    # used by call methods
    def __init__(self, city_name, country_name, citizen_number, geography_latitude, geography_longitude):
        # to create city object by using basic properties
        self.city_name = city_name
        self.country_name = country_name
        self.citizen_number = citizen_number
        self.geography_latitude = geography_latitude
        self.geography_longitude = geography_longitude
        # the constructor should check the valid type and value
        if isinstance(city_name, str) != True or city_name == '':
            raise ValueError('The name of the city should be passed as strings and not be empty')
        if isinstance(country_name, str) != True or country_name == '':
            raise ValueError('The name of the country should be passed as strings and not be empty')
        if isinstance(citizen_number, int) != True or citizen_number <= 0:
            raise ValueError('The number of the citizen should be integer')
        if isinstance(geography_latitude, float) < -90 or isinstance(geography_latitude, float) > 90:
            raise ValueError('The value of the longitude should be limited from the -90 to 90')
        if isinstance(geography_longitude, float) < -180 or isinstance(geography_longitude, float) > 180:
            raise ValueError('The value of the longitude should be limited from the -180 to 180')

    def distance_to(self, other: 'City') -> float:
        # to calculate the distance from one city to another
        R = 6371
        longitude_1 = math.radians(self.geography_longitude)
        latitude_1 = math.radians(self.geography_latitude)
        longitude_2 = math.radians(other.geography_longitude)
        latitude_2 = math.radians(other.geography_latitude)
        differ_longitude = longitude_2 - longitude_1
        differ_latitude = latitude_2 - latitude_1
        d = 2 * R * asin(
            sqrt(sin(differ_latitude / 2) ** 2 + cos(latitude_1) * cos(latitude_2) * (sin(differ_longitude / 2) ** 2)))
        return d
        raise NotImplementedError("Error: function not implemented!")

    def co2_to(self, other: 'City') -> float:
        # to calculate the emission with distance
        d_distance = self.distance_to(other)
        if d_distance <= 1000:
            co2 = 200 * d_distance * self.citizen_number
        if 1000 < d_distance <= 8000:
            co2 = 250 * d_distance * self.citizen_number
        if d_distance > 8000:
            co2 = 300 * d_distance * self.citizen_number
        return co2
        raise NotImplementedError("Error: function not implemented!")


class CityCollection:
    # to collect together all the cities from the database
    # mainly interact through this class by using CSV file
    # it should take a list of City object as an argument
    # hold it as member variable(cities)
    # call method countries and total_attendees to access
    def __init__(self, cities: City):
        self.cities = cities
        # print(cities)

    def countries(self) -> List[str]:
        countries = []
        for city in self.cities:
            if city.country_name not in countries:
                countries.append(city.country_name)
        return countries

    def total_attendees(self) -> int:
        attendees = 0
        for city in self.cities:
            attendees_num = attendees + city.citizen_number
            attendees = attendees_num
        return attendees_num

    def total_distance_travel_to(self, city: City) -> float:
        # raise NotImplementedError
        total_distance = 0
        for city_destination in self.cities:
            total_distance += city_destination.distance_to(city)

        return total_distance

    def travel_by_country(self, city: City) -> Dict[str, float]:
        # raise NotImplementedError
        Dict = {}
        for country in self.countries():
            Dict[country] = 0

        for city_destination in self.cities:
            Dict[city_destination.country_name] += (
                    city_destination.distance_to(city) * city_destination.citizen_number)

        return Dict

    def total_co2(self, city: City) -> float:
        # raise NotImplementedError
        total_co2 = 0
        for city_departure in self.cities:
            total_co2 += city_departure.co2_to(city)
        return total_co2

    def co2_by_country(self, city: City) -> Dict[str, float]:
        # raise NotImplementedError
        Dict = {}
        for country in self.countries():
            Dict[country] = 0

        for city_destination in self.cities:
            Dict[city_destination.country_name] += (city_destination.co2_to(city))

        return Dict

    def summary(self, city: City):
        # raise NotImplementedError
        total_attendees = 0
        for city_departure in self.cities:
            total_attendees += city_departure.citizen_number
        return print('Host city: ' + city.city_name + ' (' + city.country_name + ')',
                     '\nTotal CO2: ' + str(round(self.total_co2(city) / 1000, 0)) + ' tones',
                     '\nTotal attendees travelling to ' + city.city_name + ' from ' + str(len(self.cities)) +
                     ' different cities: ' + str(total_attendees))

    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        # sort a list of city names and co2 emissions
        # raise NotImplementedError
        co2_list = []
        for city_host in self.cities:
            co2_list.append((city_host.city_name, self.total_co2(city_host)))

        sorted_by_emissions = sorted(co2_list, key=lambda tup: tup[1])

        return sorted_by_emissions

    def plot_top_emitters(self, city: City, n: int, save: bool):
        # total co2 emission on y-axis, x-axis the country
        co2_list_country = self.co2_by_country(city)
        co2_list_country = dict(sorted(co2_list_country.items(), key=lambda x: x[1], reverse=True))

        country_list = []
        for i in range(0, n):
            country_list.append(list(co2_list_country.keys())[i])
        country_list.append('Left')

        co2_list = []
        co2_list_tones = []
        print(country_list)
        for i in range(0, n):
            co2_list.append(list(co2_list_country.values())[i])
        print(co2_list_country)
        co2_list_country_other = list(co2_list_country.values())[n:]
        co2_other = sum(co2_list_country_other)
        co2_list.append(co2_other)
        for i in range(0, len(co2_list)):
            a = co2_list[i] / 1000
            co2_list_tones.append(a)
        # describe the figure
        plt.figure(figsize=(15, 5), dpi=80)
        plt.xticks(range(len(country_list)), country_list, rotation=0, fontsize=12)
        plt.bar(range(len(country_list)), co2_list_tones, width=0.5, color="blue")
        plt.grid(alpha=0.6, color='black')
        plt.xlabel("")
        plt.ylabel("Total CO2 Emission /tone)")
        plt.title("Total co2 emissions from each country(TOP 10)")
        plt.savefig('city_name.png')
        plt.show()

