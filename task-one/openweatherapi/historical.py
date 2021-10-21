"""Everything related to Historical OpenWeatherAPI"""
import asyncio
import datetime
import httpx
import config


async def make_call(client, url):
    """Makes async calls to url or set of urls and returns the data"""
    response = await client.post(url)  # noqa
    return response


async def get_three_days_data(lat: str, lon: str, dates: list):
    """Gets 3 days historical weather data from OpenWeather API"""
    try:
        print("Output:")
        tasks = []
        async with httpx.AsyncClient(http2=True) as client:
            for date in dates:
                query = "?lat={0}&lon={1}&dt={2}&appid={3}".format(lat, lon, date, config.API_KEY)  # noqa
                url = "{0}{1}{2}".format(config.URL, config.PATH, query)
                tasks.append(asyncio.ensure_future(make_call(client, url)))

            responses = await asyncio.gather(*tasks)

            for response in responses:
                status = response.status_code
                if status == 200:
                    data = response.json()["hourly"][4]
                    pressure = data["pressure"]
                    human_time = str(datetime.datetime.utcfromtimestamp(data["dt"]))  # noqa
                    print("{0} UTC | Pressure -> {1}".format(human_time, pressure))  # noqa
                else:
                    data = response.json()
                    print("{0}\nMore Info:-".format(config.WARN))
                    print(" Status Code: {0}".format(data["cod"]))
                    print(" {0} {1}".format(config.MESSAGE, data["message"]))
                    exit(1)

    except Exception as ex:
        print("{0} {1} {2}".format(config.WARN, config.MESSAGE, ex))
