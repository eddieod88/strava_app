from pandas import DataFrame

from .config import EMAILS

# get list of email addresses

# get strava api key

# get key user and access the club and its data somehow?

# add up all of the data in the previous weeks (from data directory) + current week. -> if no data, get previous week and set
# When adding, also add a hash of the data. this way, we can compare quickly, if the previous week has already been stored.

# get list of members
#   for each member, get their stats and get their last weeks worht of runs, cycles etc. (maybe convert to a total here)


def convert_dataframe_to_csv(dataframe, location_path):
    # create a csv from dataframe and add to data directory chosen by location path
    pass


def hash_previous_weeks_data() -> []:
    # return a hash of each csv
    pass


def fetch_previous_weeks_data() -> DataFrame:
    pass


def aggregate_previous_weeks_data():
    # aggregate all the csvs into one be dataframe type thing.
    pass


def convert_strava_to_dataframe(strava_data):
    # convert the strava data to a dataframe so that it can be manipulated and stored to csvs easily
    pass

# run WEEKLY so that the 'recent data' is only one weeks worth..

previous_week = strava_get_previous_weeks_data()

if hash(previous_week) not in hash_previous_weeks_data():
    convert_dataframe_to_csv(convert_strava_to_dataframe(previous_week), './data/previous_weeks/')

current_week = strava_get_current_weeks_data()

aggregated_current_data = aggregate_previous_weeks_data() + convert_strava_to_dataframe(current_week)

print(aggregated_current_data)

convert_dataframe_to_csv(aggregated_current_data, './data/cumulative_totals/')
