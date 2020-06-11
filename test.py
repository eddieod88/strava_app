import requests
from requests import Session
from requests.adapters import HTTPAdapter
from pprint import pprint

from config import *

# create an instance of the API class

athlete_id = 5336175  # Long | The identifier of the athlete. Must match the authenticated athlete.

try:
    # Get Athlete Stats
    session = Session()
    session.headers = {'Authorization': f'Bearer {STRAVA_API_KEY}'}
    # adapter = HTTPAdapter()
    response = session.get(BASE_URL + f'athlete')
    print(response)
    pprint(response.content)
except requests.RequestException as e:
    print("Exception when calling getStats: %s\n" % e)
