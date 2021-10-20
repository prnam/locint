import asyncio
import time

start_time = time.time()


def main():
    """ Takes geo inputs to get 3 days historical weather data """
    try:
        from openweatherapi import historical
        import config
        print("----- INPUT -----")
        lat = float(input("Enter Latitude value [-90 to 90]: "))
        lon = float(input("Enter Longitude value [-180 to 180]: "))
        if ((lat >= -90.0) and (lat <= 90.0)) and ((lon >= -180.0) and (lon <= 180.0)):  # noqa
            dt_now = int(time.time())
            key = input("I have configured my key in config file [press any key to continue OR type 'exit' to quit]: ")  # noqa
            if key != "exit":
                dates = [dt_now, dt_now - config.DAY_IN_SECONDS, dt_now - (config.DAY_IN_SECONDS * 2)]  # noqa
                function_start_time = time.time()
                asyncio.run(historical.get_three_days_data(
                    str(lat), str(lon), dates))
                print("\nFunction execution time is %s seconds." %
                      (time.time() - function_start_time))
        else:
            print("\nWrong latitude and longitude range")

        print("Total execution (including input wait) time is %s seconds." %
              (time.time() - start_time))
    except Exception as ex:
        print("{0} {1} {2}".format(config.WARN, config.MESSAGE, ex))


if __name__ == "__main__":
    main()
