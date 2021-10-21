"""Solution to Task 1"""
import asyncio
import time
from openweatherapi import historical
import config

start_time = time.time()


def main():
    """Takes geo inputs to get 3 days historical weather data"""
    try:
        print("Input:")
        lat = float(input("Enter Latitude value [-90 to 90]: "))
        lon = float(input("Enter Longitude value [-180 to 180]: "))
        if (-90.0 <= lat <= 90.0) and (-180.0 <= lon <= 180.0):  # noqa
            dt_now = int(time.time())
            key = input("I have configured my key in config.py [press any key to continue OR type 'exit' to quit]: ")  # noqa
            if key != "exit":
                dates = [
                    dt_now,
                    dt_now - config.DAY_IN_SECONDS,
                    dt_now - (config.DAY_IN_SECONDS * 2),
                ]  # noqa
                function_start_time = time.time()
                asyncio.run(
                    historical.get_three_days_data(str(lat), str(lon), dates)
                )  # noqa
                print("Function execution time is {0} seconds".format((time.time() - function_start_time))) # noqa
        else:
            print("\nWrong latitude and longitude range")

        print("Total execution (including input wait) time  {0} seconds.".format((time.time() - start_time))) # noqa
    except Exception as ex:
        print("{0} {1} {2}".format(config.WARN, config.MESSAGE, ex))


if __name__ == "__main__":
    main()
