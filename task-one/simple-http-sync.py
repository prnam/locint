"""Sync calls using http package"""
import datetime
import json
import http.client
import time
import config

start_time = time.time()
dt_now = int(time.time())
dates = [
    dt_now,
    dt_now - config.DAY_IN_SECONDS,
    dt_now - (config.DAY_IN_SECONDS * 2),
]  # noqa
LAT = 15.0
LON = 75.0

conn = http.client.HTTPSConnection("api.openweathermap.org")
for date in dates:
    query = "?lat={0}&lon={1}&dt={2}&appid={3}".format(
        LAT, LON, date, config.API_KEY
    )  # noqa
    url = "{0}{1}{2}".format(config.URL, config.PATH, query)
    conn.request("POST",url)
    response = conn.getresponse()
    data = json.loads(response.read().decode())["hourly"][4]
    pressure = data["pressure"]
    HUMAN_TIME = str(datetime.datetime.utcfromtimestamp(data["dt"]))  # noqa
    print("{0} UTC | Pressure -> {1}".format(HUMAN_TIME, pressure))  # noqa
conn.close()
print("Took {0} seconds.".format((time.time() - start_time)))