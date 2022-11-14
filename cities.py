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
        raise NotImplementedError

    def co2_to(self, other: 'City') -> float:
        raise NotImplementedError

class CityCollection:
    ...

    def countries(self) -> List[str]:
        raise NotImplementedError

    def total_attendees(self) -> int:
        raise NotImplementedError

    def total_distance_travel_to(self, city: City) -> float:
        raise NotImplementedError

    def travel_by_country(self, city: City) -> Dict[str, float]:
        raise NotImplementedError

    def total_co2(self, city: City) -> float:
        raise NotImplementedError

    def co2_by_country(self, city: City) -> Dict[str, float]:
        raise NotImplementedError

    def summary(self, city: City):
        raise NotImplementedError

    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        raise NotImplementedError

    def plot_top_emitters(self, city: City, n: int, save: bool):
        raise NotImplementedError

