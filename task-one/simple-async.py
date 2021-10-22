""" Async calls using httpx package"""
import asyncio
import time
import datetime
import httpx
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


async def main():
    """Main function of async / await demo"""
    async with httpx.AsyncClient() as client:
        for date in dates:
            query = "?lat={0}&lon={1}&dt={2}&appid={3}".format(
                LAT, LON, date, config.API_KEY
            )  # noqa
            url = "{0}{1}{2}".format(config.URL, config.PATH, query)
            response = await client.post(url)

            data = response.json()["hourly"][4]
            pressure = data["pressure"]
            human_time = str(datetime.datetime.utcfromtimestamp(data["dt"]))
            print("{0} UTC | Pressure -> {1}".format(human_time, pressure))


asyncio.run(main())
print("Took {0} seconds".format((time.time() - start_time)))
