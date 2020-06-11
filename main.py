import requests
from requests import Session
from pprint import pprint

from pandas import DataFrame

from settings import STRAVA_BASE_URL, HEADERS


CLUB_ID = 65323

try:
    session = Session()
    session.headers = HEADERS

    club_activities_response = session.get(STRAVA_BASE_URL + f'club/f{CLUB_ID}')

    pprint(club_activities_response.content)
except requests.RequestException as e:
    raise requests.HTTPError(f'Exception when getting the club activity list: {e}')


def do_magic(strava_data) -> DataFrame:
    pass


lovely_table = do_magic(club_activities_response)
