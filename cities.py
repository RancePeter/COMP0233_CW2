from typing import Dict, List, Tuple
from math import *
import matloplib.pyplot as plt

class City:
    
    def __inin__(self, Country, City1, Citizen, Longitude, Latitude):
        self.Country = Country
        self.City1 = City1
        self.Citizen = Citizen
        self.Longitude = Longitude
        self.Latitude = Latitude
        if Country == '' or type(Country) != type('str'):
            raise ValueError('The name of the Country should be not empty and String')
        if City1 == '' or type(City1) != type('str'):
            raise ValueError('The name of the should be not empty and String')
        if Citizen <= 0 or type(Citizen) != int:
            raise ValueError('The number of the citizen should be integer')
        if float(Longitude) < -180 or float(Longitude) > 180:
            raise ValueError('The longitude should be restricted to the -180 to 180')
        if float(Latitude) < -90 or float(Latitude) > 90:
            raise ValueError('The latitude should be restricted to the -90 to 90')

    def distance_to(self, other: 'City') -> float:
        R = 6371
        Longitude_1 = self.Longitude
        Latitude_1 = self.Latitude
        Longitude_2 = other.Longitude
        Latitude_2 = other.Latitude
        differ_lon = abs(Longitude_2 - Longitude_1)
        differ_lat = abs(Latitude_2 - Latitude_1)
        d = 2 * R * asin(sqrt(sin(differ_lat / 2) ** 2 + cos(Latitude_1) * cos(Latitude_2) * (sin(differ_lon / 2) ** 2)))
        return d

    def co2_to(self, other: 'City') -> float:
        distance = self.distance_to(other)
        if distance <= 1000:
            co2 = 200 * distance * self.Citizen
        if 1000 < distance <= 8000:
            co2 = 250 * distance * self.Citizen
        if distance > 8000:
            co2 = 300 * distance * self.Citizen
        return co2

class CityCollection:
    
    def __int__(self, Cities: City):
        self.Cities = Cities

    def countries(self) -> List[str]:
        countries = []
        for city in self.Cities:
            if city.Country not in countries:
                countries.append(city.Country)
        return countries

    def total_attendees(self) -> int:
        attendees = 0
        for city in self.Cities:
            total_attendees = attendees + city.Citizen
        return total_attendees


    def total_distance_travel_to(self, city: City) -> float:
        total_distance = 0
        for city_destination in self.Cities:
            total_distance += city_destination.distance_to(city)
        return total_distance

    def travel_by_country(self, city: City) -> Dict[str, float]:
        Dict = {}
        for country in self.countries():
            Dict[country] = 0

        for city_travel in self.Cities:
            Dict[city_travel.Country] += (city_travel.distance_to(city) * city_destination.Citizen)
        return Dict

    def total_co2(self, city: City) -> float:
        total_co2 = 0
        for city_dep in self.Cities:
            total_co2 += city_dep.co2_to(city) * city_dep.Citizen
        return total_co2

    def co2_by_country(self, city: City) -> Dict[str, float]:
        Dict = {}
        for country in self.countries():
            Dict[country] = 0

        for city_destination in self.Cities:
            Dict[city_destination.Country] += (city_destination.co2_to(city) * city_destination.Citizen)

        return Dict

    def summary(self, city: City):
        total_attendees = 0
        for city_dep in self.cities:
            total_attendees += city_dep.Citizen
        return print('Host city: ' + city.City1 + ' (' + city.Country+ ')',
                     '\nTotal CO2: ' + str(round(self.total_co2(city) / 1000, 0)) + ' tones',
                     '\nTotal attendees travelling to ' + city.City1 + ' from ' + str(len(self.cities) - 1) +
                     ' different cities: ' + str(total_attendees - city.Citizen))




    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        emissions_list = []
        for city_host in self.cities:
            emissions_list.append((city_host.City1, self.total_co2(city_host)))

        sorted_by_emissions = sorted(emissions_list, key=lambda tup: tup[1])
        return sorted_by_emissions

    def plot_top_emitters(self, city: City, n: int, save: bool):
        emissions_country_list = self.co2_by_country(city)
        emissions_country_list = dict(sorted(emissions_country_list.items(), key=lambda x: x[1], reverse=True))
        # emissions_country_list = list(emissions_country_list.keys())
        country_list = []
        for i in range(0, n):
            country_list.append(list(emissions_country_list.keys())[i])
        country_list.append('Other')
        emissions_list = []
        emissions_list_tones = []
        for i in range(0, n):
            emissions_list.append(list(emissions_country_list.values())[i])
        print(emissions_country_list)
        emissions_country_list_other = list(emissions_country_list.values())[n:]
        emissions_other = sum(emissions_country_list_other)
        emissions_list.append(emissions_other)
        for i in range(0, len(emissions_list)):
            a = emissions_list[i] / 1000
            emissions_list_tones.append(a)
        plt.figure(figsize=(10, 7), dpi=80)
        plt.bar(range(len(country_list)), emissions_list_tones, width=0.3)
        plt.xticks(range(len(country_list)), country_list, rotation=40)

        plt.grid(alpha=0.4, color='pink')
        plt.ylabel("Total emissions (tones CO2)")
        plt.xlabel("")
        plt.title("Total emissions from each country")
        plt.show()

