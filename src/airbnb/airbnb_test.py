import pandas as pd
import requests
import json

from apartment import AirBnbApartment 
from core_functions import api_key


AIRBNB_HOST = 'airbnb13.p.rapidapi.com '
AIRBNB_HEADER = { 
    "X-RapidAPI-Key": api_key(),
    "X-RapidAPI-Host": AIRBNB_HOST
}

AIRBNB_URL = 'https://airbnb13.p.rapidapi.com'

querystring = {"location": "Dossenheim",
               "checkin":"2023-07-01",
               "checkout":"2023-07-08",
               "adults":"1",
               "children":"0",
               "infants":"0",
               "pets":"0",
               "page":"1",
               "currency":"EUR"}

def search_by_location_request():
    return requests.get(url=AIRBNB_URL + '/search-location', headers=AIRBNB_HEADER, params=querystring)

def save_response_to_file(response):
    with open('./airbnb/response.json', 'w') as file:
        json.dump(response.json(), fp=file, indent=4)

def get_data():
    response = search_by_location_request()
    save_response_to_file(response)
    return response

def read_json() -> pd.DataFrame:
    with open('./airbnb/response.json', 'r') as file:
        data = json.load(file)
        df = pd.DataFrame(data['results'])
        return df
    

if __name__ == '__main__':
    # get_data()

    AirBnbApartment(read_json())
