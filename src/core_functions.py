from enum import Enum
import pickle
import pandas as pd

class APIClass(Enum):

    AIRBNB = 'airbnb'
    TEST = 'test'

API_REQUESTS = {
                APIClass.AIRBNB.value: 
                    {
                        'requests_count': 0,
                        'requests_limit': 100,
                        'requests': []
                    }
                }

def api_key():
    """Get the api key from the api.key file"""

    with open('./api.key', 'r') as file:
        return file.read()


def set_api_requests(api: APIClass, number_of_requests: int):
    """Set the number of api requests for each api"""

    file = './.api_requests.csv'
    df = pd.DataFrame({'api': [api.value], 'requests_count': [number_of_requests]})
    
    existing_data = pd.read_csv(file)
    merged_data = pd.concat([df, existing_data], ignore_index=True)
    merged_data.drop_duplicates(subset=['api'], inplace=True)
    merged_data.to_csv(file, index=False)


def clear_api_requests(api: APIClass):
    """Clear the number of api requests for each api"""

    set_api_requests(api, 0)


def add_api_requests(api: APIClass, number_of_requests: int):
    """Add the number of api requests for each api"""

    file = './.api_requests.csv'
    df = pd.read_csv(file)

    if api.value in df['api'].values:
        current_value = df.loc[df['api'] == api.value, 'requests_count']
        current_value += number_of_requests
        if current_value.values[0]  < 0:
            current_value = 0
        df.loc[df['api'] == api.value, 'requests_count'] = current_value
    else:
        new_row = pd.DataFrame({'api': [api.value], 'requests_count': [number_of_requests]})
        df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv(file, index=False)


def inc_api_requests(api: APIClass):
    """Increment the number of api requests for each api"""

    add_api_requests(api, 1)


def dec_api_requests(api: APIClass):
    """Decrement the number of api requests for each api"""

    add_api_requests(api, -1)


def get_api_requests_count(api: APIClass) -> int:
    """Get the number of api requests for each api"""

    file = './.api_requests.csv'
    df = pd.read_csv(file)
    print(df)
    return df[df['api'] == api.value]['requests_count'].values[0]


def load_full_api_requests():
    """Load the api_reqeusts file and store it in a dictionary"""

api_key()