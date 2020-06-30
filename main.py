import requests
from requests import Session
from pprint import pprint

from app.utils import add_converted_distance_column, convert_strava_response_to_dataframe
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
            raw_distance_table = convert_strava_response_to_dataframe(club_activities_response, groupby_activity_type=True)
            conversions_included_table = add_converted_distance_column(raw_distance_table)
            final_table = conversions_included_table.groupby(['first_name', 'last_name']).sum()
            with open('data/cumulative_totals/test.csv', 'w') as csv_file:
                final_table.to_csv(csv_file)
        else:
            print(club_activities_response.status_code)
            pprint(club_activities_response.content)
