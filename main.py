import requests
from requests import Session
from pprint import pprint

from app.utils import convert_strava_response_to_dataframe
from settings import STRAVA_BASE_URL, HEADERS


CLUB_ID = 65323
PAGE = 1
PER_PAGE = 30

try:
    session = Session()
    session.headers = HEADERS

    club_activities_response = session.get(STRAVA_BASE_URL + f'clubs/{CLUB_ID}/activities', page=PAGE, perPage=PER_PAGE)

    pprint(club_activities_response.content)
except requests.RequestException as e:
    raise requests.HTTPError(f'Exception when getting the club activity list: {e}')


lovely_table = convert_strava_response_to_dataframe(club_activities_response)
