from typing import Dict

from pandas import DataFrame


# mapping of activity type to distance multiplier
ACTIVITY_MULTIPLIER_MAPPING = {
    'rowing': 2,
    'ride': 1,
    'run': 1.5,
    'hike': 1,
}


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
        df['type'] = df['type'].str.lower()
    else:
        drop_coloumns.append('type')

    df = df.drop(columns=drop_coloumns).groupby(groupby_columns).sum()
    return df


def add_converted_distance_column(df: DataFrame) -> DataFrame:
    def mapper(df_row):
        raw_distance = df_row.distance
        # df.name accesses the index here
        activity_type = df_row.name[2]
        try:
            return raw_distance * ACTIVITY_MULTIPLIER_MAPPING[activity_type]
        except KeyError:
            # TODO: should make this a log.
            print(f'Warning: New type not included in mapping: {activity_type}')
            return raw_distance
    df['converted_distance'] = df.apply(mapper, axis=1)
    return df
