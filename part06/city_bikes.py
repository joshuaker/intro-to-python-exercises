# tee ratkaisu tänne
# Write your solution here
#Longitude;Latitude;FID;name;total_slot;operative;id

def get_station_data(filename: str):
    stations = {}
    with open(filename) as new_file:
        for line in new_file:
            bike_data = line.split(';')
            if bike_data[0] == 'Longitude': #skip header
                continue
            stations[bike_data[3]] = (float(bike_data[0]),float(bike_data[1]))
    return stations

import math

def distance(
        stations: dict,
        station1: str,
        station2: str
        ):
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

# get distance of every station from every other station
# sort

def greatest_distance(stations:dict):
    greatest_distance = 0
    station_names_and_distance = ('',0)
    #get list of names of stations

    station_names = []

    for key, value in stations.items():
        station_names.append(key)
    
    for _ in station_names:
        for i in range(len(station_names)):
            km = distance(stations, _, station_names[i])
            if km >= greatest_distance:
                greatest_distance = km
                station_names_and_distance = _ , station_names[i], km
    return station_names_and_distance
