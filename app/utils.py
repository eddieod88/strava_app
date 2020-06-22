from typing import Dict

from pandas import DataFrame


def convert_strava_response_to_dataframe(strava_data: [Dict], groupby_activity_type=False) -> DataFrame:
    df = DataFrame(strava_data)

    first_names = [a.get('firstname') for a in df.athlete]
    last_names = [a.get('lastname') for a in df.athlete]
    df.insert(1, 'first_name', first_names)
    df.insert(2, 'last_name', last_names)

    drop_coloumns = ['athlete', 'resource_state', 'name', 'workout_type']
    groupby_columns = ['first_name', 'last_name']
    if groupby_activity_type:
        groupby_columns.append('type')
    else:
        drop_coloumns.append('type')

    df = df.drop(columns=drop_coloumns).groupby(groupby_columns).sum()
    return df
