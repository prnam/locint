# task-one

## You need

- Python v3.9 or above
- VS Code or any IDE of your comfort

## Things to do before running the script

### How to install dependencies?

- Once you clone the repo, Go to terminal / CMD and open the directory where the repo exists
- Navigate to `task-one` folder and run `pip3 install -r requirements.txt`
- Verify that it is installed by checking output of `pip list` or `pip3 list` command

### How to check if PEP8 compliant or not?

- Run `flake8 .` inside `task-one` folder

### How to configure my API Key of OpenWeather API?
- Go to `task-one` folder and open `config.py` file, insert key with variable name `api_key` and save the file

## Things you need to know before running the script
-  Since scope mentioned in question
    - is just to get 4AM UTC, the program is hard coded to check only for the 4AM UTC
    - is just to get past 3 days, the program is hard coded to check only for 3 days
    - test cases are not part of the question, hence it is not included in this submission
    - Any others cases are ignored as scope creep/out-of-scope pertainig to this excerise as per email clarificaiton
- You are expected to read the message in the prompt in the screen, w.r.t values and API key. Failing to do so may require you to re do the whole thing and you may waste your precious time too
- Pressure stands for atmospheric pressure

## Folder Structure

- task-one.py - main file that you need run using the command `python3 task-one.py`
- config.py - file that consists or one must store configuration vairables such as api_key or secrets
- requirements.txt - file consists list of dependencies for this program to run smoothly
- openweatherapi/ - folder that consists of modules, programs for historical, predict APIs of OpenWeather API
    - historical.py - as name suggests this file consists everything about historical api endpoint
    > Note: For now we have only getting past 3 days data, however more improvement can be done by adding other methods in future easily than having in one file.

## Logic

> Note: Assuming user is successful in installing, configuring and running program as above mentioned

- User enters correct Latitude and Longitude
- Program verifies and proceeds further by calling get_data from openweatherapi's historical module with necessary inputs such as lat, lon, dates ( past 3 days). If verifyication is failed then user is gets hint of wrong geo info and gracefully exits.
- get_data method process this information asynchronously and returns pressure and datetime info, if each endpoint return status is 200. If not helpful hint will provided to user. Uses make_call to perform async call to url or urls.
- get_data could have been in same file, however it was kep seperate for ease of adding new methods and call easily and share library / module if when required.
- Whole program is wrapped with try-catch to gracefully catch the edge cases.

## Run

- Go to task-one folder, open CMD and now execute command `python3 task-one.py`
- Enter Latitude and Longitude value of your choice with correct range i.e latitude is between -90 to 90 and longitude is -180 to 180
- Prompt will ask you to confirm that you pasted your API key in config.py file. If you have done it press any key to continue. If you did not the please type `exit`, configure and rerun the script.
- If there is no network blip or any issue with API service, you will get past 3 days tmospheric pressure at 4AM UTC. If there is issue then you will get error message that is friendly enough to understand what went wrong.
- You will also get time it took for funtion call execution and total execution (which includes input wait time). You can use other mechanism too.

