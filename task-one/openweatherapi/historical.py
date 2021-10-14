import httpx
import datetime

WARN = "Something went wrong!!!"
MESSAGE = "Message received:"
URL = "https://api.openweathermap.org"
PATH = "/data/2.5/onecall/timemachine"


async def get_data(lat: str, lon: str, dates: list):
    try:
        print("----- OUTPUT -----")
        import config
        async with httpx.AsyncClient() as client:
            for dt in dates:
                query = "?lat={0}&lon={1}&dt={2}&appid={3}".format(lat, lon, dt, config.api_key) # noqa
                response = await client.request("POST", "{0}{1}{2}".format(URL, PATH, query))  # noqa
                status = response.status_code
                if(status == 200):
                    data = response.json()['hourly'][4]
                    pressure = data['pressure']
                    human_time = str(datetime.datetime.utcfromtimestamp(data['dt'])) # noqa
                    print("{0} UTC | Pressure -> {1}".format(human_time, pressure)) # noqa
                else:
                    data = response.json()
                    print("{0}\nMore Info:-".format(WARN))
                    print(" Status Code: {0}".format(data['cod']))
                    print(" {0} {1}".format(MESSAGE, data['message']))
                    exit(1)
    except Exception as ex:
        print("{0} {1} {2}".format(WARN, MESSAGE, ex))
