from cities import City, CityCollection


def test_data_valid():
    beijing = City('Beijing', 'China', 950, 39.9, 116.4)
    shanghai = City('Shanghai', 'China', 96, 31.2, 121.5)
    nanjing = City('Nanjing', 'China', 232, 32.1, 118.8)
    wuhan = City('Wuhan', 'China', 81, 30.6, 114.3)
    london = City('London', 'United Kingdom', 117, 51.5, -0.1)
    list_of_cities = [beijing, shanghai, nanjing, wuhan, london]
    city_collection = CityCollection(list_of_cities)
    assert city_collection.cities == list_of_cities


def test_work_transportation():
    beijing = City('Beijing', 'China', 950, 39.9, 116.4)
    london = City('London', 'China', 117, 51.5, -0.1)
    aimd_distance = 8140.0
    aimd_co2 = 2319900000.0
    assert beijing.distance_to(london) == aimd_distance
    assert beijing.co2_to(london) == aimd_co2


def test_work_collection():
    beijing = City('Beijing', 'China', 950, 39.9, 116.4)
    shanghai = City('Shanghai', 'China', 96, 31.2, 121.5)
    nanjing = City('Nanjing', 'China', 232, 32.1, 118.8)
    wuhan = City('Wuhan', 'China', 81, 30.6, 114.3)
    london = City('London', 'United Kingdom', 117, 51.5, -0.1)
    list_of_cities = [beijing, shanghai, nanjing, wuhan, london]
    city_collection = CityCollection(list_of_cities)
    assert city_collection.countries() == ['China', 'United Kingdom']
    assert city_collection.total_attendees() == 1476
    aimd_total_distance = 11156
    assert city_collection.total_distance_travel_to(beijing) == aimd_total_distance
    aimd = {'United Kingdom': 952380.0, 'China': 395355.0}
    assert city_collection.travel_by_country(beijing) == aimd


# def test_work_host():

def test_work_sorted():
    beijing = City('Beijing', 'China', 950, 39.9, 116.4)
    shanghai = City('Shanghai', 'China', 96, 31.2, 121.5)
    nanjing = City('Nanjing', 'China', 232, 32.1, 118.8)
    wuhan = City('Wuhan', 'China', 81, 30.6, 114.3)
    london = City('London', 'United Kingdom', 117, 51.5, -0.1)
    list_of_cities = [beijing, shanghai, nanjing, wuhan, london]
    city_collection = CityCollection(list_of_cities)
    aimd = [('Beijing', 374182350.0), ('Nanjing', 497649300.0), ('Wuhan', 595635500.0), ('Shanghai', 601174100.0), ('London', 3425297400.0)]
    assert city_collection.sorted_by_emissions() == aimd


def main():
    # fixtures and test parametrisation
    test_data_valid()
    test_work_transportation()
    test_work_collection()
    # test_work_host()
    test_work_sorted()


if __name__ == '__main__':
    main()
