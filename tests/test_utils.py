import pytest
from json import JSONDecoder

from app.utils import add_converted_distance_column, convert_strava_response_to_dataframe


class TestUtils:
    @pytest.fixture
    def decoded_sample_response(self):
        sample_response = '[{\
            "resource_state": 2,\
            "athlete": {\
                "resource_state": 2,\
                "firstname": "Henny",\
                "lastname": "O."\
            },\
            "name": "World Championship",\
            "distance": 2641.7,\
            "moving_time": 577,\
            "elapsed_time": 635,\
            "total_elevation_gain": 8.8,\
            "type": "Ride",\
            "workout_type": null\
        }, {\
            "resource_state": 2,\
            "athlete": {\
                "resource_state": 2,\
                "firstname": "Henny",\
                "lastname": "O."\
            },\
            "name": "World Championship",\
            "distance": 34.7,\
            "moving_time": 33323,\
            "elapsed_time": 6335,\
            "total_elevation_gain": 83.8,\
            "type": "Run",\
            "workout_type": null\
        }, {\
            "resource_state": 2,\
            "athlete": {\
                "resource_state": 2,\
                "firstname": "Eddie",\
                "lastname": "O."\
            },\
            "name": "World Championship",\
            "distance": 2445.7,\
            "moving_time": 23,\
            "elapsed_time": 1,\
            "total_elevation_gain": 9.8,\
            "type": "Run",\
            "workout_type": null\
        }]'
        decoded_json = JSONDecoder().decode(sample_response)
        multiple_activities = []
        for _ in range(10):
            multiple_activities.extend(decoded_json)
        return multiple_activities

    def test_convert_strava_response_to_dataframe(self, decoded_sample_response):
        df = convert_strava_response_to_dataframe(decoded_sample_response, groupby_activity_type=True)

    def test_add_converted_distance_column(self, decoded_sample_response):
        cleaned_df = convert_strava_response_to_dataframe(decoded_sample_response, groupby_activity_type=True)
        converted_distances_df = add_converted_distance_column(cleaned_df)
