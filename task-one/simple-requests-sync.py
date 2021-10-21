import datetime
import requests
import time

from requests.api import request
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

for date in dates:
    query = "?lat={0}&lon={1}&dt={2}&appid={3}".format(
        LAT, LON, date, config.API_KEY
    )  # noqa
    url = "{0}{1}{2}".format(config.URL, config.PATH, query)
    response = requests.request("POST", url)
    data = response.json()["hourly"][4]
    pressure = data["pressure"]
    HUMAN_TIME = str(datetime.datetime.utcfromtimestamp(data["dt"]))  # noqa
    print("{0} UTC | Pressure -> {1}".format(HUMAN_TIME, pressure))  # noqa

response.close()
print("Took {0} seconds.".format((time.time() - start_time)))