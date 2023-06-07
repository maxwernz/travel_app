from enum import Enum
import pickle
import pandas as pd

class APIClass(Enum):

    AIRBNB = 'airbnb'


def set_api_requests(api: APIClass, number_of_requests: int):
    """Set the number of api requests for each api"""
    pass
