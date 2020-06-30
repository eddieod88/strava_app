from typing import Dict

from pandas import DataFrame


# mapping of activity type to distance multiplier
ACTIVITY_MULTIPLIER_MAPPING = {
    'rowing': 2,
    'ride': 1,
    'run': 1.5,
    'hike': 1,
}


def convert_strava_response_to_dataframe(strava_data: [Dict]) -> DataFrame:
    """
    Fill out this method
    """
    df = DataFrame(strava_data)
    #
    #
    #
    return df
