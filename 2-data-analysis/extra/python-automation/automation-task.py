import requests
import pandas as pd
import uuid

# SQLITE3 to manage a very simple database
# https://www.sqlite.org/
import sqlite3

api_key = "f275aa333c628e5a702c7d4f1fce6cdb"
measures_dict = {}

# Create if not exists
# or connect to the SQLITE3 database
conn = sqlite3.connect('db.sqlite3')

# Generate a cursor to access to the database
c = conn.cursor()

select_all_cities = """
    SELECT
        uuid,
        name,
        country,
        lon, 
        lat
    FROM city;
"""

c.execute(select_all_cities)
all_cities = c.fetchall()

for city in all_cities:

    _uuid = str(uuid.uuid4())
    city_uuid = city[0]
    lat = city[3]
    lon = city[4]
    URL = "https://api.openweathermap.org/data/2.5/weather?lat={1}&lon={0}&appid={2}&units=metric" \
        .format(lat, lon, api_key)
    response = requests.get(url = URL)
    data = response.json() 
    humi = data["main"]["humidity"]
    temp = data["main"]["temp"]
    pressure = data["main"]["pressure"]
    wind = data["wind"]["speed"]
    timestamp = data["dt"]

    #print(_uuid, timestamp, city_uuid, humi, temp, pressure, wind)

    insert_into_measure = """
        INSERT INTO measure 
            (uuid, timestamp, city_uuid, humi, temp, pressure, wind)
            VALUES ('{0}', '{1}', '{2}', {3}, {4}, {5}, {6});
        """.format(_uuid, timestamp, city_uuid, humi, temp, pressure, wind) 

    c.execute(insert_into_measure)
    conn.commit()  