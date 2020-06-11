import os

from dotenv import load_dotenv


load_dotenv()

STRAVA_ACCESS_TOKEN = os.getenv('STRAVA_ACCESS_TOKEN')

HEADERS = {'Authorization': f'Bearer {STRAVA_ACCESS_TOKEN}'}
STRAVA_BASE_URL = 'https://www.strava.com/api/v3/'
