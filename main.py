import requests
from requests import Session
from pprint import pprint

from app.utils import convert_strava_response_to_dataframe
from settings import STRAVA_BASE_URL, HEADERS


CLUB_ID = 65323
PAGE = 1
PER_PAGE = 30


if __name__ == '__main__':
    try:
        session = Session()
        session.headers = HEADERS
        payload = {'page': PAGE, 'perPage': PER_PAGE}
        club_activities_response = session.get(STRAVA_BASE_URL + f'clubs/{CLUB_ID}/activities', params=payload)
    except requests.RequestException as e:
        raise requests.HTTPError(f'Exception when getting the club activity list: {e}')
    else:
        if club_activities_response == 200:
            lovely_table = convert_strava_response_to_dataframe(club_activities_response)
        else:
            print(club_activities_response.status_code)
            pprint(club_activities_response.content)
