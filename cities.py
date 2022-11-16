import math
from typing import Dict, List, Tuple
from math import *
import matplotlib.pyplot as plt
from decimal import Decimal


class City:
    # to represent a single city, this class would be created City object and
    # used by call methods
    def __init__(self, city_name, country, citizen, geography_latitude, geography_longitude):
        # to create city object by using basic properties
        if isinstance(city_name, str) != True or city_name == '':
            raise ValueError('The name of the city should be passed as strings and not be empty')
        if isinstance(country, str) != True or country == '':
            raise ValueError('The name of the country should be passed as strings and not be empty')
        if isinstance(citizen, int) != True or citizen < 0:
            raise ValueError('The number of the citizen should be integer')
        if isinstance(geography_latitude, float) < -90 or isinstance(geography_latitude, float) > 90:
            raise ValueError('The value of the longitude should be limited from the -90 to 90')
        if isinstance(geography_longitude, float) < -180 or isinstance(geography_longitude, float) > 180:
            raise ValueError('The value of the longitude should be limited from the -180 to 180')
        self.city_name = city_name
        self.country = country
        self.citizen = citizen
        self.geography_latitude = geography_latitude
        self.geography_longitude = geography_longitude
        # the constructor should check the valid type and value

    def distance_to(self, other: 'City') -> float:
        # to calculate the distance from one city to another
        R = 6371
        a = math.radians(self.geography_longitude)
        b = math.radians(self.geography_latitude)
        c = math.radians(other.geography_longitude)
        d = math.radians(other.geography_latitude)
        A = c - a
        B = d - b
        d = 2 * R * asin(
            sqrt(sin(B / 2) ** 2 + cos(b) * cos(d) * (sin(A / 2) ** 2)))
        if other is None:
            raise ValueError("The other city is none")

        return d

    def co2_to(self, other: 'City') -> float:
        # to calculate the emission with distance
        d = self.distance_to(other)
        if d <= 1000:
            co2 = 200 * d * self.citizen
        elif 1000 < d <= 8000:
            co2 = 250 * d * self.citizen
        else:
            co2 = 300 * d * self.citizen
        if other is None:
            raise ValueError("The other city is none")

        return co2


class CityCollection:
    # to collect together all the cities from the database
    # mainly interact through this class by using CSV file
    # it should take a list of City object as an argument
    # hold it as member variable(cities)
    # call method countries and total_attendees to access
    def __init__(self, cities: City):
        if isinstance(cities, list):
            self.cities = cities
        else:
            raise ValueError("The input of the cities is invalid")
        # print(cities)

    def countries(self) -> List[str]:
        countries = []
        for city in self.cities:
            if city.country not in countries:
                countries.append(city.country)
        if not isinstance(countries, List):
            raise ValueError("The countries is not List")

        return countries

    def total_attendees(self) -> int:
        attendees = 0
        for city in self.cities:
            attendees += city.citizen
        if not isinstance(attendees, int):
            raise ValueError("The value of attendees is not int")

        return attendees

    def total_distance_travel_to(self, city: City) -> float:
        total_distance = 0
        for city_arrival in self.cities:
            total_distance += city_arrival.distance_to(city)
        if not isinstance(total_distance, float):
            raise ValueError("The value of distance is not float")

        return total_distance

    def travel_by_country(self, city: City) -> Dict[str, float]:

        Dic_country = {}
        for country in self.countries():
            Dic_country[country] = 0

        for city_arrival in self.cities:
            Dic_country[city_arrival.country] += (
                    city_arrival.distance_to(city) * city_arrival.citizen)
        if not isinstance(Dic_country, Dict):
            raise ValueError("The dic_country is not Dict")
        return Dic_country

    def total_co2(self, city: City) -> float:
        # raise NotImplementedError
        total_co2 = 0
        for city_leave in self.cities:
            total_co2 += city_leave.co2_to(city)
        if not isinstance(total_co2, float):
            raise ValueError("The total_co2 is not float")
        return total_co2

    def co2_by_country(self, city: City) -> Dict[str, float]:
        # raise NotImplementedError
        Dic_country = {}
        for country in self.countries():
            Dic_country[country] = 0

        for city_arrival in self.cities:
            Dic_country[city_arrival.country] += (city_arrival.co2_to(city))
        if not isinstance(Dic_country, Dict):
            raise ValueError("The Dic_country is not dict")
        return Dic_country

    # def summary(self, city: City):
    #     print('Host city: {}')
    #     print('Total CO2: '')
    #     raise NotImplementedError

    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        # sort a list of city names and co2 emissions
        # raise NotImplementedError
        co2_emission_list = []
        for city_emission in self.cities:
            co2_emission_list.append((city_emission.city_name, self.total_co2(city_emission)))
        print(co2_emission_list)
        sorted_by_emissions = sorted(co2_emission_list, key=lambda x: x[1])

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
            weight = co2_list[i] / 1000
            co2_list_tones.append(weight)
        # describe the figure
        plt.figure(figsize=(15, 5), dpi=80)
        plt.xticks(range(len(country_list)), country_list, rotation=0, fontsize=12)
        plt.bar(range(len(country_list)), co2_list_tones, width=0.5, color="blue")
        plt.grid(alpha=0.6, color='black')
        plt.xlabel("")
        plt.ylabel("Total CO2 Emission /tone)")
        plt.title("Total co2 emissions from each country(TOP 10)")

        plt.savefig('{}.png'.format(city.city_name.replace(' ', '_')))

        plt.show()
