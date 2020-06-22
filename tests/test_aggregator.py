import pytest
from json import JSONDecoder

from app.utils import convert_strava_response_to_dataframe


class TestAggregator:
    @pytest.fixture
    def sample_response(self):
        return '[{\
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

    def test_conversion_util(self, sample_response):
        decoded_json = JSONDecoder().decode(sample_response)
        multiple_activities = []
        for _ in range(10):
            multiple_activities.extend(decoded_json)

        df = convert_strava_response_to_dataframe(multiple_activities, groupby_activity_type=True)
