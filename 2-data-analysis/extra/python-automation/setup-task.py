# sudo apt-get install software-properties-common
# sudo apt-get install python3 python3-pip
# sudo pip3 install --upgrade pandas
# mkdir py-automater
# sudo apt-get install sqlite3
# sudo apt-get install postfix
# cat /var/mail/gustavo_martin

import requests
import pandas as pd
import uuid

# SQLITE3 to manage a very simple database
# https://www.sqlite.org/
import sqlite3

api_key = "f275aa333c628e5a702c7d4f1fce6cdb"
coords_dict = {}
cities_dict = {
    0: ["Mieres", "ES"],
    1: ["Sevilla", "ES"],
    2: ["Zarautz", "ES"],
    3: ["Barcelona", "ES"],
    4: ["Madrid", "ES"]
}

# Create if not exists
# or connect to the SQLITE3 database
conn = sqlite3.connect('db.sqlite3')

# Generate a cursor to access to the database
c = conn.cursor()

create_cities_query = """
    CREATE TABLE IF NOT EXISTS city (
        [uuid] TEXT PRIMARY KEY, 
        [name] TEXT,
        [country] TEXT,
        [lon] TEXT, 
        [lat] TEXT        
    );
"""

create_measures_query = """
    CREATE TABLE IF NOT EXISTS measure (
        [uuid] TEXT PRIMARY KEY, 
        [timestamp] TEXT,
        [city_uuid] TEXT,
        [humi] INTEGER,
        [temp] REAL,
        [pressure] INTEGER,
        [wind] REAL,
        FOREIGN KEY(city_uuid) REFERENCES city(uuid)
    );
"""

c.execute(create_cities_query)
c.execute(create_measures_query)
                     
conn.commit()

for k, v in cities_dict.items():
    URL = "https://api.openweathermap.org/data/2.5/weather?q={0},{1}&appid={2}" \
        .format(v[0], v[1], api_key)
    response = requests.get(url = URL)
    data = response.json()
    coords_dict[k] = [
        data["coord"]["lon"], 
        data["coord"]["lat"]]

for city, coord in zip(cities_dict.items(), coords_dict.items()):

    _uuid = str(uuid.uuid4())
    name = city[1][0]
    country = city[1][1]
    lon = coord[1][0]
    lat = coord[1][1]

    #print(_uuid, name, country, lon, lat)

    insert_into_city = """
        INSERT INTO city 
            (uuid, name, country, lon, lat)
            VALUES ('{0}', '{1}', '{2}', {3}, {4});
        """.format(_uuid, name, country, lon, lat)

    c.execute(insert_into_city)
    conn.commit()  